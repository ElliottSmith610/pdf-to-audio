import wave
from contextlib import closing
import requests
from dotenv import load_dotenv
from os import environ
# from pdfreader import PDFDocument, SimplePDFViewer
import PyPDF2
import io


#### Part 1: Converting PDF pages to txt files ####
n = 1
with open("tutorial-example.pdf", "rb") as file:
	pdf_reader = PyPDF2.PdfReader(file)
	page_list = pdf_reader.pages

	for page in page_list:
		with open(f"decoded_pdf_pages/pdf_page_{n}.txt", "w", encoding="utf-8") as f:
			f.write(page.extract_text())
		n += 1


#### API Variables ####
load_dotenv()
url = "https://voicerss-text-to-speech.p.rapidapi.com/"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": environ.get('X-RapidAPI-Key'),
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com",
}
api_key = {
	"key": environ.get('api-key')
}
text = {
	"src": "PLACEHOLDER",
	"hl": "en-us",
}

#### Part 2: Sendng API Request for each page.txt ####
for i in range(1):

	with open(f"decoded_pdf_pages/pdf_page_{i + 1}.txt", "rb",) as file:
		text["src"] = file.read().decode()

	response = requests.post(url=url, headers=headers, params=api_key, data=text)
	response.raise_for_status()
	# TODO: Fix this garbage
	with open(f"speech/tts_page_{i + 1}.wav", "w", encoding="utf-8") as file:
		wave.Wave_write(response.text)
		wave.Wave_write()


