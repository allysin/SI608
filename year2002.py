import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("Ministry of Health", "WHO",weight=1)
goarn_network.add_edge("MSF Belgium", "Ministry of Health",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Ministry of Health Madagascar",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "Ministry of Health Madagascar",weight=1)
goarn_network.add_edge("CDC Atlanta", "Ministry of Health Madagascar",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "WHO HQ",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "WHO_AFRO",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "UNICEF",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "World Food Programme",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "Reference and Research on Influenza London",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Institut de veille sanitaire",weight=1)
goarn_network.add_edge("CDC Atlanta", "Institut Pasteur France",weight=1)
goarn_network.add_edge("Institut Pasteur France", "WHO HQ",weight=1)
goarn_network.add_edge("Institut Pasteur France", "WHO_AFRO",weight=1)
goarn_network.add_edge("Institut Pasteur France", "UNICEF",weight=1)
goarn_network.add_edge("Institut Pasteur France", "World Food Programme",weight=1)
goarn_network.add_edge("Institut Pasteur France", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Reference and Research on Influenza London",weight=1)
goarn_network.add_edge("CDC Atlanta", "Institut de veille sanitaire",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "WHO HQ",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "WHO_AFRO",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "UNICEF",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "World Food Programme",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "Reference and Research on Influenza London",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO HQ",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO_AFRO",weight=1)
goarn_network.add_edge("CDC Atlanta", "UNICEF",weight=1)
goarn_network.add_edge("CDC Atlanta", "World Food Programme",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("CDC Atlanta", "Reference and Research on Influenza London",weight=1)
goarn_network.add_edge("WHO HQ", "WHO_AFRO",weight=2)
goarn_network.add_edge("UNICEF", "WHO HQ",weight=2)
goarn_network.add_edge("WHO HQ", "World Food Programme",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "WHO HQ",weight=2)
goarn_network.add_edge("Reference and Research on Influenza London", "WHO HQ",weight=1)
goarn_network.add_edge("UNICEF", "WHO_AFRO",weight=2)
goarn_network.add_edge("WHO_AFRO", "World Food Programme",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "WHO_AFRO",weight=2)
goarn_network.add_edge("Reference and Research on Influenza London", "WHO_AFRO",weight=1)
goarn_network.add_edge("UNICEF", "World Food Programme",weight=1)
goarn_network.add_edge("UNICEF", "WHO Collaborating Centre",weight=2)
goarn_network.add_edge("Reference and Research on Influenza London", "UNICEF",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "World Food Programme",weight=1)
goarn_network.add_edge("Reference and Research on Influenza London", "World Food Programme",weight=1)
goarn_network.add_edge("Reference and Research on Influenza London", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Institut Pasteur Dakar", "Ministry of Health Senegal ",weight=1)
goarn_network.add_edge("Institut Pasteur Dakar", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Institut Pasteur Dakar", "WHO_AFRO",weight=1)
goarn_network.add_edge("Institut Pasteur Dakar", "WHO HQ",weight=1)
goarn_network.add_edge("ICG", "Institut Pasteur Dakar",weight=1)
goarn_network.add_edge("Institut Pasteur Dakar", "MSF",weight=1)
goarn_network.add_edge("Institut Pasteur Dakar", "Red Crescent societies",weight=2)
goarn_network.add_edge("Institut Pasteur Dakar", "UNICEF",weight=1)
goarn_network.add_edge("Ministry of Health Senegal ", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Ministry of Health Senegal ", "WHO_AFRO",weight=1)
goarn_network.add_edge("Ministry of Health Senegal ", "WHO HQ",weight=1)
goarn_network.add_edge("ICG", "Ministry of Health Senegal ",weight=1)
goarn_network.add_edge("MSF", "Ministry of Health Senegal ",weight=1)
goarn_network.add_edge("Ministry of Health Senegal ", "Red Crescent societies",weight=2)
goarn_network.add_edge("Ministry of Health Senegal ", "UNICEF",weight=1)
goarn_network.add_edge("ICG", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("MSF", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO Collaborating Centre",weight=2)
goarn_network.add_edge("ICG", "WHO_AFRO",weight=1)
goarn_network.add_edge("MSF", "WHO_AFRO",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO_AFRO",weight=2)
goarn_network.add_edge("ICG", "WHO HQ",weight=1)
goarn_network.add_edge("MSF", "WHO HQ",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO HQ",weight=2)
goarn_network.add_edge("ICG", "MSF",weight=1)
goarn_network.add_edge("ICG", "Red Crescent societies",weight=2)
goarn_network.add_edge("ICG", "UNICEF",weight=1)
goarn_network.add_edge("MSF", "Red Crescent societies",weight=2)
goarn_network.add_edge("MSF", "UNICEF",weight=1)
goarn_network.add_edge("Red Crescent societies", "Red Crescent societies",weight=1)
goarn_network.add_edge("Red Crescent societies", "UNICEF",weight=2)

##centrality measures
#
#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/2002.csv", 'wb') as csvfile:
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
#    spamwriter.writerow('A')
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


nx.draw_spring(goarn_network, k=0.95,iterations=20)
plt.show()

H=nx.connected_component_subgraphs(goarn_network)[0]
print(nx.average_shortest_path_length(H))