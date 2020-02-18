# Lab_-2

Installations:

import geopy

from geopy.geocoders import Nominatim

import reverse_geocode

import folium

from tqdm import tqdm

Usage:
This program consists of module main.py where all functionallity is, locations.list - a file with films names, years and locations where there were filming.

Main module allows users to input a year of shooting, coordinates. As a result, he or she gets a map with 3 layers:
1. Main layer with a map;
2. Layer with markers with film names;
3. Layer with lines showing distance and having diiferent colors dut to the distance from inputed coordinates.

Current program can be useful to plan your trip and visit places of your favorite films scenes or to analize development in cinema industry of defferent regions and countries.

![Знімок екрана 2020-02-19 о 01 19 14](https://user-images.githubusercontent.com/60693273/74786671-f61ee700-52b5-11ea-8197-3d1a3b8759b9.png)


![Screen_map](https://user-images.githubusercontent.com/60693273/74784173-046a0480-52b0-11ea-9c48-d2cf5e6c609f.png)
