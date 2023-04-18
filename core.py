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
        return [en, ru]

    def save_data(self):
        value = self.get_word()
        cur.execute("INSERT INTO words(eng_word, ru_word) values(?,?);", value)
        db.commit()
        AddWord.destroy(self)


class DictWin(Tk):
    def __init__(self):
        super().__init__()
        self.title("Словарь")
        cur.execute("SELECT * FROM words;")
        self.all_results = cur.fetchall()
        if len(self.all_results) == 0:
            Label(self, text="Словарь пуст. Внесите хотябы одну пару слов и тогда они появятся здесь!!!").grid(row=0, column=0)
        else:
            for i in range(len(self.all_results)):
                x = i
                Label(self, text=self.all_results[i][0]).grid(row=i, column=0)
                Label(self, text=self.all_results[i][1]).grid(row=i, column=1)
                self.make_del_btn(i).grid(row=i, column=2)

    def make_del_btn(self, x):
        return tk.Button(self, text="Удалить", command=lambda:self.del_word(x))

    def del_word(self,x):
        word = self.all_results[x][0]
        print(word)
        cur.execute("DELETE FROM words WHERE eng_word=?", [word])
        db.commit()
        DictWin.destroy(self)
        DictWin()


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


add_btn = tk.Button(win, text="Добваить новое слово", command=AddWord)
add_btn.pack()
dict_btn = tk.Button(win, text="Словарь", command=DictWin)
dict_btn.pack()


win.mainloop()
