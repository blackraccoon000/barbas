class Person(object):
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        print("First")

    def say_something(self):
        print(f"I am {self.name}. hello!")
        self.run(10)

    def run(self, num):
        print("run " * num)

    # デストラクタ
    def __del__(self):
        print("Good bye!")


person = Person("Yutaka")
person.say_something()
del person

print("#############")


# def person(name):
#     if name == "A":
#         print("hello")
#     elif name == "B":
#         print("hi")
