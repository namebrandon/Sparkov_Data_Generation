#!/bin/bash

python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/leftovers.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/leftovers.csv &
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/male_30_40_bigger_cities.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/male_30_40_bigger_cities.csv &
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/male_30_40_smaller_cities.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/male_30_40_smaller_cities.csv &
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/millenials.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/millenials.csv &
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/young_adults.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/young_adults.csv &
exit 0

