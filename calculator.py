import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("320x500")
        self.window.resizable(False, False)
        self.window.configure(bg="#1a1a2e")
        
        self.expression = ""
        self.display_text = tk.StringVar()
        self.display_text.set("0")
        
        self._create_display()
        self._create_buttons()
        
    def _create_display(self):
        display_frame = tk.Frame(self.window, bg="#1a1a2e")
        display_frame.pack(expand=True, fill="both", padx=20, pady=(30, 20))
        
        display_font = font.Font(family="Helvetica", size=42, weight="bold")
        
        display = tk.Label(
            display_frame,
            textvariable=self.display_text,
            font=display_font,
            bg="#1a1a2e",
            fg="#eee",
            anchor="e",
            padx=10
        )
        display.pack(expand=True, fill="both")
        
    def _create_buttons(self):
        button_frame = tk.Frame(self.window, bg="#1a1a2e")
        button_frame.pack(expand=True, fill="both", padx=15, pady=(0, 20))
        
        buttons = [
            ("C", "#e94560"), ("±", "#16213e"), ("%", "#16213e"), ("÷", "#0f3460"),
            ("7", "#16213e"), ("8", "#16213e"), ("9", "#16213e"), ("×", "#0f3460"),
            ("4", "#16213e"), ("5", "#16213e"), ("6", "#16213e"), ("−", "#0f3460"),
            ("1", "#16213e"), ("2", "#16213e"), ("3", "#16213e"), ("+", "#0f3460"),
            ("0", "#16213e"), (".", "#16213e"), ("⌫", "#16213e"), ("=", "#e94560"),
        ]
        
        button_font = font.Font(family="Helvetica", size=20, weight="bold")
        
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        
        for idx, (text, color) in enumerate(buttons):
            row, col = divmod(idx, 4)
            
            btn = tk.Button(
                button_frame,
                text=text,
                font=button_font,
                bg=color,
                fg="#fff",
                activebackground=self._lighten(color),
                activeforeground="#fff",
                relief="flat",
                borderwidth=0,
                cursor="hand2",
                command=lambda t=text: self._on_click(t)
            )
            btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
            
            btn.bind("<Enter>", lambda e, b=btn, c=color: b.configure(bg=self._lighten(c)))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.configure(bg=c))
    
    def _lighten(self, hex_color):
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
        r, g, b = min(255, r + 30), min(255, g + 30), min(255, b + 30)
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def _on_click(self, char):
        if char == "C":
            self.expression = ""
            self.display_text.set("0")
        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.display_text.set(self.expression if self.expression else "0")
        elif char == "±":
            if self.expression and self.expression[0] == "-":
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = "-" + self.expression
            self.display_text.set(self.expression if self.expression else "0")
        elif char == "=":
            try:
                expr = self.expression.replace("×", "*").replace("÷", "/").replace("−", "-")
                result = eval(expr)
                result = int(result) if result == int(result) else round(result, 10)
                self.expression = str(result)
                self.display_text.set(self.expression)
            except:
                self.display_text.set("Error")
                self.expression = ""
        elif char == "%":
            try:
                self.expression = str(float(self.expression) / 100)
                self.display_text.set(self.expression)
            except:
                pass
        else:
            self.expression += char
            self.display_text.set(self.expression)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
