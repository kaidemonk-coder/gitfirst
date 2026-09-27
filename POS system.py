import tkinter as tk
import sys
import os



product_entries=[]
#setup
main_window=tk.Tk()
main_window.title('Ultimate Cracked POS system Skeleton (No fancy GUI version)')
main_window.geometry('800x800')

#scrollbar frame
canvas=tk.Canvas(main_window)
scrollbar=tk.Scrollbar(main_window,orient='vertical',command=canvas.yview)
scrollable_frame=tk.Frame(canvas)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


canvas_window = canvas.create_window((400, 0), window=scrollable_frame, anchor="n")



scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

#widgets
product1_label=tk.Label(scrollable_frame,text="enter name of product 1: ")
product1_label.pack()
product1_name_entry=tk.Entry(scrollable_frame)
product1_name_entry.pack()


product1_qty_label=tk.Label(scrollable_frame,text="enter number of product 1 being bought: ")
product1_qty_label.pack()
product1_qty_entry=tk.Entry(scrollable_frame)
product1_qty_entry.pack()

product1_cost_label=tk.Label(scrollable_frame,text="enter cost of product 1: ")
product1_cost_label.pack()
product1_cost_entry=tk.Entry(scrollable_frame)
product1_cost_entry.pack()




#function to be defined before result_label
def get_validated_product(name_entry, qty_entry, cost_entry, product_label):
    name = name_entry.get().strip()
    if name == "":
        raise ValueError(f"{product_label}: Enter a valid input...")

    try:
        qty = int(qty_entry.get())
    except ValueError:
        raise ValueError(f"{product_label}: Enter a valid input...")

    try:
        cost = float(cost_entry.get())
    except ValueError:
        raise ValueError(f"{product_label}: Enter a valid input...")

    if qty <= 0:
        raise ValueError(f"{product_label}: Enter a valid input...")
    if cost < 0:
        raise ValueError(f"{product_label}: Enter a valid input...")

    return name, qty, cost


def mather():
    try:
        prod1, qty1, cost1 = get_validated_product(
            product1_name_entry, product1_qty_entry, product1_cost_entry, "Product 1"
        )
        total = qty1 * cost1

        for i, (name_entry, qty_entry, cost_entry) in enumerate(product_entries, start=2):
            name, qty, cost = get_validated_product(
                name_entry, qty_entry, cost_entry, f"Product {i}"
            )
            total += qty * cost

        result_label.config(text=f'TOTAL COST TO BE PAID: ${total}')

    except ValueError as e:
        result_label.config(text=f"Invalid input — {e}", fg="red")



def AddProduct():
    new_prod_label=tk.Label(scrollable_frame,text="enter name of additional product")
    new_prod_label.pack()
    new_prod_entry=tk.Entry(scrollable_frame)
    new_prod_entry.pack()

    new_prod_qty=tk.Label(scrollable_frame,text="enter number of additional product")
    new_prod_qty.pack()
    new_prod_qty_entry=tk.Entry(scrollable_frame)
    new_prod_qty_entry.pack()

    new_prod_cost=tk.Label(scrollable_frame,text="enter cost of additional product")
    new_prod_cost.pack()
    new_prod_cost_entry=tk.Entry(scrollable_frame)
    new_prod_cost_entry.pack()

    product_entries.append((new_prod_entry,new_prod_qty_entry,new_prod_cost_entry))

    calc_button.pack_forget()
    calc_button.pack()
    add_button.pack_forget()
    add_button.pack()
    result_label.pack_forget()
    result_label.pack()
    rerun_button.pack_forget()
    rerun_button.pack()

def rerun():
    main_window.destroy()
    os.execv(sys.executable,['python']+ sys.argv)




#final result display
result_label=tk.Label(scrollable_frame,text=" ")
result_label.pack()

calc_button=tk.Button(scrollable_frame,text="calculate",command=mather)
calc_button.pack()

add_button=tk.Button(scrollable_frame,text='add another product',command=AddProduct)
add_button.pack()

rerun_button=tk.Button(scrollable_frame,text='Rerun',command=rerun)
rerun_button.pack()




main_window.mainloop()