# Routing Rules
This file provides routing to handle the context and routing a users error message the input to the right signal

## Git / SSH Authentication
Github is a web based repository solution that allows someone using the 'git' command securly using SSH protocol to upload (check in) their code

### Match Signals
- Permission denied (publickey)
- Could not read from remote repository
- Please make sure you have the correct access rights
- git@github.com
- Host key verification failed

### Likely Cause
SSH key not is loaded into git hub for this host

### First Check
Run the following command to test whether this VM can authenticate to GitHub over SSH:

```bash
ssh -T git@github.com
```

### Expected Result
If SSH is configured correctly, GitHub should return a message that it was successful, but Github does not provide shell access 

### Next Action
If the SSH test fails, check whether this VM already has SSH keys:
```bash 
ls -la ~/.ssh
```
If no SSH key exists, create one with:

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Then add the public key to GitHub

---

### Docker Permission Error

### Match Signals
```text
- permission denied while trying to connect to the Docker daemon socket
- /var/run/docker.sock
- Got permission denied
- docker ps
```
### Likely Cause

The current Ubuntu user may not be in the `docker` group, or the user was added to the group but has not logged out and back in yet.

### First Check


### Match Signals

### Likely Cause

### First Check

```bash

groups
```

### Expected Result
If docker is missing from the group list, add the current user to the Docker group:

```bash
sudo usermod -aG docker $USER
```

### Next Action
If docker is missing from the group list, add the current user to the Docker group:

```bash
sudo usermod -aG docker $USER
```
---

## Python Dependency Error

### Match Signals

### Likely Cause

### First Check

### Expected Result

### Next Action

---

## Network / Port Conflict

### Match Signals

### Likely Cause

### First Check

### Expected Result

### Next Action

---

## Unknown Error

### Match Signals

### Likely Cause

### First Check

### Expected Result

### Next Action