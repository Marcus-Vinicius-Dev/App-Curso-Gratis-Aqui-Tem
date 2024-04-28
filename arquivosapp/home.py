from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para a página principal após o login
                return redirect('main')
        elif 'signup' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                # Redirecionar para a página principal após o cadastro
                return redirect('main')
    else:
        form = UserCreationForm()

    return render(request, 'home.html', {'form': form})
