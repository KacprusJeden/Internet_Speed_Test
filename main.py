import math
import speedtest

def get_MB_size(bytes) -> float:
    i = int(math.floor(math.log(bytes, 1024)))
    power = math.pow(1024, i)
    mbps = round(bytes / power, 2)
    return mbps

wifi = speedtest.Speedtest()

print("Getting download speed...")
download_speed = get_MB_size(wifi.download())

print("Getting upload speed...")
upload_speed = get_MB_size(wifi.upload())

print(f"Download: {download_speed} mbps")
print(f"Upload: {upload_speed} mbps")