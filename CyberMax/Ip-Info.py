#CyX-Team
#Cyber-Max
#CyX-Devs-Team
#####################
from ast import Try
from email import header
from pyfiglet import figlet_format
import time
import requests
import os
import webbrowser
def CyX():
     print(red + figlet_format('CyX-Ip-Info'))
     print(green + '''
     Telegram = @CyberSpyWare
     Github = https://www.github.com/CyberX101
     Programmer{} = @CyberTrojan
      
     ''')
#colors
red     = '\033[31m'
green   = '\033[1;32m' 

os.system('clear')
CyX()
time.sleep(1)

ip= input(f'{red}Enter Target Ip : {green}')


def ipinfo():
	
	url=f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
	headers={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'demo.ip-api.com',
	'Origin': 'https://ip-api.com',
	'Referer': 'https://ip-api.com/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	 }
	
	req=requests.post(url,headers=headers)
	print(f'{red}[+] {green}status : {red} '+ req.json()['status'])
	print(f'{red}[+] {green}continent :  {red}'+req.json()['continent'])
	print(f'{red}[+] {green}continentCode : '+req.json()['continentCode'])
	print(f'{red}[+] {green}country : {red}'+req.json()['country'])
	print(f'{red}[+] {green}countryCode : {red}'+req.json()['countryCode'])
	print(f'{red}[+] {green}region :  {red}'+req.json()['region'])
	print(f'{red}[+] {green}regionName : {red}'+req.json()['regionName'])
	print(f'{red}[+] {green}city : {red}'+req.json()['city'])
	print(f'{red}[+] {green}district : {red}'+req.json()['district'])
	print(f'{red}[+] {green}zip : {red}'+req.json()['zip'])
	print(f'{red}[+] {green}timezone : {red}'+req.json()['timezone'])
	print(f'{red}[+] {green}currency : {red}'+req.json()['currency'])
	print(f'{red}[+] {green}isp : {red}'+req.json()['isp'])
	print(f'{red}[+] {green}as : {red}'+req.json()['as'])
	print(f'{red}[+] {green}asname : {red}'+req.json()['asname'])
	print(f'{red}[+] {green}query : {red}'+req.json()['query'])
	print(f'{red}[+] {green}lat : {red}'+str(req.json()['lat']))
	print(f'{red}[+] {green}lon : {red}'+str(req.json()['lon']))
	print(f'{red}[+] {green}offset : {red}'+str(req.json()['offset']))
	print(f'{red}[+] {green}mobile : {red}'+str(req.json()['mobile']))
	print(f'{red}[+] {green}proxy : {red}'+str(req.json()['proxy']))
	print(f'{red}[+] {green}hosting : {red}'+str(req.json()['hosting']))

	url1=f'https://ipwhois.pro/{ip}?key=Sxd2AkU2ZL0YtkSR&security=1&lang=en'
	headers1={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'ipwhois.pro',
	'Origin': 'https://ipwhois.io',
	'Referer': 'https://ipwhois.io/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'cross-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36ed-with'
	
	}
	req1=requests.get(url1,headers=headers1)
	
	print(f'{red}[+] {green}calling_code : {red}'+str(req1.json()['calling_code']))
	print(f'{red}[+] {green}img country : {red}'+str(req1.json()['flag']['img']))
	print(f'{red}[+] {green}vpn : {red}'+str(req1.json()['security']['vpn']))
	print(f'{red}[+] {green}tor : {red}'+str(req1.json()['security']['tor']))
	print(f'{red}[+] {green}anonymous : {red}'+str(req1.json()['security']['anonymous']))

	req3=requests.get(f'https://ipapi.co/{ip}/json/')
	print(f'{red}[+] {green}version :  {red}'+str(req3.json()['version']))
	print(f'{red}[+] {green}asn :  {red}'+str(req3.json()['asn']))
	print(f'{red}[+] {green}Location : {red}'+str(req.json()['lat'])+','+str(req.json()['lon']))

ipinfo()
time.sleep(2)
CyX_Security = input(f"{red}[+] {green}do you want to follow Our Channel on Telgegram? (Y/N)")
if CyX_Security == "y":
	webbrowser.open("https://t.me/CyberSpyWare")
elif CyX_Security == "n":
	exit()
