import sys, json, subprocess, base64
#print(sys.argv)
filename = sys.argv[1]
cmd = base64.b64decode(sys.argv[2])
filePath = "./public/temphtml/" + filename + ".jsonp"
s = { "status": False, "message": "Creating", "filename": filename }
f = open(filePath, "w")
#os.chmod(filePath, 0o777)
f.write("processJSONPResponse(" + json.dumps(s) + ")")
f.close()
#run
#print(cmd)
arg = cmd.split()
process = subprocess.Popen(arg)
process.wait()
print(process.stdout)
#read
o = open(filePath, "r")
d = o.read()
d = d.replace("processJSONPResponse(","").replace(")","")
j = json.loads(d)
j['status'] = True
j['message'] = "Competed"
#update
f = open(filePath, "w")
f.write("processJSONPResponse(" + json.dumps(j) + ")")
#os.chmod(filePath, 0o777)
f.close()
print("competed")
