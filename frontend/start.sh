#!/bin/bash

# Movie Watch List Frontend Starter Script
# This script starts the frontend server and opens it in your browser

echo "🎬 Starting Movie Watch List Frontend..."
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
cd "$SCRIPT_DIR"

echo "📂 Working directory: $SCRIPT_DIR"
echo "🚀 Starting frontend server on http://localhost:3000"
echo ""
echo "⚠️  IMPORTANT: Make sure your Flask API is running!"
echo "   Start it in another terminal with: python server.py"
echo "   (from the main project directory)"
echo ""
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Start the Python server
python3 serve.py
