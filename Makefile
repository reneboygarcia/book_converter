# Makefile

# Define the Python interpreter
PYTHON = python3

# Define the virtual environment directory
VENV_DIR = venv

# Define the requirements file
REQUIREMENTS = requirements.txt

# Create a virtual environment
$(VENV_DIR)/bin/activate: 
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies
install: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

# Run the book converter application
run: $(VENV_DIR)/bin/activate
	$(VENV_DIR)/bin/python book_converter.py

# Clean up the virtual environment
clean:
	rm -rf $(VENV_DIR)

# Phony targets
.PHONY: install run clean