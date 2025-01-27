import requests

#Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url) 
print("Status Code: ",r.status_code)

#Store the result from the api call in a variable
response_dict = r.json()
print("Total respositoreis",response_dict['total_count'])

#Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ",len(repo_dicts))

#Read the first repo
repo_dict = repo_dicts[0]
print("\nKeys: ",len(repo_dict))

for key in sorted(repo_dict.keys()):
    print(key)



print("\nSelected information about first repo: ")
print('\nName: ', repo_dict['name'])
print('Owner: ',repo_dict['owner']['login'])
print('Starts: ',repo_dict['stargazers_count'])
print('Repository: ',repo_dict['html_url'])
print('Description: ',repo_dict['description'])
