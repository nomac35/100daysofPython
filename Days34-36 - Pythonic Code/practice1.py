
workouts = {
    'Monday': 'Chest+biceps',
    'Tuesday': 'Back+triceps',
    'Wednesday': 'Core',
    'Thursday': 'Legs',
    'Friday': 'Shoulders',
    'Saturday': 'Rest',
    'Sunday': 'Rest',
}
print(workouts)

#OR

days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
activity = "Chest+biceps Back+triceps Core Legs Shoulders Rest Rest ".split()
workout = dict(zip(days,activity))
print(workouts)

def workout2(day):
    routine = workouts.get(day)
    if routine is None:
        raise ValueError('Not a valid day')
    return routine


print(workout2("Sunday"))

for i,day in enumerate(days):
    print("{}. {}".format((i+1),day))
total =0
for i in range(1,11):
    total+=i
print(total)

y = [i for i in range(1,11)]
print(sum(y))

routines = 'Chest+biceps Back+triceps Core Legs Shoulders'.split()
timings = '45 45 30 55 45'.split()

workout_times = dict(zip(routines, timings))
print(workout_times)
print(max(workout_times.items(), key=lambda x: x[1]))
print(min(workout_times.items(), key=lambda x:x[1]))