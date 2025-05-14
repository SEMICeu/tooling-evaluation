from besser.BUML.metamodel.structural import DomainModel, Class, Property, \
    Multiplicity, StringType, IntegerType, DateType, Association, BinaryAssociation
from besser.generators.rdf import RDFGenerator

# Person attributes definition
person_birthName: Property = Property(name="birthName", type=StringType)
person_birthDate: Property = Property(name="birthDate", type=DateType)
person_deathDate: Property = Property(name="deathDate", type=DateType)
person_familyName: Property = Property(name="familyName", type=StringType)
person_fullName: Property = Property(name="fullName", type=StringType)
person_givenName: Property = Property(name="givenName", type=StringType)
# Library class definition
person: Class = Class(name="Person", attributes={person_birthName, person_birthDate,
                                                person_deathDate, person_familyName,
                                                person_fullName, person_givenName})

# Address attributes definition
address_postName: Property = Property(name="postName", type=StringType)
address_postCode: Property = Property(name="postCode", type=IntegerType)
# Address class definition
address: Class = Class(name="Address", attributes={address_postName, address_postCode})

# Person-Address association definition
person_address_domicile: Property = Property(name="domicile", type=address, multiplicity=Multiplicity(0, "*"))
address_person_has: Property = Property(name="has", owner=None, type=person, multiplicity=Multiplicity(0, "*"))
person_address_association: Association = Association(name="domicile", ends={person_address_domicile, address_person_has})

# Domain model definition
library_model: DomainModel = DomainModel(name="Library_model", types={person, address},
                                         associations={person_address_association})

# Getting the attributes of the Person class
for attribute in person.attributes:
    print(attribute.name)

# Code Generation
rdf = RDFGenerator(model=library_model)
rdf.generate()