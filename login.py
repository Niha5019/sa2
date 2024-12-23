def login(username, password):
    # Simple username and password check
    if username == "admin" and password == "password123":
        return "Login successful!"
    else:
        return "Invalid credentials!"