from mixer.backend.django import mixer
from applications.music.models import Album
from applications.blog.models import Article
from applications.ecommerce.models import Product
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


for i in Product.objects.all():
	i.delete()

user = mixer.blend(User)
for i in range(25):
	product = mixer.blend(Product)