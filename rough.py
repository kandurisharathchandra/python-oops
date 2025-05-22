lst=[2,3,4,5,7]
# str="nee mama barrey"
# print(type(str))

#method
from oops_proj import chatbook

user1=chatbook()
# # user1.message_frnd()

# # print(user1._chatbook__name)


# #getter and setter
# print(user1.get_name())
# user1.set_name("sharath ")
# print(user1.get_name())
print(user1.id)

#setting static variable to assign ids
# user2=chatbook()
# print(user2.id)
# print(user2.get_name())
# user2.set_name("rachana ")
# print(user2.get_name())
# print(user2.id)

# user3=chatbook()
# print(user3.id)
# print(user3.get_name())
# user3.set_name("ravali ")
# print(user3.get_name())
# print(user3.id)


#using static method directly form class rather than obj
chatbook.set_id(10)
user2=chatbook()
print(user2.id)

user3=chatbook()
print(user3.id)



# #function 
# a1=len(lst)
# print(a1)
