from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def indexview(request):

    if request.user.is_staff:
        return render(request, "tanar.html", {'user': request.user})
    else:
        return render(request, "index.html", {'user': request.user})