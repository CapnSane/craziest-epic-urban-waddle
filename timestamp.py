from datetime import datetime

timestamp = 637776829355875500 / 10**9
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

