FROM python3
RUN git clone https://github.com/um-computacion-tm/parcial-2021-11-03-Frames2424.git
WORKDIR /home/franco24/parcial-2021-11-03-Frames2424
CMD ["python", "./test_buscaminas.py"]
