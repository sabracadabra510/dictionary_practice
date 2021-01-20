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

# furniture = {
#     'chair': 'kitchen',
#     'bed': 'bedroom',
#     'couch': 'living_room',
#     'coffee_table' : 'family_room'
# }

# for furniture in furniture.keys():
#     print(furniture)

# class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
        
    #     if s == "" and t == "":
    #         return True
        
    #     my_dict = {}
        
    #     for letter in s:
    #         my_dict[letter] = my_dict.get(letter,0)+1
            
    #     for letter in t:
    #         if letter in my_dict:
    #             my_dict[letter]=my_dict.get(letter,0)-1
    #         else:
    #             return False
            
    #     for value in my_dict.values():
    #         if value != 0:
    #             return False 
            
    #     return True

    # isAnangram('cookies','okoceis')

# groceries ={
#         'milk': 4,
#         'cheese': 1,
#         'bread':2, 
#         'meat':1,
#     }

# for key, value in groceries.items():
#     print(key, value)
    
#  def number_needed(a, b):
    

#     t = {}
#     for c in a:
#         if c not in t:
#             t[c] = 0
#         t[c] += 1

#     for c in b:
#         if c not in t:
#             t[c] = 0
#         t[c] -= 1

#     total = 0
    
#     for key, val in t.items():
#         total += abs(val)
#     print(total)       
    

# fish = {
# ...    "anglerfish": "deep ocean",
# ...    "candiru": "amazon river",
# ...    "trout": "shallow river",
# ...    "bass": "lake"
# ... }

# for i in range(1,len(s)):
#     # window start to window end
#         for j in range(0,len(s)-i+1): # 4 - 1 + 1 = [0,1,2,3] -> values of j

#             s1 = "".join(sorted(s[j:j+i])) # s[0:1]
#         # if 'k' not in d
#         if s1 not in d:
#             d[s1] = 0
#         d[s1] += 1
#         # d = { 'k' : 1 }

#     for i in d.values():
#         total += sum(range(i)) # how many combinations you can make given a certain number of elements
#         return total


# arr, r = [1, 5, 5, 25, 125], 5



# pairs = dict()
# singles = dict()
# total = 0
# for vertex in arr:
#     if vertex in pairs: # we have pairs of numbers, waiting for a third (to complete the triplet),
#                         # and we got the third
#         total += pairs[vertex]
#     if vertex in singles: # we have a single number waiting for a second number to make a pair
#                           # and we got that second number
#         if vertex * r not in pairs:
#             pairs[vertex * r] = 0
#         pairs[vertex * r] += singles[vertex]
#     if vertex * r not in singles:
#         singles[vertex * r] = 0
#     singles[vertex * r] += 1

# print('arr:', arr)
# print('pairs:', pairs)
# print('singles:', singles)
# print(total)

neighbors = {
    'Peter' : 8,
    'John': 11, 
    'Christian': 14, 
    'Jenny': 22, 
    'Warren': 22, 
    'Kendall' : 17, 
    'Veronica' : 1,
}

for key, value in neighbors.items():
    print(key,value)

for key in neighbors.keys():
    print(key)

for value in neighbors.values():
    print(value)