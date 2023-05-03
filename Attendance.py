class_list=("Adreyan Ruiz", "Alejandro Contreras", "Anothony Hauck", "Brock Chubb", "Callen Clark", "Cameron Groves", "CC Piper", "Hans Martin", "Ian Schumacher", "Jacob Erhardt", "Johnathan Hamllik", "Joshua Clark", "Josiah Simpson", "Kyden Blunt", "Landyn Rhoades", "Maxwell Christensen", "Raymond Holycross", "Rose Hanger", "Samuel Bischoff", "Lori Piper")
i=0
present=(list())
not_present=(list())
valid_input=0
while i < len(class_list):
        here=input("is " + class_list[i] + " present?")
        if here == "yes":
            present.append(class_list[i])
            i = i+1
        elif here == "no":
            not_present.append(class_list[i])
            i = i+1
        else:
            print("please type yes or no")
print("These students were present: " + str(present))
print("These students were not present: " + str(not_present))
print("Today, " + str(len(present)) + " students were here and, " + str(len(not_present)) + " were absent.")
print("This project was made by Ronald Nickelson, on 2/1/23")