def add(one: int, two: int) -> int:
    return one + two
print(add(1,3)) 


class Parent:
    def capitalize(self, text: str) -> str:
        return text.upper()

class Child(Parent):
    def capitalize(self, text: int) -> str:
        return str(text).upper()
    
test = Child()

print(test.capitalize("pls"))


from typing import List, Tuple, Dict
a: List[str] = ["1","3"]
a.append(8)
print(a)

question = "Will you use the walrus operator?"
valid_answers = {"yes", "Yes", "y", "Y", "no", "No", "n", "N"}

#user_answer = input(f"\n{question} ")
#while user_answer not in valid_answers:
    #print(f"\n\nPlease answer one of {valid_answers}")
    #user_answer = input(f"\n{question} ")


while True:
    user_answer = input(f"\n{question} ")
    if user_answer in valid_answers:
        break
    print(f"Please answer one of {', '.join(valid_answers)}")