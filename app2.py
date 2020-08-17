from tkinter import Tk
from tkinter.filedialog import askopenfilename
import textract
from gtts import gTTS

Tk().withdraw()
file_location = askopenfilename()

text = textract.process(
    file_location,
    method='tesseract',
    language='eng',
)

decoded_text = text.decode()

final_file = gTTS(text=decoded_text, lang='pt-br')
final_file.save("AudioFromPdf.mp3")
