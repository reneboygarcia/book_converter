# Book Converter

## Overview

The **Book Converter** is a Python-based tool that allows you to convert eBooks between various formats, including PDF, EPUB, MOBI, AZW3, DOCX, TXT, RTF, and HTML. This tool is designed to work offline, giving you full control over your eBook conversion process without relying on third-party services.

## Features

- **Supports Multiple Formats**: Convert your eBooks to and from various formats.
- **Offline Functionality**: No need for an internet connection; everything runs locally on your machine.
- **User-Friendly GUI**: A simple graphical user interface (GUI) for easy file selection and conversion.
- **Error Handling**: Informative error messages to guide you through any issues during conversion.

## Fun Fact

Did you know that the eBook format EPUB is based on web standards? It allows for reflowable content, meaning that the text can adapt to different screen sizes, making it perfect for reading on various devices!

## Requirements

To run this project, you need to have the following installed on your machine:

- Python 3.x
- Calibre (for the `ebook-convert` command-line tool)

### Installing Calibre

You can download Calibre from [Calibre's official website](https://calibre-ebook.com/download). Follow the installation instructions for your operating system.

## How to Run the Project

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/reneboygarcia/book_converter.git
   cd book_converter
   ```

2. **Install Required Packages**: 
   Make sure you have the required Python packages installed. You can use pip to install them:
   ```bash
   pip install tkinter
   ```

3. **Run the Application**: 
   You can run the application using the following command:
   ```bash
   python book_converter.py
   ```

4. **Using the GUI**:
   - Select the input file by clicking the "Browse" button.
   - Choose the desired output format from the dropdown menu.
   - Click the "Convert" button to start the conversion process.
   - The status will be displayed, and upon successful conversion, you will see the output file path.

## Example Usage

If you prefer to use the converter without the GUI, you can run the `book_converter.ipynb` Jupyter Notebook. This notebook demonstrates how to use the `BookConverter` class programmatically.

1. **Open Jupyter Notebook**:
   ```bash
   jupyter notebook book_converter.ipynb
   ```

2. **Run the Cells**: Follow the instructions in the notebook to convert eBooks programmatically.



---

Enjoy converting your eBooks with the Book Converter!