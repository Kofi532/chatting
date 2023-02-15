from django.shortcuts import render
import pandas as pd
import PyPDF2

# Create your views here.4
def home(request):
    pdfFileObject = open('C:\\Users\\KOFI ADUKPO\\Downloads\\acts.pdf', 'rb')
    reader = PyPDF2.PdfReader(pdfFileObject)
    count = len(reader.pages)
    output = []
    for i in range(count):
        page = reader.pages[i] 
        output.append(page.extract_text())
    my_list = str(output).split("\\n")
    matching = [s for s in my_list if "17" in s]
    l1 = [k for k in my_list if 'kill' in k and '' in k]
    ric = [i for i in my_list if i.startswith('Section')]
    ccd = ric.copy()
    for i in range(len(ccd)):
        ccd[i] = (str(ccd[i]).split(" "))[1]
    for i in range(len(ccd)):
        ccd[i] = '29-'+str(ccd[i])
    them = zip(ric,ccd)
    #ric = my_list.copy()
    if request.method == 'POST':
        return render(request, 'thanks.html', {})
    return render(request, 'index.html', {'them': them})