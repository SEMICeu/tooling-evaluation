

# Slot: givenName 



URI: [foaf:givenName](http://xmlns.com/foaf/0.1/givenName)
Alias: givenName

<!-- no inheritance hierarchy -->








## Properties

* Range: [Text](Text.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| rdfs:comment | The name(s) that identify the Person within a family with a common surname. || rdfs:isDefinedBy | http://xmlns.com/foaf/0.1/ || skos:scopeNote | Usually a first name or forename. Given to a person by his or her parents at birth or legally recognised as 'given names' through a formal process. All given names are ordered in one property so that, for example, the given name for Johann Sebastian Bach is "Johann Sebastian". |



### Schema Source


* from schema: http://data.europa.eu/m8g/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:givenName |
| native | http://data.europa.eu/m8g/givenName |




## LinkML Source

<details>
```yaml
name: givenName
annotations:
  rdfs:comment:
    tag: rdfs:comment
    value: The name(s) that identify the Person within a family with a common surname.
  rdfs:isDefinedBy:
    tag: rdfs:isDefinedBy
    value: http://xmlns.com/foaf/0.1/
  skos:scopeNote:
    tag: skos:scopeNote
    value: Usually a first name or forename. Given to a person by his or her parents
      at birth or legally recognised as 'given names' through a formal process. All
      given names are ordered in one property so that, for example, the given name
      for Johann Sebastian Bach is "Johann Sebastian".
from_schema: http://data.europa.eu/m8g/
rank: 1000
domain: Person
slot_uri: foaf:givenName
alias: givenName
range: Text
multivalued: true

```
</details>