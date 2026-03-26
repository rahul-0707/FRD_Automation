import pytest
import base64

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # HTML report plugin ko connect karo
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    
    # Aapki demand par: 'extras' (with s) use kar rahe hain
    extra = getattr(report, "extras", []) 

    if report.when == "call" and report.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            
            # Screenshot kheencho
            screenshot = page.screenshot(type='png')
            
            # Base64 mein convert karo
            encoded = base64.b64encode(screenshot).decode('utf-8')
            
            # HTML tag image ke liye
            html_img = f'<div><img src="data:image/png;base64,{encoded}" alt="screenshot" style="width:400px;height:auto;" onclick="window.open(this.src)" align="right"/></div>'
            
            # Report mein add karo
            extra.append(pytest_html.extras.html(html_img))
            
    # Report object mein wapas 'extras' set karo
    report.extras = extra