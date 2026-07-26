import urllib.request
import urllib.error

urls = [
    "https://github-profile-trophy-a0c.vercel.app/?username=diwakar1215",
    "https://github-readme-stats-eight-theta.vercel.app/api?username=diwakar1215",
    "https://github-readme-stats.shion.dev/api?username=diwakar1215",
    "https://github-profile-trophy.cyclic.app/?username=diwakar1215",
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=10)
        print(f"OK ({response.getcode()}): {url}")
    except urllib.error.URLError as e:
        print(f"FAIL ({e}): {url}")
    except Exception as e:
        print(f"ERROR ({e}): {url}")
