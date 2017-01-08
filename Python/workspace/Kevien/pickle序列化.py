# -*- coding: utf-8 -*-
 
import cPickle as pickle
import random
import os
import json
 
import time
 
LENGTH = 1024 * 10240
 
def main():
    d = {}
    a = []
    for i in range(LENGTH):
        a.append(random.randint(0, 255))
 
    d["a"] = a
 
    print "dumping...pickle---------------"
 
    t1 = time.time()
    pickle.dump(d, open("pickle1.dat", "wb"), True)
    print "dump1: %.3fs" % (time.time() - t1)
 
    t1 = time.time()
    pickle.dump(d, open("pickle2.dat", "w"))
    print "dump2: %.3fs" % (time.time() - t1)
 
    s1 = os.stat("pickle1.dat").st_size
    s2 = os.stat("pickle2.dat").st_size
 
    print "%d, %d, %.2f%%" % (s1, s2, 100.0 * s1 / s2)
 
 
    print "dumping...json-----------------"
 
    t1 = time.time()
    json.dump(d, open("json1.dat", "wb"), True)
    print "dump1: %.3fs" % (time.time() - t1)
 
    t1 = time.time()
    json.dump(d, open("json2.dat", "w"))
    print "dump2: %.3fs" % (time.time() - t1)
 
    s1 = os.stat("json1.dat").st_size
    s2 = os.stat("json2.dat").st_size
 
    print "%d, %d, %.2f%%" % (s1, s2, 100.0 * s1 / s2)
 
 
 
 
 
    print "loading...pickle------------"
 
    t1 = time.time()
    obj1 = pickle.load(open("pickle1.dat", "rb"))
    print "load1: %.3fs" % (time.time() - t1)
 
    t1 = time.time()
    obj2 = pickle.load(open("pickle2.dat", "r"))
    print "load2: %.3fs" % (time.time() - t1)
 
    t1 = time.time()
    obj3 = json.load(open("json1.dat", "r"))
    print "load3: %.3fs" % (time.time() - t1)
 
 
if __name__ == "__main__":
    main()
