import requests

SUBSCRPTION_KEY = "EBTk7SwGZlwpQhYgOGxvB4TPeT1ljCPygNWcnNlNY3mK8AzOvxMAJQQJ99BGACYeBjFXJ3w3AAAFACOGWMCy"
ENDPOINT = "https://winkey-computervision-001.cognitiveservices.azure.com/"

def analyze_image(image_path):
    ENDPOINT_URL = ENDPOINT + "vision/v3.2/analyze"

    params = {"visualFeatures": "Categories,Description,Color"}
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRPTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    except Exception as e:
        print(f"Error reading image file: {e}")
        return None
    
    response = requests.post(ENDPOINT_URL, params=params, headers=headers, data=image_data)
    if response.status_code == 200:
        analysis = response.json()
        return analysis
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def main():
    image_path = input("Enter the path to the image file: ")

    result = analyze_image(image_path)
    if result:
        print("Analysis Result:")
        print(result)

if __name__ == "__main__":
    main()