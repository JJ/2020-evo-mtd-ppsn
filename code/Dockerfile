FROM alpine:3.11 as tester

WORKDIR /tester

LABEL maintainer "info@ernesto.es"
LABEL vendor="ugr"

# Adding just requirements.txt to  optimize docker layer cache build
COPY requirements.txt .

# Installing alpine base packages
RUN apk add --no-cache \
    python3

# Installing python requirements
RUN pip3 install -r requirements.txt

# Show package versions
RUN pip3 freeze

# Copying rest of files
COPY evomtd/ /tester/evomtd/

CMD /evomtd/scripts/run.sh
