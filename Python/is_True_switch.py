#-----------------------------------------------------------
#Write a function called no_you_pick. no_you_pick should
#have two parameters. The first parameter is a dictionary
#where the keys are restaurant names and the values are lists
#of attributes of those restaurants as strings, such as
#"vegetarian", "vegan", and "gluten-free".
#
#The second parameter is a list of strings representing of
#necessary attributes of the restaurant you select.
#
#Return a list of restaurants from the dictionary who each
#contain all the diet restrictions listed in the list,
#sorted alphabetically. If there are no restaurants that
#meet all the restrictions, return the string "Sorry, no
#restaurants meet your restrictions". Types of diet
#restrictions that exist in this question's universe are:
#vegetarian, vegan, kosher, gluten-free, dairy-free
#
#For example:
#grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
#                 "jacob's pickles": ["vegetarian", "gluten-free"], \
#                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
#guests_diet = ["dairy-free"]
#no_you_pick(grading_scale, guests_diet) -> ["blossom"]


#Write your code here!
def no_you_pick(rest_names, needs):
    result = []
    for name, options in rest_names.items():
        is_match = True
        for need in needs:
            if need not in options:
                is_match = False
                break
        if is_match is True:
            result.append(name)
    if not result:
        return "Sorry, no restaurants meet your restrictions"
    result.sort()
    return result

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: blossom
grading_scale = {'Moes, Larrys, Curlys': ['vegetarian', 'vegan', 'gluten-free'], 
                 'Hot Chili Pepper': ['vegetarian', 'gluten-free', 'vegan']}
guests_diet = ["vegetarian", "vegan", "gluten-free"]
print(no_you_pick(grading_scale, guests_diet))







