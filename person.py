class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.age
    
    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print("%s is playing" % (self._name))

    def watch_tv(self):
        if self._age >17:
            print("%s is watching AV" % (self._name))
        else:
            print("%s is watching NBA" % (self._name))

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade =  grade
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade =  grade

    def study(self):
        print("%s is studying" % (self._name))

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    def teach(self):
        print("%s %s is teaching" % (self._title, self._name))

if __name__ == '__main__':
    sam = Person('Sam', 19)
    sam.play()
    sam.watch_tv()
    tom = Student('tom', 16, 80)
    tom.watch_tv()
    tom.study()
