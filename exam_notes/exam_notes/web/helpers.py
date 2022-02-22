from exam_notes.web.models import Profile, Note


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile

    return None


def get_notes():
    return Note.objects.all()
