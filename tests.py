import unittest
from unittest.mock import patch
import sys
from datetime import date
from datagen_customer import Headers, Customer
from main_config import MainConfig
import demographics
from faker import Faker
from freezegun import freeze_time

main = open('profiles/main_config.json', 'r').read()

class TestHeaders(unittest.TestCase):
    def test_headers(self):
        """
        Test header generator
        """

        h = Headers()
        h.make_headers()
        result = h.headers
        self.assertEqual(result, "|".join(['ssn', 'cc_num', 'first', 'last', 'gender', 'street', \
                  'city', 'state', 'zip', 'lat', 'long', 'city_pop', \
                  'job', 'dob', 'acct_num', 'profile']), "Headers do not match")


class TestCustomer(unittest.TestCase):
    @freeze_time("2022-01-01")
    @patch("numpy.random")
    @patch("random.random", return_value=0.333)
    @patch("datagen_customer.fake")
    @patch("datagen_customer.cities", demographics.make_cities())
    @patch("datagen_customer.age_gender", demographics.make_age_gender_dict())
    @patch("datagen_customer.all_profiles", MainConfig(main).config)
    def test_init_male(self, fake, random_mock, np_random_mock):
        # fake = fake_mock_constructor.return_value
        fake.ssn.return_value = '123-45-678'
        fake.last_name.return_value = 'Smith'
        fake.first_name_male.return_value = 'John'
        fake.first_name_female.return_value = 'Mary'
        fake.street_address.return_value = '123 Park Ave'
        fake.job.return_value = 'Engineer'
        fake.credit_card_number.return_value = '1234567890101234'
        fake.email.return_value = 'john.smith@example.com'
        fake.random_number.return_value = '123456789011'
        fake.date_time_this_century.return_value = date(1970, 1, 4)
        np_random_mock.random.return_value = 0.421
        
        c = Customer()
        print(c)

        self.assertEqual(c.ssn, '123-45-678')
        self.assertEqual(c.gender, 'M')
        self.assertEqual(c.dob, date(1977, 1,4))
        self.assertEqual(c.first, 'John')
        self.assertEqual(c.last, 'Smith')
        self.assertEqual(c.street, '123 Park Ave')
        self.assertEqual(c.ssn, '123-45-678')
        self.assertEqual(c.job, 'Engineer')
        self.assertEqual(c.cc, '1234567890101234')
        self.assertEqual(c.email, 'john.smith@example.com')
        self.assertEqual(c.account, '123456789011')
        self.assertEqual(c.profile, 'adults_2550_male_urban.json')
        self.assertEqual(c.addy, 'Fairbanks|AK|99701|64.644|-147.5221|63999')

    @freeze_time("2022-01-01")
    @patch("numpy.random")
    @patch("random.random", return_value=0.333)
    @patch("datagen_customer.fake")
    @patch("datagen_customer.cities", demographics.make_cities())
    @patch("datagen_customer.age_gender", demographics.make_age_gender_dict())
    @patch("datagen_customer.all_profiles", MainConfig(main).config)
    def test_init_male(self, fake, random_mock, np_random_mock):
        # fake = fake_mock_constructor.return_value
        fake.ssn.return_value = '123-45-678'
        fake.last_name.return_value = 'Smith'
        fake.first_name_male.return_value = 'John'
        fake.first_name_female.return_value = 'Mary'
        fake.street_address.return_value = '123 Park Ave'
        fake.job.return_value = 'Engineer'
        fake.credit_card_number.return_value = '1234567890101234'
        fake.email.return_value = 'john.smith@example.com'
        fake.random_number.return_value = '123456789011'
        fake.date_time_this_century.return_value = date(1970, 1, 4)
        np_random_mock.random.return_value = 0.2

        c = Customer()
        print(c)

        self.assertEqual(c.ssn, '123-45-678')
        self.assertEqual(c.gender, 'F')
        self.assertEqual(c.dob, date(1991, 1, 4))
        self.assertEqual(c.first, 'Mary')
        self.assertEqual(c.last, 'Smith')
        self.assertEqual(c.street, '123 Park Ave')
        self.assertEqual(c.ssn, '123-45-678')
        self.assertEqual(c.job, 'Engineer')
        self.assertEqual(c.cc, '1234567890101234')
        self.assertEqual(c.email, 'john.smith@example.com')
        self.assertEqual(c.account, '123456789011')
        self.assertEqual(c.profile, 'adults_2550_female_urban.json')
        self.assertEqual(c.addy, 'Fairbanks|AK|99701|64.644|-147.5221|63999')

    @freeze_time("2022-01-01")
    @patch("numpy.random")
    @patch("random.random", return_value=0.333)
    @patch("datagen_customer.fake")
    @patch("datagen_customer.cities", demographics.make_cities())
    @patch("datagen_customer.age_gender", demographics.make_age_gender_dict())
    @patch("datagen_customer.all_profiles", MainConfig(main).config)
    def test_generate_age_gender(self, fake, random_mock, np_random_mock):

        np_random_mock.random.return_value = 0.1
        fake.date_time_this_century.return_value = date(1970, 1, 4)
        c = Customer()

        results = [
            (0.1, ('F', date(1997, 1, 4))),
            (0.2, ('F', date(1991, 1, 4))),
            (0.3, ('F', date(1985, 1, 4))),
            (0.4, ('M', date(1978, 1, 4))),
            (0.5, ('F', date(1973, 1, 4))),
            (0.6, ('M', date(1967, 1, 4))),
            (0.7, ('M', date(1962, 1, 4))),
            (0.8, ('F', date(1956, 1, 4))),
            (0.9, ('F', date(1946, 1, 4)))
        ]

        for i in range(len(results)):
            np_random_mock.random.return_value = results[i][0]
            gender, dob = c.generate_age_gender()
            self.assertEqual(results[i][1], (gender, dob))


    @freeze_time("2022-01-01")
    @patch("numpy.random")
    @patch("random.random")
    @patch("datagen_customer.fake")
    @patch("datagen_customer.cities", demographics.make_cities())
    @patch("datagen_customer.age_gender", demographics.make_age_gender_dict())
    @patch("datagen_customer.all_profiles", MainConfig(main).config)
    def test_get_random_location(self, fake, random_mock, np_random_mock):

        np_random_mock.random.return_value = 0.1
        random_mock.return_value = 0.1
        fake.date_time_this_century.return_value = date(1970, 1, 4)
        c = Customer()

        results = [
            (0.1, 'Longview|TX|75603|32.4264|-94.7117|102348'),
            (0.2, 'Steubenville|OH|43953|40.3524|-80.6781|30603'),
            (0.3, 'Sturgeon Bay|WI|54235|44.8438|-87.3753|17203'),
            (0.4, 'Gulf Breeze|FL|32563|30.3962|-87.0274|30305'),
            (0.5, 'Memphis|TN|38106|35.1021|-90.033|697385'),
            (0.6, 'Atlanta|GA|30341|33.8879|-84.2905|900273'),
            (0.7, 'Silver Spring|MD|20910|38.9982|-77.0338|282095'),
            (0.8, 'Endicott|NY|13760|42.1506|-76.0551|44264'),
            (0.9, 'Laredo|TX|78045|27.6357|-99.5923|248858')
        ]
        for i in range(len(results)):
            random_mock.return_value = results[i][0]
            self.assertEqual(results[i][1], c.get_random_location())

    @freeze_time("2022-01-01")
    @patch("numpy.random")
    @patch("random.random")
    @patch("datagen_customer.fake")
    @patch("datagen_customer.cities", demographics.make_cities())
    @patch("datagen_customer.age_gender", demographics.make_age_gender_dict())
    @patch("datagen_customer.all_profiles", MainConfig(main).config)
    def test_find_profile(self, fake, random_mock, np_random_mock):

        random_mock.return_value = 0.1
        fake.date_time_this_century.return_value = date(1960, 1, 4)

        results = [
            (0.01, 'young_adults_male_urban.json'),
            (0.1, 'young_adults_female_urban.json'),
            (0.2, 'adults_2550_female_urban.json'),
            (0.3, 'adults_2550_female_urban.json'),
            (0.4, 'adults_2550_male_urban.json'),
            (0.5, 'adults_2550_female_urban.json'),
            (0.6, 'adults_50up_male_urban.json'),
            (0.7, 'adults_50up_male_urban.json'),
            (0.8, 'adults_50up_female_urban.json'),
            (0.9, 'adults_50up_female_urban.json')
        ]
        for i in range(len(results)):
            np_random_mock.random.return_value = results[i][0]
            c = Customer()
            self.assertEqual((results[i][0], results[i][1]), (results[i][0], c.find_profile()))


if __name__ == '__main__':
    unittest.main()