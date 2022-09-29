import requests
import json

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?sol=1000&api_key="
key = "kLTrNrLMzJSOPREtbMCUoFKxXQej7O1Dw61uIadC"

def web_build_page(url):
    
    headers = {
        "sol": "1000",
        "api_key": key
        }
    response = requests.request("GET", url, headers=headers)
    
    return json.loads(response.text)

data = web_build_page(f"{url}{key}")["latest_photos"]

html_a = ""
html = ""
html_p = ""
url_list = []

for i,j in enumerate(data):
    
    if i == 0:
        html_a += "<html>\n<head>\n</head>\n<body>"

    elif i > 0 and i <26:
        html += "<li><img src =" + j["img_src"] + " width='250' height='250'></li>\n"
        url_list.append(j["img_src"])
       
    elif i == 26:
        html_p += "</ul>\n</body>\n</head>\n</html>"
        break
        
with open("Rover_4.html", "w") as f:
    
    f.write(html_a + html + html_p)

print(url_list)

