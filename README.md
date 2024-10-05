# Elasticsearch 101
This repository is a quick tutorial to get me (and any other curious individual who ends up here) started with Elasticsearch. For accurate up-to-date information about Elasticsearch, *please* visit  the official [website](https://www.elastic.co/elasticsearch).
<br>

Table of contents: 
  - [Elasticsearch](#elasticsearch)
    - [Elastic Stack](#elastic-stack)
    - [Applications](#applications)
    - [Basic Concepts](#basic-concepts)
    - [Setup and Installation](#setup-and-installation)
  - [References](#references)


## Elasticsearch
Elasticsearch is a distributed search and analytics engine that is mainly used for fast, scalable search and data analysis. It is based on Apache Lucene and developed in Java. [RESTful API](https://aws.amazon.com/what-is/restful-api/) (using JSON format) can be used to communicate with it.

Elasticsearch can be used for searching and analyzing both structured and unstructured data up to petabypes (and beyond). It uses denormalization to improve its search performance.

### Elastic Stack
Elasticsearch is part of Elastic stack environment. Elastic Stack is a set of open source tools meant for managing and analysing data:
- **Elasticsearch**: a distributed search engine
- **Logstash**: a data processing pipeline that receives data from various sources and sends them to Elasticsearch
- **Beats**: data shipper that can send data from a large number of systems to Logstash or Elasticsearch
- **Kibana**: an analysis tool mainly used for data visualization 

### Applications
Elasticsearch can be used as a substitute for document databases such as [MongoDB](https://www.mongodb.com/) and [RavenDB](https://ravendb.net).
<br>
Due to its flexibility, speed, and scalability, it can be used for many purposes: in ML for automatic real-time data modeling; in analyzing logs and events; in analyzing security breaches; in e-commerce for search results and recommendations; and more.

### Basic Concepts
1. **Cluster**: A collection of (one or more) connected nodes,which all know about each other, is called a cluster. A cluster can index and search in the data of all its nodes.
2. **Node**: Each node is an instance of Elasticsearch. Multiple nodes can be placed on a server (physical or virtual) based on the server's resources (RAM, processing power, memory, ...).
3. **Index**: A namespace that holds a collection of documents.
4. **Shard**: A smaller (more managable) piece of an index. Sharding is done to improve horizontal scalability.
5. **Replica**: A copy of a shard used to avoid data loss and improve performance.
6. **Document**: A collection of fields which are each key-value pairs of our data

Mapping concepts across SQL and Elasticsearch:
|  SQL | Elasticsearch  |
|---|---|
|  database | cluster |
|table|index|
|row|document|
|column|field|

### Setup and Installation
Installing steps for supported operating systems can be viewed in the official website. This tutorial will use the 8.10 version.
<br>We'll use Python client to communicate with the instance. Make sure you have the correct version of python installed depending on the version of Elasticsearch you'll be using.

```bash

 pip install elasticsearch

```

## References
The information used in this repository has been gathered from vaious sources, which have been linked throughout the project to the best of my abilities. 
The major references are:
- Elastic official [website](https://www.elastic.co)
- [Quera](https://quera.org/college/landpage/14963/nosql) NoSQL course
