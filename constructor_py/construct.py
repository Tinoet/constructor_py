class person: 
  def __init__(self,name):
    self.name=name
  def talk(self):
    print(f"Hi, I am {self.name}")


john=person("john smith")
print(john.name)
john.talk()

bob = person("bob smith")
print(bob.name)
bob.talk