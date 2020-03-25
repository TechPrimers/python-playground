# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('example.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print("No of pages: ", pdfReader.numPages) 
  
# creating a page object 
pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
print("Text: ", pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() 
