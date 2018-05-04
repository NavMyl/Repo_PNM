import json


json_string = '''
{
    "_links": {
        "base": "http://localhost:8080/confluence",
        "context": "",
        "next": "/rest/api/space/ds/content/page?limit=5&start=10",
        "prev": "/rest/api/space/ds/content/page?limit=5&start=0",
        "self": "http://localhost:8080/confluence/rest/api/space/ds/content/page"
    },
    "limit": 5,
    "results": [
        {
            "_expandable": {
                "ancestors": "",
                "body": "",
                "children": "/rest/api/content/98314/child",
                "container": "",
                "descendants": "/rest/api/content/98314/descendant",
                "history": "/rest/api/content/98314/history",
                "metadata": "",
                "space": "/rest/api/space/ds",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8080/confluence/rest/api/content/98314",
                "tinyui": "/x/CoAB",
                "webui": "/pages/viewpage.action?pageId=98314"
            },
            "id": "98314",
            "status": "current",
            "title": "Let's edit this page (step 3 of 9)",
            "type": "page"
        },
        {
            "_expandable": {
                "ancestors": "",
                "body": "",
                "children": "/rest/api/content/98313/child",
                "container": "",
                "descendants": "/rest/api/content/98313/descendant",
                "history": "/rest/api/content/98313/history",
                "metadata": "",
                "space": "/rest/api/space/ds",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8080/confluence/rest/api/content/98313",
                "tinyui": "/x/CYAB",
                "webui": "/pages/viewpage.action?pageId=98313"
            },
            "id": "98313",
            "status": "current",
            "title": "Tell people what you think in a comment (step 8 of 9)",
            "type": "page"
        },
        {
            "_expandable": {
                "ancestors": "",
                "body": "",
                "children": "/rest/api/content/98312/child",
                "container": "",
                "descendants": "/rest/api/content/98312/descendant",
                "history": "/rest/api/content/98312/history",
                "metadata": "",
                "space": "/rest/api/space/ds",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8080/confluence/rest/api/content/98312",
                "tinyui": "/x/CIAB",
                "webui": "/pages/viewpage.action?pageId=98312"
            },
            "id": "98312",
            "status": "current",
            "title": "Prettify the page with an image (step 4 of 9)",
            "type": "page"
        },
        {
            "_expandable": {
                "ancestors": "",
                "body": "",
                "children": "/rest/api/content/98311/child",
                "container": "",
                "descendants": "/rest/api/content/98311/descendant",
                "history": "/rest/api/content/98311/history",
                "metadata": "",
                "space": "/rest/api/space/ds",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8080/confluence/rest/api/content/98311",
                "tinyui": "/x/B4AB",
                "webui": "/pages/viewpage.action?pageId=98311"
            },
            "id": "98311",
            "status": "current",
            "title": "Lay out your page (step 6 of 9)",
            "type": "page"
        },
        {
            "_expandable": {
                "ancestors": "",
                "body": "",
                "children": "/rest/api/content/98310/child",
                "container": "",
                "descendants": "/rest/api/content/98310/descendant",
                "history": "/rest/api/content/98310/history",
                "metadata": "",
                "space": "/rest/api/space/ds",
                "version": ""
            },
            "_links": {
                "self": "http://localhost:8080/confluence/rest/api/content/98310",
                "tinyui": "/x/BoAB",
                "webui": "/pages/viewpage.action?pageId=98310"
            },
            "id": "98310",
            "status": "current",
            "title": "Learn the wonders of autoconvert (step 7 of 9)",
            "type": "page"
        }
    ],
    "size": 5,
    "start": 5
}
'''

data = json.loads(json_string)

for p in data['results']:
    print (p['id'],p['status'])

#for item in data:
data_formatted = json.dumps(data,indent= 2)
print(data_formatted)