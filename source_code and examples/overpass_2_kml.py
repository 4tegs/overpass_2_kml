# ##########################################################################################
# Hans Straßgütl
#       Pulls data from Openstreetmaps using the OverpassTurbo API.
#       Build Point of Interest in 2 KML formats: OruxMaps and OrganicMaps
#       
#       Uses a commandline paramater AND a JSON file. See readme-licence for details
#           
# ------------------------------------------------------------------------------------------
# Version:
#	2024 02 		Initial start of coding
#
#
# ##########################################################################################

import argparse
import ast  # Module for safely evaluating strings containing Python expressions
import requests
# import geopandas as gpd
import shutil
import simplekml
import json
import os
from os import path
import sys
from pathlib import Path
import keyboard
import subprocess

# ...................................................
# Where do I find my utils to be imported? Set your path here!
sys.path.append("C:\\SynologyDrive\\Python\\00_import_utils")
import utils
# I wasn't able to find the error in my compile, but as long as I don't add the same 
# imports as in utils, the exe breaks with an import error.
# Duplicate imports from uitls.py:
from pathlib import Path
import json
import gpxpy
import sys
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import xml.etree.ElementTree as ET

# ------------------------------------------------------------------------------------------
#  _____ _ _          _                     _ _ _             
# |  ___(_) | ___    | |__   __ _ _ __   __| | (_)_ __   __ _ 
# | |_  | | |/ _ \   | '_ \ / _` | '_ \ / _` | | | '_ \ / _` |
# |  _| | | |  __/   | | | | (_| | | | | (_| | | | | | | (_| |
# |_|   |_|_|\___|___|_| |_|\__,_|_| |_|\__,_|_|_|_| |_|\__, |
#               |_____|                                 |___/ 
# ------------------------------------------------------------------------------------------
def copy_to_folder(kml_path, items_in_scope, land, tag ):
    '''
    Create Folder depending on country and tag. 
    copy file from root to new folder
    '''
    lodging = ['hotel', 'motel', 'hostel', 'guest_house', 'apartment', 'camp_site', 'alpine_hut', 'caravan_site']
    if not os.path.exists(".\\POI\\"): os.mkdir(".\\POI\\")
    if not os.path.exists(".\\POI\\"+items_in_scope): os.mkdir(".\\POI\\"+items_in_scope)
    if not os.path.exists(".\\POI\\"+items_in_scope+"\\"+land): os.mkdir(".\\POI\\"+items_in_scope+"\\"+land)
    copypath = ".\\POI\\"+items_in_scope+"\\"+land+"\\"
    if tag in lodging:
        copypath = copypath + "lodging"
        if not os.path.exists(copypath): os.mkdir(copypath)
        copypath = copypath + "\\"
    
    if tag.lower() == "motorcycle":
        copypath = copypath + "moto-dealer"
        if not os.path.exists(copypath): os.mkdir(copypath)
        copypath = copypath + "\\"
    
    copypath = copypath+kml_path
    
    if os.path.isfile(copypath):           # wenn die datei schon besteht, lösche sie weg 
        os.remove(copypath)                                     # !!! Remove remark after Test
    
    if os.path.exists(".\\"+ kml_path): shutil.copy2(".\\"+ kml_path , copypath)

# ------------------------------------------------------------------------------------------
#   ____      _       ___                                     
#  / ___| ___| |_    / _ \__   _____ _ __ _ __   __ _ ___ ___ 
# | |  _ / _ \ __|  | | | \ \ / / _ \ '__| '_ \ / _` / __/ __|
# | |_| |  __/ |_   | |_| |\ V /  __/ |  | |_) | (_| \__ \__ \
#  \____|\___|\__|___\___/  \_/ \___|_|  | .__/ \__,_|___/___/
#               |_____|                  |_|                  
# ------------------------------------------------------------------------------------------
'''
    Send Query to Overpass and download data
    Return JSON
'''
def download_data(query):
    overpass_url = "http://overpass-api.de/api/interpreter"
    # print(query)
    response = requests.get(overpass_url, params={"data": query})
    # print(response)
    return response.json()


# ------------------------------------------------------------------------------------------
#  __  __       _       
# |  \/  | __ _(_)_ __  
# | |\/| |/ _` | | '_ \ 
# | |  | | (_| | | | | |
# |_|  |_|\__,_|_|_| |_|
# ------------------------------------------------------------------------------------------
def main(args):
    # Check if the --dictionary argument is provided
    if args.dictionary is None:
        utils.error_message("dict_01", True)
        return

    try:
        # Convert the string representation of the dictionary to a dictionary
        param_json = ast.literal_eval(args.dictionary)
    except (SyntaxError, ValueError) as e:
        utils.error_message("dict_02", True)
    return param_json

if __name__ == "__main__":

    global json_file_name
    # ....................................................
    # Erhalte die Übergabeparameter. Erstelle dazu den 
    # default GPX Entry - sofern übergeben.
    # Ansonsten setze Default Pfad auf den Pfad der Exe
    # 
    #  Der Übergabe Paramater MUSS so aussehen: 
    # --dict "{'key':'shop', 'tag':'motorcycle', 'clear_name':'Yamaha-Dealer', 'icon':'motorbike.png', 'brand':'true','brand_name':'Yamaha'}"
    # ....................................................
    os.system('cls') 
    my_script = utils.IchSelbst()
    my_name = sys.argv[0]                       # the first argument is the script itself
    file_paths = sys.argv[1:]                   # the first argument (0) is the script itself. 1: heisst, wir haben nun in der file_paths alle anderen Argumente
    # ....................................................
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print("\n\tOverpass_2_KML - Pull data from Overpass Turbo and convert it to a KML for OruxMaps\n\t\tVersion 01/2024\n\t\tWritten by Hans Strassguetl - https://gravelmaps.de \n\t\tLicenced under https://creativecommons.org/licenses/by-sa/4.0/ \n\t\tIcons used are licensed under: Map Icons Collection - Creative Commons 3.0 BY-SA\n\t\tAuthor: Nicolas Mollet - https://mapicons.mapsmarker.com\n\t\tor https://creativecommons.org/publicdomain/zero/1.0/deed.en\n\n")
    # ....................................................
    # Lets get the dictionary passed via command line
    # ....................................................
    parser = argparse.ArgumentParser(description="Process a dictionary from the command line.")
    parser.add_argument("--dictionary", type=str, help="A string representation of a dictionary.\n\n Example: ""{'key1': 'value1', 'key2': 'value2'}"" ")
    args = parser.parse_args()
    param_json = main(args)

    if 'key' in param_json: key = param_json["key"]
    else: utils.error_message("dict_03", True)
    if 'tag' in param_json: tag = param_json["tag"]
    else: utils.error_message("dict_03", True)
    if 'clear_name' in param_json: clear_name = param_json["clear_name"] 
    else: utils.error_message("dict_03", True)
    if 'brand' in param_json: brand = param_json["brand"] 
    else: utils.error_message("dict_03", True)
    if brand.lower() == "true": 
        brand = True
    else:
        brand = False
    if 'brand_name' in param_json: brand_name = param_json["brand_name"] 
    else: utils.error_message("dict_03", True)
    if 'icon' in param_json: my_icon = param_json["icon"]
    else: utils.error_message("dict_03", True)
    second_key = ""
    if 'second_key' in param_json: 
        second_key = param_json["second_key"]
        second_tag = ""
        if 'second_tag' in param_json: second_tag = param_json["second_tag"]
        else: utils.error_message("dict_03", True)
    
    # ....................................................
    # Lets get the JSON
    # ....................................................
    json_file_name = my_script.path_name_without_suffix+".json"
    my_json = utils.load_json(json_file_name)

    if '7z_exe' in my_json: z_exe = my_json["7z_exe"]
    else: utils.error_message("dict_03", True)
    if not os.path.exists(z_exe): utils.error_message("7z_01", True)

    folder = True
    if 'folder' in my_json: folder = my_json["folder"] 
    else: utils.error_message("dict_03", True)
    
    if 'icon_path' in my_json: my_path_to_icon = my_json["icon_path"] 
    else: utils.error_message("dict_03", True)
    my_icon = my_path_to_icon + my_icon

    if 'in_scope' in my_json: in_scope = my_json["in_scope"]
    else: utils.error_message("dict_03", True)
    print("Fetch \t\t: "+ clear_name)
    all_zip_files = ""
    for items_in_scope in in_scope:
        zip_kml_files = ""
        my_countries = my_json["maps_geo"][items_in_scope]
        print("Working on \t: " + items_in_scope)
        for land in my_countries:
            count = 0
            if land in my_json["iso_code"]: iso =  my_json["iso_code"][land]
            else: utils.error_message("dict_04", True)
            # .......................................................................
            # Start of overpass query 
            # .......................................................................
            print("\tQuery\t: " + land.ljust(15," ") + " - " + iso)
            overpass_query = "[out:json][timeout:2400];\n// gather results\n"
            overpass_query = overpass_query+"area['ISO3166-1'='"+iso+"']->.a;\n(\n"
            if brand is False and second_key == "" :
                overpass_query = overpass_query + "node['"+key+"'='"+tag+"'](area.a);\n"
                overpass_query = overpass_query + "way['"+key+"'='"+tag+"'](area.a);\n"
                overpass_query = overpass_query + "relation['"+key+"'='"+tag+"'](area.a);\n"
            if brand == False and second_key != "" :
                overpass_query = overpass_query + "node['"+key+"'='"+tag+"'] ['"+second_key+"'='"+second_tag+"'](area.a);\n"
                overpass_query = overpass_query + "way['"+key+"'='"+tag+"'] ['"+second_key+"'='"+second_tag+"'](area.a);\n"
                overpass_query = overpass_query + "relation['"+key+"'='"+tag+"'] ['"+second_key+"'='"+second_tag+"'](area.a);\n"
            if brand == True:
                overpass_query = overpass_query + "node['"+key+"'='"+tag+"'] ['brand'~'.*"+brand_name+".*',i] (area.a);\n"
                overpass_query = overpass_query + "way['"+key+"'='"+tag+"'] ['brand'~'.*"+brand_name+".*',i] (area.a);\n"
                overpass_query = overpass_query + "relation['"+key+"'='"+tag+"'] ['brand'~'.*"+brand_name+".*',i] (area.a);\n"
            overpass_query = overpass_query+");\n// print results;\n// out body;\nout center;\n>;\nout skel qt;"
            # .......................................................................
            # End of overpass query 
            # .......................................................................
            # Perform the Overpass query and convert to GeoDataFrame
            data = download_data(overpass_query)

            # Collect coords into list
            coords = []
            for element in data['elements']:
                count += 1
                if element['type'] == 'node':
                    lon = element['lon']
                    lat = element['lat']
                elif 'center' in element:
                    lon = element['center']['lon']
                    lat = element['center']['lat']
                if 'tags' in element:
                    if 'name' in element['tags']:
                        name = (element['tags']['name'])
                    else:
                        name = "NoName"
                else:
                    name = "NoName"
                if name != "NoName":
                    new_waypoint = {"name": name, "lat": lat, "lon": lon}
                    coords.append(new_waypoint)


# ------------------------------------------------------------------------------------------
#  ____       ____          _        _         ____  _  _        ____  ____  
# |  _ \ ___ / ___|___   __| | ___  (_)_ __   |___ \| || |      |___ \| ___| 
# | |_) / _ \ |   / _ \ / _` |/ _ \ | | '_ \    __) | || |_ _____ __) |___ \ 
# |  _ <  __/ |__| (_) | (_| |  __/ | | | | |  / __/|__   _|_____/ __/ ___) |
# |_| \_\___|\____\___/ \__,_|\___| |_|_| |_| |_____|  |_|      |_____|____/ 
# ------------------------------------------------------------------------------------------
#  The following section needs recoding in season 24/25. 
#  What follows is good for the KML 4 OruxMaps. Needed is an optional secion for OrganicMaps to 
#  set the right color for the pins. See the appropriate sections of 
#                    gpx_2_kml_4_orux
#                    gpx_2_kml_4_orga
#  it has to do with the special namespace implementation of organicmaps.
#                    
# ------------------------------------------------------------------------------------------

            # Convert GeoDataFrame to KML using simplekml
            kml = simplekml.Kml(name="<![CDATA["+clear_name+"-"+land+"]]>", visibility = "1" , open ="1", atomauthor = "Hans Straßgütl" , atomlink = "https://gravelmaps.de"  )  
            for element in coords:
                pt2 = kml.newpoint(name='<![CDATA[' + element["name"] + ']]>',coords=[(element["lon"], element["lat"])])
                pt2.altitudemode='absolute'
                pt2.style.iconstyle.icon.href = my_icon
                pt2.style.iconstyle.color ='FFFFFFFF' 
                pt2.style.iconstyle.scale ='3' 
                pt2.balloonstyle.text= '<![CDATA[<p align="left"><font size="+1"><b>$[name]</b></font></p> <p align="left">$[description]</p>]]>'
                pt2.labelstyle.color='FFFFFFFF'

            kml_path = clear_name+"-"+land+".kml"
            if count != 0: 
                kml.save(kml_path)
                zip_kml_files = zip_kml_files + kml_path + " "
            if folder: copy_to_folder(kml_path, items_in_scope , land, tag )
        all_zip_files = all_zip_files + clear_name+"-"+items_in_scope + ".zip "
        if zip_kml_files != "": rc = subprocess.run(z_exe + "  a -mx7 -spe -sdel -tzip " + clear_name+"-"+items_in_scope + " " + zip_kml_files ,  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    rc = subprocess.run(z_exe + "  a -mx7 -spe -sdel -tzip " + clear_name+"-ALL " + all_zip_files ,  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    if os.path.exists(clear_name+"-ALL.zip"): 
        shutil.copy2(clear_name + "-ALL.zip" , ".\\POI")
        os.remove(clear_name + "-ALL.zip")                                
    print("Finished!")
