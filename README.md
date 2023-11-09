# SSTI-CTF (Hacksoc CTF Week 7)

## Setup

1. Install python dependencies
```bash
pip install -r requirements.txt
```

2. Modify WorkingDirectory & User parameters of SSTI-CTF.service before installing
&nbsp;
3. Install the service

```bash
cp SSTI-CTF.service /etc/systemd/system/SSTI-CTF.service \
sudo systemctl daemon-reload
sudo systemctl enable SSTI-CTF
sudo systemctl start SSTI-CTF
```

4. Check the status of the service

```bash
sudo systemctl status SSTI-CTF
```

## Accessing the service

The service can be accessed in the browser at the ip of any interface on your machine
