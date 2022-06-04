import sys
from datetime import datetime, timedelta, time, date
import random
import numpy as np
from faker import Faker
from bisect import bisect_left


class Profile:
    def __init__(self, profile):
        self.profile = profile
        self.proportions = {}
        # form profile so it can be sampled from
        self.proportions['categories_wt'] = self.weight_to_cumsum(self.profile['categories_wt'])
        self.proportions['shopping_time'] = self.weight_to_cumsum(self.profile['shopping_time']) ###BRANDON
        self.proportions['date_wt'] = {}
        self.proportions['date_wt']['day_of_week'] = self.prep_weekday()
        years_wt, leap_wt = self.prep_holidays()
        self.proportions['date_wt']['time_of_year'] = years_wt
        self.proportions['date_wt']['time_of_year_leap'] = leap_wt
        self.fake = Faker()

    def set_date_range(self, start, end):
        self.start = start
        self.end = end
        self.make_weights()

    # turn dict into cumulative sum key
    # with entry value so we can sample
    def weight_to_cumsum(self, weights):
        wt_tot = sum(weights.values())
        cumsum = 0
        temp_cat = {}
        for k in weights:
            cumsum += weights[k]/float(wt_tot)
            temp_cat[k] = cumsum
        # invert
        return {temp_cat[k]: k for k in temp_cat}

    def weight_to_prop(self, weights):
        wt_tot = sum(weights.values())
        return {k: weights[k] / float(wt_tot) for k in weights.keys()}


    # ensures all weekdays are covered,
    # converts weekday names to ints 0-6
    # and turns from weights to log probabilities
    def prep_weekday(self):
        day_map = {'monday': 0, 'tuesday': 1, 'wednesday': 2,
                   'thursday': 3, 'friday': 4, 'saturday': 5,
                   'sunday': 6}
        # create dict of day:weight using integer day values
        weekdays = {day_map[day]: self.profile['date_wt']['day_of_week'][day] \
                for day in self.profile['date_wt']['day_of_week'].keys()}
        # replace any missing weekdays with 100
        for d in [day_map[day] for day in day_map.keys() \
                if day not in self.profile['date_wt']['day_of_week'].keys()]:
            weekdays[d] = 100

        return self.weight_to_prop(weekdays)

    # take the time_of_year entries and turn into date tuples
    def date_tuple(self):
        holidays = self.profile['date_wt']['time_of_year']
        date_tuples = []
        for hol in holidays:
            start = None
            end = None
            weight = None
            for k in holidays[hol].keys():
                if 'start' in k:
                    curr_date = holidays[hol][k].split('-')
                    start = date(2000, int(curr_date[0]), int(curr_date[1]))
                elif 'end' in k:
                    curr_date = holidays[hol][k].split('-')
                    end = date(2000, int(curr_date[0]), int(curr_date[1]))
                elif 'weight' in k:
                    weight = holidays[hol][k]
            if start == None or end == None or weight == None:
                sys.stderr.write('Start or end date not found for time_of_year: ' + str(hol) + '\n')
                sys.exit(0)
            elif start > end:
                sys.stderr.write('Start date after end date for time_of_year: ' + str(hol) + '\n')
                sys.exit(0)
            date_tuples.append({'start':start, 'end':end, 'weight':weight})
        return date_tuples

    def prep_holidays(self):
        days = {}
        # all month/day combos (including leap day)
        init = date(2000, 1, 1)
        # initialize all to 100
        for i in range(366):
            curr = init + timedelta(days = i)
            days[(curr.month, curr.day)] = 100
        # change weights for holidays
        holidays = self.date_tuple()
        for h in holidays:
            while h['start'] <= h['end']:
                days[(h['start'].month, h['start'].day)] = h['weight']
                h['start'] += timedelta(days=1)

        # need separate weights for non-leap years
        days_nonleap = {k:days[k] for k in days.keys() if k != (2,29)}
        # get proportions for all month/day combos
        return self.weight_to_prop(days_nonleap), self.weight_to_prop(days)

    # checks number of years and converts
    # to proportions
    def prep_years(self):
        final_year = {}
        # extract years to have transactions for
        years = sorted(range(self.start.year, self.end.year+1))
        # extract years provided in profile
        years_wt = sorted(self.profile['date_wt']['year'].keys())
        # sync weights to extracted years
        for i, y in enumerate(years):
            if years_wt[i] in self.profile['date_wt']['year']:
                final_year[y] = self.profile['date_wt']['year'][years_wt[i]]
            # if not enough years provided, make it 100
            else:
                final_year[y] = 100
        return self.weight_to_prop(final_year)

    def combine_date_params(self, weights):
        new_date_weights = {}
        curr = self.start
        while curr <= self.end:
            # leap year:
            if curr.year%4 == 0:
                time_name = 'time_of_year_leap'
            else:
                time_name = 'time_of_year'

            date_wt = weights['year'][curr.year]*\
                      weights[time_name][(curr.month,curr.day)]*\
                      weights['day_of_week'][curr.weekday()]

            new_date_weights[curr] = date_wt
            curr += timedelta(days=1)
        # re-weight to get proportions
        return self.weight_to_prop(new_date_weights)

    def date_weights(self):
        self.proportions['date_wt']['year'] = self.prep_years()
        weights = self.combine_date_params(self.proportions['date_wt'])
        self.proportions['date_prop'] = self.weight_to_cumsum(weights)
             
    # convert dates from weights to %
    def make_weights(self):
        # convert weights to proportions and use 
        # the cumsum as the key from which to sample
        self.date_weights()

    def closest_rand(self, pro, num):
        """
        Assumes lst is sorted. Returns closest value > num.
        """
        lst = list(pro.keys())
        pos = bisect_left(lst, num)
        if pos == 0:
            return pro[lst[0]]
        if pos == len(pro):
            return pro[lst[-1]]
        return pro[lst[pos]]

    def sample_amt(self, category):
        shape = self.profile['categories_amt'][category]['mean']**2 / self.profile['categories_amt'][category]['stdev']**2
        scale = self.profile['categories_amt'][category]['stdev']**2 / self.profile['categories_amt'][category]['mean']
        amt = np.random.gamma(shape, scale, 1)[0]
        #seeing lots of <$1.00 charges, hacky fix even though it breaks the gamma distribution
        if amt < 1:
            amt = np.random.uniform(1.00, 10.00)
        return str("{:.2f}".format(amt))

    def sample_time(self, am_or_pm, is_fraud):

        if am_or_pm == 'AM':
            hr_start = 0
            hr_end = 12
        if am_or_pm == 'PM':
            hr_start = 12
            hr_end = 24

        if is_fraud == 1:
            #20% chance that the fraud will still occur during normal hours
            chance = (random.randint(1,100))
            if chance > 20:
                if am_or_pm == 'AM':
                    hr_end = 4
                if am_or_pm == 'PM':
                    hr_start = 22

        hour = random.randrange(hr_start, hr_end, 1)
        mins = random.randrange(60)
        secs = random.randrange(60)
        return [hour, mins, secs]

    def sample_from(self, is_fraud):

        # randomly sample number of transactions
        num_trans = int((self.end - self.start).days *
                np.random.randint(self.profile['avg_transactions_per_day']['min'], ## need normal, not uniform
                                  self.profile['avg_transactions_per_day']['max'] + 1))

        # randomly determine if customer is traveling based off of profile travel_pct param
        # if np.random.uniform() < self.profile['travel_pct']/100:
        #     is_traveling = True
        # else:
        #     is_traveling = False
        travel_max = self.profile['travel_max_dist']
        # travel_max=1
        is_traveling = False

        output = []
        rand_date = np.random.random(num_trans)
        rand_cat = np.random.random(num_trans)
        epoch_start = datetime(1970,1,1,0,0,0)

        fraud_dates = []
        for i, num in enumerate(rand_date):
            trans_num = self.fake.md5(raw_output=False)
            chosen_date = self.closest_rand(self.proportions['date_prop'], num)
            chosen_date_str = chosen_date.strftime('%Y-%m-%d')
            if is_fraud == 1:
                fraud_dates.append(chosen_date_str)
            chosen_cat = self.closest_rand(self.proportions['categories_wt'], rand_cat[i])
            chosen_amt = self.sample_amt(chosen_cat)
            chosen_daypart = self.closest_rand(self.proportions['shopping_time'], rand_cat[i])
            hr, mn, sec = self.sample_time(chosen_daypart, is_fraud)
            chosen_date = datetime.combine(chosen_date, time(hour=hr, minute=mn, second=sec))
            epoch = int((chosen_date - epoch_start).total_seconds())
            output.append([str(trans_num), chosen_date_str, f"{hr:02d}:{mn:02d}:{sec:02d}", str(epoch), str(chosen_cat), str(chosen_amt), str(is_fraud)])
        return output, is_traveling, travel_max, fraud_dates

