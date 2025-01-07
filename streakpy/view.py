from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login ,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from .models import Habit, HabitCompletion
from .forms import CustomUserCreationForm, HabitForm
from django.contrib.auth.decorators import login_required
from datetime import timedelta
def home(request):
    return render(request, 'streakpy/index.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            form.save()
            # Log the user in automatically after registration
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    today = now().date()
    # Get the last 10 days
    streak_days = [today - timedelta(days=i) for i in range(10)]
    # Check if the habit was completed on each of the last 10 days
    completed_streaks = []
    for habit in habits:
        for day in streak_days:
            if HabitCompletion.objects.filter(habit=habit, completed_at=day).exists():
                completed_streaks.append(day)

    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user  # Ensure the habit is linked to the current user
            habit.save()
            return redirect('habit_list')  # Refresh the page after adding a habit
    else:
        form = HabitForm()

    return render(request, 'habit_list.html', {'habits': habits, 'form': form, 'today': today,'completed_streaks': completed_streaks})


@login_required
def delete_habit(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    if habit.user == request.user:  # Ensure the habit belongs to the current user
        habit.delete()
    return redirect('habit_list')


# Add a habit via API (for AJAX handling)
@csrf_exempt
def add_habit(request):
    if request.method == "POST":
        habit_name = request.POST.get("name")
        if habit_name:
            habit = Habit.objects.create(name=habit_name, user=request.user)  # Assign the habit to the current user
            return JsonResponse({"success": True, "id": habit.id, "name": habit.name})
    return JsonResponse({"success": False, "error": "Invalid data"})


# Complete a habit via API (for AJAX handling)
@csrf_exempt
def complete_habit(request, habit_id):
    if request.method == "POST":
        habit = Habit.objects.get(id=habit_id)
        today = now().date()
        if habit.user == request.user:  # Ensure the habit belongs to the current user
            if not HabitCompletion.objects.filter(habit=habit, completed_at=today).exists():
                HabitCompletion.objects.create(habit=habit, completed_at=today)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Already completed"})
    return JsonResponse({"success": False, "error": "Habit not found or user mismatch"})


# Delete a habit via API (for AJAX handling)
@csrf_exempt
def delete_habit(request, habit_id):
    if request.method == "POST":
        habit = Habit.objects.get(id=habit_id)
        if habit.user == request.user:  # Ensure the habit belongs to the current user
            habit.delete()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Habit not found or user mismatch"})
    return JsonResponse({"success": False, "error": "Invalid request"})
@login_required
def habit_detail(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    streak = habit.calculate_streak()
    last_10_days = habit.get_last_10_days()

    return render(request, 'streakpy/habit_detail.html', {
        'habit': habit,
        'streak': streak,
        'last_10_days': last_10_days
    })
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('home')