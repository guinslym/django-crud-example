from mixer.backend.django import mixer
from lineup.models import Store, Address, StoreLocation
from lineup.models import Profile, UserLocation, UserTransaction, LineUpPost, Store
from django.contrib.auth.models import User
import random
import geocoder
from faker import Factory
fake = Factory.create()

cie = [{
'BestBuys' :[
	'380 Coventry Rd., Ottawa, ON, K1K 2C6',
	'1701 Merivale Rd. Nepean, ON, K2G 3K2',
	'2121 Carling Ave., Unit 8 Ottawa, ON, K2A 1H2',
	'920 Maloney Blvd. W Gatineau, QC, J8T 3R6',
	'2020 Mer Bleue Rd., Unit C2 Orleans, ON, K4A 0G2',
	'360 Newbury St, Boston, MA 02115, USA',
	'162 Santilli Hwy, Everett, MA 02149, EUA',
	'South Bay Center, 14 Allstate Rd, Dorchester, MA 02125, USA'
],
'Macys':[
	'450 Washington St, Boston, MA 02111, USA',
	'151 W 34th St, New York, NY 10001, USA'
]}]

for i in cie[0].keys():
	#Store
	store = Store.objects.create(cie_name=i)
	for i in cie[0][i]:
		g = geocoder.google(i)
		a = g.json
		address = a.get('address')
		postal = a.get('postal')
		country = a.get('country')
		city = a.get('city')
		state = a.get('state')
		#Address
		addresses = Address.objects.create(
			store=store,
			location=address,
			postal=postal,
			city=city,
			country=country
			)
		#StoreLocation
		location = StoreLocation.objects.create(
			address=addresses,
			latitude=a.get('lat'),
			longitude=a.get('lng')
			)


print('--------------------------')
print('--------------------------')
print('--------------------------')
print('--------------------------')
print('Create superuser')
# python manage.py dumpdata auth.user --indent 2 --format json > db.json
# python manage.py dumpdata --indent 2 --format json > db.json



locations = [[45.4231064, -75.6831329], [45.3875812,-75.6960202],
	[45.4235937,-75.700929]]
for i in locations:
	user = mixer.blend('auth.user')
	profile = mixer.blend(Profile, user=user)	
	bank = mixer.blend(UserTransaction, user=user)	
	bank = mixer.blend(UserLocation, user=user, latitude=i[0],
longitude=i[1])	


from mixer.backend.django import mixer
from django.contrib.auth.models import User
import random
import geocoder
from faker import Factory
fake = Factory.create()

for i in range(20):
	price = [25,15,35] 
	f = lambda x: random.choice(x)
	price = f(price)
	user = User.objects.all()
	user = f(user)
	store = Store.objects.all()
	store = f(store)
	lineuppost = mixer.blend(
		LineUpPost, 
		title='BestBuys, San Diego',
		description=fake.text(),
		price=price,
		user=user,
		store=store
		)



#Wadiyabi
from mixer.backend.django import mixer
from applications.wadiyabi.models import Product
from django.contrib.auth.models import User
from faker import Factory

for i in Product.objects.all():
	i.delete()

user = mixer.blend(User)
for i in range(25):
	product = mixer.blend(Product, author=user)