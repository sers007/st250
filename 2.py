class student:
    print("Hi")
    def  __init__(self, height=160):
        self.height = height


vasya  = student()
print(vasya.height)

dima = student(height=186 )
print(dima.height)