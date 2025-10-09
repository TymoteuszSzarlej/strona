from django.shortcuts import render
from .models import TeamMember, Info

# Create your views here.
def about(request):
    info = Info.objects.all()
    team = TeamMember.objects.all()
    return render(request, './About/about.html', {'team': team, 'info': info})

def team_member(request, member_id):
    member = TeamMember.objects.filter(id=member_id)
    return render(request, 'About/team_member.html', {'member': member})