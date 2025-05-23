import requests

def submit_feedback(name, email, gender, interests, comments):
    url = "http://localhost:5001/submit_feedback"
    data = [
    ('name', name),
    ('email', email),
    ('gender', gender),
] + [('interests', i) for i in interests] + [('comments', comments)]

    response = requests.post(url, data=data)

    if "Feedback Received" in response.text:
        return True
    else:
        return False

print("Test 1 (Valid):", submit_feedback(
    "Rahul Vangala", "rahul@example.com", "Male", ["Coding", "Music"], "This is awesome!"
))  

print("Test 2 (Missing Email):", submit_feedback(
    "Rahul Vangala", "", "Male", ["Coding", "Music"], "Missing email!"
)) 
