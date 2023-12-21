from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

def index (request):
    return render (request, 'index.html')

def thankyou (request):
    return render (request, 'thankyou.html')

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the data to the ContactMessage model
            return redirect('thankyou')  # Redirect to Django admin index page
    else:
        form = ContactForm()

    # Display form errors
    if form.errors:
        for field, error in form.errors.items():
            messages.error(request, f"{field}: {error}")

    return render(request, 'index.html', {'form': form})

