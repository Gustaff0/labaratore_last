from django.shortcuts import render
from accounts.forms import MyUserCreationForm

# Create your views here.

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.save()
            return redirect('webapp:home')
    else:
        form = MyUserCreationForm()
    return render(request, 'register_user.html', context={'form': form})