import urllib.request
import time

print("================================")
print("       SENTRA AI SYSTEM")
print("   Website Health Monitoring")
print("================================")

url = input("Enter website URL: ")

try:
    start = time.time()

    response = urllib.request.urlopen(
        url, timeout=10
    )

    end = time.time()
    response_time = (end - start) * 1000

    print("\nSENTRA REPORT")
    print("----------------------------")
    print("Website:", url)
    print("Status Code:", response.status)
    print("Response Time:",
          round(response_time, 2), "ms")

    if response.status == 200:
        print("Health Status: HEALTHY")
    else:
        print("Health Status: CHECK REQUIRED")

except Exception as e:
    print("\nSENTRA ALERT!")
    print("Health Status: UNHEALTHY")
    print("Error:", e)

print("\nMonitoring completed.")
