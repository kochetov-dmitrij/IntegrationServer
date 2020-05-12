# IntegrationServer

### Complete installation instruction and examples of usage can be found in
- readme.txt
- scenarios.txt

### Prerequisites
- python, 'jmespath' package
- virtualbox 5.2
- vagrant 2.0.3
- ansible 2.9

### GitLab:
- URL: http://192.168.11.10/gitlab/devopser/DevopsCalculator
- Project fetched from [kochetov-dmitrij/DevopsCalculator](https://github.com/kochetov-dmitrij/DevopsCalculator)
- User name/pass = devopser/f2qskL4Zd6 (can be modified in roles/gitlab/vars/main.yml)

### Jenkins:
- URL: http://localhost:11001/
- BlueOcean(cool UI): http://localhost:11001/blue/organizations/jenkins/DevopsCalculator/activity/
- Prod server: http://localhost:15900/
- User name/pass = devopser/cLVc1VH73D (can be modified in roles/jenkins/vars/main.yml)

### Artifactory:
- URL: http://localhost:11003/ui/repos/tree/General/generic-local
- User name/pass = admin/sHMHY6iZjh (can be modified in roles/artifactory/vars/main.yml)
