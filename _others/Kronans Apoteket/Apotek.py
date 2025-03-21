import requests
import jwt  # Install with: pip install pyjwt
from datetime import datetime

# Replace these with your actual values
GOOGLE_MAPS_API_KEY = "AIzaSyCnwqy4Lu8CEvaS6TrX9v2THYkubjFWID4"
FIREBASE_AUTH_TOKEN = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6NTc3MzIwMTcxODg5OmFuZHJvaWQ6MmU5OTVjOGI4NWU1NzE2NWJkOWVkMCIsImV4cCI6MTc0MzE4Nzc2MSwiZmlkIjoiZFUtUHBsRHdSdkNMWi16UjBuVzVQTSIsInByb2plY3ROdW1iZXIiOjU3NzMyMDE3MTg4OX0.AB2LPV8wRAIgHqHvwm-Ae7BLnltgMGO72V-g19yAly6t2kasAali1A4CIFaOsu6CSrciMoyy0rL9t2RLynnMqDdRv97I4e6DrDtn"
FIREBASE_REFRESH_TOKEN = "3_AS3qfwJ7bfNTvQvtUQfn-gpPVmSBaDaFb4qDjnJ-afRqpXMReZQ7XWl3-wpjSRBuxOhwsfEJ7HhswDzBIinSB3SPmC4y_bksSZVkulZDBbW-im0"
FIREBASE_SESSION_ID = "8d67b459f0594c75b7dffb63daae26c4"

# Function to validate Google Maps API key
def validate_google_maps_api_key(api_key):
    print("Validating Google Maps API key...")
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") == "OK":
        print("✅ Google Maps API key is valid.")
        print("Formatted Address:", data["results"][0]["formatted_address"])
    else:
        print("❌ Google Maps API key is invalid or restricted.")
        print("Error:", data.get("error_message", "Unknown error"))

# Function to validate Firebase AuthToken
def validate_firebase_auth_token(auth_token):
    print("\nValidating Firebase AuthToken...")
    try:
        # Decode the JWT token
        decoded_token = jwt.decode(auth_token, options={"verify_signature": False})
        exp_time = decoded_token.get("exp")
        if exp_time:
            exp_time = datetime.fromtimestamp(exp_time)
            print("✅ Firebase AuthToken is valid.")
            print("Expiration Time:", exp_time)
        else:
            print("❌ Firebase AuthToken is missing expiration time.")
    except jwt.ExpiredSignatureError:
        print("❌ Firebase AuthToken has expired.")
    except jwt.InvalidTokenError:
        print("❌ Firebase AuthToken is invalid.")

# Function to validate Firebase RefreshToken
def validate_firebase_refresh_token(refresh_token):
    print("\nValidating Firebase RefreshToken...")
    if refresh_token and len(refresh_token) > 10:  # Basic check for token format
        print("✅ Firebase RefreshToken appears to be valid.")
    else:
        print("❌ Firebase RefreshToken is invalid or malformed.")

# Function to validate Firebase Session ID
def validate_firebase_session_id(session_id):
    print("\nValidating Firebase Session ID...")
    if session_id and len(session_id) == 32:  # Basic check for session ID format
        print("✅ Firebase Session ID appears to be valid.")
    else:
        print("❌ Firebase Session ID is invalid or malformed.")

# Main function to run all checks
def main():
    # Validate Google Maps API key
    validate_google_maps_api_key(GOOGLE_MAPS_API_KEY)

    # Validate Firebase tokens and session ID
    validate_firebase_auth_token(FIREBASE_AUTH_TOKEN)
    validate_firebase_refresh_token(FIREBASE_REFRESH_TOKEN)
    validate_firebase_session_id(FIREBASE_SESSION_ID)

if __name__ == "__main__":
    main()
