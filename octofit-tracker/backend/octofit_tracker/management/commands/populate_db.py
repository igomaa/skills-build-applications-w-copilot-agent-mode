import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

def populate():
    # Clear existing data
    User.objects.all().delete()
    Team.objects.all().delete()
    Activity.objects.all().delete()
    Leaderboard.objects.all().delete()
    Workout.objects.all().delete()

    # Create users
    user1 = User.objects.create(username="john_doe", email="john@example.com", password="password123")
    user2 = User.objects.create(username="jane_doe", email="jane@example.com", password="password123")

    # Create teams
    team1 = Team.objects.create(name="Team Alpha")
    team1.members.add(user1, user2)

    # Create activities
    Activity.objects.create(user=user1, activity_type="Running", duration="00:30:00")
    Activity.objects.create(user=user2, activity_type="Cycling", duration="01:00:00")

    # Create leaderboard entries
    Leaderboard.objects.create(user=user1, score=100)
    Leaderboard.objects.create(user=user2, score=150)

    # Create workouts
    Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
    Workout.objects.create(name="Sit-ups", description="Do 30 sit-ups")

    print("Database populated with test data.")

if __name__ == "__main__":
    populate()

