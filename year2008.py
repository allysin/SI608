import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("FAO", "WHO",weight=1)
goarn_network.add_edge("OIE", "WHO",weight=1)
goarn_network.add_edge("FAO", "OIE",weight=1)
goarn_network.add_edge("GAVI", "WHO",weight=1)
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
goarn_network.add_edge("CIRMF", "National de Recherches Biologiques (INRB)",weight=1)
goarn_network.add_edge("CIRMF", "WHO DRC",weight=1)
goarn_network.add_edge("CIRMF", "NICD South Africa",weight=1)
goarn_network.add_edge("CIRMF", "Caritas (Belgium)",weight=1)
goarn_network.add_edge("CIRMF", "Congolese Red Cross (DRC)",weight=1)
goarn_network.add_edge("CIRMF", "MSF Belgium",weight=1)
goarn_network.add_edge("CIRMF", "UNICEF",weight=1)
goarn_network.add_edge("CIRMF", "MONUC",weight=1)
goarn_network.add_edge("CIRMF", "World Food Programme",weight=1)
goarn_network.add_edge("National de Recherches Biologiques (INRB)", "WHO DRC",weight=1)
goarn_network.add_edge("NICD South Africa", "National de Recherches Biologiques (INRB)",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "National de Recherches Biologiques (INRB)",weight=1)
goarn_network.add_edge("Congolese Red Cross (DRC)", "National de Recherches Biologiques (INRB)",weight=1)
goarn_network.add_edge("MSF Belgium", "National de Recherches Biologiques (INRB)",weight=1)
goarn_network.add_edge("National de Recherches Biologiques (INRB)", "UNICEF",weight=1)
goarn_network.add_edge("MONUC", "National de Recherches Biologiques (INRB)",weight=1)
goarn_network.add_edge("National de Recherches Biologiques (INRB)", "World Food Programme",weight=1)
goarn_network.add_edge("NICD South Africa", "WHO DRC",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "WHO DRC",weight=1)
goarn_network.add_edge("Congolese Red Cross (DRC)", "WHO DRC",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO DRC",weight=1)
goarn_network.add_edge("UNICEF", "WHO DRC",weight=1)
goarn_network.add_edge("MONUC", "WHO DRC",weight=1)
goarn_network.add_edge("WHO DRC", "World Food Programme",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "NICD South Africa",weight=1)
goarn_network.add_edge("Congolese Red Cross (DRC)", "NICD South Africa",weight=1)
goarn_network.add_edge("MSF Belgium", "NICD South Africa",weight=1)
goarn_network.add_edge("NICD South Africa", "UNICEF",weight=1)
goarn_network.add_edge("MONUC", "NICD South Africa",weight=1)
goarn_network.add_edge("NICD South Africa", "World Food Programme",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "Congolese Red Cross (DRC)",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "MSF Belgium",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "UNICEF",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "MONUC",weight=1)
goarn_network.add_edge("Caritas (Belgium)", "World Food Programme",weight=1)
goarn_network.add_edge("Congolese Red Cross (DRC)", "MSF Belgium",weight=1)
goarn_network.add_edge("Congolese Red Cross (DRC)", "UNICEF",weight=1)
goarn_network.add_edge("Congolese Red Cross (DRC)", "MONUC",weight=1)
goarn_network.add_edge("Congolese Red Cross (DRC)", "World Food Programme",weight=1)
goarn_network.add_edge("MSF Belgium", "UNICEF",weight=1)
goarn_network.add_edge("MONUC", "MSF Belgium",weight=1)
goarn_network.add_edge("MSF Belgium", "World Food Programme",weight=1)
goarn_network.add_edge("MONUC", "UNICEF",weight=1)
goarn_network.add_edge("UNICEF", "World Food Programme",weight=1)
goarn_network.add_edge("MONUC", "World Food Programme",weight=1)

#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/2008.csv", 'wb') as csvfile:
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