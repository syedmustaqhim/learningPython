# from datetime import datetime
# import pytz

# utc = pytz.utc

# now = datetime.now(tz=utc)
# ist_now = now.astimezone(ist)

# print(now)
# print(ist_now)
sq_iterator = (x**2 for x in range(10))
print(list(sq_iterator))
