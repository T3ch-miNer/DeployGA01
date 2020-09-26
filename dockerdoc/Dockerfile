FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get install -y git
RUN apt-get -y install python3-pip
RUN mkdir gadeploy
RUN git clone https://github.com/T3ch-miNer/DeployGA01.git
WORKDIR DeployGA01
RUN pip3 install -r requirements.txt
ENV JAVA_HOME /usr/local
COPY dummy.txt DeployGA01/dummy.txt
WORKDIR bin
CMD ["python3","summaryservice.py"]