import pytest
import base64

# Yeh Hook har test ke khatam hone par chalta hai
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # HTML report plugin ko connect karo
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    
    # Version 4.x ke liye 'extra' (bina s ke) variable initialize karo
    extra = getattr(report, "extra", [])

    # Agar test 'call' phase mein FAIL hua hai...
    if report.when == "call" and report.failed:
        # Check karo ki kya 'page' fixture available hai
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            
            # 1. Screenshot kheencho (PNG format mein)
            screenshot = page.screenshot(type='png')
            
            # 2. Screenshot ko Base64 text mein badlo (Taaki report ke andar fit ho jaye)
            encoded = base64.b64encode(screenshot).decode('utf-8')
            
            # 3. HTML tag banao photo dikhane ke liye
            html_img = f'<div><img src="data:image/png;base64,{encoded}" alt="screenshot" style="width:400px;height:auto;" onclick="window.open(this.src)" align="right"/></div>'
            
            # 4. Is photo ko report ke 'extra' list mein add kar do
            extra.append(pytest_html.extras.html(html_img))
            
    # Report mein extra data (screenshot) update karo
    report.extra = extra