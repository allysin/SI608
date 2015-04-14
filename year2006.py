import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("FAO", "WHO",weight=2)
goarn_network.add_edge("Minister of Health Turkey", "WHO collaborating laboratory UK",weight=1)
goarn_network.add_edge("WHO collaborating laboratory UK", "WHO_Euro",weight=1)
goarn_network.add_edge("MRC National Institute for Medical Research in Mill Hill London", "WHO collaborating laboratory UK",weight=1)
goarn_network.add_edge("Minister of Health Turkey", "WHO_Euro",weight=1)
goarn_network.add_edge("MRC National Institute for Medical Research in Mill Hill London", "Minister of Health Turkey",weight=1)
goarn_network.add_edge("MRC National Institute for Medical Research in Mill Hill London", "WHO_Euro",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "WHO",weight=4)
goarn_network.add_edge("NAMRU-3 Egypt", "UNICEF",weight=1)
goarn_network.add_edge("UNICEF", "WHO",weight=1)
goarn_network.add_edge("FAO", "UNICEF",weight=1)
goarn_network.add_edge("OIE", "UNICEF",weight=1)
goarn_network.add_edge("CDC Iraq", "UNICEF",weight=1)
goarn_network.add_edge("UNICEF", "WHO United Kingdom",weight=1)
goarn_network.add_edge("FAO", "NAMRU-3 Egypt",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "OIE",weight=1)
goarn_network.add_edge("CDC Iraq", "NAMRU-3 Egypt",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "WHO United Kingdom",weight=1)
goarn_network.add_edge("OIE", "WHO",weight=1)
goarn_network.add_edge("CDC Iraq", "WHO",weight=1)
goarn_network.add_edge("WHO", "WHO United Kingdom",weight=1)
goarn_network.add_edge("FAO", "OIE",weight=1)
goarn_network.add_edge("CDC Iraq", "FAO",weight=1)
goarn_network.add_edge("FAO", "WHO United Kingdom",weight=1)
goarn_network.add_edge("CDC Iraq", "OIE",weight=1)
goarn_network.add_edge("OIE", "WHO United Kingdom",weight=1)
goarn_network.add_edge("CDC Iraq", "WHO United Kingdom",weight=1)



#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/2006.csv", 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile)
#    spamwriter.writerow('D')
#    centrality=  nx.degree_centrality(goarn_network)
#    for each in centrality.items():
#        print 'Degree Centrality: ', each[0], each[1]
#        print each
#        spamwriter.writerow([each[0], each[1]])
#    
#    spamwriter.writerow('C')
#    close=nx.closeness_centrality(goarn_network)    
#    for each in close.items():
#        print 'Closeness Centrality: ', each[0], '\t', each[1]
#        spamwriter.writerow([each[0], each[1]])
#
#    spamwriter.writerow('B')
#    btwn=nx.betweenness_centrality(goarn_network, weight='weight')
#    for each in btwn.items():
#        print 'Betweeness Centrality: ', each[0], each[1]
#        spamwriter.writerow([each[0], each[1]])
#
#    avg_clust= nx.average_clustering(goarn_network)
#    print 'Average Clustering: ', avg_clust
#    
#
#
#
#    clustering = nx.clustering(goarn_network)
#
#    spamwriter.writerow('L')
#    for each in clustering.items():
#        print 'Clustering Coefficient per Node: ', each[0], each[1]
#        spamwriter.writerow([each[0], each[1]])
#    csvfile.close()

nx.draw(goarn_network)
plt.show()

H=nx.connected_component_subgraphs(goarn_network)[0]
print(nx.average_shortest_path_length(H))
print len(goarn_network.nodes())