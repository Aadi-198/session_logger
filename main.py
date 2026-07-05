import ctypes

# 1. Define the Python version of your C struct
class Session(ctypes.Structure):
    _fields_ = [("id", ctypes.c_int),
                ("duration", ctypes.c_float)]

# 2. Load your C library
lib = ctypes.CDLL("./liblogger.so")

# 3. Create a session object
my_session = Session(id=1, duration=30.5)

# 4. Call the C function
lib.save_session(my_session)

print("Session sent to C and saved to binary file!")