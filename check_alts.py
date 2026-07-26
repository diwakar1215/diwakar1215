import urllib.request
import urllib.error

urls = [
    "https://github-profile-trophy.vercel.app/?username=diwakar1215",
    "https://github-profile-trophy.onrender.com/?username=diwakar1215",
    "https://github-readme-stats.vercel.app/api?username=diwakar1215",
    "https://github-readme-stats.demolab.com/api?username=diwakar1215",
    "https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=24&pause=1000&color=8A2BE2&center=true&vCenter=true&width=600&lines=Software+Engineer;Java+Developer;MERN+Stack+Developer;Data+Analytics+Enthusiast;Open+Source+Contributor",
    "https://raw.githubusercontent.com/diwakar1215/diwakar1215/output/github-contribution-grid-snake-dark.svg",
    "https://raw.githubusercontent.com/diwakar1215/diwakar1215/output/github-contribution-grid-snake.svg",
    "https://raw.githubusercontent.com/diwakar1215/diwakar1215/output/dist/github-contribution-grid-snake.svg"
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
