try:
    from plyer import notification
    from datetime import datetime as date
    import time as t
    import gkeepapi

except:
    import pip
    import time as t
    import sys

    location = input("SITE PACKAGES LOCATION: ")
    pip.main(["install", f"--target={location}", "plyer", "gkeepapi"])
    print("SHUTTING APP DOWN... (please reopen to use)")
    t.sleep(3.0)
    sys.exit(0)


notification.notify(
    title="Advisory Work",
    message="Hi, please edit the TODO DURING ADVISORY note in 6 minutes for what you plan todo, enter stuff in TODO HOME which you would like todo at home.",
    timeout=10,
)
t.sleep(360.0)
notification.notify(
    title="Alert",
    message="Hi, please save your keep status, get ready to do the work in it.",
    timeout=10,
)
t.sleep(10.0)

# look through what the user has entered:
tasks = {}

keep = gkeepapi.Keep()
credentials = open("credentials/cred.txt", "r").readlines()
keep.login(credentials[0], credentials[1])

TODO = keep.get("1azgd59O9ryNeIbTyVis5sXr9vyBHts8mWOFQ5-bwU8itBjzwCkqFW5KXVslEAaE")

prev = ""
for i in TODO.text.split():
    if "m" in i:
        tasks[prev.removesuffix(":")] = i.removesuffix("m")
    elif ":" in i:
        prev = i


for i in tasks:
    notification.notify(
        title=f"{i}",
        message=f"Hi, you may start doing {i} for {tasks[i]} minutes.",
        timeout=10,
    )
    t.sleep(float(float(tasks[i])*60.0))

notification.notify(
        title=f"Your Work Is Complete!",
        message=f"Hi, you may wrap up what your doing since you've completed all your work!",
        timeout=10,
)
