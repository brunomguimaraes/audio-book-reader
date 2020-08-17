from tkinter import Tk
from tkinter.filedialog import askopenfilename
import textract
from gtts import gTTS

Tk().withdraw()
file_location = askopenfilename()

pdf = textract.process(filelocation, method='pdfminer')
decodedPdf = pdf.decode()

final_file = gTTS(text=decodedPdf, lang='en')
final_file.save("AudioFromPdf.mp3")
