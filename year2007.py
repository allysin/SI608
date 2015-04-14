import networkx as nx
import matplotlib.pyplot as plt
goarn_network= nx.Graph()

goarn_network.add_edge("WHO collaborating laboratory UK", "WHO_AFRO",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO_AFRO",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO collaborating laboratory UK",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "WHO Mediterranean Centre for Vulnerability Reduction (WMC)",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "WHO Togo",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "WHO_AFRO",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "UNICEF",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "ECHO",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "Togolese Red Cross",weight=1)
goarn_network.add_edge("Agence de Medecine Preventive", "Federation of Red Cross and Red Crescent Societies",weight=1)
goarn_network.add_edge("WHO Mediterranean Centre for Vulnerability Reduction (WMC)", "WHO Togo",weight=1)
goarn_network.add_edge("WHO Mediterranean Centre for Vulnerability Reduction (WMC)", "WHO_AFRO",weight=1)
goarn_network.add_edge("WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control", "WHO Mediterranean Centre for Vulnerability Reduction (WMC)",weight=1)
goarn_network.add_edge("UNICEF", "WHO Mediterranean Centre for Vulnerability Reduction (WMC)",weight=1)
goarn_network.add_edge("ECHO", "WHO Mediterranean Centre for Vulnerability Reduction (WMC)",weight=1)
goarn_network.add_edge("Togolese Red Cross", "WHO Mediterranean Centre for Vulnerability Reduction (WMC)",weight=1)
goarn_network.add_edge("Federation of Red Cross and Red Crescent Societies", "WHO Mediterranean Centre for Vulnerability Reduction (WMC)",weight=1)
goarn_network.add_edge("WHO Togo", "WHO_AFRO",weight=1)
goarn_network.add_edge("WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control", "WHO Togo",weight=1)
goarn_network.add_edge("UNICEF", "WHO Togo",weight=1)
goarn_network.add_edge("ECHO", "WHO Togo",weight=1)
goarn_network.add_edge("Togolese Red Cross", "WHO Togo",weight=1)
goarn_network.add_edge("Federation of Red Cross and Red Crescent Societies", "WHO Togo",weight=1)
goarn_network.add_edge("WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control", "WHO_AFRO",weight=1)
goarn_network.add_edge("UNICEF", "WHO_AFRO",weight=1)
goarn_network.add_edge("ECHO", "WHO_AFRO",weight=1)
goarn_network.add_edge("Togolese Red Cross", "WHO_AFRO",weight=1)
goarn_network.add_edge("Federation of Red Cross and Red Crescent Societies", "WHO_AFRO",weight=1)
goarn_network.add_edge("UNICEF", "WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control",weight=1)
goarn_network.add_edge("ECHO", "WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control",weight=1)
goarn_network.add_edge("Togolese Red Cross", "WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control",weight=1)
goarn_network.add_edge("Federation of Red Cross and Red Crescent Societies", "WHO HQ International Coordinating Group (ICG) on Vaccine Provision for Yellow fever Control",weight=1)
goarn_network.add_edge("ECHO", "UNICEF",weight=1)
goarn_network.add_edge("Togolese Red Cross", "UNICEF",weight=1)
goarn_network.add_edge("Federation of Red Cross and Red Crescent Societies", "UNICEF",weight=1)
goarn_network.add_edge("ECHO", "Togolese Red Cross",weight=1)
goarn_network.add_edge("ECHO", "Federation of Red Cross and Red Crescent Societies",weight=1)
goarn_network.add_edge("Federation of Red Cross and Red Crescent Societies", "Togolese Red Cross",weight=1)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "National Microbiology Laboratory Canada",weight=1)
goarn_network.add_edge("Centre for Infectious Disease Prevention and Control Canada", "National Microbiology Laboratory Canada",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "National Microbiology Laboratory Canada",weight=1)
goarn_network.add_edge("NICD South Africa", "National Microbiology Laboratory Canada",weight=1)
goarn_network.add_edge("Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)", "National Microbiology Laboratory Canada",weight=1)
goarn_network.add_edge("National Microbiology Laboratory Canada", "School of Pathology of the University of the Witwatersrand",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Microbiology Laboratory Canada",weight=2)
goarn_network.add_edge("National Microbiology Laboratory Canada", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("National Microbiology Laboratory Canada", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "National Microbiology Laboratory Canada",weight=1)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "Centre for Infectious Disease Prevention and Control Canada",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "Canadian Science Centre for Human and Animal Health",weight=1)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "NICD South Africa",weight=1)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "School of Pathology of the University of the Witwatersrand",weight=1)
goarn_network.add_edge("CDC Atlanta", "Canadian Science Centre for Human and Animal Health",weight=2)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("Canadian Science Centre for Human and Animal Health", "Kenya Medical Research Institute (KEMRI)",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "Centre for Infectious Disease Prevention and Control Canada",weight=1)
goarn_network.add_edge("Centre for Infectious Disease Prevention and Control Canada", "NICD South Africa",weight=1)
goarn_network.add_edge("Centre for Infectious Disease Prevention and Control Canada", "Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("Centre for Infectious Disease Prevention and Control Canada", "School of Pathology of the University of the Witwatersrand",weight=1)
goarn_network.add_edge("CDC Atlanta", "Centre for Infectious Disease Prevention and Control Canada",weight=2)
goarn_network.add_edge("Centre for Infectious Disease Prevention and Control Canada", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("Centre for Infectious Disease Prevention and Control Canada", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("Centre for Infectious Disease Prevention and Control Canada", "Kenya Medical Research Institute (KEMRI)",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "NICD South Africa",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "School of Pathology of the University of the Witwatersrand",weight=1)
goarn_network.add_edge("CDC Atlanta", "Canadian Field Epidemiology Programme",weight=2)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("Canadian Field Epidemiology Programme", "Kenya Medical Research Institute (KEMRI)",weight=1)
goarn_network.add_edge("Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)", "NICD South Africa",weight=1)
goarn_network.add_edge("NICD South Africa", "School of Pathology of the University of the Witwatersrand",weight=1)
goarn_network.add_edge("CDC Atlanta", "NICD South Africa",weight=2)
goarn_network.add_edge("NICD South Africa", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("NICD South Africa", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "NICD South Africa",weight=1)
goarn_network.add_edge("Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)", "School of Pathology of the University of the Witwatersrand",weight=1)
goarn_network.add_edge("CDC Atlanta", "Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)",weight=2)
goarn_network.add_edge("Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("Department of Clinical Microbiology and Infectious Disease National Health Laboratory Service (NHLS)", "Kenya Medical Research Institute (KEMRI)",weight=1)
goarn_network.add_edge("CDC Atlanta", "School of Pathology of the University of the Witwatersrand",weight=2)
goarn_network.add_edge("School of Pathology of the University of the Witwatersrand", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("School of Pathology of the University of the Witwatersrand", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "School of Pathology of the University of the Witwatersrand",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=2)
goarn_network.add_edge("CDC Atlanta", "Uganda Virology Research Institute (UVRI)",weight=2)
goarn_network.add_edge("CDC Atlanta", "Kenya Medical Research Institute (KEMRI)",weight=2)
goarn_network.add_edge("CDC Atlanta", "CDC Atlanta",weight=1)
goarn_network.add_edge("Uganda Virology Research Institute (UVRI)", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "WHO Centre for Vulnerability Reduction (WMC) Tunisia",weight=1)
goarn_network.add_edge("Kenya Medical Research Institute (KEMRI)", "Uganda Virology Research Institute (UVRI)",weight=1)
goarn_network.add_edge("MSF Belgium", "WHO DRC",weight=1)
goarn_network.add_edge("CDC Atlanta", "MSF Belgium",weight=1)
goarn_network.add_edge("MSF Belgium", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("MONUC", "MSF Belgium",weight=1)
goarn_network.add_edge("Interchurch Medical Assistance (IMA World Health)", "MSF Belgium",weight=1)
goarn_network.add_edge("MSF Belgium", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "MSF Belgium",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "MSF Belgium",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "MSF Belgium",weight=1)
goarn_network.add_edge("CIRMF", "MSF Belgium",weight=1)
goarn_network.add_edge("ECDC", "MSF Belgium",weight=1)
goarn_network.add_edge("Institut Pasteur France", "MSF Belgium",weight=1)
goarn_network.add_edge("London School of Hygiene and Tropical Medicine", "MSF Belgium",weight=1)
goarn_network.add_edge("MSF Belgium", "National University Singapore",weight=1)
goarn_network.add_edge("CDC Atlanta", "WHO DRC",weight=1)
goarn_network.add_edge("Public Health Agency of Canada", "WHO DRC",weight=1)
goarn_network.add_edge("MONUC", "WHO DRC",weight=1)
goarn_network.add_edge("Interchurch Medical Assistance (IMA World Health)", "WHO DRC",weight=1)
goarn_network.add_edge("Swiss Agency for Development and Cooperation", "WHO DRC",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "WHO DRC",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "WHO DRC",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "WHO DRC",weight=1)
goarn_network.add_edge("CIRMF", "WHO DRC",weight=1)
goarn_network.add_edge("ECDC", "WHO DRC",weight=1)
goarn_network.add_edge("Institut Pasteur France", "WHO DRC",weight=1)
goarn_network.add_edge("London School of Hygiene and Tropical Medicine", "WHO DRC",weight=1)
goarn_network.add_edge("National University Singapore", "WHO DRC",weight=1)
goarn_network.add_edge("CDC Atlanta", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("CDC Atlanta", "MONUC",weight=1)
goarn_network.add_edge("CDC Atlanta", "Interchurch Medical Assistance (IMA World Health)",weight=1)
goarn_network.add_edge("CDC Atlanta", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("CDC Atlanta", "Hopital  Cantonal in Geneva",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "CDC Atlanta",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "CDC Atlanta",weight=1)
goarn_network.add_edge("CDC Atlanta", "CIRMF",weight=1)
goarn_network.add_edge("CDC Atlanta", "ECDC",weight=1)
goarn_network.add_edge("CDC Atlanta", "Institut Pasteur France",weight=1)
goarn_network.add_edge("CDC Atlanta", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("CDC Atlanta", "National University Singapore",weight=1)
goarn_network.add_edge("MONUC", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("Interchurch Medical Assistance (IMA World Health)", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("Public Health Agency of Canada", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("CIRMF", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("ECDC", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("London School of Hygiene and Tropical Medicine", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("National University Singapore", "Public Health Agency of Canada",weight=1)
goarn_network.add_edge("Interchurch Medical Assistance (IMA World Health)", "MONUC",weight=1)
goarn_network.add_edge("MONUC", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "MONUC",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "MONUC",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "MONUC",weight=1)
goarn_network.add_edge("CIRMF", "MONUC",weight=1)
goarn_network.add_edge("ECDC", "MONUC",weight=1)
goarn_network.add_edge("Institut Pasteur France", "MONUC",weight=1)
goarn_network.add_edge("London School of Hygiene and Tropical Medicine", "MONUC",weight=1)
goarn_network.add_edge("MONUC", "National University Singapore",weight=1)
goarn_network.add_edge("Interchurch Medical Assistance (IMA World Health)", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "Interchurch Medical Assistance (IMA World Health)",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "Interchurch Medical Assistance (IMA World Health)",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "Interchurch Medical Assistance (IMA World Health)",weight=1)
goarn_network.add_edge("CIRMF", "Interchurch Medical Assistance (IMA World Health)",weight=1)
goarn_network.add_edge("ECDC", "Interchurch Medical Assistance (IMA World Health)",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Interchurch Medical Assistance (IMA World Health)",weight=1)
goarn_network.add_edge("Interchurch Medical Assistance (IMA World Health)", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("Interchurch Medical Assistance (IMA World Health)", "National University Singapore",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("CIRMF", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("ECDC", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("Institut Pasteur France", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("London School of Hygiene and Tropical Medicine", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("National University Singapore", "Swiss Agency for Development and Cooperation",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "Hopital  Cantonal in Geneva",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "Hopital  Cantonal in Geneva",weight=1)
goarn_network.add_edge("CIRMF", "Hopital  Cantonal in Geneva",weight=1)
goarn_network.add_edge("ECDC", "Hopital  Cantonal in Geneva",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "Institut Pasteur France",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("Hopital  Cantonal in Geneva", "National University Singapore",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "Bernard-Nocht Institute for Tropical Medicine",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "CIRMF",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "ECDC",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "Institut Pasteur France",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("African Field Epidemiology Network", "National University Singapore",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "CIRMF",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "ECDC",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "Institut Pasteur France",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("Bernard-Nocht Institute for Tropical Medicine", "National University Singapore",weight=1)
goarn_network.add_edge("CIRMF", "ECDC",weight=1)
goarn_network.add_edge("CIRMF", "Institut Pasteur France",weight=1)
goarn_network.add_edge("CIRMF", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("CIRMF", "National University Singapore",weight=1)
goarn_network.add_edge("ECDC", "Institut Pasteur France",weight=1)
goarn_network.add_edge("ECDC", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("ECDC", "National University Singapore",weight=1)
goarn_network.add_edge("Institut Pasteur France", "London School of Hygiene and Tropical Medicine",weight=1)
goarn_network.add_edge("Institut Pasteur France", "National University Singapore",weight=1)
goarn_network.add_edge("London School of Hygiene and Tropical Medicine", "National University Singapore",weight=1)
goarn_network.add_edge("FAO", "NAMRU-3 Egypt",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "WHO_EMRO",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "WHO",weight=1)
goarn_network.add_edge("FAO", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("FAO", "WHO_EMRO",weight=1)
goarn_network.add_edge("FAO", "WHO",weight=1)
goarn_network.add_edge("WHO Collaborating Centre", "WHO_EMRO",weight=1)
goarn_network.add_edge("WHO", "WHO Collaborating Centre",weight=1)
goarn_network.add_edge("WHO", "WHO_EMRO",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "WHO Uganda",weight=1)
goarn_network.add_edge("Ministry of Health of Uganda", "UNICEF",weight=1)
goarn_network.add_edge("MSF", "Ministry of Health of Uganda",weight=1)
goarn_network.add_edge("UNICEF", "WHO Uganda",weight=1)
goarn_network.add_edge("MSF", "WHO Uganda",weight=1)
goarn_network.add_edge("MSF", "UNICEF",weight=1)

#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/2007.csv", 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile)
#    spamwriter.writerow('D')
#    centrality=  nx.degree_centrality(goarn_network)
#    for each in centrality.items():
#        #print 'Degree Centrality: ', each[0], each[1]
#        #print each
#        spamwriter.writerow([each[0], each[1]])
#    
#    spamwriter.writerow('C')
#    close=nx.closeness_centrality(goarn_network)    
#    for each in close.items():
#        #print 'Closeness Centrality: ', each[0], '\t', each[1]
#        spamwriter.writerow([each[0], each[1]])
#
#    spamwriter.writerow('B')
#    btwn=nx.betweenness_centrality(goarn_network, weight='weight')
#    for each in btwn.items():
#        #print 'Betweeness Centrality: ', each[0], each[1]
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
#        #print 'Clustering Coefficient per Node: ', each[0], each[1]
#        spamwriter.writerow([each[0], each[1]])
#    csvfile.close()

#nx.draw(goarn_network)
#plt.show()


from networkx import find_cliques
cliques = list(find_cliques(goarn_network))
bigg= max(cliques, key=lambda l: len(l))
print bigg
print nx.graph_number_of_cliques(goarn_network, cliques)



#
#def most_important(G):
# """ returns a copy of G with
#     the most important nodes
#     according to the pagerank """ 
# ranking = nx.betweenness_centrality(G).items()
# print ranking
# r = [x[1] for x in ranking]
# m = sum(r)/len(r) # mean centrality
# t = m*3 # threshold, we keep only the nodes with 3 times the mean
# Gt = G.copy()
# for k, v in ranking:
#  if v < t:
#   Gt.remove_node(k)
# return Gt
#
#Gt = most_important(goarn_network) # trimming
#
#from pylab import show
## create the layout
#pos = nx.spring_layout(goarn_network)
## draw the nodes and the edges (all)
#nx.draw_networkx_nodes(goarn_network,pos,node_color='b',alpha=0.2,node_size=8)
#nx.draw_networkx_edges(goarn_network,pos,alpha=0.1)
#
## draw the most important nodes with a different style
#nx.draw_networkx_nodes(Gt,pos,node_color='r',alpha=0.4,node_size=254)
## also the labels this time
#nx.draw_networkx_labels(Gt,pos,font_size=12,font_color='b')
#show()


#Histogram of degree distribution
#d = nx.degree(goarn_network)
#plt.hist(d.values())
#plt.show()

#from networkx.algorithms import bipartite
#print bipartite.is_bipartite(goarn_network)

H=nx.connected_component_subgraphs(goarn_network)[0]
print(nx.average_shortest_path_length(H))

#def trim_nodes(goarn_network,d):
# """ returns a copy of G without 
#     the nodes with a degree less than d """
# Gt = goarn_network.copy()
# dn = nx.degree(Gt)
# for n in Gt.nodes():
#  if dn[n] <= d:
#   Gt.remove_node(n)
# return Gt
#
##drawing the network without nodes with degree less than 10
#
#
#Gt = trim_nodes(goarn_network,10)
#plt.figure(1)
#plt.title("2007 Network of nodes with at least degree of 10")
#nx.draw(Gt,node_size=0,node_color='w',edge_color='b',alpha=.2, with_labels=False)
#plt.show()

print len(list(nx.k_clique_communities(goarn_network, 5)))

print len(goarn_network.nodes())