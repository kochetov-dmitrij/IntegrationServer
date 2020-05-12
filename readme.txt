Asset: Integration server containing all the assets required for CI

Asset state specification:
 - Docker (last stable)
 - Ansible (last stable)
 - Python3 (last version)
 - OpenJDK8
 - Gitlab CE (last version, installed using official installation script)
 - Artifactory (docker container, last version from docker repo)
 - Jenkins (last version)
 - Gitlab, Jenkins and Artifactory have set up keys for API interaction between the tools.

Asset recreation:
Prerequisites. Other versions of packages most probably are not compatible with each other. Complete installation script for ubuntu is at the bottom of the doc.
 - 14GB RAM, 40GB hard drive. May work with less memory, try to change it in Vagrantfile.
 - python, 'jmespath' package
 - virtualbox 5.2
 - vagrant 2.0.3
 - ansible 2.9
Steps:
 - Inside this folder run `vagrant up`. It launches a VirtualBox VM using Vagrant and provisions it with Ansible playbook. ~10 min.
   <check> Vagrant and ansible did not report any error.
   <check> GitLab http://192.168.11.10/gitlab/devopser/DevopsCalculator can be opened and logged in as name/pass = devopser/f2qskL4Zd6
           The project must have 'master' and 'ready/init' branches.
   <check> Artifactory http://localhost:11003/ui/repos/tree/General/generic-local can be opened and logged in as name/pass = admin/sHMHY6iZjh
   <check> Jenkins http://localhost:11001/blue/organizations/jenkins/DevopsCalculator/activity/ (this is BlueOcean plugin for better UI) can be opened and logged in as name/pass = devopser/cLVc1VH73D
 - Inside Jenkins wait until the first build from 'ready/init' reaches 'Push to master' stage.
   <check> http://localhost:15001 (stage server) must display the app.
 - On the page with 'Push to master' stage press 'Proceed'.
   <check> A new commit will be pushed to 'master'. 'ready/init' branche will be deleted.
   <check> Artifactory obtains the first artifact ROOT.war v0.0.1
 - Inside Jenkins wait until the first pipeline from 'master' completes.
   <check> http://localhost:15900 (prod server) must display the app.




Notes:
!!! Don't run 'vagrant up' inside another VirtualBox VM, it doesn't support nested virtualization unlike VMWare

Screen recording of the installation and scenarios: https://drive.google.com/file/d/1NkCZWgm9BUHQJ16CRFxeBIlzzacXL9tW/view?usp=sharing
Presentation with described architecture: https://docs.google.com/presentation/d/1f1bVA0E8H4EucPLi2YwzHYYQz8FNb8cWthHxNXy0jE0/edit?usp=sharing

Installation of prerequisites for ubuntu. Highly recommended to use 18.04
Problems with repos and dependencies may occur on 19.04 and 19.10
Execute line by line because some commands need confirmation.
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
```
