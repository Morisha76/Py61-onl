import requests

# Task2
api_key = "DEMO-API-KEY"
url = "https://api.thedogapi.com/v1/breeds"

headers = {
    "x-api-key": api_key
}

response = requests.get(url=url, headers=headers)
response.raise_for_status()
dogs = response.json()

print(response)

if dogs:
    first_dog = dogs[0]
    print(f"ID: {first_dog['id']}")
    print(f"Name: {first_dog['name']}")
    print(f"Bred for: {first_dog.get('bred_for', 'Not Available')}")
    print(f"Life span: {first_dog['life_span']}")
    print(f"Temperament: {first_dog.get('temperament', 'Not Available')}")
    print(f"Origin: {first_dog['origin']}")
    print(f"Reference_image_id: {first_dog['reference_image_id']}")
else:
    print("No dogs found in the API response.")

# Task3
sorted_dogs = sorted(dogs, key=lambda x: x.get('life_span', 'Not Available'))
print("Top 5 Dog Breeds (Sorted by Life Span):")
for dog in sorted_dogs[0:5]:
    print(f"{dog['name']}: {dog.get('life_span', 'Unknown')}")

# Task4
print("Dog Bred Names:")
for dog in dogs:
    print(dog['name'])

# Task5
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        if response.status_code == 404:
            print("Not found.")
        elif response.status_code == 500:
            print("Internal Server Error. Try again.")
        else:
            print(f"Error HTTP {response.status_code}: {response.reason}")
        return None

    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
        print("Could not connect to server. Check the Internet connection.")
        return None

    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        print("The server response time exceeded.")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
        return None

    url = "https://api.thedogapi.com/v1/breeds"  # URL, который существует
    url = "https://jsonplaceholder.typicode.com/posts/99999" # URL, который не существует

    data = fetch_data(url)
    if data:
        print("Data are obtained:")
        print(data)
    else:
        print("Data could not be obtained.")



