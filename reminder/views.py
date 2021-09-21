
from reminder.tasks import mail, add

from django.shortcuts import redirect, render

# Create your views here.
from reminder.forms import UserForm, PlusForm


def index(request, ):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            date = form.cleaned_data['date']
            mail.apply_async((text, email), eta=date)
            return redirect('plus')
    else:
        form = UserForm()

    return render(request,
                  'reminder/index.html',
                  {'form': form})


def plus(request):
    if request.method == 'POST':
        form = PlusForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            add.delay(num1, num2)
    else:
        form = PlusForm()
    return render(request,
                  'reminder/plus.html', {'form': form})