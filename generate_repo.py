import os
import base64

def create_file(path, content, is_binary=False):
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    mode = 'wb' if is_binary else 'w'
    with open(path, mode) as f:
        f.write(content)

# DUMMY PNG (1x1 transparent)
PNG_CONTENT = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=')

# DUMMY PDF
PDF_CONTENT = b'%PDF-1.4\n1 0 obj\n<< /Title (Resume) /Creator (AI) >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF'

BANNER_SVG = """<svg width="800" height="250" viewBox="0 0 800 250" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0a0a0a" />
            <stop offset="50%" stop-color="#1a1025" />
            <stop offset="100%" stop-color="#000000" />
        </linearGradient>
        <linearGradient id="text-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#8a2be2" />
            <stop offset="50%" stop-color="#4169e1" />
            <stop offset="100%" stop-color="#00ffff" />
        </linearGradient>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <rect width="800" height="250" rx="15" fill="url(#bg)" />
    
    <g transform="translate(40, 80)">
        <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="48" font-weight="bold" fill="#ffffff" filter="url(#glow)">Diwakar Singh</text>
        <text x="0" y="45" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="24" fill="#a0a0a0">Software Engineer</text>
        
        <!-- Tags -->
        <g transform="translate(0, 85)">
            <rect x="0" y="0" width="70" height="30" rx="15" fill="#2d1b4e" stroke="#8a2be2" stroke-width="1"/>
            <text x="35" y="20" font-family="sans-serif" font-size="12" fill="#ffffff" text-anchor="middle">Java</text>
            
            <rect x="80" y="0" width="80" height="30" rx="15" fill="#1b2a4e" stroke="#4169e1" stroke-width="1"/>
            <text x="120" y="20" font-family="sans-serif" font-size="12" fill="#ffffff" text-anchor="middle">MERN</text>

            <rect x="170" y="0" width="60" height="30" rx="15" fill="#1b4e4e" stroke="#00ffff" stroke-width="1"/>
            <text x="200" y="20" font-family="sans-serif" font-size="12" fill="#ffffff" text-anchor="middle">AI</text>
            
            <rect x="240" y="0" width="90" height="30" rx="15" fill="#4e4e1b" stroke="#ffff00" stroke-width="1"/>
            <text x="285" y="20" font-family="sans-serif" font-size="12" fill="#ffffff" text-anchor="middle">Power BI</text>
        </g>
    </g>
    
    <!-- Decorative Elements -->
    <circle cx="700" cy="50" r="100" fill="#8a2be2" opacity="0.1" filter="url(#glow)"/>
    <circle cx="600" cy="200" r="80" fill="#4169e1" opacity="0.1" filter="url(#glow)"/>
</svg>
"""

README_CONTENT = """<div align="center">

<img src="./assets/banner.svg" alt="Diwakar Singh Banner" width="100%" />

<br/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=24&pause=1000&color=8A2BE2&center=true&vCenter=true&width=600&lines=Software+Engineer;Java+Developer;MERN+Stack+Developer;Data+Analytics+Enthusiast;Open+Source+Contributor)](https://git.io/typing-svg)

<p align="center">
  <a href="https://diwakarsingh.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white" alt="Portfolio"/></a>
  <a href="https://linkedin.com/in/diwakar-singh"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:contact@example.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="./assets/Diwakar_Singh_Resume.pdf"><img src="https://img.shields.io/badge/Resume-4CAF50?style=for-the-badge&logo=Read.cv&logoColor=white" alt="Resume"/></a>
</p>

---

</div>

## 👨🏻‍💻 About Me

I am a passionate **Software Engineer** specializing in full-stack development, backend systems, and data analytics. I love solving complex engineering problems and building scalable, user-centric applications.

- 🔭 **Current Focus:** Data Structures & Algorithms, System Design, Spring Boot, Docker, AWS, Open Source
- 🌱 **Learning:** Advanced System Architecture, Cloud Native Applications
- 💬 **Ask me about:** Java, React, Node.js, MERN Stack, Data Analytics
- ⚡ **Fun fact:** I believe every complex problem has a beautiful, simple solution hiding within it.

<br/>

## 🛠️ Tech Stack & Skills

<div align="center">

### Languages
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=java,js,ts,python,cpp,html,css" />
</a>

### Frameworks & Libraries
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=react,spring,nodejs,express,bootstrap,tailwind" />
</a>

### Databases & Cloud
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=mongodb,mysql,postgres,aws,gcp" />
</a>

### DevOps & Tools
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=docker,git,github,linux,postman,vscode" />
</a>

</div>

<br/>

## 🚀 Featured Projects

| 🤖 Intervix AI | 🎨 HueHaven |
| :--- | :--- |
| **AI Interview Platform**<br/>Built with React, Node, Express, MongoDB.<br/>*Next-generation mock interview platform powered by AI.* | **Java GUI Application**<br/>Built with Java Swing, MySQL.<br/>*Elegant color palette generator and management system.* |
| [View Repository](#) | [View Repository](#) |

| 🏦 Banking System | 📊 India GDP Dashboard |
| :--- | :--- |
| **Full Stack FinTech App**<br/>MERN Stack implementation.<br/>*Secure, scalable banking management solution.* | **Data Analytics**<br/>Power BI visualization.<br/>*Comprehensive analytical dashboard for economic data.* |
| [View Repository](#) | [View Repository](#) |

<br/>

## 📈 GitHub Statistics

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username=diwakar1215&theme=onedark&no-frame=true&no-bg=true&margin-w=15" alt="GitHub Trophies" />

<br/><br/>

[![GitHub Streak](https://streak-stats.demolab.com?user=diwakar1215&theme=tokyonight&hide_border=true&border_radius=10)](https://git.io/streak-stats)

<br/>

<img src="https://github-readme-stats.vercel.app/api?username=diwakar1215&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="GitHub Stats" width="48%" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=diwakar1215&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="Top Languages" width="48%" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=diwakar1215&theme=tokyo-night&hide_border=true&area=true" alt="Activity Graph" width="100%" />

### 🐍 Contribution Snake

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/diwakar1215/diwakar1215/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/diwakar1215/diwakar1215/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/diwakar1215/diwakar1215/output/github-contribution-grid-snake.svg">
</picture>

</div>

<br/>

## 🏆 Coding Profiles

<div align="center">
  <a href="https://leetcode.com/diwakar1215"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=white" alt="LeetCode"/></a>
  <a href="https://codeforces.com/profile/diwakar1215"><img src="https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=Codeforces&logoColor=white" alt="Codeforces"/></a>
  <a href="https://auth.geeksforgeeks.org/user/diwakar1215"><img src="https://img.shields.io/badge/GeeksforGeeks-298D46?style=for-the-badge&logo=GeeksforGeeks&logoColor=white" alt="GeeksforGeeks"/></a>
</div>

<br/>

<div align="center">
  
> *"Code is like humor. When you have to explain it, it’s bad."* — Cory House

<br/>

![](https://komarev.com/ghpvc/?username=diwakar1215&color=8A2BE2&style=flat-square&label=PROFILE+VIEWS)

<a href="#top">Back to Top ⬆️</a>

</div>
"""

SETUP_CONTENT = """# Setup Guide

Follow these instructions to set up your GitHub profile repository perfectly.

## 1. Repository Creation
1. Create a new repository with a name exactly matching your GitHub username (`diwakar1215`).
2. Make sure it is **Public**.
3. Initialize it with a README (or just push this generated code).

## 2. GitHub Actions Permissions
To ensure the automated workflows (like the Snake animation) run correctly:
1. Go to your repository **Settings**.
2. Navigate to **Actions** -> **General**.
3. Under **Workflow permissions**, select **Read and write permissions**.
4. Click **Save**.

## 3. Customization
- **Images**: Replace the placeholder images in `assets/screenshots/` with actual screenshots of your projects.
- **Resume**: Replace `assets/Diwakar_Singh_Resume.pdf` with your actual resume.
- **Links**: Search the `README.md` for `mailto:contact@example.com` or `#` and replace them with your actual email and project links.

## 4. Trigger Workflows
1. Go to the **Actions** tab in your repository.
2. Select the **Generate Snake** workflow.
3. Click **Run workflow**. 
4. Once completed, a new branch `output` will be created containing the snake SVG, which the README uses!

For further customization, refer to [docs/customization.md](./docs/customization.md).
"""

CUSTOMIZATION_CONTENT = """# Customization Guide

## Theme Colors
The current theme uses a dark aesthetic with **Purple** (`#8A2BE2`) and **Blue** (`#4169E1`) accents.
If you wish to change these colors:
1. Edit `assets/banner.svg` and change the hex codes in the `<linearGradient>` and tags.
2. Edit `README.md` and update badge colors (e.g., changing `color=8A2BE2` in the Visitor counter).

## Stats Themes
We are using `tokyonight` theme for stats. 
Available themes include `dracula`, `radical`, `onedark`, `github_dark`, etc.
Update the `theme=` parameter in the README image URLs to switch themes.

## Projects
To add more projects, simply copy a markdown table row in the **Featured Projects** section of `README.md`.
"""

TROUBLESHOOTING_CONTENT = """# Troubleshooting

## Images Not Loading
- Ensure the image paths are correct and case-sensitive.
- For the Snake animation, ensure the GitHub Action has run successfully and pushed to the `output` branch.

## Badges/Stats Not Showing
- Vercel-hosted stats APIs (like `github-readme-stats`) occasionally face rate limits or downtime. Give it a few minutes and refresh.
- Check if your GitHub username is spelled correctly in the URLs.

## Workflow Failing
- Did you give "Read and write permissions" to GitHub Actions in Repo Settings?
- Check the Action logs for specific error messages.
"""

GITIGNORE_CONTENT = """# macOS
.DS_Store

# IDE
.idea/
.vscode/

# Node
node_modules/
npm-debug.log
yarn-error.log

# Temp
*.tmp
*.bak
"""

LICENSE_CONTENT = """MIT License

Copyright (c) 2026 Diwakar Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

SNAKE_YML = """name: Generate Snake

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
  push:
    branches:
    - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Generate snake animation
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
            
      - name: Push to output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""

UPDATE_README_YML = """name: Update README

on:
  schedule:
    - cron: '0 */6 * * *'
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Keepalive Workflow
        uses: gautamkrishnar/keepalive-workflow@v1
"""

LINT_YML = """name: Lint Markdown

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Markdown Lint
      uses: DavidAnson/markdownlint-cli2-action@v13
      with:
        globs: "**/*.md"
"""

LINKS_CHECK_YML = """name: Check Broken Links

on:
  schedule:
    - cron: "00 12 * * 1"
  workflow_dispatch:

jobs:
  link-checker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Link Checker
        uses: lycheeverse/lychee-action@v1.9.0
        with:
          args: --accept  200,204,429,403 --exclude-mail --no-progress './**/*.md'
"""

ASSETS_README_CONTENT = """# Assets

This directory contains static assets for the GitHub profile.

- `banner.svg`: The main profile banner
- `Diwakar_Singh_Resume.pdf`: Your resume file
- `screenshots/`: App screenshots used in the README
- `*.png`: Placeholder images
"""

# Dictionary mapping file paths to their content
files = {
    'README.md': README_CONTENT,
    'SETUP.md': SETUP_CONTENT,
    'LICENSE': LICENSE_CONTENT,
    '.gitignore': GITIGNORE_CONTENT,
    'assets/README.md': ASSETS_README_CONTENT,
    'assets/banner.svg': BANNER_SVG,
    'docs/customization.md': CUSTOMIZATION_CONTENT,
    'docs/troubleshooting.md': TROUBLESHOOTING_CONTENT,
    '.github/workflows/snake.yml': SNAKE_YML,
    '.github/workflows/update-readme.yml': UPDATE_README_YML,
    '.github/workflows/lint.yml': LINT_YML,
    '.github/workflows/links-check.yml': LINKS_CHECK_YML
}

binary_files = {
    'assets/profile-photo-placeholder.png': PNG_CONTENT,
    'assets/social-preview.png': PNG_CONTENT,
    'assets/screenshots/intervix.png': PNG_CONTENT,
    'assets/screenshots/huehaven.png': PNG_CONTENT,
    'assets/screenshots/banking.png': PNG_CONTENT,
    'assets/screenshots/powerbi.png': PNG_CONTENT,
    'assets/screenshots/smarthome.png': PNG_CONTENT,
    'assets/Diwakar_Singh_Resume.pdf': PDF_CONTENT
}

for path, content in files.items():
    create_file(path, content, is_binary=False)

for path, content in binary_files.items():
    create_file(path, content, is_binary=True)

print("Repository generation complete.")
