class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    def do_work(self):
        if self.occupation =="tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")
    def speaks(self):
        print(self.name, "says how are you?")

tom =Human("tom cruise","actor")
tom.do_work()
tom.speaks()

maria = Human("Maria Sharapova ", "tennis player")
maria.do_work()
maria.speaks()

