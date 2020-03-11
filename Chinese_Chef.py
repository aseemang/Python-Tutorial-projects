#can use parentheses to define inheritance, after importing

from Chef import Chef

class Chinese_Chef(Chef):
    #say our chinese chef can do everything the normal chef can do
    '''def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")'''

    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fried_rice(self):
        print("The chef makes fried rice")