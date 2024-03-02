from tkinter import *
window=Tk()
window.title("BMI Calculator")
window.minsize(100,350)

heading=Label(text="BMI Calculator",fg="black",font=("helvetica",50))
heading.grid(column=0,row=0,columnspan=3)
def change_units(units):
    if units=="metrics":
        weight_unit["text"]="(kilograms)"
        height_unit1["text"]="(centimeters)"
        height_unit["text"]=""
        height_inch.grid_remove()


    elif units=="standard":
        weight_unit["text"] = "(pounds)"
        height_unit["text"] = "(inches)"
        height_unit1["text"]= "(feet)"
        height_inch.grid()
def calculate():
    s=vary.get()
    print(s)
    print(height_inch.get())
    print(height_feet.get())
    print(weights.get())

    if s=="metrics":
        h = float(height_feet.get())
        w = float(weights.get())
        ans_bmi = round(w/((h/100)**2),2)

    elif s=="standard" or "select units":
        h=(float(height_feet.get()))*12+(float(height_inch.get()))
        print(h)
        w=float(weights.get())
        ans_bmi=round((w/(h**2))*703,2)


    ans["text"] = ans_bmi

outer_frame = Frame(window,padx=5,pady=5)
outer_frame.grid(row=2,column=0)


label2=Label(outer_frame,text="Weights",width=33,background="grey",pady=5,padx=5)
label2.grid(column=0,row=1,padx=10,pady=10)

label3=Label(outer_frame,text="height",width=33,background="grey",pady=5,padx=5)
label3.grid(column=0,row=2,padx=10,pady=10)

L=["standard","metrics"]
vary=StringVar(window)
vary.set("select units")
units=OptionMenu(window,vary,*L, command=change_units)

units.grid(column=0,row=1,columnspan=3)

weights=Entry(outer_frame,width=34)
weights.grid(column=1,row=1)

height_feet=Entry(outer_frame,width=34)
height_feet.grid(column=1,row=2)

height_inch=Entry(outer_frame,width=34)
height_inch.grid(column=1,row=3)

weight_unit=Label(outer_frame,text="(pounds)",width=33)
weight_unit.grid(column=2,row=1)

height_unit1=Label(outer_frame,text="(feet)")
height_unit1.grid(column=2,row=2)

height_unit=Label(outer_frame,text="(inches)")
height_unit.grid(column=2,row=3)


outer_frame2=Frame(window,padx=5,pady=5)
outer_frame2.grid(row=3,column=0)

BMI=Button(outer_frame2,text="Click to Calculate BMI",command=calculate,background="grey",height=3,width=25,fg="white")
BMI.grid(column=0,row=3)

ans=Label(outer_frame2,text="----",background="green",height=3,width=75,fg="white")
ans.grid(column=1,row=3)

outer_frame3=Frame(window,padx=5,pady=5)
outer_frame3.grid(row=4,column=0)

info1=Label(outer_frame3,text="Underweight\n<18.5",background="light blue",height=3,width=25,fg="black")
info1.grid(column=0,row=4)

info2=Label(outer_frame3,text="Normal weight \n18.5-25",background="green",height=3,width=25,fg="black")
info2.grid(column=1,row=4)

info3=Label(outer_frame3,text="Overweight\n25-30",background="yellow",height=3,width=25,fg="black")
info3.grid(column=2,row=4)

info4=Label(outer_frame3,text="Obese \n>30",background="red",height=3,width=25,fg="black")
info4.grid(column=3,row=4)

window.mainloop()