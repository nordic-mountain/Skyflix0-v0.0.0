import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
import requests
from bs4 import BeautifulSoup

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Simple Search Engine")
        self.create_widgets()

    def create_widgets(self):
        self.search_label = ttk.Label(self.master, text="Search:")
        self.search_label.place(x=10, y=10)

        self.search_entry = ttk.Entry(self.master, width=50)
        self.search_entry.place(x=60, y=10)

        self.search_button = ttk.Button(self.master, text="Search", command=self.search)
        self.search_button.place(x=370, y=10)

        self.quit_button = ttk.Button(self.master, text="Quit", command=self.quit)
        self.quit_button.place(x=450, y=10)

        self.results_label = ttk.Label(self.master, text="Results:")
        self.results_label.place(x=10, y=50)

        self.results_frame = ttk.Frame(self.master)
        self.results_frame.place(x=10, y=80)

    def search(self):
        query = self.search_entry.get()
        url = "https://www.google.com/search?q=" + query
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        for anchor in soup.find_all("a"):
            link = anchor.get("href")
            if link.startswith("/url?q="):
                title = anchor.text.strip()
                links.append((title, link[7:]))
        links = links[:10] # Get the top 10 links
        for child in self.results_frame.winfo_children():
            child.destroy() # Clear the results frame
        row = 0
        for i, (title, link) in enumerate(links, 1):
            result_frame = ttk.Frame(self.results_frame)
            result_frame.grid(row=row, column=0, sticky="w")
            result_label = ttk.Label(result_frame, text=title, font="-weight bold")
            result_label.grid(row=0, column=0, sticky="w")
            result_link = ttk.Label(result_frame, text=link, foreground="green", cursor="hand2")
            result_link.grid(row=1, column=0, sticky="w")
            result_link.bind("<Button-1>", lambda e, url=link: webbrowser.open_new(url))
            row += 2 # Add extra row for spacing between results

root = tk.Tk()
root.geometry("600x800")
app = Application(master=root)
app.mainloop()
