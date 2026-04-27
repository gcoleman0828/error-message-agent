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

---

---

## Docker Permission Error

### Match Signals

- permission denied while trying to connect to the Docker daemon socket
- /var/run/docker.sock
- docker.sock
- connect: permission denied
- Got permission denied while trying to connect to the Docker daemon socket

### Likely Cause

The current Ubuntu user does not have permission to use Docker without `sudo`. This usually means the user is not in the `docker` group, or the user was recently added to the group but has not started a new login session yet.

### First Check

```bash
groups
```

### Expected Result

The output should include `docker`.

Example:

```text
gcoleman adm cdrom sudo dip plugdev docker
```

### Next Action

If `docker` is missing from the group list, add the current user to the Docker group:

```bash
sudo usermod -aG docker $USER
```

Then apply the new group membership by logging out and logging back in.

For a faster test in the current terminal session, you can also run:

```bash
newgrp docker
```

After that, test Docker again:

```bash
docker ps
```
---

---

## Python Dependency Error

### Match Signals

- ModuleNotFoundError
- No module named
- ImportError
- package not found

### Likely Cause

A required Python package is not installed in the active Python environment. This can happen when the package was never installed, or when the user is running Python outside the correct virtual environment.

### First Check

```bash
python -m pip list
```

### Expected Result

The installed Python packages should be listed.

If the missing package is not listed, then it is probably not installed in the active Python environment.

### Next Action

If the missing package is not listed, install it in the correct Python environment.

Example:

```bash
python -m pip install package-name
```

For this project, make sure the virtual environment is active before installing packages:

```bash
source .venv/bin/activate
```
---

## Unknown Error

### Match Signals

### Likely Cause

### First Check

### Expected Result

### Next Action