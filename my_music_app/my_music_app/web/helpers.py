from my_music_app.web.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile

    return None
