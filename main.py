import networkx as network
import networkx as nx
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import math
import numpy as np

alpha=0.4
beta=0.3
nodenumber=50
initial_average_degree=1
graph1 = network.barabasi_albert_graph(nodenumber, initial_average_degree)
graph2 = network.barabasi_albert_graph(nodenumber, initial_average_degree)
ps1 = network.spring_layout(graph1)
ps2 = network.spring_layout(graph2)
start_edges=graph1.number_of_edges()+graph2.number_of_edges()#初始边数量
network.draw(graph1, ps1, with_labels = False, node_size = nodenumber)
#plt.savefig("A网络.png")
plot.show()
network.draw(graph2, ps2, with_labels = False, node_size = nodenumber)
#plt.savefig("B网络.png")
plot.show()

G = network.union(graph1, graph2, rename=('Gone', 'Gtwo'))
psG=network.spring_layout(G)
network.draw(G, psG, with_labels = False, node_size = 30)
#plt.savefig("组合网络.png")
plot.show()
###三种匹配方式


match=2;
###随机匹配match=1
###正序匹配match=2
###倒序匹配match=3
###考虑附近影响的正序排列match=4
###考虑附近影响的倒序排列match=5

if match==1:#随机匹配
    degree_1 = [0] * nodenumber
    for i in range(0, nodenumber):
        degree_1[i] = graph1.degree(i)

    degree_2 = [0] * nodenumber
    for i in range(0, nodenumber):
        degree_2[i] = graph2.degree(i)

    rankdegree_1 = np.arange(50)
    rankdegree_2 = np.arange(50)
if match==2:#正序匹配
    degree_1 = [0] * nodenumber
    for i in range(0, nodenumber):
        degree_1[i] = graph1.degree(i)

    degree_2 = [0] * nodenumber
    for i in range(0, nodenumber):
        degree_2[i] = graph2.degree(i)

    # degree_1=[3,1,4,2,5]   用于测试np.argsort函数
    # 从小到大排序，并获取位置
    # 功能：如果原数组位[0.8, 0.2, 0.9, 0.1]，排好序，排成[0.1 0.2 0.8 0.9]的样子，求出这些value在原来的array中的index是多少
    rankdegree_1 = np.argsort(degree_1)
    rankdegree_2 = np.argsort(degree_2)

if match==3:#倒序匹配
    degree_1 = [0] * nodenumber
    for i in range(0, nodenumber):
        degree_1[i] = graph1.degree(i)

    degree_2 = [0] * nodenumber
    for i in range(0, nodenumber):
        degree_2[i] = graph2.degree(i)

    # degree_1=[3,1,4,2,5]   用于测试np.argsort函数
    # 从小到大排序，并获取位置
    # 功能：如果原数组位[0.8, 0.2, 0.9, 0.1]，排好序，排成[0.1 0.2 0.8 0.9]的样子，求出这些value在原来的array中的index是多少
    rankdegree_1 = np.argsort(degree_1)
    rankdegree_2 = np.argsort(degree_2)
    rankdegree_2=rankdegree_2[::-1]#翻转rank2，达到倒序耦合的目的

if match==4:
    degree_improvement_1 = [0] * nodenumber;
    degree_improvement_2 = [0] * nodenumber;
    for i in range(0,nodenumber):
        #print("win1")
        for j in range(0,nodenumber):
            #print("win2")
            if graph1.has_edge(i,j):
                #print("win3")
                for k in range(0,nodenumber):
                    if graph1.has_edge(i,k):
                        degree_improvement_1[i]=degree_improvement_1[i]+math.pow((graph1.degree(k)/graph1.degree(j)),alpha)
    for i in range(0,nodenumber):
        #print("win1")
        for j in range(0,nodenumber):
            #print("win2")
            if graph2.has_edge(i,j):
                #print("win3")
                for k in range(0,nodenumber):
                    if graph2.has_edge(i,k):
                        degree_improvement_2[i]=degree_improvement_2[i]+math.pow((graph2.degree(k)/graph2.degree(j)),alpha)
    rankdegree_1 = np.argsort(degree_improvement_1)
    rankdegree_2 = np.argsort(degree_improvement_2)

if match==5:
    degree_improvement_1 = [0] * nodenumber;
    degree_improvement_2 = [0] * nodenumber;
    for i in range(0,nodenumber):
        #print("win1")
        for j in range(0,nodenumber):
            #print("win2")
            if graph1.has_edge(i,j):
                #print("win3")
                for k in range(0,nodenumber):
                    if graph1.has_edge(i,k):
                        degree_improvement_1[i]=degree_improvement_1[i]+math.pow((graph1.degree(k)/graph1.degree(j)),alpha)
    for i in range(0,nodenumber):
        #print("win1")
        for j in range(0,nodenumber):
            #print("win2")
            if graph2.has_edge(i,j):
                #print("win3")
                for k in range(0,nodenumber):
                    if graph2.has_edge(i,k):
                        degree_improvement_2[i]=degree_improvement_2[i]+math.pow((graph2.degree(k)/graph2.degree(j)),alpha)
    rankdegree_1 = np.argsort(degree_improvement_1)
    rankdegree_2 = np.argsort(degree_improvement_2)
    rankdegree_2=rankdegree_2[::-1]#翻转rank2，达到倒序耦合的目的


#添加G1与G2的耦合边
tempGone= 'Gone{ione}'
tempGone.format(ione=1)
tempGtwo= 'Gtwo{itwo}'
tempGtwo.format(itwo=1)
graph1.nodes()
for i in range(0,50):
    G.add_edge(tempGone.format(ione=rankdegree_1[i]),tempGtwo.format(itwo=rankdegree_2[i]))
    G[tempGone.format(ione=rankdegree_1[i])][tempGtwo.format(itwo=rankdegree_2[i])]['lineweight']=2;
for i in range(0,50):
    for j in range(0,50):
        if G.has_edge(tempGone.format(ione=rankdegree_1[i]),tempGone.format(ione=rankdegree_1[j])):
            G[tempGone.format(ione=rankdegree_1[i])][tempGone.format(ione=rankdegree_1[j])]['lineweight']=1;

for i in range(0,50):
    for j in range(0,50):
        if G.has_edge(tempGtwo.format(itwo=rankdegree_1[i]), tempGtwo.format(itwo=rankdegree_1[j])):
            G[tempGtwo.format(itwo=rankdegree_1[i])][tempGtwo.format(itwo=rankdegree_1[j])]['lineweight'] = 1;

#绘制耦合图（展示耦合边）
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['lineweight'] ==1]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['lineweight'] ==2]
#实线为实际边，虚线为耦合边
nx.draw_networkx_nodes(G,psG,node_size=70)
nx.draw_networkx_edges(G,psG,edgelist=elarge,width=1)
nx.draw_networkx_edges(G,psG,edgelist=esmall,width=1,alpha=0.21,edge_color='b',style='dashed') #alpha可以调整虚实
#plt.savefig("耦合网络.png")
plt.show()

#给graph1的边附加weight
for i in range(0,50):
    for j in range(0,50):
        if graph1.has_edge(i,j):
            graph1[i][j]['weight'] = math.pow((graph1.degree(i) * graph1.degree(j)), alpha);
#给graph2的边附加weight
for i in range(0,50):
    for j in range(0,50):
        if graph2.has_edge(i, j):
            graph2[i][j]['weight'] = math.pow((graph2.degree(i) * graph2.degree(j)), alpha)
#给G的耦合边附加weight
for i in range(0,50):
    for j in range(0,50):
        if G.has_edge(tempGone.format(ione=i),tempGtwo.format(itwo=j)):
            G[tempGone.format(ione=i)][tempGtwo.format(itwo=j)]['weight']=math.pow(graph1.degree(i)*graph2.degree(j),alpha)
#调用方式G[tempGone.format(ione=1)][tempGtwo.format(itwo=1)]

#查询graph1中编号为n1的节点，在graph2中对应的节点编号
def g1_partner(n1):
    for i in range(0,50):
        if(rankdegree_1[i]==n1):
            n2=rankdegree_2[i]
    return n2;
#同理，查询graph2中编号为n2的节点的对应n1
def g2_partner(n2):
    for i in range(0,50):
        if(rankdegree_2[i]==n2):
            n1=rankdegree_1[i]
    return n1;


#给graph1的边附加初始负荷load和最大负荷loadmax
for i in range(0,50):
    for j in range(0,50):
        if i>j:
            if graph1.has_edge(i, j):
                graph1[i][j]['load'] = graph1[i][j]['weight'] \
                                       + (degree_1[i] / (degree_1[i] + degree_2[g1_partner(i)])) * \
                                       G[tempGone.format(ione=i)][tempGtwo.format(itwo=g1_partner(i))]['weight'] \
                                       + (degree_1[j] / (degree_1[j] + degree_2[g1_partner(j)])) * \
                                       G[tempGone.format(ione=j)][tempGtwo.format(itwo=g1_partner(j))]['weight']
                graph1[i][j]['loadmax'] = (1 + beta) * graph1[i][j]['load']
#给graph2的边附加初始负荷load和最大负荷loadmax
for i in range(0,50):
    for j in range(0,50):
        if i>j:
            if graph2.has_edge(i, j):
                graph2[i][j]['load'] = graph2[i][j]['weight'] \
                                       + (degree_2[i] / (degree_2[i] + degree_2[g2_partner(i)])) * \
                                       G[tempGone.format(ione=g2_partner(i))][tempGtwo.format(itwo=i)]['weight'] \
                                       + (degree_2[j] / (degree_2[j] + degree_2[g2_partner(j)])) * \
                                       G[tempGone.format(ione=g2_partner(j))][tempGtwo.format(itwo=j)]['weight']
                graph2[i][j]['loadmax'] = (1 + beta) * graph2[i][j]['load']


#该函数用于删除边（会先分配载荷，再删除边，但若该边为孤立边，则直接删除）
#注：必须存在边才能调用该函数，否则会发生错误
#测试Graph=graph1;i=1;j=0;sum_load=0;
def delete_load_edge(Graph,i,j):
    if Graph.has_edge(i,j):
        if Graph.degree(i) == 1 and Graph.degree(j) == 1:
            Graph.remove_edge(i, j);
            return;
        else:
            sum_max_load = 0  # 先给i和j遍历一圈，计算总负荷能力

            for k in range(0, 50):
                if Graph.has_edge(i, k):
                    sum_max_load = sum_max_load + Graph[i][k]['loadmax'];
            for k in range(0, 50):
                if Graph.has_edge(j, k):
                    sum_max_load = sum_max_load + Graph[j][k]['loadmax'];

            sum_max_load = sum_max_load - 2 * (Graph[i][j]['loadmax'])  # 这条边本身计算了两次，减去

            # 根据总负荷能力，分配载荷
            for k in range(0, 50):
                if Graph.has_edge(i, k) and k != j:
                    delta_load = Graph[i][j]['load'] * Graph[i][k]['loadmax'] / sum_max_load
                    Graph[i][k]['load'] = Graph[i][k]['load'] + delta_load
                    # sum_load=sum_load+delta_load

            for k in range(0, 50):
                if Graph.has_edge(j, k) and k != i:
                    delta_load = Graph[i][j]['load'] * Graph[j][k]['loadmax'] / sum_max_load
                    Graph[j][k]['load'] = Graph[j][k]['load'] + delta_load
                    # sum_load = sum_load + delta_load

            Graph.remove_edge(i, j)
            return;
    else:
        print("你不能删除一个不存在的边")

#在graph1中随机选择一条边删除
def random_delete():
    for i in range(0, nodenumber):
        for j in range(0, nodenumber):
            if i > j:
                if graph1.has_edge(i, j):
                    delete_load_edge(graph1, i, j);
                    return ;

#级联函数
#输入：任意状态的图
#功能：调整超载边，最终使载荷分配完毕，或所有节点被删除的图
def cascading(Graph):
    if Graph.number_of_edges()==0:
        #print("win1")
        return;
    else:
        for i in range(0,50):
            for j in range(0,50):
                if Graph.has_edge(i, j):
                    if Graph[i][j]['load']>Graph[i][j]['loadmax']:
                        delete_load_edge(Graph,i,j);
                        cascading(Graph)
                        #print("win2");print(i,j)

        return ;

#图之间传递耦合影响
def delete_load_node(Graph,i):
    for j in range(0,nodenumber):
        if Graph.has_edge(i,j):
            delete_load_edge(Graph,i,j)
    cascading(Graph);
    return;

def coupling(G1,G2):
    for i in range(0,nodenumber):
        if G1.degree(i)==0:#G1中i节点是孤立节点
            delete_load_node(G2,g1_partner(i));
    return;
# for i in range(0,nodenumber):
#     print(graph1.degree(i))
def end_of_coupling(G1,G2):
    coupling(G1, G2);
    coupling(G2, G1);
    coupling(G1, G2);
    coupling(G2, G1);
    coupling(G1, G2);
    coupling(G2, G1);
    coupling(G1, G2);
    coupling(G2, G1);
    coupling(G1, G2);
    return;
#主控模块
graph1.edges()
graph2.edges()
graph1.number_of_edges()
graph2.number_of_edges()

random_delete()
cascading(graph1)
end_of_coupling(graph1,graph2)

network.draw(graph1, ps1, with_labels = False, node_size = nodenumber)
plot.show()
network.draw(graph2, ps2, with_labels = False, node_size = nodenumber)
plot.show()
#失效边比例F

now_edges=graph1.number_of_edges()+graph2.number_of_edges()#现有边数量
F=(start_edges-now_edges)/(start_edges-1)
#失效节点比例S
s0=0;
for i in range(0,nodenumber):
    if graph1.degree(i)==0:
        s0=s0+1;
    if graph2.degree(i)==0:
        s0=s0+1;
S=s0/(nodenumber*2)

#现存最大功能子团的含边率P
s1 = 0
tests1=max(nx.connected_components(graph1), key=len)
for i in tests1:
    s1=s1+graph1.degree(i)
s1=s1/2

s2=0
tests2 = max(nx.connected_components(graph2), key=len)
for i in tests2:
    s2=s2+graph2.degree(i)
s2=s2/2

P=(s1+s2)/(start_edges-1)

