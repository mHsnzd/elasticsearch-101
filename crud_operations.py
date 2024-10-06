from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "<password>"

# Create an instance for Elasticsearch client with the desired port
# ca_certs should point to the http_ca.crt file (usually in the same 
# directory into which Elasticsearch has been extracted).
# Other methods of connection: https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/connecting.html#connecting
client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="/path/to/http_ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

# Retrieve basic information about the cluster
print(client.info())

# Create an index 
client.indices.create(index="my_index")

# Create a document in an index (indexing a document)
client.index(
    index="my_index",
    id="my_doc_id", # optional line: if not given, will be done automatically
    document={
        "my_field_1":"a string",
        "my_field_2": "1111"
    }
)

# Read a document with a specific from an index
client.get(
    index="my_index", 
    id="my_doc_id"
)

# Update a document: update a field
client.update(
    index="my_index",
    id="my_doc_id",
    doc={
        "my_field_1": "a new string"
    }
)

# Update a document: update a field and add a new field
client.update(
    index="my_index",
    id="my_doc_id",
    doc={
        "my_field_1": "a new string",
        "my_field_3": "some other string"
    }
)

# Update a document: remove a field
client.update(
    index="my_index",
    id="my_doc_id",
    script={
        "source": "ctx._source.remove('my_field_3')",
        "lang": "painless"
    }
)

# Delete a document from an index
client.delete(index="my_index", id="my_doc_id")

# Delete an index
client.indices.delete(index="my_index")