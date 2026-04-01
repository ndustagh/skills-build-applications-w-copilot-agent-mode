import os
import django

def setup_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
    django.setup()

setup_django()

from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Clear existing data
User.objects.all().delete()
Team.objects.all().delete()
Activity.objects.all().delete()
Workout.objects.all().delete()
Leaderboard.objects.all().delete()

# Create Users
user1 = User.objects.create(username='alice', email='alice@example.com')
user2 = User.objects.create(username='bob', email='bob@example.com')
user3 = User.objects.create(username='carol', email='carol@example.com')

# Create Teams
team1 = Team.objects.create(name='Team Alpha')
team2 = Team.objects.create(name='Team Beta')
team1.members.add(user1, user2)
team2.members.add(user3)

# Create Activities
Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2023-01-01')
Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2023-01-02')
Activity.objects.create(user=user3, activity_type='Swimming', duration=60, date='2023-01-03')

# Create Workouts
workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
workout2 = Workout.objects.create(name='Situps', description='Do 30 situps')
workout1.suggested_for.add(user1, user2)
workout2.suggested_for.add(user3)

# Create Leaderboard
Leaderboard.objects.create(team=team1, score=150)
Leaderboard.objects.create(team=team2, score=100)

print('Test data populated successfully!')
