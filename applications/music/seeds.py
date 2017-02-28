from mixer.backend.django import mixer
from applications.music.models import Album
from django.contrib.auth.models import User
from faker import Factory

for i in Album.objects.all():
	i.delete()

user = mixer.blend(User)
for i in range(25):
	Album = mixer.blend(Album)