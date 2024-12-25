from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from info.models import Information, Message, Project




@login_required()
def dashboard(request):
    template_name = 'dashboard.html'
    profile = Information.objects.first()
    return render(request, template_name, {'profile':profile, 'dashboard': True})


@login_required()
def profile(request):
    template_name = 'profile.html'
    context = {}
    profile = Information.objects.first()
    context.update({'profile_active': True, 'profile': profile})
    return render(request, template_name, context)



@login_required()
def messages(request):
    template_name = 'messages.html'
    context = {}
    profile = Information.objects.first()
    messages = Message.objects.all().order_by('-send_time')

    page = request.GET.get('page', 1)

    paginator = Paginator(messages, 6)

    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)

    context.update({'messages_active': True, 'messages': messages, 'profile': profile})
    return render(request, template_name, context)


@login_required()
def projects(request):
    template_name = 'dashboard_projects.html'
    context = {}
    profile = Information.objects.first()
    projects = Project.objects.all().order_by('-id')
    context.update({'projects_active': True, 'projects': projects, 'profile': profile})
    return render(request, template_name, context)




