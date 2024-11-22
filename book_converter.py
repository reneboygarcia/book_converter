import os
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import PyPDF2  # For PDF text extraction
import requests  # For web requests
from bs4 import BeautifulSoup  # For web scraping


class BookConverter:
    def __init__(self):
        self.supported_formats = [
            "pdf",
            "epub",
            "mobi",
            "azw3",
            "docx",
            "txt",
            "rtf",
            "html",
        ]

        # Check if Calibre is installed
        self.calibre_installed = self._check_calibre_installation()

    def _check_calibre_installation(self):
        """Check if Calibre's ebook-convert is available"""
        try:
            subprocess.run(
                ["ebook-convert", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return True
        except FileNotFoundError:
            return False

    def convert_book(self, input_path, output_format):
        """Convert book to specified format using Calibre's ebook-convert"""
        if not self.calibre_installed:
            raise RuntimeError(
                "Calibre is not installed. Please install Calibre first: "
                "https://calibre-ebook.com/download"
            )

        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        # Create output path with new extension
        output_path = input_path.with_suffix(f".{output_format}")

        # Generate TOC if converting to EPUB
        if output_format == "epub":
            toc = self._generate_toc(input_path)
            # Pass TOC to Calibre conversion (this is a conceptual step)
            # You might need to save the TOC to a file and pass it as an option

        # Run conversion
        try:
            process = subprocess.run(
                ["ebook-convert", str(input_path), str(output_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            if process.returncode != 0:
                raise RuntimeError(f"Conversion failed: {process.stderr}")

            return str(output_path)

        except Exception as e:
            raise RuntimeError(f"Conversion failed: {str(e)}")

    def _generate_toc(self, pdf_path):
        # Extract text from PDF
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Analyze text to identify headings (this is a simplified example)
            toc = []
            for page in reader.pages:
                text = page.extract_text()
                # Logic to identify headings and create TOC entries
                # This could involve regex or NLP techniques
                # Example: if "Chapter" in text: toc.append(text)
        
        # Optionally, fetch TOC from online sources
        # Example: self._fetch_toc_online("book title or ISBN")

        return toc

    def _fetch_toc_online(self, book_title):
        # Example of fetching TOC from a public site
        url = f"https://www.example.com/search?q={book_title}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract TOC from the page
        # Example: toc = soup.find_all('h2', class_='toc-entry')
        return []


class BookConverterGUI:
    def __init__(self):
        self.converter = BookConverter()

        # Create main window
        self.window = tk.Tk()
        self.window.title("Book Format Converter")
        self.window.geometry("600x400")

        # Create GUI elements
        self._create_widgets()

    def _create_widgets(self):
        # File selection
        select_frame = ttk.Frame(self.window, padding="10")
        select_frame.pack(fill=tk.X)

        ttk.Label(select_frame, text="Input File:").pack(side=tk.LEFT)
        self.file_path = tk.StringVar()
        ttk.Entry(select_frame, textvariable=self.file_path, width=50).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(select_frame, text="Browse", command=self._browse_file).pack(
            side=tk.LEFT
        )

        # Format selection
        format_frame = ttk.Frame(self.window, padding="10")
        format_frame.pack(fill=tk.X)

        ttk.Label(format_frame, text="Output Format:").pack(side=tk.LEFT)
        self.output_format = tk.StringVar()
        format_combo = ttk.Combobox(
            format_frame,
            textvariable=self.output_format,
            values=self.converter.supported_formats,
        )
        format_combo.pack(side=tk.LEFT, padx=5)

        # Convert button
        ttk.Button(self.window, text="Convert", command=self._convert).pack(pady=20)

        # Status
        self.status_var = tk.StringVar()
        ttk.Label(self.window, textvariable=self.status_var, wraplength=500).pack(
            pady=10
        )

    def _browse_file(self):
        filetypes = [
            (f"{fmt.upper()} files", f"*.{fmt}")
            for fmt in self.converter.supported_formats
        ]
        filetypes.append(("All files", "*.*"))

        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.file_path.set(filename)

    def _convert(self):
        if not self.converter.calibre_installed:
            messagebox.showerror(
                "Error",
                "Calibre is not installed. Please install Calibre first: "
                "https://calibre-ebook.com/download",
            )
            return

        input_path = self.file_path.get()
        output_format = self.output_format.get()

        if not input_path:
            messagebox.showerror("Error", "Please select an input file")
            return

        if not output_format:
            messagebox.showerror("Error", "Please select an output format")
            return

        self.status_var.set("Converting... Please wait.")
        self.window.update()

        try:
            output_path = self.converter.convert_book(input_path, output_format)
            self.status_var.set(
                f"Conversion successful!\nOutput saved to: {output_path}"
            )
            messagebox.showinfo("Success", "Conversion completed successfully!")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = BookConverterGUI()
    app.run()
