class animal:
    def speak(self):
        print('animal is speaking')
class dog(animal):
    def bark(self):
        print('dog is barking')
class cat(animal):
    def meow(self):
        print('cat is meowing')
class cow(animal):
    def mooing(self):
        print('cow is mooing')
class man(human_being):
    def speaking(self):
        print('man is speaking')





c=cow()
c.mooing()
d=dog()
d.bark()
c=cat()
c.meow()
d.speak()