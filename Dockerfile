FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install requests
RUN pip install beautifulsoup4

WORKDIR /repo
COPY . /repo
