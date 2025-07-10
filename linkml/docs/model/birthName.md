

# Slot: birthName 


_Full name of the Person given upon their birth._





URI: [person:birthName](http://www.w3.org/ns/person#birthName)
Alias: birthName

<!-- no inheritance hierarchy -->








## Properties

* Range: [Text](Text.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| rdfs:isDefinedBy | http://www.w3.org/ns/person# || skos:scopeNote | The birth name may apply to the surname, the given name, or the entire name. Where births are required to be officially registered, the entire name entered onto a births register or birth certificate may by that fact alone become the person's legal name. See Wikipedia Birth name page. All data associated with an individual are subject to change. Names can change for a variety of reasons, either formally or informally, and new information may come to light that means that a correction or clarification can be made to an existing record. Birth names tend to be persistent however and for this reason they are recorded by some public sector information systems. There is no granularity for birth name - the full name should be recorded in a single field. |



### Schema Source


* from schema: http://data.europa.eu/m8g/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | person:birthName |
| native | http://data.europa.eu/m8g/birthName |




## LinkML Source

<details>
```yaml
name: birthName
annotations:
  rdfs:isDefinedBy:
    tag: rdfs:isDefinedBy
    value: http://www.w3.org/ns/person#
  skos:scopeNote:
    tag: skos:scopeNote
    value: The birth name may apply to the surname, the given name, or the entire
      name. Where births are required to be officially registered, the entire name
      entered onto a births register or birth certificate may by that fact alone become
      the person's legal name. See Wikipedia Birth name page. All data associated
      with an individual are subject to change. Names can change for a variety of
      reasons, either formally or informally, and new information may come to light
      that means that a correction or clarification can be made to an existing record.
      Birth names tend to be persistent however and for this reason they are recorded
      by some public sector information systems. There is no granularity for birth
      name - the full name should be recorded in a single field.
description: Full name of the Person given upon their birth.
from_schema: http://data.europa.eu/m8g/
rank: 1000
domain: Person
slot_uri: person:birthName
alias: birthName
range: Text
multivalued: true

```
</details>