## CryptoPriceTracker

This is a tool to track prices of various cryptocurrencies and alert the user once the user defined maximum & minimum target is reached for that currency.

Cryptopricetracker.py helps users who deal in crypto and dont want to miss low and high's of the currencies.

The tool has no limit on the amount of currencies you can track at any time. 

CryptoPriceTracker supports the [Following Currency Pairs](https://www.cryptonator.com/api/currencies)

## Table of Contents

 - Sample Usage
 - Installation
 - Configuration
		 - Get the Twilio Api key and setup Twilio
		 - Set the SMTP address
 - Usage
 - Status

## Sample Usage

    $ tracker --add btc-usd 550 25000 eth-usd 900 5000 

## Installation 

Clone the repo,Everything except for the twilio package is from the standard library.

    pip install requirements

Usage of a virtual environment is recommended. 

## Configuration 

**Get the Twilio Api key and setup twilio**
This information is borrowed from [Twilio Api Docs](https://www.twilio.com/docs/api) 

 1. Create a account on Twilio 
 2. Go to the the dashboard and under project info find your Live Auth token and account sid 
 3. Copy paste both the things in the account sid and api blocks in the script 
 4. Below Project info is the Phone numbers managment menu,get a number,twilio offers a trial 15$ service and given their rates and how the script functions that should be enough for two months or so
 5. Paste the no in the from section of both alert_sms and alert_call section

**Setup Gmail**

 1. Input your mail adress and Password in the s.login section where id and password have been specified 
2. Fill the from and to section as well on Line 91 

Gmail has a 99 email limit via smtp,so a exception has been added.  

## Usage

    $ tracker --add btc-usd 550 25000 eth-usd 900 5000 

**Output**
![Mail Sample](https://i.imgur.com/9E1ybiI.png)

![Sms Sample](https://i.imgur.com/y74i4zj.png?1)

The script is intended to be deployed on the Cloud or a 24/7 Online server.I have deployed it on a Rpi.


## Status

This script can be further automated using the coinbase/poloniex or various other Exchange's api's to sell and buy automatically as per the set min_max targets.This is not advised though and is very risky financially. 

This is a very basic version and there are plans to develop a proper package with more functionality. 


