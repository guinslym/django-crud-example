from mixer.backend.django import mixer
from applications.music.models import Album
from applications.blog.models import Article
from django.contrib.auth.models import User
from faker import Factory

for i in Album.objects.all():
	i.delete()

user = mixer.blend(User)
for i in range(25):
	album = mixer.blend(Album)



for i in Article.objects.all():
	i.delete()

user = mixer.blend(User)
for i in range(25):
	article = mixer.blend(Article)