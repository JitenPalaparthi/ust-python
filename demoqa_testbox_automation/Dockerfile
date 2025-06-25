# Dockerfile
FROM jenkins/jenkins:lts

USER root

# Install Python and Chrome dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget unzip curl gnupg2 && \
    pip3 install selenium pytest

# Install Chrome (ARM-compatible version)
RUN curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb || true

# Fix Chrome install for headless
RUN apt --fix-broken install -y

# Install ChromeDriver matching Chrome version
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') && \
    wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$CHROME_VERSION/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver

USER jenkins