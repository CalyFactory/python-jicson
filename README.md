# Python ICS to JSon library
python ics to json lib

[Python Version](https://img.shields.io/pypi/pyversions/jicson.svg)

How to install?
---------
```
$ pip3 install jicson
```

Basic Useage
---------
```python
import jicson

#read from file
result = jicson.fromFile('./basic.ics')
print(result)

#read from text
result = jicson.fromText(icsText)
print(result)

#read from web
result = jicson.fromWeb(url, auth = base64_authtoken)
print(result)

```

This sample will show this result. 

```
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:jspiner1070@gmail.com
X-WR-TIMEZONE:Asia/Seoul
BEGIN:VEVENT
DTSTART:20170131T000000Z
DTEND:20170131T010000Z
DTSTAMP:20170116T065439Z
UID:078843F8-472A-4F1F-AB20-802685C4636E
CREATED:20170115T035832Z
DESCRIPTION:
LAST-MODIFIED:20170115T035832Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:약속1
TRANSP:OPAQUE
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC
END:VEVENT
BEGIN:VEVENT
DTSTART:20170116T000000Z
DTEND:20170116T010000Z
DTSTAMP:20170116T065439Z
UID:211189F0-6EEE-4D23-8BE7-72C1CFD08317
CREATED:20170111T074525Z
DESCRIPTION:
LAST-MODIFIED:20170111T074525Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:약속2
TRANSP:OPAQUE
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC
END:VEVENT
BEGIN:VEVENT
DTSTART:20170113T000000Z
DTEND:20170113T010000Z
DTSTAMP:20170116T065439Z
UID:E5F23518-BAF0-4CED-8593-5FA7DBC8F40A
CREATED:20170111T070526Z
DESCRIPTION:
LAST-MODIFIED:20170111T070526Z
LOCATION:
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:약속3
TRANSP:OPAQUE
X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC
END:VEVENT
BEGIN:VEVENT
DTSTART:20170111T010000Z
DTEND:20170111T020000Z
DTSTAMP:20170116T065439Z
UID:68p30d1ichhj8bb471i38b9kchi30bb26sp62bb160qm4e33cpij8c35c4@google.com
CREATED:20170111T005803Z
DESCRIPTION:
LAST-MODIFIED:20170111T005803Z
LOCATION:
SEQUENCE:1
STATUS:TENTATIVE
SUMMARY:
TRANSP:OPAQUE
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:This is an event reminder
TRIGGER:-P0DT0H10M0S
END:VALARM
END:VEVENT
END:VCALENDAR
```

this ics file to above json

```json 
{
    "VCALENDAR": [
        {
            "PRODID": "-//Google Inc//Google Calendar 70.9054//EN",
            "VERSION": "2.0",
            "CALSCALE": "GREGORIAN",
            "METHOD": "PUBLISH",
            "X-WR-CALNAME": "jspiner1070@gmail.com",
            "X-WR-TIMEZONE": "Asia/Seoul",
            "VEVENT": [
                {
                    "DTSTART": "20170131T000000Z",
                    "DTEND": "20170131T010000Z",
                    "DTSTAMP": "20170116T065439Z",
                    "UID": "078843F8-472A-4F1F-AB20-802685C4636E",
                    "CREATED": "20170115T035832Z",
                    "DESCRIPTION": "",
                    "LAST-MODIFIED": "20170115T035832Z",
                    "LOCATION": "",
                    "SEQUENCE": "0",
                    "STATUS": "CONFIRMED",
                    "SUMMARY": "약속1",
                    "TRANSP": "OPAQUE",
                    "X-APPLE-TRAVEL-ADVISORY-BEHAVIOR": "AUTOMATIC"
                },
                {
                    "DTSTART": "20170116T000000Z",
                    "DTEND": "20170116T010000Z",
                    "DTSTAMP": "20170116T065439Z",
                    "UID": "211189F0-6EEE-4D23-8BE7-72C1CFD08317",
                    "CREATED": "20170111T074525Z",
                    "DESCRIPTION": "",
                    "LAST-MODIFIED": "20170111T074525Z",
                    "LOCATION": "",
                    "SEQUENCE": "0",
                    "STATUS": "CONFIRMED",
                    "SUMMARY": "약속2",
                    "TRANSP": "OPAQUE",
                    "X-APPLE-TRAVEL-ADVISORY-BEHAVIOR": "AUTOMATIC"
                },
                {
                    "DTSTART": "20170113T000000Z",
                    "DTEND": "20170113T010000Z",
                    "DTSTAMP": "20170116T065439Z",
                    "UID": "E5F23518-BAF0-4CED-8593-5FA7DBC8F40A",
                    "CREATED": "20170111T070526Z",
                    "DESCRIPTION": "",
                    "LAST-MODIFIED": "20170111T070526Z",
                    "LOCATION": "",
                    "SEQUENCE": "0",
                    "STATUS": "CONFIRMED",
                    "SUMMARY": "약속3",
                    "TRANSP": "OPAQUE",
                    "X-APPLE-TRAVEL-ADVISORY-BEHAVIOR": "AUTOMATIC"
                },
                {
                    "DTSTART": "20170111T010000Z",
                    "DTEND": "20170111T020000Z",
                    "DTSTAMP": "20170116T065439Z",
                    "UID": "68p30d1ichhj8bb471i38b9kchi30bb26sp62bb160qm4e33cpij8c35c4@google.com",
                    "CREATED": "20170111T005803Z",
                    "DESCRIPTION": "",
                    "LAST-MODIFIED": "20170111T005803Z",
                    "LOCATION": "",
                    "SEQUENCE": "1",
                    "STATUS": "TENTATIVE",
                    "SUMMARY": "",
                    "TRANSP": "OPAQUE",
                    "VALARM": [
                        {
                            "ACTION": "DISPLAY",
                            "DESCRIPTION": "This is an event reminder",
                            "TRIGGER": "-P0DT0H10M0S"
                        }
                    ]
                }
            ]
        }
    ]
}

```
