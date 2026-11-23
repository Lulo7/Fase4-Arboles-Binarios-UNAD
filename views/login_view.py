import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class LoginView(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Fase4AlejandroGallo - Login")
        self.geometry("650x570")
        self.resizable(False, False)
        self.configure(bg="#0B1420")

        self.login_command = None

        self.colors = {
            "background": "#0B1420",
            "card": "#162638",
            "primary": "#00BCD4",
            "secondary": "#263B50",
            "text": "#E6F1F5",
            "muted": "#91A9B9",
            "border": "#087F95"
        }

        self._configure_styles()
        self._build_interface()

    def _configure_styles(self):

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Login.TEntry",
            fieldbackground=self.colors["secondary"],
            foreground=self.colors["text"],
            insertcolor=self.colors["text"],
            bordercolor=self.colors["border"],
            padding=12
        )

        style.configure(
            "Login.TButton",
            background=self.colors["primary"],
            foreground=self.colors["background"],
            font=("Segoe UI", 11, "bold"),
            padding=12,
            borderwidth=0
        )

        style.map(
            "Login.TButton",
            background=[
                ("active", "#00A5BC"),
                ("pressed", "#008FA5")
            ]
        )

    def _build_interface(self):

        main_frame = tk.Frame(
            self,
            bg=self.colors["background"]
        )
        main_frame.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=30
        )

        title = tk.Label(
            main_frame,
            text="♧  BST Explorer",
            font=("Segoe UI", 27, "bold"),
            fg=self.colors["primary"],
            bg=self.colors["background"]
        )
        title.pack(pady=(10, 2))

        subtitle = tk.Label(
            main_frame,
            text="Binary Search Tree - Phase 4",
            font=("Segoe UI", 10),
            fg=self.colors["muted"],
            bg=self.colors["background"]
        )
        subtitle.pack(pady=(0, 25))

        card = tk.Frame(
            main_frame,
            bg=self.colors["card"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        card.pack(fill="x", padx=25)

        information = [
            ("Application", "Fase4AlejandroGallo"),
            ("Student", "Alejandro Gallo"),
            ("Course", "Data Structures - 301305"),
            ("Date", datetime.now().strftime("%B %d, %Y"))
        ]

        info_frame = tk.Frame(
            card,
            bg=self.colors["card"]
        )
        info_frame.pack(fill="x", padx=22, pady=20)

        for label_text, value_text in information:

            row = tk.Frame(
                info_frame,
                bg=self.colors["card"]
            )
            row.pack(fill="x", pady=5)

            tk.Label(
                row,
                text=f"{label_text}:",
                font=("Segoe UI", 9, "bold"),
                fg=self.colors["muted"],
                bg=self.colors["card"],
                width=12,
                anchor="w"
            ).pack(side="left")

            tk.Label(
                row,
                text=value_text,
                font=("Segoe UI", 9),
                fg=self.colors["text"],
                bg=self.colors["card"],
                anchor="w"
            ).pack(side="left")

        tk.Frame(
            card,
            bg=self.colors["border"],
            height=1
        ).pack(fill="x", padx=20)

        password_frame = tk.Frame(
            card,
            bg=self.colors["card"]
        )
        password_frame.pack(
            fill="x",
            padx=22,
            pady=20
        )

        tk.Label(
            password_frame,
            text="Enter Password",
            font=("Segoe UI", 10, "bold"),
            fg=self.colors["text"],
            bg=self.colors["card"]
        ).pack(anchor="w", pady=(0, 10))

        self.password_entry = ttk.Entry(
            password_frame,
            style="Login.TEntry",
            show="*",
            font=("Segoe UI", 11)
        )
        self.password_entry.pack(fill="x")

        tk.Label(
            password_frame,
            text="Password is masked for security.",
            font=("Segoe UI", 8),
            fg=self.colors["muted"],
            bg=self.colors["card"]
        ).pack(anchor="w", pady=(7, 0))

        self.login_button = ttk.Button(
            card,
            text="Access BST Explorer  →",
            style="Login.TButton",
            command=self._execute_login
        )
        self.login_button.pack(
            fill="x",
            padx=22,
            pady=(0, 22)
        )

        footer = tk.Label(
            main_frame,
            text="UNAD - ECBTI | Systems Engineering",
            font=("Segoe UI", 8),
            fg=self.colors["muted"],
            bg=self.colors["background"]
        )
        footer.pack(pady=18)

        self.password_entry.focus_set()

        self.bind("<Return>", lambda event: self._execute_login())

    def set_login_command(self, command):

        self.login_command = command

    def _execute_login(self):

        if self.login_command is not None:
            self.login_command()

    def get_password(self):

        return self.password_entry.get()

    def show_success(self, message):

        messagebox.showinfo(
            "Access Granted",
            message,
            parent=self
        )

        self.password_entry.delete(0, tk.END)

    def show_error(self, message):

        messagebox.showerror(
            "Login Error",
            message,
            parent=self
        )

        self.password_entry.delete(0, tk.END)
        self.password_entry.focus_set()