from playwright.sync_api import Page, expect

def test_wikipedia_search(page: Page):
    print("\n🌐 Wikipedia par ja raha hoon...")
    page.goto("https://www.wikipedia.org/")
    
    print("⌨️ 'Software testing' type kar raha hoon...")
    # Wikipedia ke search box ka HTML name 'search' hota hai
    page.locator("[name='search']").fill("Software testing")
    page.locator("[name='search']").press("Enter")
    
    # --- The Judge (Assertion) ---
    print("⚖️ Judge check kar raha hai ki naye page ka title sahi hai ya nahi...")
    
    # Hum expect kar rahe hain ki search hone ke baad page ka title yeh exact text ho
    expect(page).to_have_title("Software testing - Wikipedia")