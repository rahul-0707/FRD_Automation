import pytest

# Base URL hum context mein hi set kar dete hain
@pytest.fixture(scope="session")
def api_context(playwright):
    context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield context
    context.dispose()

def test_get_first_post(api_context):
    # 1. GET Request
    response = api_context.get("/posts/1")
    
    # 2. Status Code Assertion
    assert response.status == 200
    
    # 3. Data Validation
    body = response.json()
    assert body["id"] == 1
    print(f"\nGET Success: Title is '{body['title'][:20]}...'")

def test_create_new_post(api_context):
    # 1. POST Request (Data bhej rahe hain)
    payload = {
        "title": "Rahul QA Day 17",
        "body": "Learning API Automation",
        "userId": 101
    }
    
    response = api_context.post("/posts", data=payload)
    
    # 2. Status Code Assertion (Wahi 201 jo Postman mein aaya!)
    assert response.status == 201
    
    # 3. Response Check
    body = response.json()
    assert body["title"] == "Rahul QA Day 17"
    print(f"\nPOST Success: New ID created is {body.get('id')}")