

# Slot: familyName 



URI: [foaf:familyName](http://xmlns.com/foaf/0.1/familyName)
Alias: familyName

<!-- no inheritance hierarchy -->








## Properties

* Range: [Text](Text.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| rdfs:comment | The hereditary surname of a family. || rdfs:isDefinedBy | http://xmlns.com/foaf/0.1/ || skos:scopeNote | Usually referring to a group of people related by blood, marriage or adoption. This attribute also carries prefixes or suffixes which are part of the family name, e.g. "de Boer", "van de Putte", "von und zu Orlow". Multiple family names, such as are commonly found in Hispanic countries, are recorded in the single family name property so that, for example, Miguel de Cervantes Saavedra's family name would be recorded as "de Cervantes Saavedra".	The complete name of the Person as one string. It can be equal to or different from a Person's birth name. The birth name is used as a legal term, whereas the full name just gives a representation of the complete name of a Person. In addition to the content of given name, family name and, in some systems, patronymic name, this can carry additional parts of a person's name such as titles, middle names or suffixes like "the third" or names which are neither a given nor a family name. The full name is the most reliable label for an individual and as such its use is strongly encouraged, irrespective of whether that name is broken down using the more granular elements. |



### Schema Source


* from schema: http://data.europa.eu/m8g/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:familyName |
| native | http://data.europa.eu/m8g/familyName |




## LinkML Source

<details>
```yaml
name: familyName
annotations:
  rdfs:comment:
    tag: rdfs:comment
    value: The hereditary surname of a family.
  rdfs:isDefinedBy:
    tag: rdfs:isDefinedBy
    value: http://xmlns.com/foaf/0.1/
  skos:scopeNote:
    tag: skos:scopeNote
    value: "Usually referring to a group of people related by blood, marriage or adoption.\
      \ This attribute also carries prefixes or suffixes which are part of the family\
      \ name, e.g. \"de Boer\", \"van de Putte\", \"von und zu Orlow\". Multiple family\
      \ names, such as are commonly found in Hispanic countries, are recorded in the\
      \ single family name property so that, for example, Miguel de Cervantes Saavedra's\
      \ family name would be recorded as \"de Cervantes Saavedra\".\tThe complete\
      \ name of the Person as one string. It can be equal to or different from a Person's\
      \ birth name. The birth name is used as a legal term, whereas the full name\
      \ just gives a representation of the complete name of a Person. In addition\
      \ to the content of given name, family name and, in some systems, patronymic\
      \ name, this can carry additional parts of a person's name such as titles, middle\
      \ names or suffixes like \"the third\" or names which are neither a given nor\
      \ a family name. The full name is the most reliable label for an individual\
      \ and as such its use is strongly encouraged, irrespective of whether that name\
      \ is broken down using the more granular elements."
from_schema: http://data.europa.eu/m8g/
rank: 1000
domain: Person
slot_uri: foaf:familyName
alias: familyName
range: Text
multivalued: true

```
</details>