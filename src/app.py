import requests


def lambda_handler(event, context):
    try:
        # Making a request to The Cat API
        response = requests.get("https://api.thecatapi.com/v1/images/search")

        # Checking if request was successful
        if response.status_code == 200:
            data = response.json()
            image_url = data[0]["url"]
            return {"statusCode": 200, "body": image_url}
        else:
            return {
                "statusCode": response.status_code,
                "body": f"Failed to fetch cat image: {response.text}",
            }
    except Exception as e:
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}
