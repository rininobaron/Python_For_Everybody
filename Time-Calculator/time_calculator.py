def add_time(start, duration, day = None):
    start_list = start.split(" ")
    duration_list = duration.split(":")
    if int(duration_list[1]) >= 60:
        return "The minutes in the duration time will be a whole number less than 60."
    time = start_list[0]
    meridian = start_list[1]
    [hour, minutes] = time.split(":")
    hour = int(hour)
    minutes = int(minutes)
    if hour > 12:
        return "The hour is not in 0 to 12 hours format."
    if minutes >= 60:
        return "The minutes in the start time will be a whole number less than 60."
    if meridian == 'PM':
        hour_24hrs = hour + 12
    elif meridian == 'AM':
        hour_24hrs = hour
    else:
        return "start is not PM AM correct format"
    hours_output = hour_24hrs + int(duration_list[0])
    #print(hours_output)
    final_minutes = minutes + int(duration_list[1])
    if final_minutes >= 60:
        final_minutes = final_minutes%60
        final_hour_plus = 1
    else:
        final_minutes = final_minutes%60
        final_hour_plus = 0
    if final_minutes < 10:
        left_zero = '0'
    else:
        left_zero = ''
    final_minutes = left_zero + str(final_minutes)
    final_hours_output = hours_output  + final_hour_plus
    days = int(final_hours_output/24)
    if day:
        list_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day.lower() in list_days:
            list_days.index(day.lower())
            #print(list_days.index(day.lower()))
            #print(type(list_days.index(day.lower())))
            #index = int(list_days.index(day.lower()) + days%7)%int(list_days.index(day.lower()) + days%7)
            final_day = list_days[(list_days.index(day.lower()) + days%7)%7].capitalize()
        else: 
            return "Day is not valid."
    mod_final_meridian = final_hours_output%24
    #return print(mod_final_meridian)
    if mod_final_meridian >= 12:
        final_hour = str(mod_final_meridian - 12)
        if mod_final_meridian == 12:
            final_hour = str(12)
        final_meridian = 'PM'
    else:
        final_hour = str(mod_final_meridian)
        if final_hour == '0':
            final_hour = '12'
        final_meridian = 'AM'
    #return final_meridian
    if not final_meridian:
        return "Theres is not final meridian"
    if day:
        new_time1 = final_hour + ':' + str(final_minutes) + ' ' + final_meridian + ', ' + final_day
    else:
        new_time1 = final_hour + ':' + str(final_minutes) + ' ' + final_meridian
    if (days != 0) and (days > 1):
        new_time = new_time1 + ' ' + '(' + str(days) + ' days later)'
    elif days == 1:
        new_time = new_time1 + ' ' + '(next day)'
    else:
        new_time = new_time1
    return new_time