from elasticsearch import Elasticsearch, helpers


es = Elasticsearch(
    "http://localhost:9200"
)

print(es.ping())

mappings = {
    "properties": {
        "agent_id": {"type": "keyword"},   
        "full_name": {"type": "text"},     
        "rank": {"type": "keyword"},       
        "age": {"type": "integer"},       
        "active": {"type": "boolean"},   
        "recruited_on": {"type": "date"}    
    }
}

#res = es.indices.create(index="agents", mappings=mappings)
# print(res)

agents_to_add = [
    {"agent_id": "AG-002", "full_name": "Sarah Connor", "rank": "Commander", "age": 34, "active": True, "recruited_on": "2021-03-12"},
    {"agent_id": "AG-003", "full_name": "James Bond", "rank": "007", "age": 42, "active": True, "recruited_on": "2018-09-01"},
    {"agent_id": "AG-004", "full_name": "Natasha Romanoff", "rank": "Spy", "age": 30, "active": False, "recruited_on": "2019-07-20"},
    {"agent_id": "AG-005", "full_name": "Ethan Hunt", "rank": "Field Lead", "age": 38, "active": True, "recruited_on": "2020-01-15"},
    {"agent_id": "AG-006", "full_name": "Jason Bourne", "rank": "Rogue", "age": 35, "active": False, "recruited_on": "2022-11-30"},
    {"agent_id": "AG-007", "full_name": "Sterling Archer", "rank": "Specialist", "age": 32, "active": True, "recruited_on": "2023-01-01"},
    {"agent_id": "AG-008", "full_name": "Jack Bauer", "rank": "Director", "age": 45, "active": True, "recruited_on": "2015-05-22"},
    {"agent_id": "AG-009", "full_name": "Kim Possible", "rank": "Junior", "age": 20, "active": True, "recruited_on": "2024-02-14"},
    {"agent_id": "AG-010", "full_name": "Sam Fisher", "rank": "Stealth", "age": 48, "active": False, "recruited_on": "2010-06-10"},
    {"agent_id": "AG-011", "full_name": "Fox Mulder", "rank": "Agent", "age": 40, "active": True, "recruited_on": "1993-10-13"}
]

# res = es.index(index="agents", document=agent)
# print(res)

actions = [
    {
        "_index": "agents",
        "_id": agent["agent_id"],
        "_source": agent
    }
    for agent in agents_to_add
]

success, errors = helpers.bulk(es, actions)

# print(f"Successfully indexed {success} agents.")

es.indices.refresh(index="agents")
# query = {
#     "match_all": {}
# }

# query = {
#     "match": {
#         "full_name": "James Bond"
#     }
# }

# query = {
#     "term": {
#         "rank": {
#             "value": "Rogue"
#             }
#     }
# }

# query = {
#     "bool": {
#         "must": [{"term": {"active": True}}],
#         "filter": [{"range": {"age": {"gt": 30}}}]
#     }
# }

# query = {
#     "bool": {
#         "must_not": [{
#             "term": {"rank": "Junior"}}],
#         "must": {"term": {"active": True}}
#         }
#     }

# query = {
#     "bool": {
#         "should": [{"term": {"rank": "Commander"}}, 
#                    {"term": {"rank": "007"}}],
#         "minimum_should_match": 1
#     }
# }


# aggs = {
#         "avg_age": {
#             "avg": {
#                 "field": "age"
#             }
#         }
#     }

# aggs = {
#     "agents_per_rank": {
#         "terms": {"field": "rank"}
#     }
# }

# aggs = {
#     "avg_age": {
#         ""
#     }
# }

# res = es.search(index="agents", aggs=aggs, size=0)
# print(res)
# for hit in res["aggregations"]:
#     print(hit)

# query = {
#     "_source": ["agent_id", "full_name", "rank"],
#     "query" :{
#             "match_phrase": {
#             "full_name": "james bond"
#         }
#     }
# }

# query = {
#     "bool": {
#         "must_not": {
#             "exists": {
#                 "field": "recruited_on"
#             }
#         }
#     }
# }

query = {
        "range": {
                "age": 
                    {"gte": 30, "lte": 45}
    }
}

res = es.search(index="agents", query=query)
print(res["hits"]["hits"])