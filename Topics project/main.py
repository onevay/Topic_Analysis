import csv
import webbrowser
import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from gensi import start
from vizualize import plot_topic_distribution
from probably import probably_topics
from textb import request

global lda_model, them_count, mydict, corpus, st
def read_csv_to_string(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(','.join(row))
    return '\n'.join(data)

def browse_file():
    global filename
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Выберите CSV файл",
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))
    )
    if filename:
        result_label.config(text=f"Выбранный файл: {filename}")

def start_processing():
    global lda_model, them_count, mydict, corpus, st
    if not filename:
        messagebox.showwarning("Внимание", "Пожалуйста, выберите CSV файл перед началом!")
    else:
        global data
        data = read_csv_to_string(filename)
        data = " ".join(data.split(";"))
        s, lda_model, them_count, mydict, corpus, st = start(data)
        result_label_tab2.config(text=s)
        notebook.select(tab2)

def open_presentation():
    presentation_file = "README.pptx"
    try:
        webbrowser.open(presentation_file)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть презентацию: {e}")

def open_chart():
    if(them_count <= 6):
        plot_topic_distribution(lda_model, 3)
    else:
        plot_topic_distribution(lda_model, 4)

def open_pie_chart():
    probably_topics(lda_model, mydict, them_count)

def click_action():
    answer = request(st)
    window = tk.Tk()
    window.title("Ответ")
    window.geometry("500x350")
    window.configure(bg='black')
    label=tk.Label(window, text=answer, bg="black", fg="white", font=("Times New Roman", 14, "italic"))
    label.pack()

def resize_background(event):
    bg_image_resized = bg_image.resize((event.width, event.height), Image.LANCZOS)
    bg_photo_resized = ImageTk.PhotoImage(bg_image_resized)
    bg_label.config(image=bg_photo_resized)
    bg_label.image = bg_photo_resized

root = tk.Tk()
root.title("Чтение CSV")
root.geometry("500x350")
root.configure(bg='black')
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab1 = tk.Frame(notebook, bg='black')
notebook.add(tab1, text="Выбор файла")

bg_image = Image.open("i.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(tab1, image=bg_photo, bg='black')
bg_label.place(relwidth=1, relheight=1)

title_label = tk.Label(tab1, text="Чтение CSV файлов", bg="black", fg="#FFFFFF", font=("Times New Roman", 18, "italic"))
title_label.pack(pady=20)

browse_button = tk.Button(tab1, text="Выбрать файл", command=browse_file, width=24,
                          bg="black", fg="white", borderwidth=2, relief="raised", font=("Times New Roman", 12, "italic"))
browse_button.pack(pady=10)

result_label = tk.Label(tab1, text="", bg="black", fg="white", font=("Times New Roman", 14, "italic"))
result_label.pack(pady=5)

start_button = tk.Button(tab1, text="Начать", command=start_processing, width=24,
                         bg="black", fg="white", borderwidth=2, relief="raised", font=("Times New Roman", 12, "italic"))
start_button.pack(pady=10)

instruction_frame = tk.Frame(tab1, bg='black')
instruction_frame.pack(pady=10)

instruction_label = tk.Label(instruction_frame, text="Перед использованием ознакомьтесь с инструкцией",bg="black", fg="white", font=("Times New Roman", 12, "italic"))
instruction_label.pack(side=tk.LEFT)

arrow_label = tk.Label(instruction_frame, text="⬇️", bg="black", fg="white", font=("Times New Roman", 24, "italic"))
arrow_label.pack(side=tk.LEFT)
go_button = tk.Button(tab1, text="Инструкция", command=open_presentation, width=24,
                      bg="black", fg="white", borderwidth=2, relief="raised", font=("Times New Roman", 12, "italic"))
go_button.pack(pady=10)

tab2 = tk.Frame(notebook, bg="black")
notebook.add(tab2, text="Результаты")

result_label_tab2 = tk.Label(tab2, text="", bg="black", fg="white", font=("Times New Roman", 14, "italic"))
result_label_tab2.pack(pady=20)

chart_button = tk.Button(tab2, text="Открыть диаграмму", command=open_chart, width=24,
                         bg="black", fg="white", borderwidth=2, relief="raised", font=("Times New Roman", 12, "italic"))
chart_button.pack(pady=10)

pie_chart_button = tk.Button(tab2, text="Открыть круговую диаграмму", command=open_pie_chart, width=24,
                             bg="black", fg="white", borderwidth=2, relief="raised", font=("Times New Roman", 12, "italic"))
pie_chart_button.pack(pady=10)

click_button = tk.Button(tab2, text="Основные темы от GPT", command=click_action, width=24,
                         bg="black", fg="white", borderwidth=2, relief="raised", font=("Times New Roman", 12, "italic"))
click_button.pack(pady=10)

data = []
filename = None

root.mainloop()