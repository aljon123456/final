
from django.shortcuts import render, get_object_or_404
from .models import Profile


def profile_list_view(request):
    all_profiles = Profile.objects.all()

    context = {
        'profiles': all_profiles,
        'page_title': 'Employee Profiles List'
    }
    return render(request, 'final/profile_list.html', context)

def profile_detail_view(request, pk):

    profile = get_object_or_404(Profile, pk=pk)

    context = {
        'profile': profile,
        'page_title': f'{profile.full_name}\'s Profile'
    }
    return render(request, 'final/profile_detail.html', context)