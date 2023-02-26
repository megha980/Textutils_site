from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dict ={'name':'megha','place':'pahari'}
    return render (request,'index.html',dict)

def analyze(request):
    #Get the text
    djtext=request.GET.get('text','default')
    checkbtn =request.GET.get('checkbtn','off')
    fullcaps =request.GET.get('fullcaps','off')
    remover =request.GET.get('remover','off')
    spaceremover =request.GET.get('spaceremover','off')
    
    print(djtext)
    print(checkbtn)
    # analyzed = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if checkbtn == 'on':
        
        for p in djtext:
            if p not in punctuations:
                analyzed = analyzed+p
                
        params = {
            'purpose' :'Removed_punct', 'analyzed_text':analyzed
        }
        djtext=analyzed
        # Analyze the text
        # return render(request,'analyze.html',params)
    if(fullcaps =='on'):
        analyzed=""
        for j in djtext:
            analyzed = analyzed + j.upper()
        params = {
            'purpose' :'Changed upper case', 'analyzed_text':analyzed
        }
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if(remover=='on'):
        analyzed=""
        for i in djtext:
            if (i!='\n' and i !='\r'):
                analyzed=analyzed+i
                params = {
            'purpose' :'New line removed', 'analyzed_text':analyzed
        }
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        djtext=analyzed
    return render(request, 'analyze.html', params)
                
        
    # else:
    #     return HttpResponse('error')