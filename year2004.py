import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("Global Influenza Surveillance Network", "Hong Kong National Influenza Center",weight=2)
goarn_network.add_edge("Hong Kong National Influenza Center", "Japan National Institute for Infectious Diseases",weight=1)
goarn_network.add_edge("Global Influenza Surveillance Network", "Japan National Institute for Infectious Diseases",weight=2)
goarn_network.add_edge("Global Influenza Surveillance Network", "Global Influenza Surveillance Network",weight=1)
goarn_network.add_edge("OIE", "WHO HQ",weight=1)
goarn_network.add_edge("FAO", "WHO HQ",weight=1)
goarn_network.add_edge("WHO HQ", "WHO Thailand",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "WHO HQ",weight=1)
goarn_network.add_edge("FAO", "OIE",weight=2)
goarn_network.add_edge("OIE", "WHO Thailand",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "OIE",weight=1)
goarn_network.add_edge("FAO", "WHO Thailand",weight=1)
goarn_network.add_edge("FAO", "Ministry of Health Thailand",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "WHO Thailand",weight=1)
goarn_network.add_edge("OIE", "WHO",weight=1)
goarn_network.add_edge("FAO", "WHO",weight=2)
goarn_network.add_edge("Ministray of Health Bangladesh", "WHO",weight=1)
goarn_network.add_edge("FAO", "Ministry of Health Indonesia",weight=1)
goarn_network.add_edge("FAO", "WHO Jakarta",weight=1)
goarn_network.add_edge("CDC Atlanta", "FAO",weight=1)
goarn_network.add_edge("FAO", "WHO reference laboratories Hong Kong",weight=1)
goarn_network.add_edge("FAO", "WHO reference laboratories USA",weight=1)
goarn_network.add_edge("Ministry of Health Indonesia", "WHO",weight=1)
goarn_network.add_edge("WHO", "WHO Jakarta",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO",weight=1)
goarn_network.add_edge("WHO", "WHO reference laboratories Hong Kong",weight=1)
goarn_network.add_edge("WHO", "WHO reference laboratories USA",weight=1)
goarn_network.add_edge("Ministry of Health Indonesia", "WHO Jakarta",weight=1)
goarn_network.add_edge("CDC Atlanta", "Ministry of Health Indonesia",weight=1)
goarn_network.add_edge("Ministry of Health Indonesia", "WHO reference laboratories Hong Kong",weight=1)
goarn_network.add_edge("Ministry of Health Indonesia", "WHO reference laboratories USA",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO Jakarta",weight=1)
goarn_network.add_edge("WHO Jakarta", "WHO reference laboratories Hong Kong",weight=1)
goarn_network.add_edge("WHO Jakarta", "WHO reference laboratories USA",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO reference laboratories Hong Kong",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO reference laboratories USA",weight=1)
goarn_network.add_edge("WHO reference laboratories Hong Kong", "WHO reference laboratories USA",weight=1)
goarn_network.add_edge("WHO", "WHO HQ",weight=1)
goarn_network.add_edge("NATIONAL HEALTH LABORATORY SERVICE (NHLS)", "WHO HQ",weight=1)
goarn_network.add_edge("NATIONAL HEALTH LABORATORY SERVICE (NHLS)", "WHO",weight=1)
goarn_network.add_edge("CDC Atlanta", "EPIET",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("EPIET", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("CDC Atlanta", "Kenya Medical Research Institute (KEMRI)",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "WHO South Sudan Early Warning and Response Network (EWARN)",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "WHO HQ",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "UNICEF",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "MSF France",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "WHO DRC",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO South Sudan Early Warning and Response Network (EWARN)",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO HQ",weight=1)
goarn_network.add_edge("CDC Atlanta", "UNICEF",weight=1)
goarn_network.add_edge("CDC Atlanta", "MSF France",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO DRC",weight=1)
goarn_network.add_edge("WHO HQ", "WHO South Sudan Early Warning and Response Network (EWARN)",weight=1)
goarn_network.add_edge("UNICEF", "WHO South Sudan Early Warning and Response Network (EWARN)",weight=1)
goarn_network.add_edge("MSF France", "WHO South Sudan Early Warning and Response Network (EWARN)",weight=1)
goarn_network.add_edge("WHO DRC", "WHO South Sudan Early Warning and Response Network (EWARN)",weight=1)
goarn_network.add_edge("UNICEF", "WHO HQ",weight=1)
goarn_network.add_edge("MSF France", "WHO HQ",weight=1)
goarn_network.add_edge("WHO DRC", "WHO HQ",weight=1)
goarn_network.add_edge("MSF France", "UNICEF",weight=1)
goarn_network.add_edge("UNICEF", "WHO DRC",weight=1)
goarn_network.add_edge("MSF France", "WHO DRC",weight=1)
goarn_network.add_edge("WHO", "WHO Thailand",weight=1)
goarn_network.add_edge("Queen Sirikit National Institute of Child Health-Bangkok", "WHO",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO",weight=1)
goarn_network.add_edge("Queen Sirikit National Institute of Child Health-Bangkok", "WHO Thailand",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO Thailand",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "Queen Sirikit National Institute of Child Health-Bangkok",weight=1)



#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/2004.csv", 'wb') as csvfile:
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