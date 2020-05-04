# IntegrationServer

### Prerequisites
- python, 'jmespath' package 
- virtualbox 5.2
- vagrant 2.0.3
- ansible 2.9

Installation for ubuntu. Highly recommnded to use 18.04. Problems with repos and dependencies on 19.04 and 19.10
```
ssh-keygen  # if ~/.ssh/id_rsa doesn't exist

sudo apt install python python-pip
pip install jmespath

wget -c https://download.virtualbox.org/virtualbox/5.2.38/virtualbox-5.2_5.2.38-136252~Ubuntu~bionic_amd64.deb
sudo apt install ./virtualbox-5.2_5.2.38-136252~Ubuntu~bionic_amd64.deb

wget -c https://releases.hashicorp.com/vagrant/2.0.3/vagrant_2.0.3_x86_64.deb
sudo apt install ./vagrant_2.0.3_x86_64.deb
vagrant plugin install vagrant-disksize

sudo add-apt-repository ppa:ansible/ansible-2.9
sudo apt-get update
sudo apt install ansible

git clone https://github.com/kochetov-dmitrij/IntegrationServer
cd IntegrationServer
vagrant up
```

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
