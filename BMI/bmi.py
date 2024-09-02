import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# File to store data
DATA_FILE = 'BMI/bmi_data.txt'

# BMI Calculation Function
def calculate_bmi():
    try:
        age =int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)
        result_label.configure(text=f"{bmi:.2f}")
        category_label.configure(text=f"{category}")
        age_label_3.configure(text=f"{age}")
        height_label_3.configure(text=f"{height}m")
        weight_label_3.configure(text=f"{weight}kg")

        save_data(weight, height, bmi)
        graph()
        if category=="Underweight":
            score_frame.configure(fg_color="#c9e4f3")
            result_label.configure(text_color="#35a3ef")
            category_label.configure(text_color="#35a3ef")


        elif category=="Normal":
            score_frame.configure(fg_color="#c2ff93")
            result_label.configure(text_color="#67ab00")
            category_label.configure(text_color="#67ab00")
         
        elif category=="Overweight":
            score_frame.configure(fg_color="#fffe81")
            result_label.configure(text_color="#c5c400")
            category_label.configure(text_color="#c5c400")

        else:
            score_frame.configure(fg_color="#ff8682")
            result_label.configure(text_color="#ce0600")  
            category_label.configure(text_color="#ce0600") 

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight, height and age.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Data Storage using File Handling
def save_data(weight, height, bmi):
    with open(DATA_FILE, 'a') as file:
        date_str = datetime.now().strftime('%d/%m')
        file.write(f"{date_str},{weight},{height},{bmi:.0f}\n")

def toggle_gender(gender):
    if gender=="Male":
        gender_male.configure(fg_color="#a5deff")
        gender_female.configure(fg_color="#fff")
        man_img=ctk.CTkImage(light_image=Image.open('BMI/images/man.png'),size=(100,280))
        imaage_label.configure(image=man_img)
    else:
        gender_male.configure(fg_color="#fff")
        gender_female.configure(fg_color="#a5deff")
        woman_img=ctk.CTkImage(light_image=Image.open('BMI/images/woman.png'),size=(100,280))
        imaage_label.configure(image=woman_img)
        
# GUI Setup
root = ctk.CTk()
root.geometry("600x600")
root.configure(fg_color="#c9e4f3")
root.title("BMI Calculator")
root.resizable(False,False)

Frame_1=ctk.CTkFrame(root,height=500,width=500,fg_color="#015fa4",corner_radius=0)
Frame_1.place(x=50,y=50)
# Input Fields

bmi_img=ctk.CTkImage(light_image=Image.open('BMI/images/bmi.png'),size=(210,70))
title_Label=ctk.CTkLabel(Frame_1,height=70,width=210,corner_radius=20,text="",image=bmi_img)
title_Label.place(x=20,y=20)

Gender_label=ctk.CTkLabel(Frame_1,text=" Gender",text_color="#fff",font=("Leelawadee UI",12,"bold"))
Gender_label.place(x=150,y=100)

Gender_Frame=ctk.CTkFrame(Frame_1,height=40,width=86,fg_color="#fff",corner_radius=12)
Gender_Frame.place(x=150,y=130)

imaage_label=ctk.CTkLabel(Frame_1, text='', width=100, height=280, fg_color='transparent')
imaage_label.place(x=30, y=100)

male_img=ctk.CTkImage(light_image=Image.open('BMI/images/Male.png'),size=(20,20))
gender_male=ctk.CTkButton(Frame_1,image=male_img,height=28,width=38,corner_radius=0,text="",fg_color="#fff",bg_color="#fff",hover=False,command=lambda:toggle_gender("Male"))
gender_male.place(x=156,y=136)

female_img=ctk.CTkImage(light_image=Image.open('BMI/images/Female.png'),size=(20,20))
gender_female=ctk.CTkButton(Frame_1,image=female_img,height=28,width=38,corner_radius=0,text="",fg_color="#fff",bg_color="#fff",hover=False,command=lambda:toggle_gender("Female"))
gender_female.place(x=193,y=136)

toggle_gender("Male")

age_label=ctk.CTkLabel(Frame_1, text="Age",font=("Leelawadee UI",12,"bold"),text_color="#fff")
age_label.place(x=150,y=170)
age_entry = ctk.CTkEntry(Frame_1,height=40,width=86,border_width=0,corner_radius=12,placeholder_text="00",justify="center",font=("Leelawadee UI",22,"bold"))
age_entry.place(x=150,y=200)

weight_label=ctk.CTkLabel(Frame_1, text="Weight (kg)",font=("Leelawadee UI",12,"bold"),text_color="#fff")
weight_label.place(x=150,y=240)
weight_entry = ctk.CTkEntry(Frame_1,height=40,width=86,border_width=0,corner_radius=12,placeholder_text="00",justify="center",font=("Leelawadee UI",22,"bold"))
weight_entry.place(x=150,y=270)

height_label=ctk.CTkLabel(Frame_1, text="Height (cm)",font=("Leelawadee UI",12,"bold"),text_color="#fff")
height_label.place(x=150,y=310)
height_entry = ctk.CTkEntry(Frame_1,height=40,width=86,border_width=0,corner_radius=12,placeholder_text="00",justify="center",font=("Leelawadee UI",22,"bold"))
height_entry.place(x=150,y=340)

# Calculate Button
calculate_button = ctk.CTkButton(Frame_1, text="Calculate", command=calculate_bmi,height=40,width=206,border_width=0,corner_radius=12,font=("Leelawadee UI",16,"bold"),text_color="#015fa4",fg_color="#a5deff",hover_color="#c9e4f3")
calculate_button.place(x=30,y=400)

# Result Display

Frame_2=ctk.CTkFrame(Frame_1,height=150,width=220,fg_color="#fff",corner_radius=25)
Frame_2.place(x=260,y=40)

score_frame=ctk.CTkFrame(Frame_2,height=130,width=120,corner_radius=15,fg_color="#c2ff93")
score_frame.place(x=92,y=10)

score_label=ctk.CTkLabel(score_frame,text="BMI SCORE",font=("Leelawadee UI",12,"bold"),text_color="#000")
score_label.place(x=30,y=10)

result_label = ctk.CTkLabel(score_frame, text="00",font=("Leelawadee UI",40,"bold"),text_color="#67ab00",fg_color="transparent",anchor="center",height=50,width=120)
result_label.place(x=0,y=35)

category_label=ctk.CTkLabel(score_frame,text="Normal",width=120,font=("Leelawadee UI",15,"bold"),text_color="#67ab00",anchor="center")
category_label.place(x=00,y=90)

result_frame=ctk.CTkFrame(Frame_2,height=130,width=80,corner_radius=15,fg_color="#fff")
result_frame.place(x=10,y=10)

Record=ctk.CTkLabel(result_frame,text="Record:",font=("Leelawadee UI",15,"bold"),text_color="#0000ff",height=20)
Record.place(x=0,y=10)

age_label_2=ctk.CTkLabel(result_frame,text="Age:",font=("Leelawadee UI",12,"bold"),text_color="#015fa4",height=20)
age_label_2.place(x=0,y=40)

age_label_3=ctk.CTkLabel(result_frame,text="",height=20)
age_label_3.place(x=25,y=40)

sep2=ttk.Separator(result_frame,orient='horizontal')
sep2.place(x=0,y=65,width=70)

height_label_2=ctk.CTkLabel(result_frame,text="Height:",font=("Leelawadee UI",12,"bold"),text_color="#015fa4",height=20)
height_label_2.place(x=0,y=70)

height_label_3=ctk.CTkLabel(result_frame,text="",height=20)
height_label_3.place(x=42,y=70)

sep3=ttk.Separator(result_frame,orient='horizontal')
sep3.place(x=0,y=95,width=70)

weight_label_2=ctk.CTkLabel(result_frame,text="weight:",font=("Leelawadee UI",12,"bold"),text_color="#015fa4",height=20)
weight_label_2.place(x=0,y=100)

weight_label_3=ctk.CTkLabel(result_frame,text="",height=20)
weight_label_3.place(x=42,y=100)

sep3=ttk.Separator(result_frame,orient='horizontal')
sep3.place(x=0,y=125,width=70)

#Graph
def graph():
   Frame_3=ctk.CTkFrame(Frame_1,height=220,width=220,fg_color="#fff",corner_radius=25)
   Frame_3.place(x=260,y=210)
   dates=[]
   bmis=[]
   try:
       with open(DATA_FILE, 'r') as file:
           for line in file:
               date_str, weight, height, bmi = line.strip().split(',')
               dates.append(date_str)
               bmis.append(float(bmi))
   except FileNotFoundError:
       messagebox.showerror("Error", "No historical data found.")
   
   x=dates[-5:]
   y=bmis[-5:]
   fig,ax=plt.subplots(figsize=(2,2))
   plt.figure(figsize=(10, 5))
   ax.fill_between(x,y,color="#c2ff93")
   ax.plot(x,y,color="#67ab00")
   font_size=6
   font_style="Leelawadee UI"
   font_properties={'family':font_style,'size':font_size}
   
   ax.set_title("BMI Trend Over Time",fontdict={'family':font_style,'size':9})
   ax.set_xlabel("Date",fontdict=font_properties)
   ax.set_ylabel("BMI",fontdict=font_properties)
   ax.tick_params(axis='both',labelsize=font_size)
   ax.yaxis.set_ticks_position('right')
   ax.yaxis.set_label_position('right')
   canvas=FigureCanvasTkAgg(fig,Frame_3)
   canvas.get_tk_widget().place(x=5,y=10)
   canvas.draw()

graph()
# Run the application
root.mainloop()