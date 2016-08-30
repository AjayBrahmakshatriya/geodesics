#!/usr/bin/python
import sys
import genalpha
import re
if len(sys.argv)<2:
        print "Enter dom file"
        exit(-1)

print "Parsing dom file :", sys.argv[1]

f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

#parsing domain_parameters
def extract_params(param):
        param_lines = []
        param_flag = 0
        for i in lines:
                if param_flag == 0 and i.strip() == "%"+param:
                        param_flag = 1
                        continue
                if param_flag == 1 and i.strip() == "%":
                        break
                if param_flag == 1:
                        param_lines = param_lines+[i.strip()]
	params={}
	for i in param_lines:
		if i=="":
			continue
        	key = i.split(":")[0].strip()
	        value = i.split(":")[1].strip()
        	params[key]=value
        return params
config = extract_params("config")

if "domain" not in config or config["domain"]!="sphere":
        print "Invalid parameter for domain, please check the dom file"
        exit(-1)
if "model" not in config or config["model"]!="geodesics":
        print "Invalid parameter for model. Presently only geodesics supported"
	exit(-1)

channel_count = int(config["channel-count"])
channels = []
channels_list = config["channels"].split(",")
for i in channels_list:
        i = i.strip()
        var_name = i.split("(")[0]
        var_type = i.split("(")[1].split(")")[0]
        channels += [{"name":var_name, "type":var_type}]
print channels
system = config["system"]
f = open(sys.argv[1]+".ab","w")


f.write("affine "+system+" {N,T | (N,T)>0}\n")
f.write("input\n")
f.write("output\n")
for i in channels:
	f.write("\t"+i["type"]+" ")
	f.write(i["name"]+"_FINAL {i,j,k | 0<=i<N && 0<=j<N && 0<=k<12};\n")
f.write("local\n")
segments="ABCDEFGHIJKL"
for i in channels:
	for j in segments:
		f.write("\t"+i["type"]+" ")
		f.write(i["name"]+"_"+j+" {i,j,t | 0<=i<N && 0<=j<N && 0<=t<=T};\n")
f.write("let\n")
for i in channels:
	f.write("\t"+i["name"]+"_FINAL[i,j,k] = \n")
	f.write("\tcase\n")
	for j in range(0,12):
		f.write("\t\t{|k=="+str(j)+"} : "+segments[j]+"[i,j,T];\n")
	f.write("\tesac;\n")

stencil6=extract_params("stencil6")
stencil5=extract_params("stencil5")

def replace_vars(i,j,N,expr,channels,n_count=6):
	for d in channels:
		expr = re.sub(r'\b%s_0\b'% d["name"], genalpha.getL(("i,j",k), d["name"]), expr)
		for x in range(0,n_count):
			expr = re.sub(r'\b%s_%d\b' % (d["name"], x+1), genalpha.getL(genalpha.getAx(i,j,k,N,x),d["name"]),expr)	
	return expr	

for c in channels:
	expr6 = stencil6[c["name"]]
	expr5 = stencil5[c["name"]]
	for k in range(0,12):
		f.write("\t"+c["name"]+"_"+segments[k]+"[i,j,t]=\n")
		f.write("\tcase\n")
		f.write("\t\t{|t==0} : 0;\n")
		f.write("\t\t{|i==0 && j==0} : "+replace_vars(0,0,8,expr5,channels,5)+";\n")
		if k!=10 and k!=11:
			f.write("\t\t{|i==N-1 && j==N-1} : "+replace_vars(7,7,8,expr6,channels)+";\n")
			f.write("\t\t{|i==0 && j==N-1} : "+replace_vars(0,7,8,expr6,channels)+";\n")
			f.write("\t\t{|i==N-1 && j==0} : "+replace_vars(7,0,8,expr6,channels)+";\n")
			f.write("\t\t{|i==0} : "+replace_vars(0,1,8,expr6,channels)+";\n")
			f.write("\t\t{|i==N-1} : "+replace_vars(7,1,8,expr6,channels)+";\n")
			f.write("\t\t{|j==0} : "+replace_vars(1,0,8,expr6,channels)+";\n")
			f.write("\t\t{|j==N-1} : "+replace_vars(1,7,8,expr6,channels)+";\n")
			f.write("\t\t{|} : "+replace_vars(1,1,8,expr6,channels)+";\n")
		else:
			f.write("\t\t{|} : 0;\n");
		f.write("\tesac;\n")

f.write(".\n")
f.close()
f = open(sys.argv[1]+".cs","w")
filename=sys.argv[1]+".ab"
filename=filename.split("/")
filename=filename[len(filename)-1]

f.write("prog=ReadAlphabets(\""+filename+"\");\n")
f.write("system=\""+config["system"]+"\";\n")
f.write("outDir=\"output/\"+system;\n")

f.write("generateWriteC(prog, system, outDir);\n")
f.write("generateWrapper(prog, system, outDir);\n")
f.write("generateMakefile(prog, system, outDir);\n")
f.close()
