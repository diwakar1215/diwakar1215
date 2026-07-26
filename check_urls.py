import urllib.request
import urllib.error

urls = [
    "https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=24&pause=1000&color=8A2BE2&center=true&vCenter=true&width=600&lines=Software+Engineer;Java+Developer;MERN+Stack+Developer;Data+Analytics+Enthusiast;Open+Source+Contributor",
    "https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=24&pause=1000&color=8A2BE2&center=true&vCenter=true&width=600&lines=Software+Engineer;Java+Developer;MERN+Stack+Developer;Data+Analytics+Enthusiast;Open+Source+Contributor",
    "https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white",
    "https://skillicons.dev/icons?i=java,js,ts,python,cpp,html,css",
    "https://github-profile-trophy.vercel.app/?username=diwakar1215",
    "https://streak-stats.demolab.com?user=diwakar1215",
    "https://github-readme-stats.vercel.app/api?username=diwakar1215",
    "https://github-readme-activity-graph.vercel.app/graph?username=diwakar1215",
    "https://github-readme-activity-graph.cyclic.app/graph?username=diwakar1215",
    "https://komarev.com/ghpvc/?username=diwakar1215"
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
