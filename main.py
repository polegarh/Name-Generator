import operator
import random

class Main: 
    def __init__(self):
        gender = eval(raw_input("What is the gender for the name?(M/F) "))
        min_length = eval(raw_input("What is the minimum length for the name? "))
        while min_length < 2:
            min_length = eval(raw_input("What is the minimum length for the name? "))
        max_length = eval(raw_input("What is the maximum length for the name? "))
        number_of_names = eval(raw_input("How many names would you like? "))

        data = []
        if gender.upper() == 'M':
            f = open("./data/namesBoys.txt", "r")
            data = f.read().lower().split('\n')
            other_f = open("./data/namesGirls.txt", "r")
            other_data = other_f.read().lower().split('\n')
            f.close(); other_f.close()
        else: 
            f = open("./data/namesGirls.txt", "r")
            data = f.read().lower().split('\n')
            other_f = open("./data/namesBoys.txt", "r")
            other_data = other_f.read().lower().split('\n')
            f.close(); other_f.close()

        my_dict = self.getNamesDict(data)
        final_names = []
        while len(final_names) < number_of_names:
            name = self.generateName(my_dict)
            if len(name) >= min_length and len(name) <= max_length and name not in final_names and name.title() not in data and name.title() not in other_data:
                final_names.append(name)
        self.printToScreen(number_of_names, gender, final_names)
        
            
    def printToScreen(self, number, gender, list_of_names,):
        if (gender.upper() == "M"): gender = "male"
        else: gender = "female"
        print ("Here are " + str(number) + " novel " + str(gender) + " names: ")
        for name in list_of_names:
            print(name.title())

    # building data for Markov model 
    def getNamesDict(self, names):
        # ease the parsing of data
        list_of_names = []
        for name in names:
            if (name != ""):
                list_of_names.append("__" + name + "__")
        #
        dict_of_names = {}
        for name in list_of_names:                                      # take 'alex' as example
            for i in range(len(name)-3):
                combination = name[i:i+2]                               # combination of two letters such as 'al'
                if combination not in dict_of_names:                    # check if combo has been seen, 
                    dict_of_names[combination] = []                     # if not create a new array as its value     
                dict_of_names[combination].append(name[i+2])            # append the letter that went after this combination to its array 
        return dict_of_names                                            # so now the dict_of_names looks like this {('al', ['e'])}
    

    # generating new name
    def generateName(self, dict_of_names):
        combination = "__"
        next_letter = ""
        result = ""
        while True: 
            number_of_letters = len(dict_of_names[combination])         # get length of the array of letters that follow a combiation
            index = random.randint(0,number_of_letters - 1)             # get random index out of letters that follow a combination
            next_letter = dict_of_names[combination][index]             # this random index will get us the next predicted letter. 
            if next_letter == "_":                                      # random can be used because if there are 5 As and 6 Bs then B 
                break                                                   # has a higher probability of being the chosen letter
            else:
                result = result + next_letter
                combination = combination[1] + next_letter
        return result


Main()