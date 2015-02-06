# **Next Prime Number** - Have the program find prime numbers until the user chooses to stop asking for the next one.

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self,parent)
        self.parent = parent

        self.primes = []
        self.current_number = 2
        self.is_prime = True
        self.found_prime = False

        self.initialize()

    def initialize(self):
        self.grid()

        self.prime_label = tk.Label(self)
        self.prime_label["text"] = "Click 'Next' to get prime!"
        self.prime_label.grid(columnspan=4, row=0, padx=5, pady=5)

        self.next_prime_button = tk.Button(self, text="Next", command=self.next_prime)
        self.next_prime_button.grid(column=0, row=1, padx=2, pady=2, sticky="W")

        self.quit_button = tk.Button(self, text="Quit", command=root.destroy)
        self.quit_button.grid(column=1, row=1, padx=2, pady=2, sticky="W")

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

        self.prime_label["text"] = "Current Prime Number: " + str(self.current_number)

        self.found_prime = False
        self.current_number += 1

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Primes")
    app = Application(parent=root)
    app.mainloop()
