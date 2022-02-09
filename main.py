from plyer import notification
from datetime import datetime as date
import time as t

advisory_supp_time_start = "" # some value
if advisory_supp_time_start == "": raise ValueError("Add a valid time for all of the time vars for the reminder to work")
advisory_supp_time_end = "" # some value
if advisory_supp_time_end == "": raise ValueError("Add a valid time for all of the time vars for the reminder to work")
advisory_init_time_start = "" # some value
if advisory_init_time_start == "": raise ValueError("Add a valid time for all of the time vars for the reminder to work")
advisory_init_time_end = "" # some value
if advisory_init_time_end == "": raise ValueError("Add a valid time for all of the time vars for the reminder to work")

today = date.today().strftime("%A").lower()
time = date.now().strftime("%H:%M")

init_class = ["tuesday", "thursday"]
sup_class = ["monday", "wednesday", "friday"]

while True:
    for i in init_class:
        if today == i:
            if time == advisory_init_time_start:
                notification.notify(
                    title="Advisory Initiative Work",
                    message="Hi, you may take 6 minutes to plan out what you want todo / what to do at home.",
                    app_name="Reminder",
                    timeout=50,
                )
                t.sleep(360.0)
                notification.notify(
                    title="Advisory Initiative Work",
                    message="Hi, you may work on what you planned to do in the previous 6 minutes.",
                    app_name="Reminder",
                    timeout=50,
                )
                while True:
                    if time == advisory_init_time_end:
                        notification.notify(
                            title="Advisory Initiative Work",
                            message="Hi, you may stop working on what you were doing, since its time for you to go",
                            app_name="Reminder",
                            timeout=50,
                        )
                        break

    for i in sup_class:
        if today == i:
            if time == advisory_supp_time_start:
                notification.notify(
                    title="Advisory Support Work",
                    message="Hi, you may take 6 minutes to plan out what you want todo / what to do at home.",
                    app_name="Reminder",
                    timeout=50,
                )
                t.sleep(360.0)
                notification.notify(
                    title="Advisory Support Work",
                    message="Hi, you may work on what you planned to do in the previous 6 minutes.",
                    app_name="Reminder",
                    timeout=50,
                )
                while True:
                    if time == advisory_supp_time_end:
                        notification.notify(
                            title="Advisory Support Work",
                            message="Hi, you may stop working on what you were doing, since its time for you to go",
                            app_name="Reminder",
                            timeout=50,
                        )
                        break


