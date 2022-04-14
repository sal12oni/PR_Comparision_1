import requests
import base64

import urllib3
import yaml
import json
import os
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pullRequestLink = os.getenv("Pull_Request")
def get_pullRequest_number(pullRequestLink):
    getprnumber=[]
    for pullRequestLink in pullRequestLink.split(","):
        pullRequestNumber = pullRequestLink.split("_")
        print("pullRequestNumber",pullRequestNumber)
        if len(pullRequestNumber) > 1:
            getprnumber.append(pullRequestNumber[-1])
    print("getprnumber", getprnumber)

get_pullRequest_number(pullRequestLink)

print("pullRequestLink", pullRequestLink)
data = pullRequestLink.split(";")
print("data",data)

pr_brk= list(filter(None, data[1].split("/")))
project = pr_brk[pr_brk.index('projects')+1]
repoName = pr_brk[pr_brk.index('repos')+1]
pullRequestNumber = pr_brk[pr_brk.index('pull-requests') +1]

def get_pr_application(project, repoName, pullRequestNumber):
    pullRequestDiffUrl = "https://git.tools.pci.aws/rest/api/1.0/project/{project}/repos/{repoName}/pull-requests/{pullRequestID}/Diff?contextLine=owhitespace=ignoreall"
    pullRequestDiffUrl = pullRequestDiffUrl.format(project=project, repoName=repoName, pullRequestID=pullRequestNumber)
    r = requests.get(pullRequestDiffUrl, headers={"Authorization": "Beebksdbcksdn", 'content': 'application/json'}, verify=false)
    PR_diff_json_data = r.json()

    print("PR_diff_json_data", PR_diff_json_data)
    pr_application = PR_diff_json_data['diff'][0] ['source']['name']
    print("pr_application",pr_application)
    return pr_application
