FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN echo \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free\
    > /etc/apt/sources.list
RUN apt-get update \
  && apt-get install gcc make -y
WORKDIR /app
COPY pi-dal.txt /app/pi-dal.txt
RUN pip install -r pi-dal.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install uvicorn -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python manage.py colletstatic
COPY . /app
COPY ./compose/production/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
