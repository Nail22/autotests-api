import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

user_token = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}
get_response_user = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=user_token)
get_response_user_data = get_response_user.json()
print("Me response:", get_response_user_data)
print("Me Status Code:", get_response_user.status_code)
