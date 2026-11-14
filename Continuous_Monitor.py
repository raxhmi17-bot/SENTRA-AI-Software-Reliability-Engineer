import urllib.request
import time

print("================================")
print("       SENTRA AI SYSTEM")
print("   CONTINUOUS MONITORING")
print("================================")

url = input("Enter Website URL: ")

while True:
    try:
        start = time.time()

        response = urllib.request.urlopen(url, timeout=10)

        end = time.time()
        response_time = (end - start) * 1000

        print("\nWebsite Status: HEALTHY")
        print("Status Code:", response.status)
        print("Response Time:", round(response_time, 2), "ms")

    except Exception as e:
        print("\nSENTRA ALERT!")
        print("Website Status: UNHEALTHY")
        print("Error:", e)

    choice = input("\nContinue Monitoring? (yes/no): ")

    if choice.lower() != "yes":
        print("\nMonitoring Stopped.")
        break

    time.sleep(5)
