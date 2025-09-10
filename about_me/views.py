from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request,'home.html')
def contactPage(request):
    context = {}  # always exists

    if request.method == 'POST':
        firstname = request.POST.get('firstname', '').strip()
        lastname = request.POST.get('lastname', '').strip()
        sent_message = request.POST.get('sent_message', '').strip()

        if firstname:  # only add message if firstname is provided
            context['message'] = f"{firstname}, thank you for reaching out! We'll get back to you promptly."

    return render(request, 'contact.html', context)
def educPage(request):
    return render(request, 'educ.html')