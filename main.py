import wave
from contextlib import closing
import requests
from dotenv import load_dotenv
from os import environ
# from pdfreader import PDFDocument, SimplePDFViewer
import PyPDF2
import io
from gtts import gTTS


#### Part 1: Converting PDF pages to txt files ####
n = 1
with open("tutorial-example.pdf", "rb") as file:
	pdf_reader = PyPDF2.PdfReader(file)
	page_list = pdf_reader.pages

	for page in page_list:
		with open(f"decoded_pdf_pages/pdf_page_{n}.txt", "w", encoding="utf-8") as f:
			if page.extract_text() != "":
				# Only creates a txt file if the txt isnt blank
				f.write(page.extract_text())
				n += 1


#### Part 2: Sendng API Request for each page.txt ####
for i in range(n - 1):

	with open(f"decoded_pdf_pages/pdf_page_{i + 1}.txt", "rb",) as file:
		text = file.read().decode()

	try:
		tts = gTTS(text=text, lang="en", slow=False)
		tts.save(f"speech/tts_page_{i + 1}.mp3")
	except AssertionError:
		# Originally setup as to skip blank txt files, but fixed no blanks above
		pass

