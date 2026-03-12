import pytest

# Yeh ek VIP Hook (CCTV Camera) hai jo har test ke result par nazar rakhta hai
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # HTML report wale plugin ko jagao
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])
    
    # Agar test fail hua hai (call phase mein)...
    if report.when == "call" and report.failed:
        # Check karo ki kya is test mein 'page' (browser) use hua tha?
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            
            # Browser se turant ek photo (screenshot) kheencho
            screenshot = page.screenshot(type='png')
            
            # Photo ko code mein convert karke (Base64) direct HTML mein chipka do
            import base64
            encoded = base64.b64encode(screenshot).decode('utf-8')
            html = f'<div><img src="data:image/png;base64,{encoded}" alt="screenshot" style="width:600px;height:auto;" onclick="window.open(this.src)" align="right"/></div>'
            
            # Report ke andar yeh photo (html code) add kar do
            extra.append(pytest_html.extras.html(html))
            
    report.extras = extra