

# Slot: deathDate 


_The point in time on which the Person died._





URI: [m8g:deathDate](http://data.europa.eu/m8g/deathDate)
Alias: deathDate

<!-- no inheritance hierarchy -->








## Properties

* Range: [GenericDate](GenericDate.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| rdfs:isDefinedby | http://data.europa.eu/m8g || skos:scopeNote | The date of birth could be expressed as date, gYearMonth or gYear, example; - 1980-09-16^^xs:date - 1980-09^^xs:gYearMonth - 1980^^xs:gYear |



### Schema Source


* from schema: http://data.europa.eu/m8g/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | m8g:deathDate |
| native | http://data.europa.eu/m8g/deathDate |




## LinkML Source

<details>
```yaml
name: deathDate
annotations:
  rdfs:isDefinedby:
    tag: rdfs:isDefinedby
    value: http://data.europa.eu/m8g
  skos:scopeNote:
    tag: skos:scopeNote
    value: The date of birth could be expressed as date, gYearMonth or gYear, example;
      - 1980-09-16^^xs:date - 1980-09^^xs:gYearMonth - 1980^^xs:gYear
description: The point in time on which the Person died.
from_schema: http://data.europa.eu/m8g/
rank: 1000
domain: Person
slot_uri: m8g:deathDate
alias: deathDate
range: GenericDate
multivalued: true

```
</details>