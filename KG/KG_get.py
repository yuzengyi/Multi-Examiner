from py2neo import Graph, Node, Relationship, NodeMatcher

def get_KG(keyword):
    g = Graph('http://localhost:7474', name='neo4j', password='Yuzeyu777')
    # 执行Cypher查询，获取包含关键词的节点及其相邻节点
    query = f"""
    MATCH (p)-[r]-(n)
    WHERE p.name= '{keyword}'
    RETURN p, r, n
    """
    question_list = []
    # question_tpye = []
    # 执行查询
    try:
        results = g.run(query).data()
        if len(results) > 0:
            question_list.append(results[0]['p']['type'])
            question_list.append(results[0]['p']['desc'])
            # print("该知识点的信息：",question_list)
            # # 打印结果
            for record in results:
                desc = record['n']['desc']
                if desc != "":
                    question_list.append(record['n']['desc'])
    except:
        print("未找到相关内容")

    return question_list



# # 执行查询
# query = "MATCH (n:Computer_Hardware) RETURN n.name, n.desc"
# result = g.run(query).data()
#
# # 打印结果
# for record in result:
#     print(record["n.name"], record["n.desc"])


if __name__ == '__main__':
    keyword = "存储器"
    get_KG(keyword)
