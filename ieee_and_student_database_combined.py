def ieee(decimal):
    decimal = str(decimal)
    import math
    ieee_final = []
    if float(decimal) >= 1:
        ieee_final.append(0)
    elif float(decimal) < 1:
        decimal = decimal[1:]
        ieee_final.append(1)

    decimal_left = math.floor(float(decimal))
    floating_right = round(float(decimal) - decimal_left, 3)

    def dec_to_bin(decimal_left, lst=[]):
        if decimal_left >= 1:
            dec_to_bin(decimal_left // 2)
            lst.append(decimal_left % 2)

        s = ''.join(map(str, lst))
        return s

    def float_converter(num, lst=[]):

        if num < 1 and len(lst) < 32:
            num = float('{:,.3f}'.format(num * 2))
            lst.append(0)
            float_converter(num)
        elif num > 1 and len(lst) < 32:
            num -= 1
            lst.append(1)
            float_converter(num * 2)
        elif num == 1 and len(lst) < 32:
            lst.append(1)

        s = ''.join(map(str, lst))

        return s[1:]


    float_bin_num = float_converter(floating_right)


    def exponent_and_mantissa():
        num = dec_to_bin(decimal_left)

        if (len(num)) > 1:
            exponent = len(num) // 2 - 1

            bias = 127 + exponent

            exponent_data = bin(bias)


            mantissa = num[1:exponent+1]+float_bin_num



            while len(mantissa) < 23:
                mantissa += "0"



            return exponent_data[2:] , mantissa


    exponent,mantissa = exponent_and_mantissa()

    ieee_final.append(exponent)
    ieee_final.append(mantissa)
    return(ieee_final)




# -----------------------------------------------------------------------------------------------


import json

database_filename = "student_database.txt"
with open(database_filename) as file:
    students_file = json.load(file)


def add(new_student):
    students_file.update(new_student)
    with open(database_filename, 'w') as f:
        json.dump(students_file, f, sort_keys=True, indent=4)


new_student = {
    "Student1": {
        "Name": "Charlie Morgan",
        "AXS-214": 70,
        "ZYK": 82
    }
}
add(new_student)


def show():
    print(students_file)


show()


def show_all_students_id():
    for students in students_file:
        print(students)

"""
def search_student_by_name(search_name):
    values = students_file.values()
    for names in values:
        for items in names:
            if names[items] == search_name:
                return names


search_student_by_name("Malcolm Patrick")


def search_student_by_id(search_id):
    return students_file[search_id]
"""



def add_new_course_to_existent_student(search_name, course_data):
    values = students_file.values()
    for names in values:
        for items in names:
            if names[items] == search_name:
                new_student_data = names
    new_student_data.update(course_data)
    for names in values:
        for items in names:
            if names[items] == search_name:
                items = new_student_data

    students_file.update(new_student)
    with open(database_filename, 'w') as f:
        json.dump(students_file, f, sort_keys=True, indent=4)


add_new_course_to_existent_student("Malcolm Patrick", {"XBS-121": 86})


def del_student_by_id(student_id):
    del students_file[student_id]
    with open(database_filename, 'w') as f:
        json.dump(students_file, f, sort_keys=True, indent=4)


#del_student_by_id()


def show_grades(student_id):
    print(students_file[student_id])


def search_student_by_id_or_name(search_name_or_id):
    search_name_or_id = str(search_name_or_id)
    ids = []
    ids = students_file.keys()

    st_values = []
    s_values = students_file.values()

    res = None

    for names in s_values:
        for items in names:
            st_values.append(names[items])

    if search_name_or_id in ids:
        res = (students_file[search_name_or_id])



    elif search_name_or_id in st_values:

        values = students_file.values()
        for names in values:
            for items in names:
                if names[items] == search_name_or_id:
                    res = (names)
    if res is not None:
        return res
    else:
        return ("The entered name or id does not exists in the database ")


from tkinter import *
from tkinter import ttk, messagebox
#Create an instance of tkinter frame or window


def ieee_btn():




    win = Tk()
    # Set the geometry of tkinter frame
    win.geometry("750x250")

    def get_value_ieee():
        try:
            e_text = entry.get()
            value = ieee(e_text)
            Label(win, text=value, font=('Century 15 bold')).pack(pady=20)
        except ValueError:
            messagebox.showerror('Input is invalid', 'Input is invalid')

    # Create an Entry Widget

    entry = ttk.Entry(win, font=('Century 12'), width=40)
    entry.pack(pady=30)

    # Create a button to display the text of entry widget
    button = ttk.Button(win, text="Enter", command=get_value_ieee)
    button.pack()
    win.mainloop()


def search_student_btn():




    win = Tk()
    # Set the geometry of tkinter frame
    win.geometry("750x250")

    def get_value_student():
        try:
            stud_id_name = entry_name_or_id.get()
            stud_value = search_student_by_id_or_name(stud_id_name)
            Label(win, text=stud_value, font=('Century 15 bold')).pack(pady=20)
        except ValueError:
            messagebox.showerror('Input is invalid', 'Input is invalid')

    # Create an Entry Widget

    entry_name_or_id = ttk.Entry(win, font=('Century 12'), width=40)
    entry_name_or_id.pack(pady=30)

    # Create a button to display the text of entry widget
    button = ttk.Button(win, text="Enter", command=get_value_student)
    button.pack()
    win.mainloop()

def show_all_students_id_btn():
    win = Tk()
    # Set the geometry of tkinter frame
    win.geometry("750x250")
    def show_students():
        lst = []
        for strings in students_file:
            lst.append(strings)
            lst.append(students_file[strings])
            lst.append('\n')
        return lst
    def show_all_students():
        try:

            stud_value = show_students()
            Label(win, text=stud_value, font=('Century 15 bold')).pack(pady=20)
        except ValueError:
            messagebox.showerror('Input is invalid', 'Input is invalid')







    # Create a button to display the text of entry widget
    button = ttk.Button(win, text="Show All Students", command=show_all_students)
    button.pack()
    win.mainloop()

def update_student_course_btn():


    win = Tk()
    # Set the geometry of tkinter frame
    win.geometry("750x250")

    def add_new_course_to_existent_student(search_name, course_name,course_grade ):
        search_name = str(search_name)
        course_data = {str(course_name):course_grade}

        values = students_file.values()
        try:
            for names in values:
                for items in names:
                    if names[items] == search_name:
                        new_student_data = names
            new_student_data.update(course_data)
            return "Success"

            students_file.update(new_student)
            with open(database_filename, 'w') as f:
                json.dump(students_file, f, sort_keys=True, indent=4)
            database_filename.close()

        except UnboundLocalError:
            return "Error, the Entered Student is not in DataBase"


    def update_student_course():
            stud_id_name = entry_name_or_id.get()
            course_name = course_name_.get()
            course_grade = course_grade_.get()
            stud_value = add_new_course_to_existent_student(stud_id_name,course_name,course_grade)
            Label(win, text=stud_value, font=('Century 15 bold')).pack(pady=20)


    # Create an Entry Widget

    label = ttk.Label(win, text='Enter Students Name')
    label.pack()
    entry_name_or_id = ttk.Entry(win, font=('Century 12'), width=40,)
    entry_name_or_id.pack(pady=30)
    label = ttk.Label(win, text='Enter the New Course Name')
    label.pack()
    course_name_ = ttk.Entry(win, font=('Century 12'), width=40)
    course_name_.pack(pady=30)
    label = ttk.Label(win, text='Enter the Course Grade')
    label.pack()
    course_grade_ = ttk.Entry(win, font=('Century 12'), width=40)
    course_grade_.pack(pady=30)

    # Create a button to display the text of entry widget
    button = ttk.Button(win, text="Enter", command=update_student_course)

    button.pack()
    win.mainloop()

def delete_student_btn():




    win = Tk()
    # Set the geometry of tkinter frame
    win.geometry("750x250")

    def del_student_by_id(student_id):
        try:
            del students_file[student_id]
            with open(database_filename, 'w') as f:
                json.dump(students_file, f, sort_keys=True, indent=4)
            return "Success"
        except KeyError:
            return "Wrong Id Input"


    def delete_student_():
        try:

            stud_id_name = entry_name_or_id.get()
            stud_value = del_student_by_id(stud_id_name)
            Label(win, text=stud_value, font=('Century 15 bold')).pack(pady=20)
        except ValueError:
            messagebox.showerror('Input is invalid', 'Input is invalid')

    # Create an Entry Widget
    label = ttk.Label(win, text='Enter Students ID')
    label.pack()
    entry_name_or_id = ttk.Entry(win, font=('Century 12'), width=40)
    entry_name_or_id.pack(pady=30)

    # Create a button to display the text of entry widget
    button = ttk.Button(win, text="Enter", command=delete_student_)
    button.pack()
    win.mainloop()
def add_new_student_btn():


    win = Tk()
    # Set the geometry of tkinter frame
    win.geometry("750x250")

    def add(new_student_id , student_name , student_course , student_grade):
        new_student_id = str(new_student_id)
        student_name = str(student_name)
        student_course = str(student_course)
        new_student = {new_student_id:{
            "Name": student_name,
             student_course:student_grade}}
        students_file.update(new_student)

        with open(database_filename, 'w') as f:
            json.dump(students_file, f, sort_keys=True, indent=4)
        return "Success"





    def add_new_student():
            stud_id_name = entry_name_or_id.get()
            stud_name = entry_student_name.get()
            course_name = course_name_.get()
            course_grade = course_grade_.get()
            stud_value = add(stud_id_name,stud_name,course_name,course_grade)
            Label(win, text=stud_value, font=('Century 15 bold')).pack(pady=20)


    # Create an Entry Widget

    label = ttk.Label(win, text='Enter Students Id')
    label.pack()
    entry_name_or_id = ttk.Entry(win, font=('Century 12'), width=40,)
    entry_name_or_id.pack(pady=30)
    label = ttk.Label(win, text='Enter Students Name')
    label.pack()
    entry_student_name = ttk.Entry(win, font=('Century 12'), width=40, )
    entry_student_name.pack(pady=30)
    label = ttk.Label(win, text='Enter the New Course Name')
    label.pack()
    course_name_ = ttk.Entry(win, font=('Century 12'), width=40)
    course_name_.pack(pady=30)
    label = ttk.Label(win, text='Enter the Course Grade')
    label.pack()
    course_grade_ = ttk.Entry(win, font=('Century 12'), width=40)
    course_grade_.pack(pady=30)

    # Create a button to display the text of entry widget
    button = ttk.Button(win, text="Enter", command=add_new_student)

    button.pack()
    win.mainloop()
root = Tk()
root.title("Assistant")
root.geometry("550x500")

btn = Button(text="Conversion",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = ieee_btn
             )
btn.pack()
btn = Button(text="Ieee",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = ieee_btn
             )
btn.pack()
btn = Button(text="Recursive - Functions",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = ieee_btn
             )
btn.pack()
btn = Button(text="Student Search",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = search_student_btn
             )
btn.pack()
btn = Button(text="Show all Students",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = show_all_students_id_btn
             )
btn.pack()
btn = Button(text="Update Students Course",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = update_student_course_btn
             )
btn.pack()
btn = Button(text="Delete Student From the Database",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = delete_student_btn
             )
btn.pack()
btn = Button(text="Add New Student To Database",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             width = "40",
             command = add_new_student_btn
             )
btn.pack()

root.mainloop()