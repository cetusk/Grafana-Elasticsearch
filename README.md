# 1
Install Elasticsearch Python module and start daemons.
```
python3 -m pip install elasticsearch
service grafana-server start
service elasticsearch start
systemctl enable grafana-server
systemctl enable elasticsearch
```

# 2
Check data registration.
```
python3 sample.py
```