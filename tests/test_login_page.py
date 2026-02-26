def test_login_page_title(browser):
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_selector("input[name='username']")

    assert "OrangeHRM" in page.title()