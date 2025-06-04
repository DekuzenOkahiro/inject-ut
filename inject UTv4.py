from mitmproxy import http
import json

def request(flow: http.HTTPFlow):
    print(f"[MITM] Intercepted: {flow.request.method} {flow.request.pretty_url}")
    if "/apiv4r11/auth_key" in flow.request.path:
        flow.response = http.Response.make(
            200,
            json.dumps({
                "data": "9C89F3F568FAFFD20ADB229284923C587D480EC450933CBF38E4EF981F72932D26AE4058DF4DCD65B18EF16E3F93669782AACD6109B4DC7EA722107EA1FFEBAAB67044E5D7F939F713BB938EB8F0C245"
            }),
            {"Content-Type": "application/json"}
        )
