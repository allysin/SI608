import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("MSF Belgium", "MSF Holland",weight=1)
goarn_network.add_edge("MSF Belgium", "MSF Switzerland",weight=2)
goarn_network.add_edge("MSF Belgium", "MSF France",weight=1)
goarn_network.add_edge("Institut National de Recherche Biomedicale", "MSF Belgium",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO Ethiopia",weight=1)
goarn_network.add_edge("MSF Belgium", "Red Crescent societies",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO HQ",weight=2)
goarn_network.add_edge("MSF Holland", "MSF Switzerland",weight=1)
goarn_network.add_edge("MSF France", "MSF Holland",weight=1)
goarn_network.add_edge("Institut National de Recherche Biomedicale", "MSF Holland",weight=1)
goarn_network.add_edge("MSF Holland", "WHO Ethiopia",weight=1)
goarn_network.add_edge("MSF Holland", "Red Crescent societies",weight=1)
goarn_network.add_edge("MSF Holland", "WHO HQ",weight=1)
goarn_network.add_edge("MSF France", "MSF Switzerland",weight=1)
goarn_network.add_edge("Institut National de Recherche Biomedicale", "MSF Switzerland",weight=1)
goarn_network.add_edge("MSF Switzerland", "WHO Ethiopia",weight=1)
goarn_network.add_edge("MSF Switzerland", "Red Crescent societies",weight=1)
goarn_network.add_edge("MSF Switzerland", "WHO HQ",weight=2)
goarn_network.add_edge("Institut National de Recherche Biomedicale", "MSF France",weight=1)
goarn_network.add_edge("MSF France", "WHO Ethiopia",weight=1)
goarn_network.add_edge("MSF France", "Red Crescent societies",weight=1)
goarn_network.add_edge("MSF France", "WHO HQ",weight=1)
goarn_network.add_edge("Institut National de Recherche Biomedicale", "WHO Ethiopia",weight=1)
goarn_network.add_edge("Institut National de Recherche Biomedicale", "Red Crescent societies",weight=1)
goarn_network.add_edge("Institut National de Recherche Biomedicale", "WHO HQ",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO Ethiopia",weight=1)
goarn_network.add_edge("WHO Ethiopia", "WHO HQ",weight=1)
goarn_network.add_edge("Red Crescent societies", "WHO HQ",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Ministry of Health Madagascar",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "Ministry of Health Madagascar",weight=1)
goarn_network.add_edge("CDC Atlanta", "Ministry of Health Madagascar",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "WHO HQ",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "WHO_AFRO",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "UNICEF",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "World Food Programme",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Ministry of Health Madagascar", "Reference and Research on Influenza London",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Institut de veille sanitaire",weight=2)
goarn_network.add_edge("CDC Atlanta", "Institut Pasteur France",weight=2)
goarn_network.add_edge("Institut Pasteur France", "WHO HQ",weight=1)
goarn_network.add_edge("Institut Pasteur France", "WHO_AFRO",weight=1)
goarn_network.add_edge("Institut Pasteur France", "UNICEF",weight=1)
goarn_network.add_edge("Institut Pasteur France", "World Food Programme",weight=1)
goarn_network.add_edge("Institut Pasteur France", "WHO Collaborating Centre",weight=2)
goarn_network.add_edge("Institut Pasteur France", "Reference and Research on Influenza London",weight=1)
goarn_network.add_edge("CDC Atlanta", "Institut de veille sanitaire",weight=2)
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
goarn_network.add_edge("UNICEF", "WHO HQ",weight=1)
goarn_network.add_edge("WHO HQ", "World Food Programme",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "WHO HQ",weight=1)
goarn_network.add_edge("Reference and Research on Influenza London", "WHO HQ",weight=1)
goarn_network.add_edge("UNICEF", "WHO_AFRO",weight=1)
goarn_network.add_edge("WHO_AFRO", "World Food Programme",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "WHO_AFRO",weight=1)
goarn_network.add_edge("Reference and Research on Influenza London", "WHO_AFRO",weight=1)
goarn_network.add_edge("UNICEF", "World Food Programme",weight=1)
goarn_network.add_edge("UNICEF", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Reference and Research on Influenza London", "UNICEF",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "World Food Programme",weight=1)
goarn_network.add_edge("Reference and Research on Influenza London", "World Food Programme",weight=1)
goarn_network.add_edge("Reference and Research on Influenza London", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Global Influenza Surveillance Network", "Hong Kong National Influenza Center",weight=1)
goarn_network.add_edge("Department of Health in Hong Kong", "Hong Kong National Influenza Center",weight=1)
goarn_network.add_edge("Hong Kong National Influenza Center", "Ministry of Health in Beijing",weight=1)
goarn_network.add_edge("Department of Health in Hong Kong", "Global Influenza Surveillance Network",weight=1)
goarn_network.add_edge("Global Influenza Surveillance Network", "Ministry of Health in Beijing",weight=1)
goarn_network.add_edge("Department of Health in Hong Kong", "Ministry of Health in Beijing",weight=1)
goarn_network.add_edge("CDC Atlanta", "Centre of International Health Australia",weight=1)
goarn_network.add_edge("CDC Atlanta", "Epicentre France",weight=1)
goarn_network.add_edge("CDC Atlanta", "Institut Pasteur Viet Nam",weight=1)
goarn_network.add_edge("CDC Atlanta", "MSF",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Health Service UK",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("CDC Atlanta", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("CDC Atlanta", "Central Field Epidemiology Group Smittskyddsinstitutet (SMI)",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO_WPRO",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "Epicentre France",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "Institut de veille sanitaire",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "Institut Pasteur France",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "Institut Pasteur Viet Nam",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "MSF",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "National Health Service UK",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "Centre of International Health Australia",weight=1)
goarn_network.add_edge("Centre of International Health Australia", "WHO_WPRO",weight=1)
goarn_network.add_edge("Epicentre France", "Institut de veille sanitaire",weight=1)
goarn_network.add_edge("Epicentre France", "Institut Pasteur France",weight=1)
goarn_network.add_edge("Epicentre France", "Institut Pasteur Viet Nam",weight=1)
goarn_network.add_edge("Epicentre France", "MSF",weight=1)
goarn_network.add_edge("Epicentre France", "National Health Service UK",weight=1)
goarn_network.add_edge("Epicentre France", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("Epicentre France", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "Epicentre France",weight=1)
goarn_network.add_edge("Epicentre France", "WHO_WPRO",weight=1)
goarn_network.add_edge("Institut Pasteur Viet Nam", "Institut de veille sanitaire",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "MSF",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "National Health Service UK",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "Institut de veille sanitaire",weight=1)
goarn_network.add_edge("Institut de veille sanitaire", "WHO_WPRO",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Institut Pasteur Viet Nam",weight=1)
goarn_network.add_edge("Institut Pasteur France", "MSF",weight=1)
goarn_network.add_edge("Institut Pasteur France", "National Health Service UK",weight=1)
goarn_network.add_edge("Institut Pasteur France", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "Institut Pasteur France",weight=1)
goarn_network.add_edge("Institut Pasteur France", "WHO_WPRO",weight=1)
goarn_network.add_edge("Institut Pasteur Viet Nam", "MSF",weight=1)
goarn_network.add_edge("Institut Pasteur Viet Nam", "National Health Service UK",weight=1)
goarn_network.add_edge("Institut Pasteur Viet Nam", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("Institut Pasteur Viet Nam", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "Institut Pasteur Viet Nam",weight=1)
goarn_network.add_edge("Institut Pasteur Viet Nam", "WHO_WPRO",weight=1)
goarn_network.add_edge("MSF", "National Health Service UK",weight=1)
goarn_network.add_edge("MSF", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("MSF", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "MSF",weight=1)
goarn_network.add_edge("MSF", "WHO_WPRO",weight=1)
goarn_network.add_edge("National Health Service UK", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("National Health Service UK", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "National Health Service UK",weight=1)
goarn_network.add_edge("National Health Service UK", "WHO_WPRO",weight=1)
goarn_network.add_edge("National Health Service Viet Nam", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "National Health Service Viet Nam",weight=1)
goarn_network.add_edge("National Health Service Viet Nam", "WHO_WPRO",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "Robert Koch Institute Germany",weight=1)
goarn_network.add_edge("Robert Koch Institute Germany", "WHO_WPRO",weight=1)
goarn_network.add_edge("Central Field Epidemiology Group Smittskyddsinstitutet (SMI)", "WHO_WPRO",weight=1)
goarn_network.add_edge("Ministry of Health in Singapore", "WHO",weight=1)
goarn_network.add_edge("Chinese Ministry of Health", "WHO China",weight=1)
goarn_network.add_edge("CDC Taiwan", "WHO",weight=1)
goarn_network.add_edge("Ministry of Health Algeria", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Ministry of Health Algeria",weight=1)
goarn_network.add_edge("Kazakh Scientific Centre for Quarantine and Zoonotic Disease", "Ministry of Health Algeria",weight=1)
goarn_network.add_edge("Kazakh Scientific Centre for Quarantine and Zoonotic Disease", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Kazakh Scientific Centre for Quarantine and Zoonotic Disease",weight=1)
goarn_network.add_edge("IMTSSA", "WHO",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO",weight=1)
goarn_network.add_edge("Public Health Agency of Canada", "WHO",weight=1)
goarn_network.add_edge("EPIET", "WHO",weight=1)
goarn_network.add_edge("CDC Atlanta", "IMTSSA",weight=1)
goarn_network.add_edge("IMTSSA", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("EPIET", "IMTSSA",weight=1)
goarn_network.add_edge("CDC Atlanta", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("CDC Atlanta", "EPIET",weight=1)
goarn_network.add_edge("EPIET", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("WHO DRC", "WHO HQ",weight=1)
goarn_network.add_edge("Ministry of Health DRC", "WHO HQ",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "WHO HQ",weight=1)
goarn_network.add_edge("Medair", "WHO HQ",weight=1)
goarn_network.add_edge("Institut de la Recherche Biomedicale", "WHO HQ",weight=1)
goarn_network.add_edge("WHO DRC", "WHO_AFRO",weight=1)
goarn_network.add_edge("Ministry of Health DRC", "WHO DRC",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "WHO DRC",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO DRC",weight=1)
goarn_network.add_edge("MSF Switzerland", "WHO DRC",weight=1)
goarn_network.add_edge("Medair", "WHO DRC",weight=1)
goarn_network.add_edge("Institut de la Recherche Biomedicale", "WHO DRC",weight=1)
goarn_network.add_edge("Ministry of Health DRC", "WHO_AFRO",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "WHO_AFRO",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO_AFRO",weight=1)
goarn_network.add_edge("MSF Switzerland", "WHO_AFRO",weight=1)
goarn_network.add_edge("Medair", "WHO_AFRO",weight=1)
goarn_network.add_edge("Institut de la Recherche Biomedicale", "WHO_AFRO",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "Ministry of Health DRC",weight=1)
goarn_network.add_edge("MSF Belgium", "Ministry of Health DRC",weight=1)
goarn_network.add_edge("MSF Switzerland", "Ministry of Health DRC",weight=1)
goarn_network.add_edge("Medair", "Ministry of Health DRC",weight=1)
goarn_network.add_edge("Institut de la Recherche Biomedicale", "Ministry of Health DRC",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "MSF Belgium",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "MSF Switzerland",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "Medair",weight=1)
goarn_network.add_edge("Institut Pasteur Madagascar", "Institut de la Recherche Biomedicale",weight=1)
goarn_network.add_edge("MSF Belgium", "Medair",weight=1)
goarn_network.add_edge("Institut de la Recherche Biomedicale", "MSF Belgium",weight=1)
goarn_network.add_edge("MSF Switzerland", "Medair",weight=1)
goarn_network.add_edge("Institut de la Recherche Biomedicale", "MSF Switzerland",weight=1)
goarn_network.add_edge("Institut de la Recherche Biomedicale", "Medair",weight=1)


#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/airborne.csv", 'wb') as csvfile:
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
#
#
#nx.draw_spring(goarn_network, k=0.95,iterations=20, font_size=10)
#plt.show()

##Histogram of degree distribution
#d = nx.degree(goarn_network)
#plt.hist(d.values())
#plt.show()


def most_important(G):
 """ returns a copy of G with
     the most important nodes
     according to the pagerank """ 
 ranking = nx.betweenness_centrality(G).items()
 print ranking
 r = [x[1] for x in ranking]
 m = sum(r)/len(r) # mean centrality
 t = m*3 # threshold, we keep only the nodes with 3 times the mean
 Gt = G.copy()
 for k, v in ranking:
  if v < t:
   Gt.remove_node(k)
 return Gt

Gt = most_important(goarn_network) # trimming

from pylab import show
# create the layout
pos = nx.spring_layout(goarn_network)
# draw the nodes and the edges (all)
nx.draw_networkx_nodes(goarn_network,pos,node_color='b',alpha=0.2,node_size=8)
nx.draw_networkx_edges(goarn_network,pos,alpha=0.1)

# draw the most important nodes with a different style
nx.draw_networkx_nodes(Gt,pos,node_color='r',alpha=0.4,node_size=254)
# also the labels this time
nx.draw_networkx_labels(Gt,pos,font_size=12,font_color='b')
show()


from networkx.algorithms import bipartite
print bipartite.is_bipartite(goarn_network)


#from networkx import find_cliques
#cliques = list(find_cliques(goarn_network))
#bigg= max(cliques, key=lambda l: len(l))
#print bigg
#print nx.graph_number_of_cliques(goarn_network, cliques)

H=nx.connected_component_subgraphs(goarn_network)[0]
print(nx.average_shortest_path_length(H))

print len(goarn_network.nodes())