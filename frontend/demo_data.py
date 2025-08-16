#!/usr/bin/env python3
"""
Demo Data Script for Movie Watch List Frontend
This script populates the database with sample data for testing the frontend.
"""

import requests
import json
from datetime import datetime, timedelta

API_BASE = "http://localhost:8080"

def check_server():
    """Check if the Flask server is running"""
    try:
        response = requests.get(f"{API_BASE}/movies")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def create_users():
    """Create sample users"""
    users = ["demo", "alice", "bob", "charlie"]

    print("Creating sample users...")
    for user in users:
        try:
            response = requests.post(f"{API_BASE}/users",
                                   json={"user_name": user})
            if response.status_code == 200:
                print(f"✓ Created user: {user}")
            else:
                print(f"⚠ User {user} might already exist")
        except Exception as e:
            print(f"✗ Error creating user {user}: {e}")

def create_movies():
    """Create sample movies with various release dates"""

    # Past movies (already released)
    past_movies = [
        {"title": "The Shawshank Redemption", "days_ago": 365 * 29},
        {"title": "The Godfather", "days_ago": 365 * 51},
        {"title": "The Dark Knight", "days_ago": 365 * 15},
        {"title": "Pulp Fiction", "days_ago": 365 * 29},
        {"title": "Forrest Gump", "days_ago": 365 * 29},
        {"title": "Inception", "days_ago": 365 * 13},
        {"title": "Fight Club", "days_ago": 365 * 24},
        {"title": "The Matrix", "days_ago": 365 * 24},
        {"title": "Goodfellas", "days_ago": 365 * 33},
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "days_ago": 365 * 22}
    ]

    # Future movies (upcoming)
    future_movies = [
        {"title": "Avatar 3", "days_future": 365},
        {"title": "Marvel's Next Big Thing", "days_future": 180},
        {"title": "Star Wars: New Hope", "days_future": 500},
        {"title": "The Batman 2", "days_future": 300},
        {"title": "Dune: Part Three", "days_future": 600}
    ]

    print("\nCreating sample movies...")

    # Create past movies
    for movie in past_movies:
        release_date = datetime.now() - timedelta(days=movie["days_ago"])
        date_str = release_date.strftime("%d-%m-%Y")

        try:
            response = requests.post(f"{API_BASE}/movies",
                                   json={
                                       "title": movie["title"],
                                       "release_date": date_str
                                   })
            if response.status_code == 200:
                print(f"✓ Created movie: {movie['title']} ({date_str})")
            else:
                print(f"⚠ Error creating movie: {movie['title']}")
        except Exception as e:
            print(f"✗ Error creating movie {movie['title']}: {e}")

    # Create future movies
    for movie in future_movies:
        release_date = datetime.now() + timedelta(days=movie["days_future"])
        date_str = release_date.strftime("%d-%m-%Y")

        try:
            response = requests.post(f"{API_BASE}/movies",
                                   json={
                                       "title": movie["title"],
                                       "release_date": date_str
                                   })
            if response.status_code == 200:
                print(f"✓ Created upcoming movie: {movie['title']} ({date_str})")
            else:
                print(f"⚠ Error creating movie: {movie['title']}")
        except Exception as e:
            print(f"✗ Error creating movie {movie['title']}: {e}")

def create_watched_entries():
    """Create some watched movie entries for users"""

    print("\nSetting up watched movies for users...")

    # Get all movies first
    try:
        response = requests.get(f"{API_BASE}/movies")
        movies = response.json()

        if not movies:
            print("No movies found to mark as watched")
            return

        # Demo user watches several movies
        demo_watches = movies[:5]  # First 5 movies
        for movie in demo_watches:
            try:
                response = requests.post(f"{API_BASE}/movies/{movie['id']}/watch",
                                       json={"user_name": "demo"})
                if response.status_code == 200:
                    print(f"✓ Demo watched: {movie['title']}")
            except Exception as e:
                print(f"✗ Error marking {movie['title']} as watched for demo: {e}")

        # Alice watches different movies
        alice_watches = movies[2:7] if len(movies) > 6 else movies[2:]
        for movie in alice_watches:
            try:
                response = requests.post(f"{API_BASE}/movies/{movie['id']}/watch",
                                       json={"user_name": "alice"})
                if response.status_code == 200:
                    print(f"✓ Alice watched: {movie['title']}")
            except Exception as e:
                print(f"✗ Error marking {movie['title']} as watched for alice: {e}")

        # Bob watches a few movies
        bob_watches = movies[5:8] if len(movies) > 7 else movies[-3:]
        for movie in bob_watches:
            try:
                response = requests.post(f"{API_BASE}/movies/{movie['id']}/watch",
                                       json={"user_name": "bob"})
                if response.status_code == 200:
                    print(f"✓ Bob watched: {movie['title']}")
            except Exception as e:
                print(f"✗ Error marking {movie['title']} as watched for bob: {e}")

    except Exception as e:
        print(f"✗ Error getting movies for watched entries: {e}")

def main():
    print("🎬 Movie Watch List Demo Data Setup")
    print("=" * 40)

    # Check if server is running
    if not check_server():
        print("❌ Flask server is not running on http://localhost:8080")
        print("Please start the server with: python server.py")
        return

    print("✅ Flask server is running")

    # Create demo data
    create_users()
    create_movies()
    create_watched_entries()

    print("\n🎉 Demo data setup complete!")
    print("\nYou can now:")
    print("1. Start the frontend with: ./start.sh (or start.bat on Windows)")
    print("2. Open http://localhost:3000 in your browser")
    print("3. Test all the features with the sample data")
    print("\nSample users created: demo, alice, bob, charlie")
    print("Movies include both past releases and upcoming titles")

if __name__ == "__main__":
    main()
