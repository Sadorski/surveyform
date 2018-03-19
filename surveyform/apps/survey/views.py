from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    
    return render(request, 'survey/index.html')

def process(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['loc'] = request.POST['loc']
        request.session['lang'] = request.POST['lang']
        request.session['optional'] = request.POST['optional']
        return redirect('/result')
    else:
        return redirect('/')


def result(request):
    return render(request, 'survey/result.html')