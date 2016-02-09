
python datagen_customer.py 10000 4144 profiles/main_config.json >> /mnt/1k/customers.csv



python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_2550_female_rural.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_2550_female_rural.csv &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_2550_female_urban.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_2550_female_urban.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_2550_male_rural.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_2550_male_rural.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_2550_male_urban.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_2550_male_urban.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/young_adults_female_rural.json 1-1-2012 12-31-2015 >> /mnt/1k/young_adults_female_rural.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/young_adults_female_urban.json 1-1-2012 12-31-2015 >> /mnt/1k/young_adults_female_urban.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/young_adults_male_rural.json 1-1-2012 12-31-2015 >> /mnt/1k/young_adults_male_rural.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/young_adults_male_urban.json 1-1-2012 12-31-2015 >> /mnt/1k/young_adults_male_urban.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_50up_female_rural.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_50up_female_rural.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_50up_female_urban.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_50up_female_urban.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_50up_male_rural.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_50up_male_rural.csv  &
python datagen_transaction.py /mnt/1k/customers.csv /capstone/new_segements_data_gen/profiles/adults_50up_male_urban.json 1-1-2012 12-31-2015 >> /mnt/1k/adults_50up_male_urban.csv  &

