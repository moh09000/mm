import requests
import time

# Define the URL and headers for the POST request
url = "https://ably.com/users/auth_two_factor"
headers = {
    "Host": "ably.com",
    "Cookie": ("hubspotutk=9cc3698eeb38221b2e627cfe7093f806; _gcl_au=1.1.1735562880.1724372407; messagesUtk=f01a48da035b4ca7bd1386cc2fd81b4f; "
               "fpestid=7PZfDWhf0tAnOVtdQ0G9LCYDodyMaF-CZkY6AXLiRaSrPFZ5lej2TVB7-gSctitCNmC3dA; _cc_id=bbe1ac12e7eb6eb6b7a1e37a15171fc3; "
               "newsletter=signedup; OptanonAlertBoxClosed=2024-08-26T21:35:18.596Z; signals-sdk-user-id=393f93a2-3bb5-404f-a723-ba2fee1e6f85; "
               "_uetvid=62f3bd405bff11efb61753484a62fdd0; _ga=GA1.1.2054625547.1724707665; "
               "_hjSessionUser_1372065=eyJpZCI6IjczMTBmNzAyLTQzNGUtNTI0OC04MzQzLTdkNzhiY2U4OWViNSIsImNyZWF0ZWQiOjE3MjQ3MDgxMjE0MzgsImV4aXN0aW5nIjpmYWxzZX0=; "
               "_reb2bgeo=%7B%22city%22%3A%22Cairo%22%2C%22country%22%3A%22Egypt%22%2C%22countryCode%22%3A%22EG%22%2C%22hosting%22%3Afalse%2C%22isp%22%3A%22LINKdotNET%20AS%20number%22%2C%22lat%22%3A30.0588%2C%22proxy%22%3Afalse%2C%22region%22%3A%22C%22%2C%22regionName%22%3A%22Cairo%20Governorate%22%2C%22status%22%3A%22success%22%2C%22timezone%22%3A%22Africa%2FCairo%22%2C%22zip%22%3A%22%22%7D; "
               "SL_C_23361dd035530_SID={\"2528f8b7bdabb714ddbf8c85dbf20ddc22368b35\":{\"sessionId\":\"Qm4hVlSboK8BJSvD4oX4R\",\"visitorId\":\"J4n4r890r5gO2Ix4I0wli\"}}; "
               "_ga_CBCM9QS4TH=GS1.1.1724712342.42.0.1724712342.60.0.0; __hstc=12655464.9cc3698eeb38221b2e627cfe7093f806.1724372406090.1725071354530.1725144510531.9; "
               "__hssrc=1; cookie_test=ping; accept_cookie=yes; hs_session_identified=56606; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Sep+01+2024+02%3A08%3A43+GMT%2B0300+(Eastern+European+Summer+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6b8cbaaa-a0b1-4442-b498-70c43591ddec&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&AwaitingReconsent=false; "
               "ably_device_id=aj%2F0bKlx0woF7gQzC50KN9T7v0EUUSulrD30RhjZwLrkaI%2B0YaqywUdUyLP6VISGktF73tqznIyet9PztB1jto%2F8HeVNjC5eEXlf%2F%2BApXKMsWd626qhmfZUXkvju7pfYHPeNFfaWUqm%2FicEZIexHNGqReteteF%2BBFMkkVk75UM28HEWM%2BJT%2FIUySzKc%3D--Mb7qMovlN1re06qO--VSP36dQt%2B8NXg9rIpATnnQ%3D%3D; "
               "_ably_session=FPXM2gVixptIhUnOWdd1SLSXuN5MelotNeGEkykDyr9QS3tiS1vbwUFRyJ0gq%2FFgjklU%2BHphd2QuOxrv7dZq6DDzt%2BQV62VlzZaMxhk5bsaPe3n1VrHm33Sn2OrGPQelpJTsaPvOU%2BDDkGRF3gEDsFtirrgTYfT4uippTM7tRYdJmQw3BC2jJMN%2BiysznNwSK5TYX9TxdP3cPsYuFDmnAXjK8AMupVyi7BUrMsxcm4AI%2BVFFV6F4YHImAIXYuXruyqQNfUx3OGyifc9gElWJp5SUb%2FzG0Sefg3lzpWdBbGYlsBWDxeMa0w%2FxkO4afFuK5MQC%2FRvdElRxvhHTr79xBb509VE1QUYuWwWBL2gr5Y8%2FNYX%2Fx1bcqZiBJE9ASNzINzk%2BagYv0KZABpIzY2jTeUDC2YHY2zsdY99YoANDK2fF53d%2FUqRw55hccHlGm7%2B99lvO8WUdk9MMqeaLjiYd4st2ng%3D%3D--%2F5PgWYOLtsXuK1k3--qFxTu%2BHdVQqOii8%2FiS7TMw%3D%3D; "
               "OptanonConsent=isGpcEnabled=0&datestamp=Sun+Sep+01+2024+02%3A09%3A21+GMT%2B0300+(Eastern+European+Summer+Time)&version=202402.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6b8cbaaa-a0b1-4442-b498-70c43591ddec&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&AwaitingReconsent=false; __hssc=12655464.26.1725144510531"),
    "Content-Length": "169",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://ably.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://ably.com/users/auth_two_factor",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Priority": "u=0, i",
}

# Define the data for the POST request
data = {
    "utf8": "✓",
    "authenticity_token": "v11IBlMsp5WKXzVMtOX7Zwe-RWUhZX85eK11-KjB-8xLYE6QF6PsDZ-yvulXNHJym2vaLeO2JQPs9VBU1b3C4Q",
    "user_id": "56606",
    "token": "123456",
    "commit": "Verify security code"
}

# Send the request every 10 seconds
while True:
    response = requests.post(url, headers=headers, data=data)
    print(f"Response Code: {response.status_code}")
    time.sleep(10)
