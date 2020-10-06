FROM ubuntu:18.04

# utils
RUN apt --yes update \
 && apt --yes upgrade \
 && apt install --yes wget systemd python3.8 python3-pip \
# Grafana
 && apt install --yes adduser libfontconfig1 \
 && cd /tmp \
 && wget https://dl.grafana.com/oss/release/grafana_7.2.0_amd64.deb \
 && dpkg -i grafana_7.2.0_amd64.deb \
# Elastic Search
 && apt install --yes gnupg2 \
 && wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
 && apt install --yes apt-transport-https \
 && echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-7.x.list \
 && apt --yes update && apt install --yes elasticsearch \
 && rm -rf /var/lib/apt/lists/* \
# Plotly
 && grafana-cli plugins install natel-plotly-panel \

ENTRYPOINT ["tail", "-f", "/dev/null"]