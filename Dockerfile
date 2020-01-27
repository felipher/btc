FROM python:3
RUN pip install pystrich
CMD [ "python", "./load/load_price.py" ]