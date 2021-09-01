# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Lah U cp Atur atur
# Owl-Userbot
#
RUN git clone -b Owl-Userbot https://github.com/maspion27/Owl-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/maspion27/Owl-Userbot/Owl-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
