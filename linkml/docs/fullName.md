

# Slot: fullName 


_The complete name of the Person as one string._





URI: [foaf:name](http://xmlns.com/foaf/0.1/name)
Alias: fullName

<!-- no inheritance hierarchy -->








## Properties

* Range: [Text](Text.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| rdfs:isDefinedBy | http://xmlns.com/foaf/0.1/ || skos:skosNote | It is anticipated that some systems will only provide or process the full name of a person. Where an individual has more than one full legal name (a relatively rare but not unknown phenomenon), the full name property can be used more than once. In this case, however, the granular name elements should not be used since the intention is that these provide a breakdown of the full name and it will not be clear of which full name this is true. Note that the vocabulary provides an alternative name property. This allows name(s) to be recorded that have no legal status but that nevertheless are the names by which an individual is generally known. A name usually sticks with a person for a long time period. In some European countries a name may only be changed according to certain laws and life events, e.g. marriage. The name denominates a natural person even if he/she changes their address. Documents like birth certificate or diploma usually don't carry an address but always the name. Thus the name is one of the core attributes. However it is not sufficient to identify a person since there are combinations of very common names like Smith in the UK, Meier in Germany, or Li in China. |



### Schema Source


* from schema: http://data.europa.eu/m8g/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:name |
| native | http://data.europa.eu/m8g/fullName |




## LinkML Source

<details>
```yaml
name: fullName
annotations:
  rdfs:isDefinedBy:
    tag: rdfs:isDefinedBy
    value: http://xmlns.com/foaf/0.1/
  skos:skosNote:
    tag: skos:skosNote
    value: It is anticipated that some systems will only provide or process the full
      name of a person. Where an individual has more than one full legal name (a relatively
      rare but not unknown phenomenon), the full name property can be used more than
      once. In this case, however, the granular name elements should not be used since
      the intention is that these provide a breakdown of the full name and it will
      not be clear of which full name this is true. Note that the vocabulary provides
      an alternative name property. This allows name(s) to be recorded that have no
      legal status but that nevertheless are the names by which an individual is generally
      known. A name usually sticks with a person for a long time period. In some European
      countries a name may only be changed according to certain laws and life events,
      e.g. marriage. The name denominates a natural person even if he/she changes
      their address. Documents like birth certificate or diploma usually don't carry
      an address but always the name. Thus the name is one of the core attributes.
      However it is not sufficient to identify a person since there are combinations
      of very common names like Smith in the UK, Meier in Germany, or Li in China.
description: The complete name of the Person as one string.
from_schema: http://data.europa.eu/m8g/
rank: 1000
domain: Person
slot_uri: foaf:name
alias: fullName
range: Text
multivalued: true

```
</details>