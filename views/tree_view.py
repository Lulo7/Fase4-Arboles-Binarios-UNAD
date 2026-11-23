import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from controllers.tree_controller import TreeController
from utils.tree_visualizer import TreeVisualizer


class TreeView(tk.Toplevel):

    def __init__(self, master):

        super().__init__(master)

        self.title("BST Explorer - Main Interface")
        self.geometry("1250x850")
        self.minsize(1000, 700)
        self.configure(bg="#0B1420")

        self.colors = {
            "background": "#0B1420",
            "card": "#162638",
            "primary": "#00BCD4",
            "secondary": "#263B50",
            "text": "#E6F1F5",
            "muted": "#91A9B9"
        }

        self.visualizer = TreeVisualizer()
        self.controller = TreeController(self)

        self._configure_styles()
        self._build_interface()
        self._draw_initial_state()

        self.protocol("WM_DELETE_WINDOW", self.close)

    def _configure_styles(self):

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Tree.TEntry",
            fieldbackground=self.colors["secondary"],
            foreground=self.colors["text"],
            padding=10
        )

        style.configure(
            "Tree.TButton",
            background=self.colors["primary"],
            foreground=self.colors["background"],
            font=("Segoe UI", 9, "bold"),
            padding=10,
            borderwidth=0
        )

        style.map(
            "Tree.TButton",
            background=[
                ("active", "#00A5BC")
            ]
        )

    def _build_interface(self):

        header = tk.Frame(
            self,
            bg=self.colors["background"]
        )
        header.pack(fill="x", padx=25, pady=20)

        tk.Label(
            header,
            text="BST Explorer",
            font=("Segoe UI", 25, "bold"),
            fg=self.colors["primary"],
            bg=self.colors["background"]
        ).pack(side="left")

        tk.Label(
            header,
            text="Binary Search Tree Visualization",
            font=("Segoe UI", 10),
            fg=self.colors["muted"],
            bg=self.colors["background"]
        ).pack(side="right", pady=10)

        controls = tk.Frame(
            self,
            bg=self.colors["card"],
            highlightbackground=self.colors["secondary"],
            highlightthickness=1
        )
        controls.pack(fill="x", padx=25, pady=(0, 15))

        tk.Label(
            controls,
            text="Enter Integer:",
            font=("Segoe UI", 10, "bold"),
            fg=self.colors["text"],
            bg=self.colors["card"]
        ).pack(side="left", padx=(18, 10), pady=15)

        self.input_entry = ttk.Entry(
            controls,
            style="Tree.TEntry",
            font=("Segoe UI", 11),
            width=18
        )
        self.input_entry.pack(side="left", padx=5, pady=15)

        self._create_button(
            controls,
            "Add Node",
            self.controller.add_node
        )

        self._create_button(
            controls,
            "Search Node",
            self.controller.search_node
        )

        self._create_button(
            controls,
            "Clear",
            self.controller.clear_tree
        )

        self._create_button(
            controls,
            "Exit",
            self.controller.exit_application
        )

        graph_container = tk.Frame(
            self,
            bg=self.colors["background"]
        )
        graph_container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 20)
        )

        self.figure = Figure(
            figsize=(12, 7),
            dpi=100,
            facecolor=self.colors["background"]
        )

        self.axes = self.figure.subplots(2, 2)

        self.figure.subplots_adjust(
            left=0.05,
            right=0.97,
            top=0.95,
            bottom=0.06,
            hspace=0.35,
            wspace=0.20
        )

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=graph_container
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def _create_button(self, parent, text, command):

        button = ttk.Button(
            parent,
            text=text,
            style="Tree.TButton",
            command=command
        )

        button.pack(side="left", padx=5, pady=15)

    def _draw_initial_state(self):

        self.update_tree(
            None, [], [], []
        )

    def get_input_value(self):

        return self.input_entry.get().strip()

    def clear_input(self):

        self.input_entry.delete(0, tk.END)
        self.input_entry.focus_set()

    def update_tree(
        self,
        root,
        preorder,
        inorder,
        postorder
    ):

        self.visualizer.draw_tree(
            self.axes[0, 0],
            root
        )

        self.visualizer.draw_traversal(
            self.axes[0, 1],
            preorder,
            "Preorder Traversal"
        )

        self.visualizer.draw_traversal(
            self.axes[1, 0],
            inorder,
            "Inorder Traversal"
        )

        self.visualizer.draw_traversal(
            self.axes[1, 1],
            postorder,
            "Postorder Traversal"
        )

        self.canvas.draw_idle()

    def show_success(self, message):

        messagebox.showinfo(
            "Success",
            message,
            parent=self
        )

    def show_error(self, message):

        messagebox.showerror(
            "Error",
            message,
            parent=self
        )

    def show_info(self, message):

        messagebox.showinfo(
            "Information",
            message,
            parent=self
        )

    def close(self):

        self.master.destroy()