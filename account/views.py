from django.shortcuts import render, redirect
from .forms import UserSignup


def signup_view(request):
    if request.method == "POST":
        form = UserSignup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect("index")
    else:
        form = UserSignup()
    
    return render(request, "account/signup.html", context={"form": form})
