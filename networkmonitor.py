import pyspeedtest

st = pyspeedtest.SpeedTest()
converted = st.download()/1024/1024
print(converted)
