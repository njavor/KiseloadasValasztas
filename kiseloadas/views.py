from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from kiseloadas.models import Kisealoadas


@login_required
def indexview(request):
    context = {'user': request.user}
    if request.user.is_staff:
        return render(request, "tanar.html", context)
    else:
        context['eloadasok'] = Kisealoadas.objects.all()
        if request.method == 'POST':
            Kisealoadas.objects.filter(user = request.user).update(user = None)
            Kisealoadas.objects.filter(tema = request.POST['atema']).update(user = request.user)
            print()
        return render(request, "index.html", context)


@login_required
def feladatview(request):
    context = {'feladatok': Kisealoadas.objects.all()}
    return render(request, "feladatok.html", context)

@login_required
def tanuloview(request):
    tanulok = User.objects.filter(is_staff=False)
    context = {'tanulok': tanulok}
    return render(request, "tanulok.html", context)