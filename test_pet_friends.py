import os

from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Край Бин', animal_type='Дракон',
                                    age='4', pet_photo='images/cat1.jpg'):
   pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

def test_successful_update_self_pet_info(self, name='Край Бин', animal_type='Дракон', age=4):
   _, auth_key = self.pf.get_api_key(valid_email, valid_password)
   _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

   if len(my_pets['pets']) > 0:
       status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'],
                                                name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("There is no my pets")
