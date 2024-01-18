import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from FinTrackDBSQ import FinTrackDBSQ

class FinTrackGUI(customtkinter.CTk):

# === GENERAL WINDOW SETTINGS ==========================
    def __init__(self, dataBase=FinTrackDBSQ('AppDb.db')):
        super().__init__()
        self.db = dataBase

        self.title('FinTracker')
        self.geometry('1400x600')
        self.config(bg='#88CABE')
        self.resizable(True, True)

        # used fonts
        self.FHeading = ('Helvetica', 20, 'bold')
        self.FWidget = ('Helvetica', 14)
        self.FSubWidget = ('Helvetica', 10, 'italic')
        self.FEntry = ('Helvetica', 14, 'bold')
        self.FEntryMini = ('Helvetica', 11, 'bold')
        self.FTreeview = ('Helvetica', 11, 'bold')

# === ENTRY/COMBO WIDGETS + PLACEMENTS ========================

        # [Entry] id - 000
        self.id_label = self.newCtkWidgetLabel('Entry (#)')
        self.id_label.place(x=1020, y=25)
        self.id_entry = self.newCtkEntryMini()
        self.id_entry.place(x=1020, y=50)

        # [Entry] DATE & TIME - YYMMDD
        self.date_label = self.newCtkWidgetLabel('Date & Time (YYMMDD 2400)')
        self.date_label.place(x=1130, y=25)
        self.date_entry = self.newCtkEntry()
        self.date_entry.place(x=1130, y=50)

        # [Combo] CASH FLOW TYPE — Earning / Expense
        self.cf_type_label = self.newCtkWidgetLabel('Cash Flow Type')
        self.cf_type_label.place(x=1020, y=90)
        self.cf_type_cboxVar = StringVar()
        self.cf_type_cboxOptions = ['=', 'Earning', 'Expense']
        self.cf_type_cbox = self.newCtkComboBox(options=self.cf_type_cboxOptions, 
                                    entryVariable=self.cf_type_cboxVar)
        self.cf_type_cbox.place(x=1020, y=115)
        
        # [Label] SPECIFIC CATEGORIES — Earning / Expense
        self.cf_specific_label = self.newCtkWidgetLabel('Specific Categories')
        self.cf_specific_label.place(x=1020, y=155)

        # [Combo] EARNING SOURCE
        self.earning_label = self.newCtkSubWidgetLabel('For Earning Sources')
        self.earning_label.place(x=1040, y=208)
        self.earning_cboxVar = StringVar()
        self.earning_cboxOptions = ['=', 'Salary (Work)', 'Passive Income', 'Gift', 'Borrowed', 'Payed Owe', 'Others']
        self.earning_cbox = self.newCtkComboBoxMini(options=self.earning_cboxOptions, 
                                    entryVariable=self.earning_cboxVar)
        self.earning_cbox.place(x=1020, y=180)

        # [Combo] EXPENSE OUT
        self.expense_label = self.newCtkSubWidgetLabel('For Expense Outs')
        self.expense_label.place(x=1220, y=208)
        self.expense_cboxVar = StringVar()
        self.expense_cboxOptions = ['=', 'Grocery', 'Transportation', 'School Necessities', 'Work Necessities', 'Home Necessities', 'Utility Bills', 'Medical Bills', 'Taxes', 'Other Insurance', 'Housing/Rent', 'Entertainment', 'Lended', 'Settled Dues', 'Others']
        self.expense_cbox = self.newCtkComboBoxMini(options=self.expense_cboxOptions, 
                                    entryVariable=self.expense_cboxVar)
        self.expense_cbox.place(x=1200, y=180)
        
        # [Combo] MODE OF PAYMENT
        self.paymode_label = self.newCtkWidgetLabel('Mode of Payment')
        self.paymode_label.place(x=1020, y=235)
        self.paymode_cboxVar = StringVar()
        self.paymode_cboxOptions = ['=', 'Cash', 'Bank Transfer', 'Cheque', 'GCash', 'PayMaya', 'Other Digital Wallets']
        self.paymode_cbox = self.newCtkComboBox(options=self.paymode_cboxOptions, 
                                    entryVariable=self.paymode_cboxVar)
        self.paymode_cbox.place(x=1020, y=260)

        # [Entry] AMOUNT
        self.amount_label = self.newCtkWidgetLabel('Amount (₱)')
        self.amount_label.place(x=1020, y=300)
        self.amount_entry = self.newCtkEntryLarge()
        self.amount_entry.place(x=1020, y=325)

# === FUNCTIONAL BUTTONS =========================================

        # [Add Button]
        self.add_button = self.newCtkButton(text='Add statement',
                                onClickHandler=self.add_entry,
                                bgColor='#88CABE',
                                fgColor='#DAFFA3',
                                hoverColor='#2DFF07',
                                borderColor='#2DFF07')
        self.add_button.place(x=1020,y=400)

        # [Update Button]
        self.update_button = self.newCtkButton(text='Update statement',
                                    onClickHandler=self.update_entry,
                                    bgColor='#88CABE',
                                    fgColor='#FFDCA3',
                                    hoverColor='#FFAF11',
                                    borderColor='#FFAF11')
        self.update_button.place(x=1020,y=440)

        # [New Button]
        self.new_button = self.newCtkButton(text='New statement',
                                onClickHandler=lambda:self.clear_form(True),
                                bgColor='#88CABE',
                                fgColor='#FFDCA3',
                                hoverColor='#FFAF11',
                                borderColor='#FFAF11')
        self.new_button.place(x=1020,y=480)

        # [Delete Button]
        self.delete_button = self.newCtkButton(text='Delete statement',
                                    onClickHandler=self.delete_entry,
                                    bgColor='#88CABE',
                                    fgColor='#FFA3A3',
                                    hoverColor='#FF3319',
                                    borderColor='#FF3319')
        self.delete_button.place(x=1020,y=520)

        # [Export Buttons]
        self.export_button = self.newCtkButtonMini(text='Export to CSV',
                                    onClickHandler=self.export_to_csv,
                                    bgColor='#88CABE',
                                    fgColor='#A3FFEE',
                                    hoverColor='#009D8D',
                                    borderColor='#009D8D')
        self.export_button.place(x=30,y=520)

        self.export_button = self.newCtkButtonMini(text='Export to JSON',
                                    onClickHandler=self.export_to_json,
                                    bgColor='#88CABE',
                                    fgColor='#A3FFEE',
                                    hoverColor='#009D8D',
                                    borderColor='#009D8D')
        self.export_button.place(x=240,y=520)


# === DATABASE TREE VIEW MAIN ====================================
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        # [Treeview Layout]
        self.style.configure('Treeview', 
                        font=self.FTreeview, 
                        foreground='#009D8D',
                        background='#FFFFFF',
                        fieldbackground='#FFFFFF',
                        bordercolor='#88CABE',
                        rowheight=40)

        self.style.configure('Treeview.Heading', 
                        font=self.FTreeview, 
                        foreground='#FFB319',
                        background='#005149',
                        bordercolor='#005149',
                        borderwidth=8,
                        fieldlbackground='#008782')

        self.style.map('Treeview', background=[('selected', '#00D6E6')])

        # [Treeview Column Assignments]
        self.tree = ttk.Treeview(self, height=40, padding=0)
        self.tree['columns'] = ('id', 'date', 'cf_type', 'earning', 'expense', 'paymode', 'amount')
        self.tree.column('#0', width=0, stretch=tk.NO)

        self.tree.column('id', anchor=tk.CENTER, width=40)
        self.tree.column('date', anchor=tk.CENTER, width=110)
        self.tree.column('cf_type', anchor=tk.CENTER, width=180)
        self.tree.column('earning', anchor=tk.CENTER, width=180)
        self.tree.column('expense', anchor=tk.CENTER, width=180)
        self.tree.column('paymode', anchor=tk.CENTER, width=180)
        self.tree.column('amount', anchor=tk.CENTER, width=220)

        self.tree.heading('id', text='ID')
        self.tree.heading('date', text='Date')
        self.tree.heading('cf_type', text='Cash Flow Type')
        self.tree.heading('earning', text='Earning Sources')
        self.tree.heading('expense', text='Expense Outs')
        self.tree.heading('paymode', text='Mode of Payment')
        self.tree.heading('amount', text='Amount (₱)')

        self.tree.place(x=40, y=40, width=1200, height=600)
        self.tree.bind('<ButtonRelease>', self.read_display_data)

        self.add_to_treeview()


# === LABEL TEMPLATES ====================================
    def newCtkWidgetLabel(self, text = 'CTK Widget Label'):
        widget_Font=self.FWidget
        widget_TextColor='#2E2E2E'
        widget_BgColor='#88CABE'

        widget = customtkinter.CTkLabel(self, 
                                    text=text,
                                    font=widget_Font, 
                                    text_color=widget_TextColor,
                                    bg_color=widget_BgColor)
        return widget
    
    def newCtkSubWidgetLabel(self, text = 'CTK SubWidget Label'):
        widget_Font=self.FSubWidget
        widget_TextColor='#2E2E2E'
        widget_BgColor='#88CABE'

        widget = customtkinter.CTkLabel(self, 
                                    text=text,
                                    font=widget_Font, 
                                    text_color=widget_TextColor,
                                    bg_color=widget_BgColor)
        return widget


# === WIDGET TEMPLATES ====================================

    # [New ENTRY Widgets]
    def newCtkEntry(self, text = 'CTK Entry Label'):
        widget_Font=self.FEntry
        widget_TextColor='#008782'
        widget_BGColor='#88CABE'
        widget_FgColor='#FFFFFF'
        widget_BorderColor='#FFFFFF'
        widget_CornerRadius=20
        widget_width=238
        widget_Height=35

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    bg_color=widget_BGColor,
                                    border_color=widget_BorderColor,
                                    width=widget_width,
                                    height=widget_Height,
                                    corner_radius=widget_CornerRadius)
        return widget
    
    def newCtkEntryMini(self, text = 'CTK Mini Entry Label'):
        widget_Font=self.FEntry
        widget_TextColor='#008782'
        widget_BGColor='#88CABE'
        widget_FgColor='#FFFFFF'
        widget_BorderColor='#FFFFFF'
        widget_CornerRadius=20
        widget_width=100
        widget_Height=35

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    bg_color=widget_BGColor,
                                    border_color=widget_BorderColor,
                                    width=widget_width,
                                    height=widget_Height,
                                    corner_radius=widget_CornerRadius)
        return widget
    
    def newCtkEntryLarge(self, text = 'CTK Large Entry Label'):
        widget_Font=self.FEntry
        widget_TextColor='#008782'
        widget_BGColor='#88CABE'
        widget_FgColor='#FFFFFF'
        widget_BorderColor='#FFFFFF'
        widget_CornerRadius=20
        widget_width=350
        widget_Height=60

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    bg_color=widget_BGColor,
                                    border_color=widget_BorderColor,
                                    width=widget_width,
                                    height=widget_Height,
                                    corner_radius=widget_CornerRadius)
        return widget


    # [New COMBO Box Widgets]
    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.FEntry
        widget_TextColor='#008782'
        widget_BGColor='#88CABE'
        widget_FgColor='#FFFFFF'
        widget_DropdownFGColor='#005149'
        widget_ButtonHoverColor='#005149'
        widget_ButtonColor='#009D8D'
        widget_BorderColor='#FFFFFF'
        widget_CornerRadius=20
        widget_width=350
        widget_Height=35
        widget_Options=options

        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        bg_color=widget_BGColor,
                                        dropdown_fg_color=widget_DropdownFGColor,
                                        button_hover_color=widget_ButtonHoverColor,
                                        button_color=widget_ButtonColor,
                                        border_color=widget_BorderColor,
                                        width=widget_width,
                                        height=widget_Height,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly',
                                        corner_radius=widget_CornerRadius)
        
        # 1st option = default
        widget.set(options[0])

        return widget

    def newCtkComboBoxMini(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.FEntryMini
        widget_TextColor='#008782'
        widget_BGColor='#88CABE'
        widget_FgColor='#FFFFFF'
        widget_DropdownFGColor='#005149'
        widget_ButtonHoverColor='#005149'
        widget_ButtonColor='#009D8D'
        widget_BorderColor='#FFFFFF'
        widget_CornerRadius=20
        widget_width=170
        widget_Height=35
        widget_Options=options

        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        bg_color=widget_BGColor,
                                        dropdown_fg_color=widget_DropdownFGColor,
                                        button_hover_color=widget_ButtonHoverColor,
                                        button_color=widget_ButtonColor,
                                        border_color=widget_BorderColor,
                                        width=widget_width,
                                        height=widget_Height,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly',
                                        corner_radius=widget_CornerRadius)
        
        # 1st option = default
        widget.set(options[0])

        return widget

    # [New BUTTON Widgets]
    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#88CABE', hoverColor='#FF5002', bgColor='#88CABE', borderColor='#F15704'):
        widget_Font=self.FWidget
        widget_TextColor='#2E2E2E'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_Borderwidth=2
        widget_Cursor='hand2'
        widget_CornerRadius=20
        widget_width=350
        widget_Height=35
        widget_Function=onClickHandler

        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_Borderwidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_width,
                                        height=widget_Height)
        return widget
    
    def newCtkButtonMini(self, text = 'CTK Button', onClickHandler=None, fgColor='#88CABE', hoverColor='#FF5002', bgColor='#88CABE', borderColor='#F15704'):
        widget_Font=self.FWidget
        widget_TextColor='#2E2E2E'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_Borderwidth=2
        widget_Cursor='hand2'
        widget_CornerRadius=20
        widget_width=200
        widget_Height=35
        widget_Function=onClickHandler

        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_Borderwidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_width,
                                        height=widget_Height)
        return widget


# === TREEVIEW HANDLES ====================================
    
    def add_to_treeview(self):
        statements = self.db.fetch_statements()
        self.tree.delete(*self.tree.get_children())
        for statement in statements:
            print(statement)
            self.tree.insert('', END, values=statement)

    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.id_entry.delete(0, END) 
        self.date_entry.delete(0, END)
        self.cf_type_cboxVar.set('=')
        self.earning_cboxVar.set('=')
        self.expense_cboxVar.set('=')
        self.paymode_cboxVar.set('=')  
        self.amount_entry.delete(0, END)

    def read_display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear_form()
            self.id_entry.insert(0, row[0])
            self.date_entry.insert(0, row[1])
            self.cf_type_cboxVar.set(row[2])
            self.earning_cboxVar.set(row[3])
            self.expense_cboxVar.set(row[4])
            self.paymode_cboxVar.set(row[5])
            self.amount_entry.insert(0, row[6])
        else:
            pass

    def add_entry(self):
        id=self.id_entry.get()
        date=self.date_entry.get()
        cf_type=self.cf_type_cboxVar.get()
        earning=self.earning_cboxVar.get()
        expense=self.expense_cboxVar.get()
        paymode=self.paymode_cboxVar.get()
        amount=self.amount_entry.get()

        if not (id and date and cf_type and earning and expense and paymode and amount):
            messagebox.showerror('Error', 'Enter all fields.')
        elif self.db.id_exists(id):
            messagebox.showerror('Error', 'id already exists')
        else:
            self.db.insert_statement(id, date, cf_type, earning, expense, paymode, amount)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been inserted')

    def delete_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose an statement to delete')
        else:
            id = self.id_entry.get()
            self.db.delete_statement(id)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been deleted')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose an statement to update')
        else:
            id = self.id_entry.get()
            date = self.date_entry.get()
            new_id=self.id_entry.get()
            new_date=self.date_entry.get()
            new_cf_type=self.cf_type_cboxVar.get()
            new_earning=self.earning_cboxVar.get()
            new_expense=self.expense_cboxVar.get()
            new_paymode=self.paymode_cboxVar.get()
            new_amount=self.amount_entry.get()
            self.db.update_statement(new_date, new_cf_type, new_earning, new_expense, new_paymode, new_amount, id)
            self.db.update_statementID(new_id, date)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been updated')


# === DATA EXPORT ====================================
            
    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbName}.csv')

    def export_to_json(self):
        self.db.export_json()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbName}.json')
