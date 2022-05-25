from xml.etree import ElementTree
from numpy.core.fromnumeric import mean
import matplotlib.pyplot as plt

def find_Node(id, ids):
    nodes= term_dict[id]
    if nodes!=[]:
        for node in nodes:
            ids.add(node)
            find_Node(node, ids)

if __name__ == "__main__":
    terms = ElementTree.parse("go_obo.xml").findall('term')  #Find all term nodes
    print("There are {} terms in go_obo.xml.".format(len(terms)))

    term_dict={}    #All nodes is_a under term
    node_sum= {}     #Number of nodes under term
    trans={}   #If there is translation under defstr, write 1 exists, and zero does not exist
    # read is_a, ids and terms related to 'translation'
    for term in terms:      #Iterate through all term nodes
        id=term.find('id').text     #Find the node id under def
        is_a=term.findall('is_a')   #Find the node is_a under def
        defstr=term.find("def/defstr").text   #Find the node defstr under def
        node_sum[id]=0
        is_a_list=[]    #GO of the is_a node
        for a in is_a:
            is_a_list.append(a.text)
        term_dict[id]=is_a_list
        if "translation" in defstr:     #Whether the node defstr contains translation
            trans[id]=1     #Write 1 if there is
        else:
            trans[id]=0     #Write 0 if there is not
    # count the childnotes of terms and subtract a subset of duplicates
    for key in term_dict.keys():
        ids= set()
        find_Node(key,ids)
        for id in ids:
            node_sum[id]+=1

    Nodes= []     #Number of all nodes
    NodesByT=[]     #Number of nodes with 'translation'
    for k,v in node_sum.items():
        Nodes.append(v)
        if trans[k]==1:
            NodesByT.append(v)

    # draw the boxplot of all terms and terms related to translation
    plt.figure(figsize=(8,6))
    plt.boxplot(Nodes, vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
    plt.title('Distribution of child node number of all GO terms')
    plt.xlabel("all GO terms")
    plt.ylabel("Number")
    plt.show()

    plt.figure(figsize=(8,6))
    plt.boxplot(NodesByT, vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
    plt.title('Distribution of child node number of terms associated with ‘translation’')
    plt.xlabel("associated with ‘translation’")
    plt.ylabel("Number")
    plt.show()
    #compare
    if mean(Nodes)>mean(NodesByT):
        print("the translation terms contain, on average, a smaller number of child nodes than the overall Gene Ontology")
    elif mean(Nodes)<mean(NodesByT):
        print("the translation terms contain, on average, a greater number of child nodes than the overall Gene Ontology")
    else:
        print("They contain an equal number of average child nodes")