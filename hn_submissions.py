import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code:", r.status_code)

# Process the info from the request and store the response
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Creating a separate API call for each article
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    submission_r = requests.get(url)
    print("Article Status Code:", submission_r.status_code)

    if submission_r.status_code == 200:
        response_dict = submission_r.json()

        # Handle missing keys using `.get()`
        submission_dict = {
            'title': response_dict.get('title', 'No Title'),  # Use 'No Title' if the title key is missing
            'link': f'https://news.ycombinator.com/item?id={submission_id}',
            'comments': response_dict.get('descendants', 0),  # Default to 0 if descendants key is missing
        }
        submission_dicts.append(submission_dict)
    else:
        print(f"Failed to fetch article with ID {submission_id}")

# Sort the submissions by the number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Print the sorted submissions
for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
