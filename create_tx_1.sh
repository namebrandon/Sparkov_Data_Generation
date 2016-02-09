

##Linux / OSX Boxes
#Generate customer file

#python datagen_customer.py 10000 4444 profiles/main_config.json >> ../data/customers.csv

#Generate transactions per profile

python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/40_60_bigger_cities.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/40_60_bigger_cities.csv &
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/40_60_smaller_cities.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/40_60_smaller_cities.csv &
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/all_60_up.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/all_60_up.csv &
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/female_30_40_bigger_cities.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/female_30_40_bigger_cities.csv&
python datagen_transaction.py /capstone/data_gen/data/customers.csv ./profiles/female_30_40_smaller_cities.json 1-1-2012 12-31-2015 >> /capstone/data_gen/data/female_30_40_smaller_cities.csv &


##Windows Boxes
#Generate customer file

#python datagen_customer.py 10 4444 C:\Users\Brandon\git\data_generation\profiles\main_config.json >>C:\Users\Brandon\git\data_generation\data\customers.csv

#Generate transactions per profile

#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\40_60_bigger_cities.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\40_60_bigger_cities.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\40_60_smaller_cities.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\40_60_smaller_cities.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\all_60_up.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\all_60_up.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\female_30_40_bigger_cities.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\female_30_40_bigger_cities.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\female_30_40_smaller_cities.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\female_30_40_smaller_cities.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\leftovers.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\leftovers.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\male_30_40_bigger_cities.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\male_30_40_bigger_cities.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\male_30_40_smaller_cities.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\male_30_40_smaller_cities.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\millenials.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\millenials.csv
#python datagen_transaction.py C:\Users\Brandon\git\data_generation\data\customers.csv C:\Users\Brandon\git\data_generation\profiles\young_adults.json 1-1-2012 12-31-2015 >> C:\Users\Brandon\git\data_generation\data\young_adults.csv
exit 0

