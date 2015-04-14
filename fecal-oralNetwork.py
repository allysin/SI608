import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("Ministry of Health", "WHO",weight=1)
goarn_network.add_edge("MSF Belgium", "Ministry of Health",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO",weight=1)
goarn_network.add_edge("MSF Luxembourg", "Ministry of Health Mali",weight=1)
goarn_network.add_edge("WHO", "WHO Thailand",weight=1)
goarn_network.add_edge("Queen Sirikit National Institute of Child Health-Bangkok", "WHO",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO",weight=1)
goarn_network.add_edge("Queen Sirikit National Institute of Child Health-Bangkok", "WHO Thailand",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "WHO Thailand",weight=1)
goarn_network.add_edge("National Institute for Infectious Diseases Japan", "Queen Sirikit National Institute of Child Health-Bangkok",weight=1)
goarn_network.add_edge("UNICEF", "WHO",weight=1)
goarn_network.add_edge("IOM", "WHO",weight=1)
goarn_network.add_edge("OXFAM-GB", "WHO",weight=1)
goarn_network.add_edge("Medecins du Monde", "WHO",weight=1)
goarn_network.add_edge("ICRC", "WHO",weight=1)
goarn_network.add_edge("ACF", "WHO",weight=1)
goarn_network.add_edge("MSF Spain", "WHO",weight=1)
goarn_network.add_edge("MSF Holland", "WHO",weight=1)
goarn_network.add_edge("MSF Luxemburg", "WHO",weight=1)
goarn_network.add_edge("Plan International", "WHO",weight=1)
goarn_network.add_edge("GOAL", "WHO",weight=1)
goarn_network.add_edge("Save the Children-UK", "WHO",weight=1)
goarn_network.add_edge("IOM", "UNICEF",weight=1)
goarn_network.add_edge("OXFAM-GB", "UNICEF",weight=1)
goarn_network.add_edge("Medecins du Monde", "UNICEF",weight=1)
goarn_network.add_edge("ICRC", "UNICEF",weight=1)
goarn_network.add_edge("ACF", "UNICEF",weight=1)
goarn_network.add_edge("MSF Spain", "UNICEF",weight=1)
goarn_network.add_edge("MSF Holland", "UNICEF",weight=1)
goarn_network.add_edge("MSF Luxemburg", "UNICEF",weight=1)
goarn_network.add_edge("Plan International", "UNICEF",weight=1)
goarn_network.add_edge("GOAL", "UNICEF",weight=1)
goarn_network.add_edge("Save the Children-UK", "UNICEF",weight=1)
goarn_network.add_edge("IOM", "OXFAM-GB",weight=1)
goarn_network.add_edge("IOM", "Medecins du Monde",weight=1)
goarn_network.add_edge("ICRC", "IOM",weight=1)
goarn_network.add_edge("ACF", "IOM",weight=1)
goarn_network.add_edge("IOM", "MSF Spain",weight=1)
goarn_network.add_edge("IOM", "MSF Holland",weight=1)
goarn_network.add_edge("IOM", "MSF Luxemburg",weight=1)
goarn_network.add_edge("IOM", "Plan International",weight=1)
goarn_network.add_edge("GOAL", "IOM",weight=1)
goarn_network.add_edge("IOM", "Save the Children-UK",weight=1)
goarn_network.add_edge("Medecins du Monde", "OXFAM-GB",weight=1)
goarn_network.add_edge("ICRC", "OXFAM-GB",weight=1)
goarn_network.add_edge("ACF", "OXFAM-GB",weight=1)
goarn_network.add_edge("MSF Spain", "OXFAM-GB",weight=1)
goarn_network.add_edge("MSF Holland", "OXFAM-GB",weight=1)
goarn_network.add_edge("MSF Luxemburg", "OXFAM-GB",weight=1)
goarn_network.add_edge("OXFAM-GB", "Plan International",weight=1)
goarn_network.add_edge("GOAL", "OXFAM-GB",weight=1)
goarn_network.add_edge("OXFAM-GB", "Save the Children-UK",weight=1)
goarn_network.add_edge("ICRC", "Medecins du Monde",weight=1)
goarn_network.add_edge("ACF", "Medecins du Monde",weight=1)
goarn_network.add_edge("MSF Spain", "Medecins du Monde",weight=1)
goarn_network.add_edge("MSF Holland", "Medecins du Monde",weight=1)
goarn_network.add_edge("MSF Luxemburg", "Medecins du Monde",weight=1)
goarn_network.add_edge("Medecins du Monde", "Plan International",weight=1)
goarn_network.add_edge("GOAL", "Medecins du Monde",weight=1)
goarn_network.add_edge("Medecins du Monde", "Save the Children-UK",weight=1)
goarn_network.add_edge("ACF", "ICRC",weight=1)
goarn_network.add_edge("ICRC", "MSF Spain",weight=1)
goarn_network.add_edge("ICRC", "MSF Holland",weight=1)
goarn_network.add_edge("ICRC", "MSF Luxemburg",weight=1)
goarn_network.add_edge("ICRC", "Plan International",weight=1)
goarn_network.add_edge("GOAL", "ICRC",weight=1)
goarn_network.add_edge("ICRC", "Save the Children-UK",weight=1)
goarn_network.add_edge("ACF", "MSF Spain",weight=1)
goarn_network.add_edge("ACF", "MSF Holland",weight=1)
goarn_network.add_edge("ACF", "MSF Luxemburg",weight=1)
goarn_network.add_edge("ACF", "Plan International",weight=1)
goarn_network.add_edge("ACF", "GOAL",weight=1)
goarn_network.add_edge("ACF", "Save the Children-UK",weight=1)
goarn_network.add_edge("MSF Holland", "MSF Spain",weight=1)
goarn_network.add_edge("MSF Luxemburg", "MSF Spain",weight=1)
goarn_network.add_edge("MSF Spain", "Plan International",weight=1)
goarn_network.add_edge("GOAL", "MSF Spain",weight=1)
goarn_network.add_edge("MSF Spain", "Save the Children-UK",weight=1)
goarn_network.add_edge("MSF Holland", "MSF Luxemburg",weight=1)
goarn_network.add_edge("MSF Holland", "Plan International",weight=1)
goarn_network.add_edge("GOAL", "MSF Holland",weight=1)
goarn_network.add_edge("MSF Holland", "Save the Children-UK",weight=1)
goarn_network.add_edge("MSF Luxemburg", "Plan International",weight=1)
goarn_network.add_edge("GOAL", "MSF Luxemburg",weight=1)
goarn_network.add_edge("MSF Luxemburg", "Save the Children-UK",weight=1)
goarn_network.add_edge("GOAL", "Plan International",weight=1)
goarn_network.add_edge("Plan International", "Save the Children-UK",weight=1)
goarn_network.add_edge("GOAL", "Save the Children-UK",weight=1)

#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/fecal_oral.csv", 'wb') as csvfile:
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