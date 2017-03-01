from django.forms import ModelForm
from .models import Album

class AlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = ['title', 'artist_name', 'nb_title', 'description']

'''
description
birth_date
image
'''