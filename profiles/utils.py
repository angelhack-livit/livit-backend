from profiles.models import UserProfile, Trainer
import requests
import random



def gen():
	for i in range(1, 50):
		user = requests.get('https://randomuser.me/api/').json()['results'][0]
		UserProfile.objects.get_or_create(email=user['email'], image_url=user['picture']['large'],
										 username=user['login']['username'], first_name=user['name']['first'],
										 last_name=user['name']['last'], age=user['dob']['age'],
										 height=random.randint(4, 8), weight=random.randint(50, 80),
										 location=user['location']['timezone']['description'])



	for i in range(1, 50):
		user = requests.get('https://randomuser.me/api/').json()['results'][0]
		Trainer.objects.get_or_create(email=user['email'], image_url=user['picture']['large'],
										 username=user['login']['username'], first_name=user['name']['first'],
										 last_name=user['name']['last'], age=user['dob']['age'],
										 location=user['location']['timezone']['description'])






