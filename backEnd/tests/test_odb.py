import odb

connection = obd.OBD() 
cmd = obd.commends.RPM

response = connection.query(cmd)

print(response.value)
