# Movie Watch List Frontend

A simple, single-page HTML application for managing your movie watch list. This frontend provides a clean, intuitive interface for all the API endpoints in your Movie Watch List application.

## 🎬 Features

- **User Management**: Create, switch between, and delete users
- **Movie Management**: Add new movies with release dates
- **Watch Tracking**: Mark movies as watched/unwatched per user
- **Movie Categories**: View all movies, upcoming releases, and personal watched lists
- **Clean Interface**: Simple, responsive design with intuitive controls
- **Real-time Updates**: Lists refresh automatically after operations

## 🚀 Quick Start

### Option 1: Using the Start Scripts (Recommended)

**On Unix/Linux/macOS:**
```bash
./start.sh
```

**On Windows:**
```batch
start.bat
```

### Option 2: Manual Setup

1. Make sure your Flask API server is running on `http://localhost:8080`
   ```bash
   cd movie-watch-list-app
   python server.py
   ```

2. Start the frontend server:
   ```bash
   cd frontend
   python3 serve.py
   ```

3. Open `http://localhost:3000` in your browser

### Option 3: Direct File Access

Simply open `index.html` in your browser (may have CORS issues with some browsers).

## 📋 Prerequisites

- Python 3.x installed
- Flask backend server running on `http://localhost:8080`
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🔧 Backend Setup

If you haven't set up the backend yet, make sure to:

1. Install dependencies:
   ```bash
   pip install flask flask-cors
   # or if using uv:
   uv sync
   ```

2. Start the Flask server:
   ```bash
   python server.py
   ```

The backend should be running on `http://localhost:8080` before starting the frontend.

## 🌐 API Endpoints Covered

This frontend supports all available API endpoints:

### Movies
- `GET /movies` - View all movies
- `GET /movies/upcoming` - View upcoming movies (release date > today)
- `GET /movies/{username}/watched` - View user's watched movies
- `POST /movies` - Add new movie (title + release date)
- `POST /movies/{id}/watch` - Mark movie as watched for current user
- `DELETE /movies/{id}/unwatch` - Remove movie from watched list
- `DELETE /movies/{id}` - Delete movie completely

### Users
- `GET /users` - View all users
- `POST /users` - Create new user
- `DELETE /users/{username}/delete` - Delete user and all their data

## 📖 Usage Guide

### Getting Started
- The app starts with a default user "demo"
- Use the "Switch User" button or User Management section to change users
- Each user has their own independent watched list

### Adding Movies
1. Go to the "Add New Movie" section
2. Enter movie title and release date
3. Click "Add Movie"
4. Movie will appear in "All Movies" and "Upcoming Movies" (if release date is in the future)

### Managing Your Watch List
- **Mark as Watched**: Click this button on any movie to add it to your personal watched list
- **Unwatch**: Remove a movie from your watched list (movie stays in the system)
- **Delete Movie**: Permanently remove a movie from the entire system (affects all users)

### User Management
- **Create User**: Add new users with unique usernames
- **Switch User**: Change the current active user
- **Delete User**: Remove a user and all their watch history

## 🎨 Interface Sections

1. **Current User Display**: Shows active user with quick switch option
2. **User Management**: Create, view, and manage users
3. **Add New Movie**: Form to add movies to the system
4. **All Movies**: Complete list of movies with watch/delete options
5. **Upcoming Movies**: Movies with future release dates
6. **My Watched Movies**: Personal watched list for current user

## 📅 Date Handling

- **Input**: Standard HTML date picker (YYYY-MM-DD format)
- **API Communication**: Automatically converts to DD-MM-YYYY for backend
- **Display**: Uses browser's localized date format for readability

## 🔧 Technical Details

- **Technology**: Pure HTML, CSS, and JavaScript (no frameworks)
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Error Handling**: User-friendly error messages and confirmations
- **CORS Support**: Includes CORS headers for API communication
- **Loading States**: Visual feedback during API calls

## 🌍 Browser Compatibility

Works with any modern web browser supporting:
- ES6+ JavaScript (async/await, fetch API)
- CSS Flexbox
- HTML5 form elements

Tested on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🚨 Troubleshooting

### CORS Issues
If you get CORS errors:
1. Use the provided `serve.py` script instead of opening the file directly
2. Ensure your Flask backend has CORS enabled (flask-cors dependency)
3. Check that both frontend (port 3000) and backend (port 8080) are running

### Connection Issues
- Verify Flask API is running on `http://localhost:8080`
- Check browser developer console for network errors
- Ensure no firewall is blocking local connections

### User Interface Issues
- Hard refresh the page (Ctrl+F5 or Cmd+Shift+R)
- Clear browser cache if experiencing display problems
- Check browser console for JavaScript errors

## 📁 File Structure

```
frontend/
├── index.html          # Main application (complete frontend)
├── serve.py           # Python HTTP server with CORS support
├── start.sh           # Unix/Linux/macOS start script
├── start.bat          # Windows start script
└── README.md          # This documentation
```

## 🔄 Development

The entire frontend is contained in `index.html` for maximum simplicity and portability. To modify:

1. Edit `index.html` directly
2. Refresh your browser to see changes
3. No build process or compilation required

## 🆘 Support

If you encounter issues:
1. Check that both frontend and backend servers are running
2. Verify the API endpoints are working (test with curl or Postman)
3. Check browser developer console for error messages
4. Ensure all dependencies are installed

## 🎯 Design Philosophy

This frontend was built with these principles:
- **Simplicity**: Single HTML file, no build process
- **Completeness**: Covers all API functionality
- **User-Friendly**: Clear interface with helpful feedback
- **Economic**: Minimal dependencies, maximum functionality
- **Portable**: Works anywhere with a web browser