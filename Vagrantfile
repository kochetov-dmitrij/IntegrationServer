# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"
  config.vm.hostname = "integration-server"

  config.vm.network "private_network", ip: "192.168.11.10"
  config.vm.network "forwarded_port", guest: 8080, host: 11000
  config.vm.network "forwarded_port", guest: 8081, host: 11001
  config.vm.network "forwarded_port", guest: 8021, host: 11002
  config.vm.network "forwarded_port", guest: 8022, host: 11003

  for i in 15000..15999
    config.vm.network :forwarded_port, guest: i, host: i
  end

  config.vm.synced_folder "./data", "/vagrant_data", create: true

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "14000"
    config.disksize.size = '40GB'
    vb.cpus = 6
  end

  config.vm.provision "ansible" do |ansible|
     ansible.compatibility_mode = "2.0"
     ansible.playbook = "playbook.yml"
     # ansible.verbose = "vvvv"
  end

end
