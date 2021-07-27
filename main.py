# basic program for web scraping of any webpage
# only for study purpose link of justdial is taken.

import requests
from bs4 import BeautifulSoup
# filename = " name of file in which data is extracted.csv"
filename="banquate_hall_mumbai.csv"
f=open(filename,"w")
headers="name, address, number\n"
f.write(headers)
i=0
while i<50:
	i=i+1
	#url = url of page from ehich data need to srap
	url= 'https://www.justdial.com/Mumbai/Banquet-Halls/nct-10035861/page-'+str(i)
	agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
	page=requests.get(url, headers=agent)
	soup=BeautifulSoup(page.content,'html.parser')
	containers=soup.findAll("li",{"class":"cntanr"})

	for container in containers:
		name=container.find("span",{"class":"lng_cont_name"}).text
		address=container.find("span",{"class":"cont_fl_addr"}).text
		number=""
		try:
			contain=container.find("p",{"class":"contact-info"})
			spans=contain.find_all('span')
			for x in range(1,len(spans)):
				digit=spans[x].get('class')
				string=digit[-1].split("-")[-1]
				if string=='dc':
					number+='+'
				elif string=='fe':
					number+='('
				elif string=='hg':
					number+=')'
				elif string=='ba':
					number+='-'
				elif string=='abc':
					number+='0'
				elif string=='yz':
					number+='1'
				elif string=='wx':
					number+='2'
				elif string=='vu':
					number+='3'
				elif string=='ts':
					number+='4'
				elif string=='rq':
					number+='5'
				elif string=='po':
					number+='6'
				elif string=='nm':
					number+='7'
				elif string=='lk':
					number+='8'
				elif string=='ji':
					number+='9'
				else:
					number+='0'
		except:
			number='Not Provided'
		print(name)
		print(address)
		print(number)
		f.write(name+","+address.replace(","," ")+","+number.replace("-","")+"\n")
f.close()
