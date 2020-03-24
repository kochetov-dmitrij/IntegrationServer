# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "integration-server"

  config.vm.network "private_network", ip: "192.168.11.10"
  config.vm.network "forwarded_port", guest: 8080, host: 11000
  config.vm.network "forwarded_port", guest: 8081, host: 11001

  config.vm.synced_folder "./data", "/vagrant_data", create: true

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "10240"
    vb.cpus = 6
  end

  # ENV['LC_ALL']="en_US.UTF-8"

  config.vm.provision "ansible" do |ansible|
     ansible.compatibility_mode = "2.0"
     ansible.playbook = "playbook.yml"
  end


  # config.vm.provision "shell", inline: <<-SHELL
  #    	sudo apt-get update
  #    	sudo apt-get install --yes python
  #    	# apt-get install -y default-jre
  # 	  # apt-get install -y apache2
  #  	SHELL

end
