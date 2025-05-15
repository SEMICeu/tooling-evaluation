

# Slot: birthDate 



URI: [m8g:birthDate](http://data.europa.eu/m8g/birthDate)
Alias: birthDate

<!-- no inheritance hierarchy -->








## Properties

* Range: [GenericDate](GenericDate.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| rdfs:comment | The point in time on which the Person was born. || rdfs:isDefinedby | http://data.europa.eu/m8g || skos:scopeNote | The date of birth could be expressed as date, gYearMonth or gYear, example; - 1980-09-16^^xs:date - 1980-09^^xs:gYearMonth - 1980^^xs:gYear |



### Schema Source


* from schema: http://data.europa.eu/m8g/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | m8g:birthDate |
| native | http://data.europa.eu/m8g/birthDate |




## LinkML Source

<details>
```yaml
name: birthDate
annotations:
  rdfs:comment:
    tag: rdfs:comment
    value: The point in time on which the Person was born.
  rdfs:isDefinedby:
    tag: rdfs:isDefinedby
    value: http://data.europa.eu/m8g
  skos:scopeNote:
    tag: skos:scopeNote
    value: The date of birth could be expressed as date, gYearMonth or gYear, example;
      - 1980-09-16^^xs:date - 1980-09^^xs:gYearMonth - 1980^^xs:gYear
from_schema: http://data.europa.eu/m8g/
rank: 1000
domain: Person
slot_uri: m8g:birthDate
alias: birthDate
range: GenericDate
multivalued: true

```
</details>