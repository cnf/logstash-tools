# ElasticSearch

These are the tools I use for dealing with ES, as it relates to logstash.

## apply_template.py

    ./apply_template.py templates/logstash_per_index.json

Apply your json template against your elasticsearch cluster.

## clean-elasticsearch.sh

    ./clean-elasticsearch.sh

Deletes old logstash indexes from elasticsearch, one index per day.


## counter.py

    ./counter.py 60

Returns the number of entries in elasticsearches logstash index for the last `60` minutes.

## optimize.sh

    ./optimize.sh

Optimizes older logstash indexes.
