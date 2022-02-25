from online_library.library.models import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]

    return None
