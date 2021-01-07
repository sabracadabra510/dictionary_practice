# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']

# print(f"You have just earned {new_points} points!")

# things_to_do = {'write_letters': 4, 'chores': 5, 'buy_presents': 10}

# presents_to_buy = things_to_do['buy_presents']
# print(f"You have {presents_to_buy} presents to buy before next week!")

# children_in_fam = {'Porter': 3, 'Wells': 3, 'Bradley': 2, 'Espinoza': 5}

# most_children = children_in_fam['Espinoza']

# print(f"You have the most children out of everyone, with a total of {most_children}, wow!")

# favorite_foods = {
#     'Jenny':'pizza',
#     'Justin':'pasta',
#     'Dominic':'Indian food',
#     'Shannon':'steak',
#     'Dad':'chicken',
# }

# food = favorite_foods['Dad']
# print(f"The favorite food of Dad is {food}.")


# best_friend = {
#     'Tigger': 'Oakland',
#     'Elmo' : 'San Franciso',
#     'Barney' : 'Pleasanton',

# }

# print(best_friend['Tigger'])

# sister = {
#     'first_name' : 'Jenny',
#     'last_name' : 'Yee',
#     'city' : 'Oakland',
# }

# print(sister['first_name'])
# print(sister['last_name'])
# print(sister['city'])


# favorite_numbers = {
#     'Justin' : 15,
#     'Shannon' :22,
#     'Elvis' : 12,
#     'Savannah' : 2, 
# }
# Shannon = favorite_numbers['Shannon']
# Savannah = favorite_numbers['Savannah']
# Justin = favorite_numbers['Justin']
# print(f'The favorite number of Shannon is {Shannon}')
# print(f'The favorite number of Savannah is {Savannah}')
# print(f'The favoite number of Justin is {Justin}')

# for key, value in favorite_numbers.items():
#     print(key)
#     print(value)

# for number in favorite_numbers.keys():
#     print(number)

# for name in favorite_numbers.keys():
#     print(name)

# for value in favorite_numbers.values():
#     print(value)

# rivers = {
#     'Mississippi': 'United States',
#     'Sacramento' : 'United States', 
#     'Nile' : 'Egypt', 
#     'Jordan' : 'Africa', 
# }

# for country in rivers.values():
#     print(country)

# for key, value in rivers.items():
#     print(key)
#     print(value)

# for key in rivers:
#     print(key)

# for country in rivers.values():
#     print(country)

# alien_0 = {'color': 'green','points':5}
# alien_1 = {'color': 'yellow', 'points' : 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# alients = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens [:5]:
#     print(alien)
#     print(f'Total number of aliens: {len(aliens)}')

# for alien in aliens [:10]:
#     if alien['color'] == 'green':
#         aliens['color'] = 'purple'
#         aliens['points'] = 22
#         aliens['speed'] = 'fast'
#     elif alien['color'] == 'yellow':
#         aliens['color'] = 'red'
#         aliens['points'] = 16
#         aliens['speed'] = 'slow'

# users = {
#     'aeinstein' : {
#         'first': 'albert',
#         'last' : 'einstein',
#         'location': 'princeton',
#     },

#     'mcurie' :{
#         'first': 'marie', 
#         'last' :' curie', 
#         'location': 'paris',
#     },
# }

# for username, user_info in users.items():
#     print(username)
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']

#     print(full_name)
#     print(location)


# families = {
#     'Porter' : {
#         'Justin' : 'Dad',
#         'Michelle' : 'Mom', 
#         'Laila' : 'Daughter', 
#         'Cora' : 'Sister', 
#         'Savannah' : 'Daughter',
#     }, 

#     'Wells' : {
#         'Shannon' : 'Dad',
#         'Kristen' : 'Mom', 
#         'Jaden' :'Son', 
#         'Natalia': 'Daughter', 
#         'Niko' :'Son', 
#     }, 

#     'Yee' : {
#         'Warren': 'Husband', 
#         'Jennifer' : 'Wife', 
    
#     }, 
# }

# for family, name in families.items():
#     print(name)
    

# for family in families.values():
#     print(family)

# for family, title in families.items():
#     print(family)
#     print(title)

# for family in families:
#     print(family)


# holidays = {
#     'Christmas' : 'December', 
#     'Thanksgiving' :'November', 
#     'Halloween' : 'October', 
#     'Labor Day' : 'September'
# }

# dogs = ['Lucky', 'Princeton', 'Bruiser', 'Potato', 'Harlem', 'Georgie', 'Baloo', 'Lucky']

# for dog in dogs: 
#     print(dog)

# dogs = set(dogs)

# if 'Potato' in dogs:
#     print("yes!")

# # if 'Ravi' in dogs:
# #     print('Yes!')

# # else:
# #     print("I don't see him here!")

# # print(dogs)


# class Niece:
#     """A simple to attempt to classify my crazy nieces"""
    
#     def __init__(self, name, age):
#         """initialize name and age attributes"""
#         self.name = name
#         self.age = age

#     def sing(self):
#        """Simulate niece singing"""
#     # print(f"{self.name} is now singing.")

#     def dance(self):
#         """Simulate niece dancing"""
#         # print(f"{self.name} is now dancing.")

#         eldest_niece = Niece('Laila', 6)
#         print(f"My niece's name is {eldest_niece.name} and she is {eldest.niece.age} years old.")


# toys = ['Daniel_Tiger', 'Unicorns', 'Dolls', 'Shoes', 'Dresses']

# for toy in toys:
#     print(toy)

furniture = {
    'chair': 'kitchen',
    'bed': 'bedroom',
    'couch': 'living_room',
    'coffee_table' : 'family_room'
}

for furniture in furniture.keys():
    print(furniture)