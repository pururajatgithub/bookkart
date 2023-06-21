FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1



WORKDIR /bookkart/


# creating virtual evironment
RUN pip install virtualenv
RUN virtualenv bookkart
ENV PATH /bookkart/bin:$PATH


#Installing Dependencies
COPY requirements.txt /bookkart/
RUN pip install -r /bookkart/requirements.txt

# ENV PATH /dicomrouter/bin:$PATH

# Change default environment - also auto activates env when execed
# RUN sed -i 's/conda activate base/conda activate dcmio/g' /root/.bashrc

# Copying the backend
COPY . .

# copy scripts
# ENV PATH /scripts:$PATH
