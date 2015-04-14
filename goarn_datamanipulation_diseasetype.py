from bs4 import BeautifulSoup
import pydot, json, urllib2, re, itertools, time, codecs


pair_list = list()


def convert():
    #tabsep = open("goarn_tab.txt","w")
    fornetworkx = open("fornetworkx_disease.txt","w")
    jasonfile = open("WHO_DATA_0418.txt","rU")


    jasonlist = list()


    for line in jasonfile:


        jlist = json.loads(line)#convert the string to json
        jasonlist.append(jlist)
        event = jlist["Event"].encode('utf-8')
        collaborators = json.dumps(jlist["Collaborators"]).encode('utf-8')
        year = json.dumps(jlist["Year"]).encode('utf-8')
        diseasetype = json.dumps(jlist["DiseaseType"]).encode('utf-8')
        #tabsep.write(event+"\t"+collaborators+"\n")
        #print len(jlist["Collaborators"])

    print len(jasonlist)






    match = list() #Create a list to store the entry that meet the criteria
    pair_list = list()
    for i in jasonlist:
        #print matchyear
        if "unidentifiable" in i["DiseaseType"]:
            match.append(i)
            filename = 'disease_unidentifiable.txt'
            yeardisease = open(filename,"w")
    print len(match)



    for itemevent in match:
        print itemevent
        for i in range (0,len(itemevent["Collaborators"])):
             for j in range (i+1,len(itemevent["Collaborators"])): #01,02,03,04,12,13,14,23,24
                pairs = list() #To store the list of dictionaries
                pair_dict = dict() #To store the pair and count dictonary
                if i != len(itemevent["Collaborators"])-1:
                    pairs.append(itemevent["Collaborators"][i])
                    pairs.append(itemevent["Collaborators"][j])
                    pairs.sort()
                    pair_dict['pair'] = pairs
                    pair_dict['count'] = 1
                    #To check if this pair appear before:
                    #If pair_list is empty:
                    if  pair_list == []:
                        pair_dict['count'] = 1
                        pair_list.append(pair_dict)
                    #If pair_list is not empty:
                    else:
                        #If the pair didn't appear before in pair_list
                        a = next((item for item in pair_list if item['pair'] == pair_dict['pair']), None)
                        if  a == None:  #Caution! It is not a=='None'
                            pair_dict['count'] = 1
                            pair_list.append(pair_dict)
                            #print "success"
                            #print pair_dict
                            #print next((item for item in pair_list if item["pair"] == pair_dict["pair"]), None)
                        #print len(pair_list)
                        #If the pair appeared before in pair_list,
                        #the 'same pair' means they will have the same count number, which is not what I want.So I cannot use 'if pair_dict in pair_list'
                        else:
                            #print "Have this pair before:"#,pair_dict
                            pair_new = next((item for item in pair_list if item["pair"] == pair_dict["pair"]), None) #In case the count is bigger than 2, show the new dict
                            index = pair_list.index(pair_new)
                            pair_list[index]["count"] = pair_list[index]["count"] + 1
    flag = 0
    for item in pair_list:
        flag +=1
        print flag
        print
        pairs = json.dumps(item["pair"]).encode('utf-8')
        pairs = pairs.replace('[','')
        pairs = pairs.replace(']','')
        count = json.dumps(item["count"]).encode('utf-8')
        yeardisease.write("goarn_network.add_edge("+pairs+",weight="+count+")\n")


    return
#
# ################################################################
#
def creatgraph():
    tabsep = open("goarn_tab.txt","rU")
    graph = pydot.Dot(graph_type = 'graph')

    for line in tabsep:
        group = line.split("\t")
        partners = group[1]#Getthe partner list
        partners = json.loads(partners)
        partners_pair = list(itertools.combinations(partners,2))
        for i in range(len(partners_pair)):
            partner1 = str(partners_pair[i][0].encode("utf-8"))#Need to encode it before converting it to string
            partner2 = str(partners_pair[i][1].encode("utf-8"))
            graph.add_edge(pydot.Edge(partner1,partner2))
        graph.write("partner_graph_output.dot")

    return








def main():
    convert()
    #creatgraph()



if __name__ == '__main__':
  main()
