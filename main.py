
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/6dc7c9fb-7064-4e14-9d1f-9931bf384276/api/v1/run/5ff861d5-b8e7-4aed-acdb-9db4fc85dba6"  
appID = "AstraCS:ENlrUZCtolCFgJecbZZwrJQT:09666943d0d5e362197636145a578353d337ad2e703e45825ca9d4d053204827"
payload = {
    "input_value": "atom",  # The input value to be processed by the flow
    "output_type": "chat", 
    "input_type": "chat" 
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer AstraCS:ENlrUZCtolCFgJecbZZwrJQT:09666943d0d5e362197636145a578353d337ad2e703e45825ca9d4d053204827"  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    