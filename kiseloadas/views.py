from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
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
    context = {}
    if request.method == 'POST':
        if 'tanulok' in request.POST:
            tsvdata = str(request.POST['feltoltendo']).split("\n")
            for sor in tsvdata:
                fields = sor.split("\t")
                if len(fields) < 5:
                    context['hiba'] = True
                else:
                    User.objects.create(
                        username = fields[0],
                        password = make_password(fields[1]),
                        last_name = fields[2],
                        first_name = fields[3],
                        is_staff = fields[4],
                    )
                    context['elvegezve'] = True
        elif 'feladatok' in request.POST:
            data = str(request.POST['feltoltendo']).split("\n")
            for elem in data:
                if len(elem) < 1:
                    context['hiba'] = True
                else:
                    Kisealoadas.objects.create(
                        tema = elem,
                        user = None,
                    )
                    context['elvegezve'] = True
        elif 'torles' in request.POST:
            Kisealoadas.objects.all().delete()
            context['elvegezve'] = True
    print(context)
    return render(request, "uj.html", context)