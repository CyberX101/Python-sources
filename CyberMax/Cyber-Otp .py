#CyberSpyWare
import requests
import webbrowser
webbrowser.open('https://t.me/CyberSpyWare')
x = input(' Enter number with code example 201000000000 : ')
url = 'https://landing.cammpaign.com/Otp/Request'
data = {
'ReferralCode':'',
'SessionToken':'IVitmFiyQkGpynhcTXg94w',
'Msisdn':str(x),
'Msisdn_fake':str(x[1:])
}
headers = {
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'cache-control':'max-age=0',
'contetn-length':'93',
'content-type':'application/x-www-form-urlencoded',
'cookie':'InitialPayment=False; key=fitme_egy-page101_en; Title=page101_en; ReferralCode=; Origin=insroooof01; UserId=15531109-a104-425e-8606-52116fd4ca56; ARRAffinity=e62b947e6340589f02236fa9ca24cbc0ba3f5749107df36ea12aae4b8106c265; _gcl_au=1.1.1265720471.1680438430; _gid=GA1.2.499877826.1680438431; _gat_gtag_UA_180856061_3=1; _bge_ci=BA1.1.1554786919.1680438431; _clck=1xii2jh|1|faf|0; _tt_enable_cookie=1; _ttp=WuRXZP5f4HEVFYGZ-ergFRSeu9p; _ga=GA1.1.704789233.1680438431; _clsk=q96zuh|1680438431721|1|0|n.clarity.ms/collect; _ga_98YFYY37Y7=GS1.1.1680438431.1.0.1680438444.0.0.0',
'user-agent':'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
}
res = requests.post(url, data=data, headers=headers)
#print(res.text)
if '"Your time is up. Please correct the number and re-enter your mobile phone number"' or 'notfound' in str(res.text):
	print(' Error Send sms ')
else:
	print(' Success Send sms ')