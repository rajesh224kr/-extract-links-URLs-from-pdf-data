import requests
import pdfplumber

def download_file(url):
	local_filename = url.split('/')[-1]

	with requests.get(url) as r:
		with  open(local_filename, 'wb') as f:
			f.write(r.content)
	return local_filename

url = 'https://www.occ.gov/static/enforcement-actions/ea2018-001.pdf'
inv = download_file(url) 
print(inv)

with pdfplumber.open(inv) as pdf:
	page = pdf.pages[0]
	text = page.extract_text()
print(text)

