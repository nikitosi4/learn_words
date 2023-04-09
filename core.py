from tkinter import *
import tkmacosx as tk
import sqlite3 as sl


class AddWord(Tk):
    def __init__(self):
        super().__init__()

        self.title("Добавить новое слово")
        Label(self, text="English word: ").grid(row=0, column=0)
        self.eng_word = Entry(self)
        self.eng_word.grid(row=0, column=1)
        Label(self, text="Русское слово: ").grid(row=1, column=0)
        self.ru_word = Entry(self)
        self.ru_word.grid(row=1, column=1)
        tk.Button(self, text="Добавить", command=self.save_data).grid(row=2, column=0, columnspan=2)

    def get_word(self):
        en = self.eng_word.get()
        ru = self.ru_word.get()
        print([en, ru])
        return [en, ru]

    def save_data(self):
        value = self.get_word()
        cur.execute("INSERT INTO words(eng_word, ru_word) values(?,?);", value)
        db.commit()


db = sl.connect("DataBase.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS words(
   eng_word TEXT PRIMARY KEY,
   ru_word TEXT);
""")
db.commit()


win = Tk()
win.title("Запоминалка слов")
win.config(bg="black")


add_btn = tk.Button(win, text="Добваить новое слово", command=lambda: AddWord())
add_btn.pack()


win.mainloop()
