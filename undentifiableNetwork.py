import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("WHO Sri Lanka", "WHO_SEARO",weight=1)
goarn_network.add_edge("EPIET", "WHO Sri Lanka",weight=1)
goarn_network.add_edge("Health Protection Agency/London-KSS Deanery-UK", "WHO Sri Lanka",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "WHO Sri Lanka",weight=1)
goarn_network.add_edge("National University Hospital Singapore", "WHO Sri Lanka",weight=1)
goarn_network.add_edge("National University Singapore", "WHO Sri Lanka",weight=1)
goarn_network.add_edge("WHO Sri Lanka", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO Sri Lanka",weight=1)
goarn_network.add_edge("EPIET", "WHO_SEARO",weight=1)
goarn_network.add_edge("Health Protection Agency/London-KSS Deanery-UK", "WHO_SEARO",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "WHO_SEARO",weight=1)
goarn_network.add_edge("National University Hospital Singapore", "WHO_SEARO",weight=1)
goarn_network.add_edge("National University Singapore", "WHO_SEARO",weight=1)
goarn_network.add_edge("WHO_SEARO", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO_SEARO",weight=1)
goarn_network.add_edge("EPIET", "Health Protection Agency/London-KSS Deanery-UK",weight=1)
goarn_network.add_edge("EPIET", "Ministry of Health Thailand",weight=1)
goarn_network.add_edge("EPIET", "National University Hospital Singapore",weight=1)
goarn_network.add_edge("EPIET", "National University Singapore",weight=1)
goarn_network.add_edge("EPIET", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "EPIET",weight=1)
goarn_network.add_edge("Health Protection Agency/London-KSS Deanery-UK", "Ministry of Health Thailand",weight=1)
goarn_network.add_edge("Health Protection Agency/London-KSS Deanery-UK", "National University Hospital Singapore",weight=1)
goarn_network.add_edge("Health Protection Agency/London-KSS Deanery-UK", "National University Singapore",weight=1)
goarn_network.add_edge("Health Protection Agency/London-KSS Deanery-UK", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "Health Protection Agency/London-KSS Deanery-UK",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "National University Hospital Singapore",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "National University Singapore",weight=1)
goarn_network.add_edge("Ministry of Health Thailand", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "Ministry of Health Thailand",weight=1)
goarn_network.add_edge("National University Hospital Singapore", "National University Singapore",weight=1)
goarn_network.add_edge("National University Hospital Singapore", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "National University Hospital Singapore",weight=1)
goarn_network.add_edge("National University Singapore", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "National University Singapore",weight=1)
goarn_network.add_edge("CDC Atlanta", "the National Centre for Immunization Research and Surveillance of Vaccine Preventable Diseases-Australia",weight=1)



#
#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/unidentifiable.csv", 'wb') as csvfile:
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

H=nx.connected_component_subgraphs(goarn_network)[0]
print(nx.average_shortest_path_length(H))

nx.draw_spring(goarn_network)
plt.show()
print len(goarn_network.nodes())