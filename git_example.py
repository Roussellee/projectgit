class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('Мяу, - сказал', self.name)

    def change_name(self, new_name):
        if len(new_name) >= 2:
            self.name = new_name
        else:
            print('Плохое имя')


cat1 = Cat('Вася')
cat2 = Cat('Борис')

cat1.say()
cat2.say()

cat1.change_name('Снежок')

cat1.say()
cat2.say()
