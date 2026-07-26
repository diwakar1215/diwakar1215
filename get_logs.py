import urllib.request
import json
import zipfile
import io

url = "https://api.github.com/repos/diwakar1215/diwakar1215/actions/runs"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        runs = data.get('workflow_runs', [])
        for run in runs:
            print(f"Run ID: {run['id']}, Name: {run['name']}, Conclusion: {run['conclusion']}")
            if run['name'] == 'Generate Snake' and run['conclusion'] == 'failure':
                jobs_url = run['jobs_url']
                jobs_req = urllib.request.Request(jobs_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(jobs_req) as jobs_response:
                    jobs_data = json.loads(jobs_response.read().decode())
                    for job in jobs_data['jobs']:
                        print(f"  Job: {job['name']}, Status: {job['conclusion']}")
                        if job['conclusion'] == 'failure':
                            print(f"  Check URL for logs: {job['html_url']}")
                break
except Exception as e:
    print(e)
