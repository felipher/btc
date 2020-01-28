FROM python:3

ADD load_price.py /

RUN pip install pystrich

CMD [ "python", "./load_price.py" ]
