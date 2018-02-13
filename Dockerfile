FROM python
COPY ./app /home
EXPOSE 8888
RUN pip3 install tornado
CMD ["python","/home/app.py"]

