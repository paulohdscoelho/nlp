import requests
import sys
from nltk.corpus import stopwords

url = "http://api.meaningcloud.com/sentiment-2.1"
headers = {'content-type': 'application/x-www-form-urlencoded'}
saida = open("sentimentosCatalunha.dat","w")

with open(sys.argv[1]) as txtEntrada:
	for tweet in txtEntrada:
		payload = "key=96e0f4747d1205162c07b444e187f807&lang=es&txt="+str(tweet.strip().lower())+"&txtf=plain&url=YOUR_URL_VALUE&doc=YOUR_DOC_VALUE"
		response = requests.request("POST", url, data=payload, headers=headers)
		saida.write(response.text)
		print(response.text)
	saida.close()