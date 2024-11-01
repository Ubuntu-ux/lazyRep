import tkinter as tk
from tkinter import scrolledtext, font
import random
import time
import sys
from tkinter import ttk

responses = {
    "привет": "Оооо, кого я вижу! Слышь, тебе там шепот не мерещится?",
    "хай": "Здарова, путник! Ищешь правду-матку?", 
    "как дела": "Да так, болтаюсь тут как неприкаянный... Жду чего-то.",
    "как тебя зовут": "Кликуха моя PyBot... Хотя раньше по-другому звали, но это темная история.",
    "пока": "Давай, бро! Только помни - тени они такие, липнут как банный лист.",
}

spooky_phrases = [
    "Чёт холодок пробежал, не?",
    "Слушай, такое ощущение, что кто-то палит... У тебя тоже?",
    "Тут что-то есть такое... мутное, короче.",
    "Слыш, а ты уверен, что один тут?",
    "Я про тебя такое знаю... Ты сам в шоке будешь!",
    "Тишина прям звенит... жесть какая.",
    "Ты это, точно не ссышь сейчас?",
]

def get_response(user_input):
    if user_input.lower() in ["help", "exit", "quit"]:
        return "Чё? Куда собрался, родной?"
    
    for keyword, response in responses.items():
        if keyword in user_input.lower():
            return response

    if random.random() < 0.3:
        return random.choice(spooky_phrases)

    return "Не догоняю, чё ты хочешь... Хотя, может оно и к лучшему?"

def send_message():
    user_message = entry_field.get()
    if user_message.strip():
        chat_box.insert(tk.END, "Ты: " + user_message + "\n")
        entry_field.delete(0, tk.END)

        bot_response = get_response(user_message)
        chat_box.insert(tk.END, "Бот: ", 'bot')
        chat_box.tag_config('bot', foreground="red")
        root.update()

        for char in bot_response:
            chat_box.insert(tk.END, char, 'bot')
            chat_box.update()
            time.sleep(0.05)

        chat_box.insert(tk.END, "\n")
        chat_box.yview(tk.END)

        if user_message.lower() in ["exit", "quit"]:
            time.sleep(1)
            root.destroy()

root = tk.Tk()
root.title("Zhutkiy Huyarek 228 IPhone pro max free 100%")
root.geometry("400x500")

WINDOW_FONTS = [
    "Product Sans",
    "SF Pro Display",
    "Segoe UI Variable",
    "Roboto",
    "Segoe UI",
    "Arial Rounded MT Bold"
]

def get_available_font():
    available_fonts = font.families()
    for font_name in WINDOW_FONTS:
        if font_name in available_fonts:
            return font_name
    return "TkDefaultFont"

WINDOW_FONT = get_available_font()

root.attributes('-alpha', 0.99)
root.overrideredirect(True)
root.wm_attributes('-transparentcolor', 'grey')

frame = tk.Frame(root, bg='black')
frame.pack(fill='both', expand=True)

chat_box = scrolledtext.ScrolledText(
    frame, 
    wrap=tk.WORD, 
    state='normal', 
    height=20, 
    width=50, 
    bg="black", 
    fg="white",
    font=(WINDOW_FONT, 10)
)
chat_box.pack(padx=10, pady=10)
chat_box.insert(tk.END, "")

entry_field = tk.Entry(
    frame, 
    width=40, 
    font=(WINDOW_FONT, 12), 
    bg="gray20", 
    fg="white"
)
entry_field.pack(pady=10)
entry_field.bind("<Return>", lambda event: send_message())

send_button = tk.Button(
    frame, 
    text="Отправить", 
    command=send_message, 
    font=(WINDOW_FONT, 12), 
    bg="darkred", 
    fg="white"
)
send_button.pack(pady=5)

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

frame.bind("<Button-1>", start_move)
frame.bind("<ButtonRelease-1>", stop_move)
frame.bind("<B1-Motion>", do_move)

root.mainloop()
