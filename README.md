# Nearest bars

Finds from JSON data in the file a biggest, a smallest, a closest bars and prints its  prettified json data to the console.
Also promts yours longitude and latitude to calculate the closest bar.
# Quickstart

Example of script launch on Linux, Python 3.5:

```
$ python3 bars.py bars.json 
Enter longitude:  38
Enter latitude:  57

The biggest BAR is:
 {
    "Address": "Автозаводская улица, дом 23, строение 1",
    "AdmArea": "Южный административный округ",
    "District": "Даниловский район",
    "ID": "00138530",
    "IsNetObject": "нет",
    "Latitude_WGS84": "55.7011146292467670",
    "Longitude_WGS84": "37.6382285008039050",
    "Name": "Спорт бар «Красная машина»",
    "PublicPhone": [
        {
            "PublicPhone": "(905) 795-15-84",
            "global_id": 33761.0,
            "global_object_id": 169375059.0,
            "system_object_id": "00138530 _1"
        }
    ],
    "SeatsCount": 450,
    "SocialPrivileges": "нет",
    "TypeObject": "бар",
    "geoData": {
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ],
        "type": "Point"
    },
    "global_id": 169375059,
    "system_object_id": "00138530"
}

The smallest BAR is:
 {
    "Address": "Дубравная улица, дом 34/29",
    "AdmArea": "Северо-Западный административный округ",
    "District": "район Митино",
    "ID": "00107283",
    "IsNetObject": "нет",
    "Latitude_WGS84": "55.8461447588834330",
    "Longitude_WGS84": "37.3580592058223000",
    "Name": "БАР. СОКИ",
    "PublicPhone": [
        {
            "PublicPhone": "(495) 258-94-19",
            "global_id": 22348.0,
            "global_object_id": 20675518.0,
            "system_object_id": "00107283 _1"
        }
    ],
    "SeatsCount": 0,
    "SocialPrivileges": "нет",
    "TypeObject": "бар",
    "geoData": {
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ],
        "type": "Point"
    },
    "global_id": 20675518,
    "system_object_id": "00107283"
}

The closest BAR is:
 {
    "Address": "город Зеленоград, корпус 315",
    "AdmArea": "Зеленоградский административный округ",
    "District": "район Савёлки",
    "ID": "00144982",
    "IsNetObject": "нет",
    "Latitude_WGS84": "55.9175687313618820",
    "Longitude_WGS84": "37.7442349738896180",
    "Name": "Гудсон бар",
    "PublicPhone": [
        {
            "PublicPhone": "(499) 740-97-58",
            "global_id": 35010.0,
            "global_object_id": 281494735.0,
            "system_object_id": "00144982 _1"
        }
    ],
    "SeatsCount": 30,
    "SocialPrivileges": "нет",
    "TypeObject": "бар",
    "geoData": {
        "coordinates": [
            37.744234974114,
            55.917568731248
        ],
        "type": "Point"
    },
    "global_id": 281494735,
    "system_object_id": "00144982"
}

```

Launch on Windows is the same.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
