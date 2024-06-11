import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class GoogleTranslateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Translate")

        self.translator = Translator()

        self.source_lang_label = ttk.Label(root, text="Source Language:")
        self.source_lang_label.grid(row=0, column=0, padx=5, pady=5)

        self.source_lang_entry = ttk.Entry(root)
        self.source_lang_entry.grid(row=0, column=1, padx=5, pady=5)

        self.target_lang_label = ttk.Label(root, text="Target Language:")
        self.target_lang_label.grid(row=1, column=0, padx=5, pady=5)

        self.target_lang_entry = ttk.Entry(root)
        self.target_lang_entry.grid(row=1, column=1, padx=5, pady=5)

        self.source_text_label = ttk.Label(root, text="Source Text:")
        self.source_text_label.grid(row=2, column=0, padx=5, pady=5)

        self.source_text_entry = ttk.Entry(root)
        self.source_text_entry.grid(row=2, column=1, padx=5, pady=5)

        self.translate_button = ttk.Button(root, text="Translate", command=self.translate)
        self.translate_button.grid(row=3, columnspan=2, padx=5, pady=5)

        self.result_label = ttk.Label(root, text="Translation:")
        self.result_label.grid(row=4, column=0, padx=5, pady=5)

        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.grid(row=4, column=1, padx=5, pady=5)

    def translate(self):
        source_lang = self.source_lang_entry.get()
        target_lang = self.target_lang_entry.get()
        source_text = self.source_text_entry.get()

        translated = self.translator.translate(source_text, src=source_lang, dest=target_lang)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, translated.text)


def main():
    root = tk.Tk()
    app = GoogleTranslateApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
