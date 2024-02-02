import pymongo
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
mongocon=pymongo.MongoClient('mongodb://localhost:27017')
mydb=mongocon['SCHOOL']
mycol=mydb['students']
class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text='student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='student mark'))
        self.s_mark = TextInput()
        self.add_widget(self.s_mark)

        self.add_widget(Label(text='student age'))
        self.s_age = TextInput()
        self.add_widget(self.s_age)

        self.add_widget(Label(text='student gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.add_widget(Label(text='student blood'))
        self.s_blood = TextInput()
        self.add_widget(self.s_blood)

        self.press = Button(text='Click me')
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        # Retrieve text from TextInput widgets
        name = self.s_name.text
        mark = self.s_mark.text
        age = self.s_age.text
        gender = self.s_gender.text
        blood = self.s_blood.text

        # Create a dictionary with the data
        mydoc = {'name': name, 'mark': mark, 'age': age, 'gender': gender, 'blood': blood}
        
        # Insert the dictionary into MongoDB
        insertmy = mycol.insert_one(mydoc)
        print(f"Inserted document with ID: {insertmy.inserted_id}")

        # Display the information
        print("Name of student is " + name)
        print("Mark of student is " + mark)
        print("Age of student is " + age)
        print("Gender of student is " + gender)
        print("Blood Group of student is " + blood)
        print("")

class studentApp(App):
    def build(self):
        return childApp()
if __name__=='__main__':
    studentApp().run()
