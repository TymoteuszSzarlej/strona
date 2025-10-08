from django.shortcuts import render
from .models import TeamMember

# Create your views here.
def about(request):
    team = TeamMember.objects.all()
    return render(request, './About/about.html', {'team': team})

def team_member(request, member_id):
    member = TeamMember.objects.filter(id=member_id)
    return render(request, 'About/team_member.html', {'members': member})