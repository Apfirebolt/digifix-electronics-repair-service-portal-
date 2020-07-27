from django.shortcuts import render


def complaints_view(request):
  return render(request, 'complaints/complaints_home.html', {})


