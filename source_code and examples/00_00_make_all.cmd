@echo off
cls
@REM -----------------------------------------------------------
@REM  _              _       _             
@REM | |    ___   __| | __ _(_)_ __   __ _ 
@REM | |   / _ \ / _` |/ _` | | '_ \ / _` |
@REM | |__| (_) | (_| | (_| | | | | | (_| |
@REM |_____\___/ \__,_|\__, |_|_| |_|\__, |
@REM                    |___/         |___/ 
@REM -----------------------------------------------------------
:lodging
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'alpine_hut',    'clear_name':'Alpine_Hut',      'icon':'Alpinehut.svg',     'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'apartment',     'clear_name':'Apartment',       'icon':'Apartment.svg',     'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'camp_site',     'clear_name':'Camping',         'icon':'Camping-16.svg',    'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'caravan_site',  'clear_name':'Camper_Car_Site', 'icon':'Caravan-16.svg',    'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'guest_house',   'clear_name':'Guesthouse',      'icon':'guest_house.svg',   'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'hostel',        'clear_name':'Hostel',          'icon':'Hostel-16.svg',     'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'hotel',         'clear_name':'Hotel',           'icon':'Hotel-16.svg',      'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'tourism', 'tag':'motel',         'clear_name':'Motel',           'icon':'Motel-16.svg',      'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
@REM -----------------------------------------------------------
@REM  _____           _ 
@REM |  ___|   _  ___| |
@REM | |_ | | | |/ _ \ |
@REM |  _|| |_| |  __/ |
@REM |_|   \__,_|\___|_|
@REM -----------------------------------------------------------
:fuel 
overpass_2_kml.exe --dictionary "{'key':'amenity', 'tag':'fuel',          'clear_name':'Gas_Station',     'icon':'Fuel.png',          'brand':'false', 'brand_name':'', 'second_key':'', 'second_tag':'' }"
overpass_2_kml.exe --dictionary "{'key':'amenity', 'tag':'fuel',          'clear_name':'LPG_Gas_Station', 'icon':'gas-station.png',   'brand':'false', 'brand_name':'', 'second_key':'fuel:lpg', 'second_tag':'yes' }"

@REM -----------------------------------------------------------
@REM  ____             _           
@REM |  _ \  ___  __ _| | ___ _ __ 
@REM | | | |/ _ \/ _` | |/ _ \ '__|
@REM | |_| |  __/ (_| | |  __/ |   
@REM |____/ \___|\__,_|_|\___|_| 
@REM -----------------------------------------------------------
:dealer
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'Motorcycle-Generic',  'icon':'motorbike.png', 'brand':'false','brand_name':''}"
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'BMW-Dealer',          'icon':'motorbike.png', 'brand':'true', 'brand_name':'BMW'}"
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'CF_Moto-Dealer',      'icon':'motorbike.png', 'brand':'true', 'brand_name':'CF'}"
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'Honda-Dealer',        'icon':'motorbike.png', 'brand':'true', 'brand_name':'Honda'}"
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'Husqvarna-Dealer',    'icon':'motorbike.png', 'brand':'true', 'brand_name':'Husqvarna'}"
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'KTM-Dealer',          'icon':'motorbike.png', 'brand':'true', 'brand_name':'KTM'}"
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'Suzuki-Dealer',       'icon':'motorbike.png', 'brand':'true', 'brand_name':'Suzuki'}"
overpass_2_kml.exe --dictionary "{'key':'shop', 'tag':'motorcycle',     'clear_name':'Yamaha-Dealer',       'icon':'motorbike.png', 'brand':'true', 'brand_name':'Yamaha'}"
:end