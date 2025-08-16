#!/usr/bin/env python3
"""
Simple HTTP server for serving the Movie Watch List frontend.
This avoids CORS issues when accessing the Flask API from a local file.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with CORS headers to allow API access"""

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to the frontend directory
    os.chdir(DIRECTORY)

    # Create server
    with socketserver.TCPServer(("", PORT), CORSHTTPRequestHandler) as httpd:
        print(f"🎬 Movie Watch List Frontend Server")
        print(f"📂 Serving directory: {DIRECTORY}")
        print(f"🌐 Server running at: http://localhost:{PORT}")
        print(f"📱 Open http://localhost:{PORT} in your browser")
        print("\n⚠️  Make sure your Flask API is running on http://localhost:8080")
        print("   You can start it with: python server.py")
        print("\n🛑 Press Ctrl+C to stop the server")

        # Try to open browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}')
            print("🚀 Opening browser automatically...")
        except:
            print("❌ Could not open browser automatically")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
            sys.exit(0)

if __name__ == "__main__":
    main()
