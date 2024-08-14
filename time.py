def add_time(start, duration, day_of_week=None):
    # Helper function to convert 12-hour format to 24-hour format
    def convert_to_24_hour(hour, period):
        if period == "PM" and hour != 12:
            hour += 12
        if period == "AM" and hour == 12:
            hour = 0
        return hour
    
    # Helper function to convert 24-hour format back to 12-hour format
    def convert_to_12_hour(hour):
        period = "AM"
        if hour >= 12:
            period = "PM"
        if hour > 12:
            hour -= 12
        if hour == 0:
            hour = 12
        return hour, period
    
    # Helper function to calculate the new day of the week
    def get_new_day_of_week(start_day, days_later):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        return days_of_week[new_day_index]
    
    # Parse the start time and duration
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert the start time to 24-hour format
    start_hour = convert_to_24_hour(start_hour, period)
    
    # Add the duration to the start time
    new_minute = start_minute + duration_minute
    new_hour = start_hour + duration_hour + new_minute // 60
    new_minute %= 60
    days_later = new_hour // 24
    new_hour %= 24
    
    # Convert back to 12-hour format
    final_hour, final_period = convert_to_12_hour(new_hour)
    
    # Format the new time
    new_time = f"{final_hour}:{new_minute:02d} {final_period}"
    
    # Determine the day of the week if provided
    if day_of_week:
        new_day_of_week = get_new_day_of_week(day_of_week, days_later)
        new_time += f", {new_day_of_week}"
    
    # Handle the day count display
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time
