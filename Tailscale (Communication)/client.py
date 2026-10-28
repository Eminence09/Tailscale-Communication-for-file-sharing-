import urllib.request

# Replace with your actual Tailscale Sender IP
tailscale_ip = "100.127.36.121"
url = f"http://{tailscale_ip}:8000/OneDrive/Pictures/Camera%20Roll/WIN_20240702_20_07_54_Pro.jpg"

urllib.request.urlretrieve(url, "tail_image.jpg")
print("Data transfer complete!")
	