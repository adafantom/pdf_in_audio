import pdfplumber
from gtts import gTTS


def get_pdf_file(file_path):
    pages_pdf_text = ''
    with pdfplumber.open(file_path) as pdf_file:
        pdf_pages = pdf_file.pages
        pages_pdf_text = ''.join([pdf_page.extract_text() for pdf_page in pdf_pages])
    solid_pdf_text = pages_pdf_text.replace('\n', ' ')
    return solid_pdf_text


def get_audio_file(pdf_file):
    language = 'ru'
    phrase = gTTS(text=pdf_file, lang=language, slow=False)
    phrase.save("audio_text.mp3")


def main():   
    pdf_file = get_pdf_file("text.pdf")
    get_audio_file(pdf_file)
    

if __name__ == '__main__':
		main()
