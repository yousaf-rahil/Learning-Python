class school_lib:
    books = ["Maths", "English", "Urdu", "Pak Studies"]
    list = 4

    @property
    def show(self):
        return f"The school library has books on {self.books}"

    @show.setter
    def show(self, b):
        self.books.append(b)
        self.list= self.list +1

    def check(self):
        if len(self.books) == self.list:
            print("The program is working well")
            print(f"There are total {self.list} boooks in the library")
        else:
            print("There is something wrong with the program")

class college(school_lib):
    books = school_lib.books + ["Statistics", "Physcology", "AI", "GK"]
    list = len(school_lib.books) + 4



std = school_lib()

std.check()

print(std.show)

std.show = "Physics"
    
print(std.show)
std.check()
        

clg = college()

print(clg.show)
clg.show = "Computer Architecture"

print(clg.show)
clg.check()