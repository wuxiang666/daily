#! /usr/bin/env python
# -*- coding:utf8 -*-

import sys,os
import ConfigParser
import json

def write_config(config_file_path, field, key, value):  
    cf = ConfigParser.ConfigParser()  
    try:  
        cf.read(config_file_path)  
        cf.set(field, key, value)  
        cf.write(open(config_file_path,'w'))  
    except:
        print u"替换%s的值为%s时发生异常。请检查" % (key,value)
        sys.exit(1)  
    return True  

def parse_json(json_str):
    json_obj = json.loads(json_str)
    return zip(json_obj.keys(),json_obj.values())



if __name__ == "__main__":  
    if len(sys.argv) < 4:
        print u"参数个数不符合要求，请检查"
        sys.exit(1) 
        
    field = sys.argv[1]
    config_file_path = sys.argv[2]
    k_values = sys.argv[3]
    print field,config_file_path,k_values
    for key_value in parse_json(k_values):
        key = key_value[0]
        value = key_value[1].encode("utf8")
        print key,value
        write_config(config_file_path, field, key, value)  
