# -*- coding: utf-8 -*-
#pymd5cracker.py
import hashlib, sys
from time import time

# Change to commandline swtiches when you have the time!
hash = ""
hash_file = "hash2.csv"
wordlist = "mass_rules.txt"; 


# Read the hash file entered
try:
        hashdocument = open(hash_file,"r")
except IOError:
        print "Invalid file."
            raw_input()
                sys.exit()
            else:
                    # Read the csv values seperated by colons into an array
                        hashes=[]
                            for line in hashdocument:
                                        line=line.replace("\n","")
                                                inp = line.split(":")
                                                        if (line.count(":")<2):
                                                                        inp.append("")
                                                                                hashes.append(inp)
                                                                                    hashdocument.close();


                                                                                    # Read wordlist in
                                                                                    try:
                                                                                            wordlistfile = open(wordlist,"r")
                                                                                    except IOError:
                                                                                            print "Invalid file."
                                                                                                raw_input()
                                                                                                    sys.exit()
                                                                                                else:
                                                                                                        pass

                                                                                                    tested=0
                                                                                                    cracked=0
                                                                                                    tic = time()
                                                                                                    for line in wordlistfile:
                                                                                                            
                                                                                                            line = line.replace("\n","")
                                                                                                                tested+=1
                                                                                                                    for i in range(0,len(hashes)):
                                                                                                                            
                                                                                                                                m = hashlib.md5()
                                                                                                                                        m.update(hashes[i][2]+line)
                                                                                                                                                word_hash = m.hexdigest()
                                                                                                                                                        if word_hash==hashes[i][1]:
                                                                                                                                                                        toc = time()
                                                                                                                                                                                    cracked+=1
                                                                                                                                                                                                hashes[i].append(line)
                                                                                                                                                                                                            print hashes[i][0]," : ", line, "\t(",time()-tic,"s)"

                                                                                                                                                                                                                # Show progress evey 1000 passwords tested
                                                                                                                                                                                                                    if tested%1000==0:
                                                                                                                                                                                                                                print "Cracked: ",cracked," (",tested,") ", line


                                                                                                                                                                                                                                # Save the output of this program so we can use again 
                                                                                                                                                                                                                                # with another program/dictionary adding the password 
                                                                                                                                                                                                                                # to each line we have solved.
                                                                                                                                                                                                                                crackout = open("pycrackout.txt","w")
                                                                                                                                                                                                                                for i in hashes:
                                                                                                                                                                                                                                        s=""
                                                                                                                                                                                                                                            for j in i:
                                                                                                                                                                                                                                                        if s!="":
                                                                                                                                                                                                                                                                        s+=":"
                                                                                                                                                                                                                                                                                s+=j
                                                                                                                                                                                                                                                                                    s+="\n"
                                                                                                                                                                                                                                                                                        crackout.write(s)
                                                                                                                                                                                                                                                                                        crackout.close()

                                                                                                                                                                                                                                                                                        print "Passwords found: ",cracked,"/",len(hashes)
                                                                                                                                                                                                                                                                                        print "Wordlist Words :", test
                                                                                                                                                                                                                                                                                        print "Hashes computed: ",len(hashes)*tested
                                                                                                                                                                                                                                                                                        print "Total time taken: ",time
