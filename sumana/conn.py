import ibm_db
from flask import *

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hkv41604;PWD=3wqNxanB3Yd1Tzlr",'','')
print(conn)

app=Flask(__name__)
