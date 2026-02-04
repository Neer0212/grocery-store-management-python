from tkinter import *
from tkinter import messagebox
import database

root = Tk()
root.title("Grocery Store Management System")
root.withdraw()  # hidden until login


def add_item():
    database.add_product(
        name_entry.get(),
        float(price_entry.get()),
        int(qty_entry.get()),
        int(threshold_entry.get())
    )
    messagebox.showinfo("Success", "Product Added!")


def show_items():
    items = database.get_products()
    listbox.delete(0, END)

    serial = 1
    for item in items:
        # store real id inside tuple but show serial
        display = (serial, item[1], item[2], item[3], item[4], item[0])
        listbox.insert(END, display)

        if item[3] <= item[4]:
            messagebox.showwarning(
                "Low Stock Alert",
                f"{item[1]} is running low!"
            )

        serial += 1



def delete_item():
    selected = listbox.get(ACTIVE)
    real_id = selected[5]
    database.delete_product(real_id)
    show_items()



def update_item():
    selected = listbox.get(ACTIVE)
    real_id = selected[5]
    database.update_quantity(real_id, int(qty_entry.get()))
    show_items()



def open_billing():
    bill_win = Toplevel(root)
    bill_win.title("Billing")

    Label(bill_win, text="Quantity").grid(row=0, column=0)
    qty_entry_bill = Entry(bill_win)
    qty_entry_bill.grid(row=0, column=1)

    def generate():
        selected = listbox.get(ACTIVE)
        if not selected:
            return

        real_id = selected[5]   # correct index
        qty = int(qty_entry_bill.get())

        total = database.make_sale(real_id, qty)

        if total is None:
            messagebox.showerror("Error", "Not enough stock")
        else:
            messagebox.showinfo("Bill", f"Total: ₹{total}")
            show_items()

    Button(bill_win, text="Generate Bill", command=generate).grid(row=1, column=0, columnspan=2)



def search_item():
    items = database.search_product(search_entry.get())
    listbox.delete(0, END)
    for item in items:
        listbox.insert(END, item)


# ---------- UI ----------

Label(root, text="Product Name").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Price").grid(row=1, column=0)
price_entry = Entry(root)
price_entry.grid(row=1, column=1)

Label(root, text="Quantity").grid(row=2, column=0)
qty_entry = Entry(root)
qty_entry.grid(row=2, column=1)

Label(root, text="Threshold").grid(row=3, column=0)
threshold_entry = Entry(root)
threshold_entry.grid(row=3, column=1)

Button(root, text="Add Product", command=add_item).grid(row=4, column=0)
Button(root, text="Show Products", command=show_items).grid(row=4, column=1)
Button(root, text="Delete Selected", command=delete_item).grid(row=4, column=2)
Button(root, text="Update Quantity", command=update_item).grid(row=5, column=0)
Button(root, text="Open Billing", command=open_billing).grid(row=5, column=1)

Label(root, text="Search").grid(row=6, column=0)
search_entry = Entry(root)
search_entry.grid(row=6, column=1)
Button(root, text="Search", command=search_item).grid(row=6, column=2)

listbox = Listbox(root, width=70)
listbox.grid(row=7, column=0, columnspan=3)

def start_app():
    root.deiconify()
    root.mainloop()

