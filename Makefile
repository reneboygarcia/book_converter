.PHONY: setup clean install run lint format test calibre

# Python settings
PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip
PYTHON_VENV := $(VENV)/bin/python

# Project settings
NOTEBOOK := book_converter.ipynb
REQUIREMENTS := requirements.txt

# Default target
all: setup install

# Create virtual environment
setup:
	@echo "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

# Install dependencies
install:
	@echo "Installing dependencies..."
	@$(PIP) install -r $(REQUIREMENTS)
	@$(PIP) install jupyter black flake8
	@echo "Dependencies installed."

# Install Calibre
calibre:
	@echo "Installing Calibre..."
	@sudo apt-get install calibre -y
	@echo "Calibre installed."

# Run the notebook
run:
	@echo "Starting Jupyter notebook..."
	@$(VENV)/bin/jupyter notebook $(NOTEBOOK)

# Run linting
lint:
	@echo "Running linter..."
	@$(VENV)/bin/flake8 .

# Format code
format:
	@echo "Formatting code..."
	@$(VENV)/bin/black .

# Clean up generated files and virtual environment
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@rm -rf __pycache__
	@rm -rf .ipynb_checkpoints
	@echo "Cleanup complete."

# Create requirements.txt from current environment
freeze:
	@echo "Creating requirements.txt..."
	@$(PIP) freeze > $(REQUIREMENTS)
	@echo "Requirements file updated."

# Help target
help:
	@echo "Available targets:"
	@echo "  setup    - Create virtual environment"
	@echo "  install  - Install dependencies"
	@echo "  calibre   - Install Calibre"
	@echo "  run      - Run the Jupyter notebook"
	@echo "  lint     - Run code linter"
	@echo "  format   - Format code using black"
	@echo "  clean    - Remove virtual environment and cache files"
	@echo "  freeze   - Update requirements.txt"
	@echo "  help     - Show this help message" 