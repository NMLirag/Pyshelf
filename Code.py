import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

# Store user data
users = {
    "admin": {"password": "admin", "type": "Admin"}
}

# List of dictionaries to store book information
books = [
    {"id": "B001", "title": "Engineering Mechanics", "author": "R.C. Hibbeler", "shelf": "A1"},
    {"id": "B002", "title": "Strength of Materials", "author": "Ferdinand L. Singer", "shelf": "A2"},
    {"id": "B003", "title": "Thermodynamics: An Engineering Approach", "author": "Yunus A. Çengel", "shelf": "A3"},
    {"id": "B004", "title": "Fluid Mechanics", "author": "Frank M. White", "shelf": "A4"},
    {"id": "B005", "title": "Mechanics of Materials", "author": "R.C. Hibbeler", "shelf": "A5"},
    {"id": "B006", "title": "Engineering Circuit Analysis", "author": "William H. Hayt Jr.", "shelf": "A6"},
    {"id": "B007", "title": "Control Systems Engineering", "author": "Norman S. Nise", "shelf": "A7"},
    {"id": "B008", "title": "Structural Analysis", "author": "Russell C. Hibbeler", "shelf": "A8"},
    {"id": "B009", "title": "Engineering Economy", "author": "Leland Blank", "shelf": "A9"},
    {"id": "B010", "title": "Materials Science and Engineering", "author": "William D. Callister", "shelf": "A10"},
    {"id": "B011", "title": "Machine Design", "author": "Robert L. Norton", "shelf": "A11"},
    {"id": "B012", "title": "Signals and Systems", "author": "Alan V. Oppenheim", "shelf": "A12"},
    {"id": "B013", "title": "Digital Design", "author": "M. Morris Mano", "shelf": "A13"},
    {"id": "B014", "title": "Environmental Engineering", "author": "Mackenzie L. Davis", "shelf": "A14"},
    {"id": "B015", "title": "Engineering Mathematics", "author": "K.A. Stroud", "shelf": "A15"},
    {"id": "B016", "title": "Transportation Engineering", "author": "C.J. Khisty", "shelf": "A16"},
    {"id": "B017", "title": "Surveying", "author": "Jack C. McCormac", "shelf": "A17"},
    {"id": "B018", "title": "Hydraulics and Fluid Mechanics", "author": "Modi & Seth", "shelf": "A18"},
    {"id": "B019", "title": "Introduction to Heat Transfer", "author": "Frank P. Incropera", "shelf": "A19"},
    {"id": "B020", "title": "Principles of Geotechnical Engineering", "author": "Braja M. Das", "shelf": "A20"},

    {"id": "B021", "title": "Introduction to Algorithms", "author": "Cormen, Leiserson, Rivest & Stein", "shelf": "B1"},
    {"id": "B022", "title": "Database System Concepts", "author": "Abraham Silberschatz", "shelf": "B2"},
    {"id": "B023", "title": "Computer Networking", "author": "James Kurose & Keith Ross", "shelf": "B3"},
    {"id": "B024", "title": "Operating System Concepts", "author": "Abraham Silberschatz", "shelf": "B4"},
    {"id": "B025", "title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell & Peter Norvig", "shelf": "B5"},
    {"id": "B026", "title": "Programming Language Pragmatics", "author": "Michael L. Scott", "shelf": "B6"},
    {"id": "B027", "title": "Clean Code", "author": "Robert C. Martin", "shelf": "B7"},
    {"id": "B028", "title": "The Pragmatic Programmer", "author": "Andrew Hunt & David Thomas", "shelf": "B8"},
    {"id": "B029", "title": "Design Patterns", "author": "Erich Gamma et al.", "shelf": "B9"},
    {"id": "B030", "title": "Computer Organization and Design", "author": "David Patterson & John Hennessy", "shelf": "B10"},
    {"id": "B031", "title": "Cryptography and Network Security", "author": "William Stallings", "shelf": "B11"},
    {"id": "B032", "title": "Software Engineering", "author": "Ian Sommerville", "shelf": "B12"},
    {"id": "B033", "title": "Theory of Computation", "author": "Michael Sipser", "shelf": "B13"},
    {"id": "B034", "title": "Human-Computer Interaction", "author": "Alan Dix et al.", "shelf": "B14"},
    {"id": "B035", "title": "HTML5 and CSS3", "author": "Terry Felke-Morris", "shelf": "B15"},
    {"id": "B036", "title": "Data Structures and Algorithms in Java", "author": "Michael T. Goodrich", "shelf": "B16"},
    {"id": "B037", "title": "Python Crash Course", "author": "Eric Matthes", "shelf": "B17"},
    {"id": "B038", "title": "Learning SQL", "author": "Alan Beaulieu", "shelf": "B18"},
    {"id": "B039", "title": "Computer Graphics", "author": "John F. Hughes et al.", "shelf": "B19"},
    {"id": "B040", "title": "Capstone Project Guide", "author": "Peter J. Farrell", "shelf": "B20"},

    {"id": "B041", "title": "Foundations of Education", "author": "Ornstein & Hunkins", "shelf": "C1"},
    {"id": "B042", "title": "Educational Psychology", "author": "Anita Woolfolk", "shelf": "C2"},
    {"id": "B043", "title": "Curriculum Development", "author": "Purita Bilbao et al.", "shelf": "C3"},
    {"id": "B044", "title": "Assessment of Learning", "author": "Posadas & Gregorio", "shelf": "C4"},
    {"id": "B045", "title": "Theories of Personality", "author": "Feist & Feist", "shelf": "C5"},
    {"id": "B046", "title": "Philosophy of Education", "author": "Nel Noddings", "shelf": "C6"},
    {"id": "B047", "title": "Educational Research", "author": "L.R. Gay et al.", "shelf": "C7"},
    {"id": "B048", "title": "Learning Theories", "author": "Dale H. Schunk", "shelf": "C8"},
    {"id": "B049", "title": "Multicultural Education", "author": "Gollnick & Chinn", "shelf": "C9"},
    {"id": "B050", "title": "Teaching Strategies", "author": "Donald C. Orlich et al.", "shelf": "C10"},
    {"id": "B051", "title": "Classroom Management", "author": "Evertson & Emmer", "shelf": "C11"},
    {"id": "B052", "title": "Principles of Teaching", "author": "Brenda Corpuz", "shelf": "C12"},
    {"id": "B053", "title": "The Skillful Teacher", "author": "Stephen D. Brookfield", "shelf": "C13"},
    {"id": "B054", "title": "Differentiated Instruction", "author": "Gregory & Chapman", "shelf": "C14"},
    {"id": "B055", "title": "Inclusive Education", "author": "Miles & Ainscow", "shelf": "C15"},
    {"id": "B056", "title": "Instructional Technology", "author": "Sharon Smaldino et al.", "shelf": "C16"},
    {"id": "B057", "title": "Language, Culture, and Society", "author": "Mananay & Sumalinog", "shelf": "C17"},
    {"id": "B058", "title": "Introduction to Research Methods", "author": "Catherine Dawson", "shelf": "C18"},
    {"id": "B059", "title": "Research Writing Modules", "author": "Lacaba & Abadiano", "shelf": "C19"},
    {"id": "B060", "title": "Religions and Spirituality", "author": "Galang et al.", "shelf": "C20"},

    {"id": "B061", "title": "Principles of Accounting", "author": "Belverd E. Needles", "shelf": "D1"},
    {"id": "B062", "title": "Fundamentals of Financial Management", "author": "Brigham & Houston", "shelf": "D2"},
    {"id": "B063", "title": "Marketing Management", "author": "Philip Kotler", "shelf": "D3"},
    {"id": "B064", "title": "Strategic Management", "author": "Fred R. David", "shelf": "D4"},
    {"id": "B065", "title": "Managerial Accounting", "author": "Hilton", "shelf": "D5"},
    {"id": "B066", "title": "Advanced Accounting", "author": "Beams", "shelf": "D6"},
    {"id": "B067", "title": "Financial Accounting", "author": "Nick Aduana", "shelf": "D7"},
    {"id": "B068", "title": "Fundamentals of Accounting", "author": "Flocer Lao Ong", "shelf": "D8"},
    {"id": "B069", "title": "Selling Tourist Destinations", "author": "Marc Mancini", "shelf": "D9"},
    {"id": "B070", "title": "Total Quality Management", "author": "Robert Ford et al.", "shelf": "D10"},
    {"id": "B071", "title": "HR Management: Local & Global", "author": "Diamante & Tan", "shelf": "D11"},
    {"id": "B072", "title": "Principles of Management", "author": "Cynthia Zarate", "shelf": "D12"},
    {"id": "B073", "title": "Retailing: Principles and Practices", "author": "Eduardo Garovillas", "shelf": "D13"},
    {"id": "B074", "title": "Marketing: Simplified Approach", "author": "Eduardo Garovillas", "shelf": "D14"},
    {"id": "B075", "title": "Business Continuity Planning", "author": "The Art of Service", "shelf": "D15"},
    {"id": "B076", "title": "Optimizing Project Management", "author": "Te Wu", "shelf": "D16"},
    {"id": "B077", "title": "Technology Entrepreneurship", "author": "Thomas Duening et al.", "shelf": "D17"},
    {"id": "B078", "title": "Introduction to Technopreneurship", "author": "Juaneza & Pomperada", "shelf": "D18"},
    {"id": "B079", "title": "Pro Microsoft Power BI Administration", "author": "Asgeir Gunnarsson", "shelf": "D19"},
    {"id": "B080", "title": "Introduction to Information Systems", "author": "Rainer & Prince", "shelf": "D20"}
]

# Dictionary to track borrowed books per user
borrowed_books = {}

class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library System")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda e: self.attributes('-fullscreen', False))
        self.current_user = None     
        self.create_login_ui()   
        self.tree = None
        
    # Clear the current frame
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Create the login UI
    def create_login_ui(self):
        self.clear_frame()

        container = ttk.Frame(self)
        container.pack(expand=True, fill='both')

        frame = ttk.Frame(container)
        frame.place(relx=0.5, rely=0.5, anchor='center')  

        font_config = ("Arial", 10)

        ttk.Label(frame, text="SR Code:", font=font_config).grid(row=1, column=0, sticky='e', pady=10, padx=10)
        self.sr_entry = ttk.Entry(frame, font=font_config, width=25)
        self.sr_entry.grid(row=1, column=1, pady=10)

        ttk.Label(frame, text="Password:", font=font_config).grid(row=2, column=0, sticky='e', pady=10, padx=10)
        self.pass_entry = ttk.Entry(frame, show="*", font=font_config, width=25)
        self.pass_entry.grid(row=2, column=1, pady=10)

        ttk.Label(frame, text="User Type:", font=font_config).grid(row=3, column=0, sticky='e', pady=10, padx=10)
        self.user_type = ttk.Combobox(frame, values=["Admin", "Student"], font=font_config, width=25)
        self.user_type.grid(row=3, column=1, pady=10)

        ttk.Button(frame, text="Login", command=self.login, width=20).grid(row=4, column=0, pady=20)
        ttk.Button(frame, text="Register", command=self.register, width=20).grid(row=4, column=1, pady=20)

    # Handle user login
    def login(self):
        sr = self.sr_entry.get()
        password = self.pass_entry.get()
        utype = self.user_type.get()
        
        if sr in users and users[sr]["password"] == password and users[sr]["type"] == utype:
            self.current_user = sr
            if utype == "Admin":
                self.create_admin_dashboard()
            else:
                self.create_student_dashboard()
        else:
            messagebox.showerror("Login Failed", "Ivalid credentials")

    # Handle new user registration
    def register(self):
        sr = self.sr_entry.get()
        password = self.pass_entry.get()
        utype = self.user_type.get()

        if sr and password and utype:
            if sr in users:
                messagebox.showerror("Error", "User already exists")
            else:
                users[sr] = {"password": password, "type": utype}
                messagebox.showinfo("Registered Successfully", f"Registered successfully.")
        else:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields")

    # Show the student dashboard
    def create_student_dashboard(self):
        self.clear_frame()

        ttk.Label(self, text="Student Dashboard", font=("Helvetica", 16)).pack(pady=20)
        ttk.Button(self, text="My Profile", command=self.show_student_profile).pack(pady=5) 
        ttk.Button(self, text="Borrow Book", command=self.borrow_selected_book).pack(pady=5)

        self.search_book_frame = ttk.Frame(self)
        self.search_book_frame.pack(pady=5)

        ttk.Label(self.search_book_frame, text="Search Book:").grid(row=0, column=0, padx=4)
        self.search_entry = ttk.Entry(self.search_book_frame)
        self.search_entry.grid(row=0, column=1, padx=4)
        ttk.Button(self.search_book_frame, text="Search", command=self.search_book).grid(row=0, column=2, padx=4)

        columns = ("shelf", "id", "title", "author")
        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=30)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
        for book in books:
            self.tree.insert('', tk.END, values=(book['shelf'], book['id'], book['title'], book['author']))
        self.tree.pack(pady=20)

    # Search for books
    def search_book(self):
        search_term = self.search_entry.get().strip()
        if not search_term:
            messagebox.showwarning("Empty Search", "Please enter a search term")
            return

        for item in self.tree.get_children():
            self.tree.delete(item)

        for book in books:
            if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower() or search_term.lower() in book['id'].lower() or search_term.lower() in book['shelf'].lower():
                self.tree.insert('', tk.END, values=(book['shelf'], book['id'], book['title'], book['author']))

    # Borrow a selected book
    def borrow_selected_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a book to borrow")
            return
        
        book_data = self.tree.item(selected_item)['values']
        book_id, title = book_data[1], book_data[2]

        self.selected_book = {
            'id': book_id,
            'title': title
        }

        form = tk.Toplevel(self)
        form.title("Borrow Book")
        form.geometry("500x400")

        ttk.Label(form, text=f"Title: {title}").grid(row=0, column=0, columnspan=4, pady=10)

        ttk.Label(form, text="Last Name:").grid(row=1, column=1, sticky='e', padx=5, pady=5)
        last_name_entry = ttk.Entry(form)
        last_name_entry.grid(row=1, column=2, pady=10)

        ttk.Label(form, text="First Name:").grid(row=2, column=1, sticky='e', padx=5, pady=5)
        first_name_entry = ttk.Entry(form)
        first_name_entry.grid(row=2, column=2, pady=10)

        ttk.Label(form, text="Program:").grid(row=3, column=1, sticky='e', padx=5, pady=5)
        program_entry = ttk.Entry(form)
        program_entry.grid(row=3, column=2, pady=10)

        ttk.Label(form, text="SR Code:").grid(row=4, column=1, sticky='e', padx=5, pady=5)
        sr_entry = ttk.Entry(form)
        sr_entry.grid(row=4, column=2, pady=10)

        ttk.Label(form, text="Contact No.:").grid(row=5, column=1, sticky='e', padx=5, pady=5)
        contact_entry = ttk.Entry(form)
        contact_entry.grid(row=5, column=2, pady=10)

        ttk.Button(
            form, text="Confirm",
            command=lambda: self.confirm_borrow(
                last_name_entry, first_name_entry, program_entry, contact_entry, sr_entry, form, title)
        ).grid(row=7, column=2, pady=10, padx=5)

        ttk.Button(form, text="Cancel", command=form.destroy).grid(row=7, column=1, pady=10, padx=5)

        for col in range(4):
            form.grid_columnconfigure(col, weight=1)

    # Confirm the borrowing of the book
    def confirm_borrow(self, last_name_entry, first_name_entry, program_entry, contact_entry, sr_entry, form, title):
        last_name_entry = last_name_entry.get().strip()
        first_name_entry = first_name_entry.get().strip()
        program_entry = program_entry.get().strip()
        contact_entry = contact_entry.get().strip()
        borrower_id = sr_entry.get().strip()

        if not all([last_name_entry, first_name_entry, program_entry, contact_entry, borrower_id]):
            messagebox.showwarning("Incomplete", "Please fill all fields")
            return
        
        borrower_date = datetime.today()
        due_date = borrower_date + timedelta(days=7)

        if self.current_user not in borrowed_books:
            borrowed_books[self.current_user] = []

        borrowed_books[self.current_user].append({
            'borrower_id': borrower_id,
            'last_name': last_name_entry, 
            'first_name': first_name_entry,
            'borrower_program': program_entry,
            'contact': contact_entry,
            'id': self.selected_book['id'],
            'title': self.selected_book['title'],
            'date_borrowed': borrower_date.strftime("%Y-%m-%d"),
            'due_date': due_date.strftime("%Y-%m-%d")
        })

        messagebox.showinfo(
            "Book Borrowed",
            f"You borrowed '{self.selected_book['title']}' successfully.\n"
            f"Due Date: {due_date.strftime('%Y-%m-%d')}"
        )
        form.destroy()
        self.tree.delete(self.tree.selection())

    # Handle returning a borrowed book
    def return_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a book to return")
            return
        
        book_data = self.tree.item(selected_item)['values']
        book_id, title = book_data[1], book_data[2]

        for book in borrowed_books.get(self.current_user, []):
            if book['id'] == book_id:
                borrowed_books[self.current_user].remove(book)
                messagebox.showinfo("Book Returned", f"{title} has been returned.")
                self.tree.delete(selected_item)
                return
        
        messagebox.showwarning("Not Borrowed", f"{title} was not borrowed by you.")
        
    # Show student profile
    def show_student_profile(self):
        self.clear_frame()
        ttk.Label(self, text="Student Profile", font=("Helvetica", 16)).pack(pady=20)
        ttk.Label(self, text=f"SR Code: {self.current_user}").pack()
        ttk.Button(self, text="My Borrowed Books", command=self.borrowed_books).pack(pady=10)
        ttk.Button(self, text="Back", command=self.create_student_dashboard).pack(pady=5)
        ttk.Button(self, text="Logout", command=self.create_login_ui).pack(pady=10)
        
    # Show the list of borrowed books by the current user
    def borrowed_books(self):
        self.clear_frame()
        ttk.Label(self, text="Borrowed Books", font=("Helvetica", 16)).pack(pady=10)
        ttk.Button(self, text="Return Book", command=self.return_book).pack(pady=5)

        columns = ("Date Borrowed", "Book ID", "Book Title", "Due Date")
        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=30)

        for col in columns:
            self.tree.heading(col, text=col.capitalize())

        for book in borrowed_books.get(self.current_user, []):
            self.tree.insert('', tk.END, values=( 
                book.get('date_borrowed', 'N/A'),
                book['id'], 
                book['title'], 
                book.get('due_date', 'N/A')
                ))
            
        self.tree.pack(pady=20)

        ttk.Button(self, text="Back", command=self.show_student_profile).pack(pady=5)

    #Show the admin dashboard
    def create_admin_dashboard(self):
        self.clear_frame()
        ttk.Label(self, text="Admin Dashboard", font=("Helvetica", 16)).pack(pady=10)
        ttk.Button(self, text="My Profile", command=self.show_admin_profile).pack(pady=5)

        self.search_book_frame = ttk.Frame(self)
        self.search_book_frame.pack(pady=5)

        ttk.Label(self.search_book_frame, text="Search Book:").grid(row=0, column=0, padx=4)
        self.search_entry = ttk.Entry(self.search_book_frame)
        self.search_entry.grid(row=0, column=1, padx=4)
        ttk.Button(self.search_book_frame, text="Search", command=self.search_book).grid(row=0, column=2, padx=4)

        self.columns = ("shelf", "id", "title", "author")
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings', height=33)
    
        for col in self.columns:
            self.tree.heading(col, text=col.capitalize())

        self.tree.pack(pady=20)
    
        self.populate_treeview()

    # Search for books in the admin dashboard
    def search_book(self):
        search_query = self.search_entry.get().lower()  
        filtered_books = [book for book in books if search_query in book['title'].lower() or search_query in book['author'].lower() or search_query in book['id'].lower() or search_query in book['shelf'].lower()]
    
        for item in self.tree.get_children():
            self.tree.delete(item)
    
        self.populate_treeview(filtered_books)

    def populate_treeview(self, books_to_display=None):
        if books_to_display is None:
            books_to_display = books  

        for book in books_to_display:
            self.tree.insert('', tk.END, values=(book['shelf'], book['id'], book['title'], book['author']))

    # Show the admin profile
    def show_admin_profile(self):
        self.clear_frame()
    
        frame = ttk.Frame(self)
        frame.pack(pady=40)

        ttk.Label(frame, text="Admin Profile", font=("Helvetica", 18, "bold")).pack(pady=10)
        ttk.Button(frame, text="Add Book", width=25, command=self.add_book).pack(pady=10)
        ttk.Button(frame, text="Manage Student Accounts", width=25, command=self.manage_student_accounts).pack(pady=10)
        ttk.Button(frame, text="View Borrowed Books", width=25, command=self.show_borrowed_books).pack(pady=10)
        ttk.Button(frame, text="Back", width=25, command=self.create_admin_dashboard).pack(pady=10)
        ttk.Button(frame, text="Logout", width=25, command=self.create_login_ui).pack(pady=10)

    # Adding a new book
    def add_book(self):
        form = tk.Toplevel(self)
        form.geometry("300x400")
        ttk.Label(form, text="Book Details", font=("Helvetica", 16)).pack(pady=20)

        ttk.Label(form, text="Shelf No.:").pack()
        shelf_entry = ttk.Entry(form)
        shelf_entry.pack(pady=5)

        ttk.Label(form, text="Book No.:").pack()
        book_id_entry = ttk.Entry(form)
        book_id_entry.pack(pady=5)

        ttk.Label(form, text="Book Title:").pack()
        title_entry = ttk.Entry(form)
        title_entry.pack(pady=5)

        ttk.Label(form, text="Author:").pack()
        author_entry = ttk.Entry(form)
        author_entry.pack(pady=5)

        ttk.Button(form, text="Add New Book", command=lambda: self.confirm_add_book(shelf_entry, book_id_entry, title_entry, author_entry, form)).pack(pady=10)
        ttk.Button(form, text="Cancel", command=self.create_admin_dashboard).pack(pady=5)

    # Confirm the addition of a new book
    def confirm_add_book(self, shelf_entry, book_id_entry, title_entry, author_entry, form):
        shelf = shelf_entry.get().strip()
        book_id = book_id_entry.get().strip()
        title = title_entry.get().strip()
        author = author_entry.get().strip()

        if not all([shelf, book_id, title, author]):
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
            return
        
        books.append({
            "shelf": shelf,
            "id": book_id,
            "title": title,
            "author": author
        })

        form.destroy()
        messagebox.showinfo("Success", f"Book '{title}' added successfully.")
        self.create_admin_dashboard()

    # Show the list of borrowed books for admin
    def show_borrowed_books(self):
        self.clear_frame()
        ttk.Label(self, text="Borrowed Books", font=("Helvetica", 16)).pack(pady=10)
        columns = (
            "SR Code", "Last Name", "First Name", "Program", "Contact No.",
            "Book ID", "Title", "Date Borrowed", "Due Date"
                   )
        tree = ttk.Treeview(self, columns=columns, show='headings', height=35)

        tree.column("SR Code", width=90, anchor='center')
        tree.column("Last Name", width=100, anchor='center')
        tree.column("First Name", width=100, anchor='center')
        tree.column("Program", width=80, anchor='center')
        tree.column("Contact No.", width=110, anchor='center')
        tree.column("Book ID", width=70, anchor='center')
        tree.column("Title", width=180, anchor='center')
        tree.column("Date Borrowed", width=100, anchor='center')
        tree.column("Due Date", width=100, anchor='center')

        for col in columns:
            tree.heading(col, text=col.capitalize())

        for user, books_list in borrowed_books.items():
            for book in books_list:
                last_name = book.get('first_name', '')
                first_name = book.get('last_name', '')
                program = book.get('borrower_program', '')
                contact = book.get('contact', '')

                tree.insert('', tk.END, values=(
                    user,
                    last_name,
                    first_name,
                    program,
                    contact,
                    book['id'],
                    book['title'],
                    book.get('date_borrowed', 'N/A'),
                    book.get('due_date', 'N/A')
                ))

        tree.pack(pady=20)
        ttk.Button(self, text="Back", command=self.show_admin_profile).pack(pady=5)

    # Manage student accounts UI
    def manage_student_accounts(self):
        self.clear_frame()
        ttk.Label(self, text="Manage Student Accounts", font=("Helvetica", 16)).pack(pady=10)
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=5)

        ttk.Button(self, text="Add Student", command=self.add_student).pack(pady=5)
        ttk.Button(self, text="Delete Account", command=self.delete_student_account).pack(pady=5)

        columns = ("SR Code", "Password")
        self.student_tree = ttk.Treeview(self, columns=columns, show='headings', height=30)

        for col in columns:
            self.student_tree.heading(col, text=col.capitalize())

        for sr, details in users.items():
            if details["type"] == "Student":
                self.student_tree.insert('', tk.END, values=(sr, details["password"]))

        self.student_tree.pack(pady=20)
        ttk.Button(self, text="Back", command=self.show_admin_profile).pack(pady=5)

    # Refresh the student tree view
    def refresh_student_tree(self):
        if not hasattr(self, 'student_tree'):
            return
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        for sr, details in users.items():
            if details["type"] == "Student":
                self.student_tree.insert('', tk.END, values=(sr, details["password"]))

    # Add a new student
    def add_student(self):
        form = tk.Toplevel(self)
        form.geometry("300x400")
        ttk.Label(form, text="Add Student", font=("Helvetica", 16)).pack(pady=20)

        ttk.Label(form, text="SR Code:").pack()
        sr_entry = ttk.Entry(form)
        sr_entry.pack(pady=5)

        ttk.Label(form, text="Password:").pack()
        password_entry = ttk.Entry(form, show="*")
        password_entry.pack(pady=5)

        ttk.Button(form, text="Add Student", command=lambda: self.confirm_add_student(sr_entry, password_entry, form)).pack(pady=10)
        ttk.Button(form, text="Cancel", command=form.destroy).pack(pady=5)

    # Confirm the addition of a new student
    def confirm_add_student(self, sr_entry, password_entry, form):
        sr = sr_entry.get().strip()
        password = password_entry.get().strip()

        if not sr or not password:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
            return

        if sr in users:
            messagebox.showerror("Error", "Student already exists.")
            return

        users[sr] = {"password": password, "type": "Student"}

        self.refresh_student_tree()

        form.destroy()
        messagebox.showinfo("Success", f"Student '{sr}' added successfully.")

    # Delete a student account
    def delete_student_account(self):
        if not hasattr(self, 'student_tree'):
            messagebox.showwarning("No Selection", "Please select a student to delete")
            return
        
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a student to delete")
            return
        
        item_id = selected_item[0]
        student_data = self.student_tree.item(item_id, 'values')
        if not student_data:
            messagebox.showwarning("No Selection", "Please select a student to delete")
            return
        
        sr_code = student_data[0]

        if sr_code in users:
            confirm = messagebox.askyesno("Delete Account", f"Are you sure you want to delete the account of '{sr_code}'?")
            if confirm:
                del users[sr_code]
                self.student_tree.delete(selected_item[0])

if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()