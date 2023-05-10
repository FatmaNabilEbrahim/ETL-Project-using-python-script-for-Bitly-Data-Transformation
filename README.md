# Bitly Data Transformation Script

This Python script reads JSON files with anonymous data gathered from users who shorten links ending with `.gov` or `.mil`, transforms it to a Pandas DataFrame, and commits each file to a separate CSV file in the target directory. The CSV files will have the following columns:

* `web_browser`: The web browser that has requested the service.
* `operating_sys`: The operating system that initiated this request.
* `from_url`: The main URL the user came from. If the retrieved URL was in a long format (`http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf`), it appears in the file in a short format like this (`www.facebook.com`).
* `to_url`: The same is applied to the `to_url`.
* `city`: The city from which the request was sent.
* `longitude`: The longitude where the request was sent.
* `latitude`: The latitude where the request was sent.
* `time_zone`: The time zone that the city follows.
* `time_in`: The time when the request started.
* `time_out`: The time when the request ended.

## Requirements

* Python 3
* Pandas library

## How to Use

1. Clone this repository to your local machine.
2. Place the JSON files in the `input` directory.
3. Open a terminal in the project directory and run the following command:

```
python task2.py
```

4. The script will transform each JSON file in the `input` directory and create a separate CSV file with the same name in the `output` directory.

