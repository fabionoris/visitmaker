# Visit Maker

A fast tool for performing multiple visits to a user-specified URL. Built with aiohttp architecture and asynchronous support, it provides an efficient solution for simulating website traffic to a specific URL. The URL and number of visits can be set through the command line for easy use and customization.


## Requirements

To use this program, you must have Python 3.7 or higher installed on your system, and the [requirements](/requirements.txt):

```
pip install -r requirements.txt
```


## Usage

```
visitmaker -u URL -s NUMBER_OF_REQUESTS
```

or the extended form:

```
visitmaker --url URL --size NUMBER_OF_REQUESTS
```

where `URL` is the website to be visited and `NUMBER_OF_REQUESTS` is the number of visits to be made.

Please note that the protocol (`http`, `https`) is strictly required.


## Example

To make 10 visits to the website `www.example.com`, use the following command:

```
visitmaker -u http://www.example.com -s 10
```
