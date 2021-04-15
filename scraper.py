#!/usr/bin/env python3
import requests
import urllib.request
import time
import sys
import os
import re
from bs4 import BeautifulSoup

# TODO: pass in site url as an argument
def scrape_site( dataDir ):
    url = 'https://pcpartpicker.com/products/pricedrop/'
    response = requests.get(url)

    if str(response) == "<Response [200]>":
        print("Connection Accepted")
    else:
        print("Connection Refused")

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        with open("orig", 'w+') as scrapedFile: #closes file after
            scrapedFile.write(soup.get_text(separator=' '))
    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    os.rename("orig", dataDir + "/orig")
    return

def directory_does_exist( directory ):
    if os.path.exists( directory ):
        return True
    else:
        return False

def create_directory( directory ):
    print( "Directory: \'" + directory + "\' did not exist. So it was created.\n" )
    os.makedirs( directory )
    return

def remove_whitespace_characters():
    try:
        origFile  = open(orig, 'r')
        temp0File = open(temp0, 'w+')

        for line in origFile:
            if not re.match(r'^\s*$', line): #and re.match(): # match: \t\n\r and whitespace)
                temp0File.write(line)

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    origFile.close()
    temp0File.close()
    return

def set_item_list( itemList ):
    try:
        temp0File = open(temp0, 'r')

        for line in temp0File:
            if re.match(r'(\s)(Item)(\s)', line):
                match = temp0File.readline()
                itemList.append(match)

        #print(itemList)
        for item in itemList:
            if re.search( r'(\s)(Previous)(\s)', item ):
                itemList.remove(item)
                continue

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    temp0File.close()
    return

def set_previous_list( previousList ):
    try:
        temp0File = open(temp0, 'r')

        for line in temp0File:
            if re.match(r'(\s)(Item)(\s)', line):
                match = temp0File.readline() # Read two lines below 'Item'
                match = temp0File.readline() # which contains 'Previous'
                previousList.append(match)   

        for previous in previousList:
            if re.search( r'(\s)(Current)(\s)', previous ):
                previousList.remove(previous)
                continue

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    temp0File.close()
    return

def set_current_list( currentList ):
    try:
        temp0File = open(temp0, 'r')

        for line in temp0File:
            if re.match(r'(\s)(Item)(\s)', line):
                match = temp0File.readline() # Read two lines below 'Item'
                match = temp0File.readline() # which contains 'Previous'
                match = temp0File.readline() # which contains 'Current'
                currentList.append(match)   

        for current in currentList:
            if re.search( r'(\s)(Where)(\s)', current ):
                currentList.remove(current)
                continue

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    temp0File.close()
    return

def set_where_list( whereList ):
    try:
        temp0File = open(temp0, 'r')

        for line in temp0File:
            if re.match(r'(\s)(Item)(\s)', line):
                match = temp0File.readline() # Read two lines below 'Item'
                match = temp0File.readline() # which contains 'Previous'
                match = temp0File.readline() # which contains 'Current'
                match = temp0File.readline() # which contains 'Where'
                whereList.append(match)   

        for where in whereList:
            if re.search( r'(\s)(Save)(\s)', where ):
                whereList.remove(where)
                continue

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    temp0File.close()
    return

def set_save_list( saveList ):
    try:
        temp0File = open(temp0, 'r')

        for line in temp0File:
            if re.match(r'(\s)(Item)(\s)', line):
                match = temp0File.readline() # Read two lines below 'Item'
                match = temp0File.readline() # which contains 'Previous'
                match = temp0File.readline() # which contains 'Current'
                match = temp0File.readline() # which contains 'Where'
                match = temp0File.readline() # which contains 'Save'
                saveList.append(match)   

        for save in saveList:
            if re.search( r'(\s)(Drop)(\s)', save ):
                saveList.remove(save)
                continue

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    temp0File.close()
    return

def set_drop_list( dropList ):
    try:
        temp0File = open(temp0, 'r')

        for line in temp0File:
            if re.match(r'(\s)(Item)(\s)', line):
                match = temp0File.readline() # Read two lines below 'Item'
                match = temp0File.readline() # which contains 'Previous'
                match = temp0File.readline() # which contains 'Current'
                match = temp0File.readline() # which contains 'Where'
                match = temp0File.readline() # which contains 'Save'
                match = temp0File.readline() # which contains 'Drop'
                dropList.append(match)   

        for drop in dropList:
            if re.search( r'(\s)(Promo)(\s)', drop ):
                dropList.remove(drop)
                continue

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    temp0File.close()
    return

def set_promo_list( promoList ):
    try:
        temp0File = open(temp0, 'r')

        for line in temp0File:
            if re.match(r'(\s)(Promo)(\s)', line):
                match = temp0File.readline() # Read one lines below 'Promo'
                promoList.append(match)   

        for promo in promoList:
            if re.search( r'(\s)(Item)(\s)', promo ):
                promoList.remove(promo)

    except IOError: # catches FileNotFound and PermissionError
        print("Error opening one of the files.")
        sys.exit(1)

    temp0File.close()
    return

def pair_promos_in_dict( promoList, promoDictionary ):
    c = 0
    for promo in promoList:
        if not re.search( r'(\s)(Add)(\s)', promo ):
            promoDictionary[c] = promo
        c += 1
    return promoDictionary

def print_item_with_promos( itemList, previousList, currentList, whereList, 
                           saveList, dropList, promoList, promoDictionary ):
    a = 0
    m = len(itemList)
    while( a <= m ):
        if promoDictionary.get(a):
            print( "Item: ", itemList[a], end="" )
            print( previousList[a], end="" ) 
            print( currentList[a],  end="" )
            print( whereList[a],    end="" )
            print( dropList[a],     end="" )
            print( promoDictionary.get(a), end="" )
            print()
        a += 1
    return

def debug_print_list_lengths():
    print( "len(itemList)    = ", len(itemList) )
    print( "len(previousList = ", len(previousList) )
    print( "len(currentList  = ", len(currentList) )
    print( "len(whereList)   = ", len(whereList) )
    print( "len(saveList)    = ", len(saveList) )
    print( "len(dropList)    = ", len(dropList) )
    print( "len(promoList)   = ", len(promoList) )
    return

def debug_print_lists( list ):
    print( list )
    return

# ------------ MAIN ------------
itemList = []
previousList = []
currentList = []
whereList = []
saveList = []
dropList = []
promoList = []

promoDictionary = {}

dataDir = os.path.abspath("./data")
if not directory_does_exist( dataDir ):
    create_directory( dataDir )

orig  = dataDir + "/orig"
temp0 = dataDir + "/temp0"
temp1 = dataDir + "/temp1" 

#scrape_site( dataDir )

remove_whitespace_characters()
set_item_list( itemList )
set_previous_list( previousList )
set_current_list( currentList )
set_where_list( whereList )
set_save_list( saveList )
set_drop_list( dropList )
set_promo_list( promoList )

promoDictionary = pair_promos_in_dict(promoList, promoDictionary)
keys   = promoDictionary.keys()
values = promoDictionary.values()

print_item_with_promos( itemList, previousList, currentList, whereList, 
                        saveList, dropList, promoList, promoDictionary )

#print( "keys   = ", keys )
#print( "values = ", values ) 

# -------
# Item 
# Enermax MarbleShell MS30 ATX Mid Tower Case 
# Previous $77.99 
# Current $75.99 
# Where Newegg 
# Save $2.00 
# Drop 3% 
# Promo 

