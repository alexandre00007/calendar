from django.shortcuts import render
from django.http import JsonResponse
from .models import Presence
from django.shortcuts import render, get_object_or_404

def calendrier(request):
    return render(request, 'calendrier_app/calendrier.html')

def get_presences(request):
    presences = Presence.objects.all()
    events = []
    for presence in presences:
        events.append({
            'title': presence.noms,
            'start': f"{presence.date}T{presence.heure_arrive}",
            'end': f"{presence.date}T{presence.heure_depart}",
             'id': presence.id,
        })
    return JsonResponse(events, safe=False)


 

def presence_detail(request, presence_id):
    presence = get_object_or_404(Presence, id=presence_id)
    return render(request, 'calendrier_app/presence_detail.html', {'presence': presence})