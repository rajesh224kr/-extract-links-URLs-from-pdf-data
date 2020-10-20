import io

import requests
import pdfplumber

url = 'https://crpf.gov.in/writereaddata/Portal/Tender/5247_1/1_RFI.pdf'
# import pdb; pdb.set_trace()
r = requests.get(url)
f = io.BytesIO(r.content)

with pdfplumber.open(f) as pdf:
    page1 = pdf.pages[::]
    for page in page1:
        text = page.extract_text()
        print(text)
