from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Team, Task, Comment, Attachment
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    teams = request.user.teams.all()
    tasks = Task.objects.filter(team__in=teams)
    task_statuses = ['To Do', 'In Progress', 'Done']  # 👈 Add this

    return render(request, 'dashboard.html', {
        'teams': teams,
        'tasks': tasks,
        'users': User.objects.exclude(id=request.user.id),
        'task_statuses': task_statuses  # 👈 Pass to template
    })

'''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Team, Task

@login_required
def dashboard(request):
    
    teams = request.user.teams.all()
    tasks = Task.objects.filter(team__in=teams)
    return render(request, 'dashboard.html', {
        'teams': teams,
        'tasks': tasks,
        'users': User.objects.exclude(id=request.user.id),
    })

@login_required
def create_team(request):
    if request.method == 'POST':
        name = request.POST.get('team_name')
        if name:
            team = Team.objects.create(name=name)
            team.members.add(request.user)
    return redirect('dashboard')

@login_required
def invite_member(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        team_id = request.POST.get('team_id')
        try:
            team = Team.objects.get(id=team_id)
            user = User.objects.get(email=email)
            team.members.add(user)
        except (Team.DoesNotExist, User.DoesNotExist):
            pass
    return redirect('dashboard')

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        assignee_id = request.POST.get('assignee_id')
        team_id = request.POST.get('team_id')

        if title and description and team_id:
            team = Team.objects.get(id=team_id)
            assignee = User.objects.filter(id=assignee_id).first() if assignee_id else None
            Task.objects.create(
                title=title,
                description=description,
                priority=priority,
                assignee=assignee,
                created_by=request.user,
                team=team
            )
    return redirect('dashboard')'''
