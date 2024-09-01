from tkinter import *
import monthly_expenses as monexp
from savings import calculate_monthly_saving_amount
from tkinter import messagebox
from f_plan import Retier_funds

BACKGROUND_COLOUR = "#C4B078"
STANDARD_FONT = ("Aerial", 25 , "bold")
STANDARD_FONT2 = ("Aerial" , 15 , "bold")

def main_page(widget):
    # Define some constants for the design
    BACKGROUND_COLOUR = '#f0f8ff'  # Light Alice Blue background
    BUTTON_COLOR = '#4CAF50'  # Green button color
    TEXT_COLOR = '#ffffff'  # White text color
    FONT_STYLE = ('Arial', 12)  # Font style for general text
    BUTTON_FONT_STYLE = ('Arial', 12, 'bold')  # Font style for buttons

    # Function to get salary value
    def entry_value():
        return entry_salary.get()

    # Function to get selected option
    def value_ru():
        return clicked.get()

    # Create the main window
    widget.destroy()
    page = Tk()
    page.title("Personal Financing")
    page.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)

    # Title Label
    label_title = Label(page, text="Your Personal Finance App: FINO HELP",
                        font=("Arial", 25, "bold"), bg=BACKGROUND_COLOUR, fg='#333333')
    label_title.grid(row=1, column=1, columnspan=3, pady=10)

    # Drop-down menu for options
    options = ["Urban", "Rural"]
    clicked = StringVar(page)
    clicked.set(options[0])  # Default value
    drop = OptionMenu(page, clicked, *options)
    drop.config(font=FONT_STYLE, bg='#ffffff', fg='#000000', borderwidth=2, relief='solid')
    drop.grid(row=2, column=2, pady=10)

    # Salary Entry
    entry_salary = Entry(page, font=FONT_STYLE, bg='#ffffff', fg='#000000', borderwidth=2, relief='solid')
    entry_salary.insert(0, "Enter Your Salary")
    entry_salary.grid(row=3, column=2, pady=10)

    # Buttons
    button_p = Button(page, text="Plan Future", font=BUTTON_FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                      command=lambda: future_plan(widget=page,salar=entry_value()))
    button_p.grid(row=4, column=1, padx=10, pady=10)

    button_me = Button(page, text="Monthly Expenses", font=BUTTON_FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                       command=lambda: monthly(widget=page, u_r=value_ru(), salar=entry_value()))
    button_me.grid(row=4, column=3, padx=10, pady=10)

    button_s = Button(page, text="Savings", font=BUTTON_FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                      command=lambda: savem(widget=page, salar=entry_value()))
    button_s.grid(row=5, column=3, padx=10, pady=10)

    button_fg = Button(page, text="Finance Guidance", font=BUTTON_FONT_STYLE, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                       command=lambda: print(f"Button Clicked"))
    button_fg.grid(row=5, column=1, padx=10, pady=10)


def savem(widget,salar):
    # Define colors and fonts
    BACKGROUND_COLOUR = "#f0f8ff"  # Light blue background for the window
    LABEL_FONT = ("Helvetica", 16, "bold")  # Bold font for labels
    ENTRY_BG_COLOUR = "#e0f7fa"  # Light cyan background for entry fields
    ENTRY_FONT = ("Helvetica", 14)  # Font for the entry fields
    BUTTON_BG_COLOUR = "#007acc"  # Blue background for buttons
    BUTTON_FONT = ("Helvetica", 14, "bold")  # Bold font for buttons
    BUTTON_TEXT_COLOUR = "white"  # White text for buttons

    # Define your functions (dummy implementation for placeholders)
    def calculation():
        salary = salar
        goal = enter_g.get()
        time = enter_t.get()

        monthly_saving = calculate_monthly_saving_amount(
            years=int(time), goal_saving=int(goal), monthly_salary=int(salary)
        )
        monthly_saving = round(monthly_saving)
        messagebox.showinfo("Savings",
                            f"You need to save {monthly_saving} per month to reach your target in {time} years")

    # Assuming widget is already defined somewhere
    widget.destroy()

    page = Tk()
    page.title("Personal Financing")
    page.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)

    # Savings Label
    label_s = Label(page, text="Savings", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_s.grid(row=1, column=2, columnspan=2, pady=(0, 20))

    # Goal Amount Label and Entry
    label_g = Label(page, text="Enter goal amount", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_g.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    enter_g = Entry(page, font=ENTRY_FONT, bg=ENTRY_BG_COLOUR)
    enter_g.grid(row=2, column=3, padx=10, pady=5)

    # Year Label and Entry
    label_y = Label(page, text="Enter Year", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_y.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    enter_t = Entry(page, font=ENTRY_FONT, bg=ENTRY_BG_COLOUR)
    enter_t.grid(row=3, column=3, padx=10, pady=5)

    # Calculate Button
    button_work = Button(
        page,
        text="Calculate",
        font=BUTTON_FONT,
        bg=BUTTON_BG_COLOUR,
        fg=BUTTON_TEXT_COLOUR,
        command=calculation,
    )
    button_work.grid(row=4, column=3, pady=20)


def future_plan(widget,salar):
    # Define colors and fonts
    BACKGROUND_COLOUR = "#e6f7ff"  # Very light blue background for the window
    TITLE_FONT = ("Helvetica", 24, "bold")  # Bold font for the main title
    LABEL_FONT = ("Helvetica", 14)  # Font for general labels
    ENTRY_BG_COLOUR = "#ffffff"  # White background for entry fields to stand out
    ENTRY_FONT = ("Helvetica", 12)  # Font for the entry fields
    BUTTON_BG_COLOUR = "#007acc"  # Blue background for buttons
    BUTTON_FONT = ("Helvetica", 14, "bold")  # Bold font for buttons
    BUTTON_TEXT_COLOUR = "white"  # White text for buttons

    # Define your functions (dummy implementation for placeholders)
    def calc():
        salary = salar
        t = enter_t.get()
        mon_e = enter_exp.get()

        monthly_saving = Retier_funds(time=t, monthly_exp=mon_e, salary=salary)
        monthly_saving = round(monthly_saving)
        messagebox.showinfo("Savings", f"You need to save {monthly_saving} per month to reach your target in {t} years")

    # Assuming widget is already defined somewhere
    widget.destroy()

    page = Tk()
    page.title("Personal Financing")
    page.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)

    # Title Label
    label_title = Label(page, text="Future Planning", font=TITLE_FONT, bg=BACKGROUND_COLOUR)
    label_title.grid(row=1, column=1, columnspan=2, pady=(0, 20))

    # Monthly Expenses Label and Entry
    label_exp = Label(page, text='Enter your monthly expenses', font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_exp.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    enter_exp = Entry(page, font=ENTRY_FONT, bg=ENTRY_BG_COLOUR)
    enter_exp.grid(row=2, column=2, padx=10, pady=5)

    # Retirement Time Label and Entry
    label_t = Label(page, text="Enter time of retirement", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_t.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    enter_t = Entry(page, font=ENTRY_FONT, bg=ENTRY_BG_COLOUR)
    enter_t.grid(row=3, column=2, padx=10, pady=5)

    # Calculate Button
    button_calc = Button(
        page,
        text="Calculate",
        font=BUTTON_FONT,
        bg=BUTTON_BG_COLOUR,
        fg=BUTTON_TEXT_COLOUR,
        command=calc
    )
    button_calc.grid(row=4, column=2, pady=20)


def monthly(widget , u_r , salar):
    # Define colors and fonts
    BACKGROUND_COLOUR = "#f0f8ff"  # Light blue background
    HEADING_FONT = ("Helvetica", 45, "bold")  # Font for the main heading
    LABEL_FONT = ("Helvetica", 14)  # Font for general labels
    VALUE_FONT = ("Helvetica", 14, "bold")  # Bold font for value labels
    LABEL_BG_COLOUR = "#e0f7fa"  # Light cyan background for labels

    # Initialize the window
    widget.destroy()
    win_month = Tk()
    win_month.title("Monthly Expenses")
    win_month.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)

    # Heading Label
    label_heading = Label(win_month, text="Monthly Expenses", font=HEADING_FONT, bg=BACKGROUND_COLOUR)
    label_heading.grid(row=1, column=1, columnspan=2, pady=(0, 20))

    # Salary Label
    label_s = Label(win_month, text=f"Salary: {salar}", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_s.grid(row=2, column=1, columnspan=2, pady=(0, 20))

    # Calculate and display expenses
    spread = {}

    if u_r == "Urban":
        spread = monexp.salary_calculator_urban(int(salar))
    else:
        spread = monexp.distribution_of_salary_rural(int(salar))

    row = 3
    for key, value in spread.items():
        label_key = Label(win_month, text=f"{key}", font=LABEL_FONT, bg=LABEL_BG_COLOUR, padx=10, pady=5)
        label_key.grid(row=row, column=1, padx=5, pady=5, sticky="w")

        label_value = Label(win_month, text=str(value), font=VALUE_FONT, bg=LABEL_BG_COLOUR, padx=10, pady=5)
        label_value.grid(row=row, column=2, padx=5, pady=5, sticky="w")

        row += 1


def details(widget):
    # Define colors and fonts
    BACKGROUND_COLOUR = "#f0f8ff"  # Light blue background
    LABEL_FONT = ("Helvetica", 12, "bold")  # Bold font for labels
    ENTRY_BG_COLOUR = "#e0f7fa"  # Light cyan background for entry fields
    BUTTON_BG_COLOUR = "#007acc"  # Blue background for button
    BUTTON_FONT = ("Helvetica", 12, "bold")  # Bold font for button

    # Initialize the detail window
    widget.destroy()
    detail = Tk()
    detail.title("Enter Details")
    detail.config(height=500, width=500, padx=100, pady=50, bg=BACKGROUND_COLOUR)

    # Name Label and Entry
    label_name = Label(detail, text="Name", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    entry_name = Entry(detail, bg=ENTRY_BG_COLOUR, font=LABEL_FONT)
    entry_name.grid(row=1, column=2, padx=10, pady=5)

    # Email Label and Entry
    label_mail = Label(detail, text="Email", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_mail.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    entry_mail = Entry(detail, bg=ENTRY_BG_COLOUR, font=LABEL_FONT)
    entry_mail.grid(row=2, column=2, padx=10, pady=5)

    # Age Label and Entry
    label_age = Label(detail, text="Age", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_age.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    entry_age = Entry(detail, bg=ENTRY_BG_COLOUR, font=LABEL_FONT)
    entry_age.grid(row=3, column=2, padx=10, pady=5)

    # Gender Label and Entry
    label_gender = Label(detail, text="Gender", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_gender.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    entry_gender = Entry(detail, bg=ENTRY_BG_COLOUR, font=LABEL_FONT)
    entry_gender.grid(row=4, column=2, padx=10, pady=5)

    # Marital Status Label and Entry
    label_married = Label(detail, text="Marital Status", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_married.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    entry_married = Entry(detail, bg=ENTRY_BG_COLOUR, font=LABEL_FONT)
    entry_married.grid(row=5, column=2, padx=10, pady=5)

    # Salary Label and Entry
    label_salary = Label(detail, text="Salary", font=LABEL_FONT, bg=BACKGROUND_COLOUR)
    label_salary.grid(row=6, column=1, padx=10, pady=5, sticky="w")
    entry_salary = Entry(detail, bg=ENTRY_BG_COLOUR, font=LABEL_FONT)
    entry_salary.grid(row=6, column=2, padx=10, pady=5)

    # Submit Button
    end_page = Button(detail, text="Submit", command=lambda: main_page(detail), bg=BUTTON_BG_COLOUR, fg="white",
                      font=BUTTON_FONT)
    end_page.grid(row=7, column=2, pady=20)


def insert_detail():
    BACKGROUND_COLOUR = "#f0f0f0"  # Set a background color
    STANDARD_FONT = ("Helvetica", 12)  # Define a standard font for labels and entries
    BUTTON_FONT = ("Helvetica", 12, "bold")  # Define a font for buttons
    BUTTON_COLOR = "#4CAF50"  # Define a button color
    BUTTON_TEXT_COLOR = "#ffffff"  # Define a button text color


    window.destroy()
    window_detail = Tk()
    window_detail.title("Login")
    window_detail.config(height=500, width=500, padx=50, pady=50, bg=BACKGROUND_COLOUR)

    # Username Label
    label_usnm = Label(window_detail, text="Username", font=STANDARD_FONT, bg=BACKGROUND_COLOUR)
    label_usnm.grid(row=1, column=1, padx=10, pady=10, sticky="e")

    # Username Entry
    entry_usnm = Entry(window_detail, font=STANDARD_FONT)
    entry_usnm.grid(row=1, column=2, padx=10, pady=10)

    # Email Label
    label_mail = Label(window_detail, text="Email", font=STANDARD_FONT, bg=BACKGROUND_COLOUR)
    label_mail.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    # Email Entry
    entry_mail = Entry(window_detail, font=STANDARD_FONT)
    entry_mail.grid(row=2, column=2, padx=10, pady=10)

    # Password Label
    label_pass = Label(window_detail, text="Password", font=STANDARD_FONT, bg=BACKGROUND_COLOUR)
    label_pass.grid(row=3, column=1, padx=10, pady=10, sticky="e")

    # Password Entry
    entry_pass = Entry(window_detail, font=STANDARD_FONT, show="*")
    entry_pass.grid(row=3, column=2, padx=10, pady=10)

    # Spacer Label
    label_b1 = Label(window_detail, bg=BACKGROUND_COLOUR)
    label_b1.grid(row=4, column=1)

    # Login Button
    end_page = Button(window_detail, text="Login", font=BUTTON_FONT, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                          command=lambda: details(window_detail))
    end_page.grid(row=5, column=1, columnspan=2, pady=20)

window = Tk()
window.title("FINO HELP")
window.config(height=500, width=500)
window.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)  # Updated background color


# Create a canvas for the logo
canvas_logo = Canvas(window, width=500, height=400, bg=BACKGROUND_COLOUR, highlightthickness=0)
logo_image = PhotoImage(file="LOGO.png")
canvas_logo.create_image(225, 200, image=logo_image)
canvas_logo.grid(row=1, column=1)

# Label for introductory text with updated font and color
label_intro = Label(window, text="Are you concerned about your financial future?\n"
                                 "Don’t know how to manage your financial life?\n"
                                 "Then we are here, the Fino Help team, with our amazing app FINO HELP.",
                    font=("Arial", 14, "italic"), fg="#333333", bg=BACKGROUND_COLOUR, wraplength=400, justify="center")
label_intro.grid(row=2, column=1, pady=20)

# Button to start, with updated font and color
button_start = Button(window, text="Let's start", font=("Arial", 16, "bold"), fg="white", bg="#4caf50",
                      command=insert_detail, relief=RAISED, bd=3, padx=10, pady=5)
button_start.grid(row=3, column=1, pady=20)

window.mainloop()
