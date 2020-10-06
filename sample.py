from elasticsearch import Elasticsearch, helpers
es = Elasticsearch("http://localhost:9200")


def createIndex ():
    mapping = {
        "mappings": {
            "properties": {
                "id": { "type": "integer" },
                "t": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss"
                },
                "coordinates": {
                    "type": "nested",
                    "properties": {
                        "x": { "type": "float" },
                        "y": { "type": "float" },
                        "z": { "type": "float" }
                    }
                }
            }
        }
    }
    es.indices.create(index="person", body=mapping)

def setData ():
    person0 = {
        "id": 0,
        "t": "2020-10-06 07:05:16",
        "coordinates": {
            "properties": {
                "x": 101.2,
                "y": 230.5,
                "z": 1550.9
            }
        }
    }
    person1 = {
        "id": 1,
        "t": "2020-10-06 07:07:16",
        "coordinates": {
            "properties": {
                "x": 1017.2,
                "y": 2360.5,
                "z": 1780.9
            }
        }
    }
    es.create(index="person", id=0, body=person0)
    es.create(index="person", id=1, body=person1)


if __name__ == "__main__":

    createIndex()
    setData()

    res = es.indices.get_mapping(index="person")
    print( res )

    es.close()