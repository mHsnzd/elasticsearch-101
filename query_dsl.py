from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "<password>"

# Create an instance for Elasticsearch client with the desired port
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="/path/to/http_ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Create people index which holds name and age of people
client.indices.create(index="people")

# Create people documents
client.index(
    index="people",document={
        "name": "Jack Daniel",
        "lastname": "Whiskey",
        "age": 158
    }
)
client.index(
    index="people",document={
        "name": "Jack",
        "lastname": "Skellington",
        "age": 31
    }
)

# Elasticsearch provides a Query DSL (Domain Specific Language) 
# based on JSON, consisting of two types:

# 1. Leaf Query: looks in one field

# Match: full-text search to see if a field contains a value
result = client.search(
    index="people", 
    query={
        "match": {
            "name": "Jack"
        }
    }
)
# Use operator to specify mode if multiple values are given
# by default it is set to "or"
result = client.search(
    index="people", 
    query={
        "match": {
            "name": {
                "query": "Jack Daniel",
                "operator": "and"
            }
        }
    }
)

# Term: search to see if a field is equal to a value
result = client.search(
    index="people", 
    query={
        "term": {
            "name": "Jack"
        }
    }
)

# Range: search to see if a field falls within a range: gt, gte, lt, lte
result = client.search(
    index="people", 
    query={
        "range": {
            "age": {
                "gt": 30,
                "lt": 100
            }
        }
    }
)

# 2. Compound Query: combines leaf queries or other compound queries

# Bool: can combine queries based on different operators: 
#   Must: works like a logical "and" between the queries
#   Filter: works like Must but doesn't consider scores*** -> more efficient
#   Should: works like a logical "or" between the queries
#   Must not: works like a logical "nor" between the queries
result = client.search(
    index="people", 
    query={
        "bool": {
            "filter": [ 
                {
                    "match": {
                        "name": "Jack"
                    }
                },
                {
                    "range": {
                        "age": {
                            "gt": 30,
                            "lt": 100
                        }
                    }                    
                }
            ]
        }
    }
)

# ***: Elasticsearch by default calculates a score for all docs in 
# an index and returns the results by the descending order of the scores
# We canhange the priority (score factor) of different clauses of a compound query
result = client.search(
    index="people", 
    query={
        "bool": {
            "must": [ 
                {
                    "match": {
                        "name": "Jack",
                        "boost": 1.0
                    }
                },
                {
                    "match": {
                        "name": "Daniel",
                        "boost": 2.0    # finding daniel is more important than finding jack 
                    }                  
                }
            ]
        }
    }
)

# Specify how many clauses should match in a compound query
result = client.search(
    index="people", 
    query={
        "bool": {
            "must": [ 
                {
                    "match": {
                        "name": "Jack"
                    }
                },
                {
                    "range": {
                        "age": {
                            "gt": 30,
                            "lt": 100
                        }
                    }                    
                }
            ],
            "minimum_should_match": 2
        }
    }
)

# Delete the index
client.indices.delete(index="people")