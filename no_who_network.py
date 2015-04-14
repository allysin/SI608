from networkx import nx
import matplotlib.pyplot as plt

goarn_network = nx.Graph()
goarn_network.add_edge("CDC Atlanta", "FAO",weight=1)
goarn_network.add_edge("CDC Atlanta", "NAMRU-3 Egypt",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("CDC Atlanta", "National Institute of Virology (NIV-South Africa)",weight=2)
goarn_network.add_edge("CDC Atlanta", "Ministry of Health Saudi Arabia",weight=1)
goarn_network.add_edge("FAO", "NAMRU-3 Egypt",weight=1)
goarn_network.add_edge("FAO", "National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("FAO", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("FAO", "Ministry of Health Saudi Arabia",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("NAMRU-3 Egypt", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("Ministry of Health Saudi Arabia", "NAMRU-3 Egypt",weight=1)
goarn_network.add_edge("National Health Laboratory Service (NHLS)", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("Ministry of Health Saudi Arabia", "National Health Laboratory Service (NHLS)",weight=1)
goarn_network.add_edge("Ministry of Health Saudi Arabia", "National Institute of Virology (NIV-South Africa)",weight=1)
goarn_network.add_edge("Global Influenza Surveillance Network", "Hong Kong National Influenza Center",weight=3)
goarn_network.add_edge("Department of Health in Hong Kong", "Hong Kong National Influenza Center",weight=1)
goarn_network.add_edge("Hong Kong National Influenza Center", "Ministry of Health in Beijing",weight=1)
goarn_network.add_edge("Department of Health in Hong Kong", "Global Influenza Surveillance Network",weight=1)
goarn_network.add_edge("Global Influenza Surveillance Network", "Ministry of Health in Beijing",weight=1)
goarn_network.add_edge("Department of Health in Hong Kong", "Ministry of Health in Beijing",weight=1)
goarn_network.add_edge("MSF Luxembourg", "Ministry of Health Mali",weight=1)
goarn_network.add_edge("Hong Kong National Influenza Center", "Japan National Institute for Infectious Diseases",weight=1)
goarn_network.add_edge("Global Influenza Surveillance Network", "Japan National Institute for Infectious Diseases",weight=2)
goarn_network.add_edge("Global Influenza Surveillance Network", "Global Influenza Surveillance Network",weight=1)
goarn_network.add_edge("CDC Atlanta", "EPIET",weight=1)
goarn_network.add_edge("EPIET", "National Institute of Virology (NIV-South Africa)",weight=1)




#import csv
#with open("/Users/grizzlemuff/Documents/SI608/GOARN/no_who_participation.csv", 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile)
#    spamwriter.writerow('D')
#    centrality=  nx.degree_centrality(goarn_network)
#    for each in centrality.items():
#        print 'Degree Centrality: ', each[0], each[1]
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



import matplotlib.pyplot as plt 
nx.draw(goarn_network)
plt.show()

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
#
#
#from networkx import find_cliques
#cliques = list(find_cliques(goarn_network))
#bigg= max(cliques, key=lambda l: len(l))
#print bigg
#print nx.graph_number_of_cliques(goarn_network, cliques)


##Histogram of degree distribution
#d = nx.degree(goarn_network)
#plt.hist(d.values())
#plt.show()


#nx.draw_spring(goarn_network, k=.96, with_labels=False)
#plt.show()


#import networkx.utils as utils
#
#plt.plot(list(utils.cumulative_sum(nx.degree_histogram(goarn_network)))) 
#plt.show()



##http://stackoverflow.com/questions/21921185/simple-fat-tailed-log-binning
#import numpy as np  
#import math as mt
#  
#degree_list=nx.degree(goarn_network).values()
#
#kmin=min(degree_list)
#kmax=max(degree_list)
#
#bins=[float(k) for k in range(kmin,kmax+2,1)]
#density, binedges = np.histogram(degree_list, bins=bins, density=True)
#bins = np.delete(bins, -1)
#
#
#
#logBins = np.logspace(np.log10(kmin), np.log10(kmax),num=20)
#logBinDensity, binedges = np.histogram(degree_list, bins=logBins, density=True)
#logBins = np.delete(logBins, -1)
#
#for x in range(len(logBins)):
#    logBins[x] = mt.ceil(logBins[x])
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.set_xscale('log')
#ax.set_yscale('log')
#
##plt.plot(bins,density,'x',color='black')
#plt.plot(logBins,logBinDensity,'x',color='blue')
#plt.show()


H=nx.connected_component_subgraphs(goarn_network)[0]
print(nx.average_shortest_path_length(H))

print len(goarn_network.nodes())