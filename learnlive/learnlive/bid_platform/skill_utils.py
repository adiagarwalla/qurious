# util file for skill processing.
from learnlive.bid_platform.models import Skill
from warnings import warn
from django.contrib.auth.models import User 
from learnlive.auth.models import UserProfile

def get_profile_for_entity(entity, start, limit):
    """
    given an entity, we want to return
    profiles that have the given entity as
    skills
    limit - is the max number of profiles we want to return
    """
    skills = Skill.objects.filter(name=entity.name) # there is a way to put a limit straight into the filter function, but I do not remember how to do this....
    retlist = []

    # there should only be on e skill that is ever returned, because our db should not be clutterecd
    # with excess skills.
    # given this skill, we want to pull the profiles that have this skill listed.
    profile = []
    for skill in skills:
        profiles = skill.userprofile_set.all()
        for prof in profiles:
            if prof not in profile:
                profile.append(prof)

    for i in range(0, min(len(profile), limit)):
        retlist.append(profile[i])

    # if we have not reached the limit yet, we need the second layer
    if len(retlist) < limit:
        # second layer needed
        parent_entity = entity.get_parent()
        parent_skill = Skill.objects.filter(name=parent_entity.name)
        if len(parent_skill) > 0:
            parent_skill = parent_skill[0]
            parent_profs = parent_skill.userprofile_set.all()
            # now append as many as you need to make this work.
            for i in range(0, limit - len(retlist)):
                retlist.append(parent_profs[i])

    return retlist

def create_sample_profs():
    """
    This function creates a random set of sapmle profiles that can be used for testing purposes
    """

    warn('This function is only for testing purposes: create_sample_profs')
    u1 = User(username='ai1994', password='1234')
    u2 = User(username='ai1995', password='1234')
    u3 = User(username='ai1996', password='1234')
    u4 = User(username='ai1997', password='1234')
    u5 = User(username='ai1998', password='1234')

    u1.save()
    u2.save()
    u3.save()
    u4.save()
    u5.save()

    # now add skills
    s1 = Skill(name='paneer')
    s2 = Skill(name='roasting_pan')
    s3 = Skill(name='indian_cuisine')
    s4 = Skill(name='french_cuisine')
    s5 = Skill(name='paneer')

    s1.save()
    s2.save()
    s3.save()
    s4.save()
    s5.save()

    up1 = UserProfile(user=u1, profile_name='Indian Chef', skills=s1)
    up2 = UserProfile(user=u2, profile_name='Roasting Pan Man', skills=s2)
    up3 = UserProfile(user=u3, profile_name='Indian Cuisine Expert', skills=s3)
    up4 = UserProfile(user=u4, profile_name='French Cuisine Expert', skills=s4)
    up5 = UserProfile(user=u5, profile_name='Abhinav', skills=s5)

    up1.save()
    up2.save()
    up3.save()
    up4.save()
    up5.save()






