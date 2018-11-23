#!/usr/bin/python

import dns.resolver
import socket


myResolver = dns.resolver.Resolver()



f = open("properties.txt")
num_line = sum(1 for line in f)
f.close()

with open("properties.txt", "r") as ins:
        array = []
        for current_host in ins:

                if current_host[0] != "#": #ignore if hostname is hashed out

                    current_host = current_host.strip()

                    try:
                        myAnswers = myResolver.query(current_host, "CNAME")
                        for rdata in myAnswers: #for each response
                            current_edge_host = str(rdata)
                            if current_edge_host.endswith('edgekey.net.'):
                                    staging_edge_host = current_edge_host.replace("edgekey.net.","edgekey-staging.net")

                                    StageAnswers = myResolver.query(staging_edge_host)
                                    for sdata in StageAnswers: #for each response
                                        staging_ip = str(sdata)
                                        #print staging_ip + "      " + current_host  #print the data
                                        print("%s\t\t%s" % (staging_ip, current_host))
                    except:
                        staging_edge_host = current_host + ".edgekey-staging.net"
                        StageAnswers = myResolver.query(staging_edge_host)
                        for sdata in StageAnswers: #for each response
                            staging_ip = str(sdata)
                            #print staging_ip + "      " + current_host  #print the data
                            print("%s\t\t%s #Public hostname not resolvable - created by appending .edgekey-staging.net to public hostname" % (staging_ip, current_host))
