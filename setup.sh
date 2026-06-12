#!/bin/bash
# Project Eclipse Setup Script for macOS/Linux

echo "======================================="
echo "PROJECT ECLIPSE: Horror Survival Setup"
echo "======================================="
echo ""

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo ""

# Create asset directories
echo "Creating asset directories..."
mkdir -p assets/textures
mkdir -p assets/models
mkdir -p assets/sounds
mkdir -p assets/ui
echo "Asset directories created"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""

echo "======================================="
echo "Setup complete!"
echo "Run: python main.py"
echo "======================================="
