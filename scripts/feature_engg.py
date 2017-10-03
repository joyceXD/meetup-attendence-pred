import math


UNIX_4_WEEKS = 2419200000


def count_past_group_events(df, event_id):
    event = df[df.e_event_id == event_id]
    event_time = int(event.e_time)
    group_id = event.e_group_id.values[0]
    past_events = df[(df.e_time > (event_time - UNIX_4_WEEKS)) & (df.e_time < event_time) & (df.e_group_id==group_id)]
    return past_events.shape[0]


def count_past_user_events(df, user_id, event_id):
    event = df[(df.user_id == user_id) & (df.e_event_id == event_id)]
    event_time = int(event.e_time)
    user_id = event.user_id.values[0]
    past_events = df[(df.e_time > (event_time - UNIX_4_WEEKS)) & (df.e_time < event_time) & (df.user_id==user_id)]
    return past_events.shape[0]


def label_attendance(attend):
    if attend == 'yes' or attend == 'waitlist':
        return 1
    else:
        return 0
