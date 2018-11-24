#!/usr/bin/python
#Cycle through list of properties to determine whether site routes through Global KSD map or European E3 Map


import dns.resolver
import socket


myResolver = dns.resolver.Resolver()



f = open("properties.txt")
num_line = sum(1 for line in f)
f.close()

with open("properties.txt", "r") as ins:
        array = []
        for current_host in ins:#for each public hostname

            if current_host[0] != "#": #ignore if hostname is hashed out
                current_host = current_host.strip()

                #lookup ALL CNAME records and add to myAnswers
                try:
                    myAnswers = myResolver.query(current_host, "CNAME")
                except:
                    print "Error resolving " + current_host

                #loop through myAnswers to get edge hostname (should only be one edge hostname returned)
                for rdata in myAnswers: #for each response
                    current_edge_host = str(rdata).strip()

                    try:
                        EdgeAnswers = myResolver.query(current_edge_host, "CNAME")
                    except:
                        print "Error resolving " + current_edge_host

                    for edata in EdgeAnswers: #for each response
                        edge_node_name = str(edata).strip()


                    #print edge_node_name
                    if edge_node_name.find(".e3.") != -1:
                        print "E3:  " + current_host
                    else:
                        print "KSD: " + current_host
