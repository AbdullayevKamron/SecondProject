# yil = input('yilingiz:')
# yosh = 2023 - int(yil)
# print(yosh)


# yosh = input('yoshingiz:')
# yil = 2023 - int(yosh)
# print(yil)



# ism = [1,2,3,4,5,6,7,8,9]
# # ism[0]=10
# print(ism[0:9:3])

# Matrix = [1,[2,3,[4,5,],6,7,],8,9,]
# print(Matrix[1][2][0])

# dunyo = [1,2,3,4,5]
# print(len(dunyo))


# dunyo = [1,2,3,4,5]
# dunyo.append(5)
# print(dunyo)


# dunyo = [1,2,3,4,5]
# dunyo.insert(0,0)
# print(dunyo)


# dunyo = [1,2,3,4,5]
# dunyo.extend([1,2,3])
# print(dunyo)


# dunyo = [1,2,3,4,5]
# dunyo.pop(0)
# print(dunyo)



# dunyo = [1,5,8,3,7]
# print(sorted(dunyo))
# print(dunyo)



# dunyo = [1,5,8,3,7]
# ism = dunyo[::1]
# print(dunyo)
# print(ism)




# dunyo = [1,5,8,3,7]
# ism = 'Xush kelibsiz '.join(['Kamron ','Qudrat'])
# # print(dunyo)
# print(ism)










# List Method2
# index
# olmalar = ['a','b','c','d','e']
# print(olmalar.index('e'))
# print(olmalar.index('d', 0))
#
# in
# olmalar = ['a','b','c','d','e']
# print('x' in olmalar)
# ism = 'Doniyor'
# print('o' in ism)
#
# count
# olmalar = ['a','b','d','e']
# print(olmalar.count('x'))
#
# List_Mehtods3
# # sort
# olmalar = ['e','a','d','c','b']
# olmalar.sort()
# # new_olmalar = sorted(olmalar)
# # print(new_olmalar)
# print(olmalar)
#
# sorted
# olmalar = ['eld','anv','das','c','bob']
# sorted(olmalar)
# new = sorted(olmalar)
# print(new)
# print(olmalar)
#
# copy
# olmalar = ['e','a','d','c','b']
# yangi_olmalar = olmalar
# yangi_olmalar.clear()
# print(yangi_olmalar)
# print(olmalar)
#
# reverse
# olmalar = ['e','a','d','c','b']
# print(olmalar)
# olmalar.reverse()
# print(olmalar)
# print(olmalar[::-1])
#
# range
# range(1,100)
# print(range(1,100))
# print(list(range(21)))
# print(list(range(21, 41)))
#
# .join()
# letter = '\n'
# print(letter)
# new_letter = '\n'.join(['olma', 'anor', 'nok'])
# print(new_letter)
#
# List Unpacking
# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)
#
# a,b,c, *other, d = [1,2,3,4,5,6]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)
#
# None
# weapons
# new = [3,4,5,6,1]
# nyu = new[::]
# print(nyu)
# print(new)



# Dictionary - Lug'at
# dict
# list = [{'name': 'a'}, {'name': 'b'}, {'name': 'c'}]
# data = {
#     'Ism': "Kamron",
#     "Yoshi": 12,
#     "Uylanganmi": False,
#     "Qiziqishlari": ["Kodlash", "Play game", "Kitob o'yish"]
# }
# print(data['Ism'])
#
# print(data.get('Familiyasi', 'Iskandarov'))
# data2 = dict(Familiyasi = 'Iskandarov')
# print(data2)
# print('Ism' in data2)
# print('Ism' in data)
# print('Yoshi' in data.keys())
# print(12 in data.values())
# print(data.keys())
# print(data.values())
# print(data.items())
# print(data)
# data.clear()
# print(data)
# data3 = data.copy()
# print(data3)
# print(data.pop('Yoshi'))
# print(data)
# print(data.popitem())
# print(data)
# print(data.update({'Uylanganmi': True}))
# print(data)



# data = {
#     'Ism':input('Ismingiz:'),
#     "Yoshi": int(input('Yoshingiz:')),
#     "Uylanganmi": input('Uylanganmisiz:'),
#     # "Qiziqishlari": ["Kodlash", "Play game", "Kitob o'qish"]
# }
# # data.int('Yoshi')
# print(data)


Foydalanuvchilar = []
data = {
    'Ism': input('Ismingiz:'),
    'Yoshi': int(input('Yoshingiz:')),
    'Uylanganmi': bool(input('Uylganimisiz:')),
   "Qiziqishlari": list(input('Qiziqishlaringiz:').split())
}
print(data)


# Tuple
# tuple = (1,2,3)
# tuple2 = ('Kamron', 'Doniyor', 'Sanjar')
# print(tuple)
# list = [1,2,3,4,5,6,7,8]
# list[0] = 10
# print(list)
# immutable_tuple = (1,2,3,4,5,6,7,8)

# print(immutable_tuple)
# in
# print(7 in immutable_tuple)
#
# user = {
#     'savat': [1,2,3]
#     'text': 'Salom',
#     'yosh': 20
# }
# print(user[(1,2,3)])
# tuple_list = (1,2,3,4,5)
# #
# new_tuple = ('Doniyor', 'Kamron')
#
# print(new_tuple)
# # len
# print(len(new_tuple))
#
# # # count
#
# print(new_tuple.count('Kamron'))
# # # index
# print(new_tuple.index('Kamron'))
#
# # set
# my_set = {1,2,3,4,5}
# print(my_set)
# my_set2 = {1,1,2,2,2,3,3,4,5,5}
# print(my_set2)
# # my_set.add(6)
# my_set.add(12)
# print(my_set)
#
# # Exercise
# my_list = [1,1,2,3,3,4,5,5]
# print(my_list)
# print(set(my_list))