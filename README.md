# AnsibleLearningLab
Ansible Playbooks for testing/learning
This repo will change a lot as it's used to try and optimise ansible configurations as much as possible while using the cisco.ios collection where applicable


# Dependencies:
Some of the playbooks use cisco.ios collection, use the following command to install
```
ansible-galaxy collection install cisco.ios
```

ntpconfig.yaml is currently using ios_ntp under the local ./modules/\
Pending [PR#307](https://github.com/ansible-collections/cisco.ios/pull/307) in cisco.ios

