import tkinter as tk
from tkinter import messagebox
import random


# ==========================
# QUOTE DATA
# ==========================

quotes = [
    {
        "quote": "The future depends on what you do today.",
        "author": "Mahatma Gandhi"
    },
    {
        "quote": "Success is not final, failure is not fatal.",
        "author": "Winston Churchill"
    },
    {
        "quote": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt"
    },
    {
        "quote": "Dream big and never give up.",
        "author": "Unknown"
    }
]


favorites = []


# ==========================
# FUNCTIONS
# ==========================

def show_quote():

    selected = random.choice(quotes)

    quote_text.config(
        text=f'"{selected["quote"]}"'
    )

    author_text.config(
        text=f'- {selected["author"]}'
    )


def add_quote():

    new_quote = quote_entry.get()
    new_author = author_entry.get()


    if new_quote == "" or new_author == "":
        messagebox.showwarning(
            "Missing Data",
            "Please enter quote and author"
        )

    else:

        quotes.append(
            {
                "quote": new_quote,
                "author": new_author
            }
        )


        messagebox.showinfo(
            "Success",
            "New Quote Added"
        )


        quote_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)



def save_favorite():

    current_quote = quote_text["text"]
    current_author = author_text["text"]


    favorites.append(
        current_quote + "\n" + current_author
    )


    messagebox.showinfo(
        "Saved",
        "Quote added to favorites"
    )



def show_favorites():

    if len(favorites) == 0:

        messagebox.showinfo(
            "Favorites",
            "No favorite quotes saved"
        )

    else:

        messagebox.showinfo(
            "Favorite Quotes",
            "\n\n".join(favorites)
        )



# ==========================
# GUI DESIGN
# ==========================

window = tk.Tk()

window.title("Quote Generator")
window.geometry("500x600")

window.config(bg="#f2f2f2")



title = tk.Label(
    window,
    text="✨ Quote Generator ✨",
    font=("Arial",22,"bold"),
    bg="#f2f2f2"
)

title.pack(pady=20)



quote_text = tk.Label(
    window,
    text="Click Generate Quote",
    font=("Arial",16),
    wraplength=400,
    bg="#f2f2f2"
)

quote_text.pack(pady=20)



author_text = tk.Label(
    window,
    text="",
    font=("Arial",14,"italic"),
    bg="#f2f2f2"
)

author_text.pack()



generate_btn = tk.Button(
    window,
    text="Generate Quote",
    command=show_quote,
    width=20
)

generate_btn.pack(pady=10)



favorite_btn = tk.Button(
    window,
    text="Save Favorite",
    command=save_favorite,
    width=20
)

favorite_btn.pack(pady=10)



view_btn = tk.Button(
    window,
    text="View Favorites",
    command=show_favorites,
    width=20
)

view_btn.pack(pady=10)



# Add Quote Section

tk.Label(
    window,
    text="Add New Quote",
    font=("Arial",16,"bold"),
    bg="#f2f2f2"
).pack(pady=15)



quote_entry = tk.Entry(
    window,
    width=40
)

quote_entry.pack()



author_entry = tk.Entry(
    window,
    width=40
)

author_entry.pack(pady=5)



add_btn = tk.Button(
    window,
    text="Add Quote",
    command=add_quote,
    width=20
)

add_btn.pack(pady=10)



window.mainloop()