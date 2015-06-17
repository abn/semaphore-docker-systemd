# Containerized Semaphore systemd Wrapper

Provides service files for use with systemd enabled distributions for conveniently using [Semaphore](https://github.com/ansible-semaphore/semaphore) - An Open Source Alternative to Ansible Tower.

## Quick Start

### Installation
```sh
git clone https://github.com/abn/semaphore-docker-systemd.git
cd semaphore-docker-systemd
sudo make install
```

### Usage
```
# This is as simple as
systemctl start semaphore

# If you want semaphore to start on systemboot
systemctl enable semaphore
```
