from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from kiseloadas.models import Kisealoadas


@login_required
def indexview(request):
    context = {'user': request.user}
    if request.user.is_staff:
        context['feladatok'] = Kisealoadas.objects.all()
        context['tanarok'] = User.objects.filter(is_staff=True)
        context['tanulok'] = User.objects.filter(is_staff=False)
        return render(request, "tanar.html", context)
    else:
        context['eloadasok'] = Kisealoadas.objects.all()
        if request.method == 'POST':
            Kisealoadas.objects.filter(user = request.user).update(user = None)
            if 'le' not in request.POST:
                Kisealoadas.objects.filter(tema = request.POST['atema']).update(user = request.user)
        return render(request, "index.html", context)

@login_required
def ujview(request):
    if request.method == 'POST':
        nu = True
    return render(request, "uj.html", {})