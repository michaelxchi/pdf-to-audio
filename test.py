'''A simple python script to convert the pdf file into audio format'''
#importing required modules
import pyttsx3 
import PyPDF2
engine = pyttsx3.init()#setting engine
print("Place the pdf file in the same folder as the code. ")
user_file = input("Enter file name\nEg:python.pdf ")#taking the file to convert
file_object = open(user_file, 'rb')
reader = PyPDF2.PdfFileReader(file_object)#taking the pdf object
count = reader.numPages  #total no of pages in pdf
new_page = []
for i in range(count):
    page = reader.getPage(i)
    new_page.append(page.extractText())#appending to the list
    text = "".join(new_page)#seperating the lines and words
    engine.setProperty('rate', 125)#set the speech rate
    engine.say(text)
    engine.runAndWait()
print("<--*Completed*-->")
