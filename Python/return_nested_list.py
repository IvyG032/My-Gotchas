#Write a function called concrete_names. concrete_names takes
#as input one parameter, a dictionary. Each key in the
#dictionary will be a string corresponding to a first name.
#Each value in the dictionary will be a list of last names.
#
#concrete_names should return a list of lists. Each list
#should be an alphabetically-sorted list of names constructed
#by putting each first name together with each of its last
#names. The lists themselves should also be in alphabetical
#order by what first name is shared by all names in the list.
#
#For example, this could be one of the dictionaries your
#function receives:
#
# {"David": ["Beckham", "Tennant", "Joyner"],
#  "Ananya": ["Agarwal", "Chatterjee", "Birla", "Roy"],
#  "Ines": ["Sainz", "Melchor", "Suarez"]}
#
#Your function would then return:
#
# [["Ananya Agarwal", "Ananya Birla", "Ananya Chatterjee", "Ananya Roy"],
#  ["David Beckham", "David Joyner", "David Tennant"],
#  ["Ines Melchor", "Ines Sainz", "Ines Suarez"]]
#
#HINT: To get a list of the keys of a dictionary in alphabetical
#order, use this code:
#
# the_keys = list(a_dict.keys())
# the_keys.sort()


#Write your function here!
def concrete_names(name_dict):
     name_list = []

     the_keys = list(name_dict.keys())
     the_keys.sort()

     for first in the_keys:
          lasts = name_dict[first]

          first_group = []

          for last in lasts:
               full_name = first + " " + last
               first_group.append(full_name)
               
          first_group.sort() 
          name_list.append(first_group)

     return name_list


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#
#[["Ananya Agarwal", "Ananya Birla", "Ananya Chatterjee", "Ananya Roy"], ["David Beckham", "David Joyner", "David Tennant"], ["Inés Melchor", "Inés Sainz", "Inés Suarez"]]
print(concrete_names({"David": ["Beckham", "Tennant", "Joyner"], "Ananya": ["Agarwal", "Chatterjee", "Birla", "Roy"], "Ines": ["Sainz", "Melchor", "Suarez"]}))
