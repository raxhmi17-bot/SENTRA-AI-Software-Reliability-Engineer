
import urllib.request
import urllib.error

print("================================")
print("       SENTRA AI SYSTEM")
print(" Intelligent Reliability Engineer")
print("================================")

url = input("Enter website URL: ")

try:
    response = urllib.request.urlopen(url, timeout=10)

    print("\nSENTRA STATUS: ONLINE")
    print("Website Status Code:", response.status)

except Exception as e:
    print("\nSENTRA ALERT: WEBSITE ISSUE")
    print("Possible Error:", e)
