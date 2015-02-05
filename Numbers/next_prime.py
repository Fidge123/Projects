# **Next Prime Number** - Have the program find prime numbers until the user chooses to stop asking for the next one.

import tkinter

class Application(tkinter.Frame):
    def __init__(self, parent=None):
        tkinter.Frame.__init__(self,parent)
        self.parent = parent

        self.primes = [2]
        self.current_number = 2
        self.is_prime = True
        self.found_prime = False

        self.initialize()

    def initialize(self):
        self.grid()

        self.prime_label = tkinter.Label(self)
        self.prime_label["text"] = self.current_number
        self.prime_label.grid(column=0, row=0)

        self.next_prime_button = tkinter.Button(self, text="Next", command=self.next_prime)
        self.next_prime_button.grid(column=0, row=1)

        self.quit_button = tkinter.Button(self, text="QUIT!", command=root.destroy)
        self.quit_button.grid(column=1, row=1)

    def next_prime(self):
        while self.found_prime == False:
            for p in self.primes:
                if self.current_number % p == 0:
                    self.is_prime = False

            if self.is_prime == True:
                self.primes.append(self.current_number)
                self.found_prime = True
            else:
                self.current_number += 1
                self.is_prime = True

        self.prime_label["text"] = self.current_number

        self.found_prime = False
        self.current_number += 1

if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(parent=root)
    app.mainloop()
