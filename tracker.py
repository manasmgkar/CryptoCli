import requests
import time
import json
import argparse
from twilio.rest import Client
import smtplib

account_sid = "add account sid here" # account_id for auth
auth_token = "add twilio api token here" # token 
client = Client(account_sid, auth_token) 
# setup client
base_url = "https://api.cryptonator.com/api/ticker/"

parser = argparse.ArgumentParser()
#parser.add_argument('-a',action='append',dest='collection',default=[],help='Add values to list')
parser.add_argument('--add', nargs='+',dest='accepteddata',help="Add values to list")

currdata = parser.parse_args()

dlist = currdata.accepteddata 
print(dlist)

currlist = dlist[::3]# sliced from 0 iterating by 2
currvalmin = dlist[1::3] # sliced from 1 iterating by 2
currvalmax = dlist[2::3] # sliced from 2 interating by 3

def dataprocess(currlist, currvalmin,currvalmax):
	for i in range(len(currlist)):
		datacall_url = base_url + currlist[i]
		targetpricemin = int(currvalmin[i])
		targetpricemax = int(currvalmax[i])
		datafetch(datacall_url,i,targetpricemin,targetpricemax)

def datafetch(datacall_url,i,targetpricemin,targetpricemax):
	pdata = requests.get(datacall_url) # fetches the data from the url 
	
	#since the response contains way more than the payload
	#only the json should be acessed thus line 38 
	
	pdatajson = pdata.json() 
	curr = pdatajson['ticker'] 
	currencyname = curr['base']
	currencyprice = int(float(curr['price']))
	# currencyprice = float(cprice)
	if currencyprice < targetpricemin:
		max_minchecker = 0
		#alert_sms(currencyname,currencyprice)
		#alert_call(currencyname)
		mailfunc(currencyname,currencyprice,max_minchecker)
	elif currencyprice > targetpricemax:
		max_minchecker = 1
		alert_sms(currencyname,currencyprice,max_minchecker)
		alert_call(currencyname)
		mailfunc(currencyname,currencyprice,max_minchecker)

def alert_sms(currencyname,currencyprice,max_minchecker):
	client.messages.create(
		to="", # add phone no here 
		from_="", # add the twilio number here 
		if max_minchecker == 0:
			body="Min target set price has been achived,for currency {} with price {}".format(currencyname,currencyprice)
		else:
			body="Max target set price has been achived,for currency {} with price {}".format(currencyname,currencyprice)
	)


"""
The url used to refer to the twillio xml file below has been left empty
since twillio will call the person anyways and the file doesent spcify 
the currency so

"""
def alert_call(currencyname):
	client.calls.create(
		to="", # add phone no here 
		from_="", # add the twilio number here
		url="" 
	)	




def mailfunc(currencyname):
	try:
		s = smtplib.SMTP('smtp.gmail.com',587 ) #default port for mail
		s.starttls() # intialize secured connection using tls
		s.login("email_id","pass") #input mail id and pass
		message = ("Target set has been reached for {}".format(currency))
		s.sendmail("from_id", "to_id", message)
		s.quit()
	except:
		print("Something went wrong")


while True:
	dataprocess(currlist, currvalmax,currvalmin)
	time.sleep(300) # default refresh time is set to 5 minitues  
