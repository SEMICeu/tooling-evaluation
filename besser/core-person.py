from besser.BUML.metamodel.structural import DomainModel, Class, Property, \
    Multiplicity, StringType, IntegerType, DateType, Association, BinaryAssociation, AnyType, Metadata
from besser.generators.rdf import RDFGenerator

# Person attributes definition
person_birthName: Property = Property(name="birthName", type=StringType, metadata=Metadata(uri="http://www.w3.org/ns/person#birthName",description="Full name of the Person given upon their birth."))
person_birthDate: Property = Property(name="birthDate", type=DateType, metadata=Metadata(uri="http://data.europa.eu/m8g/birthDate",description="The point in time on which the Person was born."))
person_deathDate: Property = Property(name="deathDate", type=DateType, metadata=Metadata(uri="http://data.europa.eu/m8g/deathDate", description="The point in time on which the Person died."))
person_familyName: Property = Property(name="familyName", type=StringType, metadata=Metadata(uri="http://xmlns.com/foaf/0.1/familyName", description="The hereditary surname of a family."))
person_fullName: Property = Property(name="fullName", type=StringType, metadata=Metadata(uri="http://xmlns.com/foaf/0.1/name", description="The complete name of the Person as one string."))
person_givenName: Property = Property(name="givenName", type=StringType, metadata=Metadata(uri="http://xmlns.com/foaf/0.1/givenName", description="The name(s) that identify the Person within a family with a common surname."))
# Library class definition
person: Class = Class(name="Person", attributes={person_birthName, person_birthDate,
                                                person_deathDate, person_familyName,
                                                person_fullName, person_givenName}, metadata=Metadata(uri="http://www.w3.org/ns/person#Person", description="A individual human being who may be dead or alive, but not imaginary."))


contactpoint_hasEmail: Property = Property(name="hasEmail", type=StringType, metadata=Metadata(uri="http://data.europa.eu/m8g/email", description="	An electronic address through which the Contact Point can be contacted."))
contactpoint_hasTelephone: Property = Property(name="hasTelephone", type=StringType, metadata=Metadata(uri="http://data.europa.eu/m8g/telephone", description="A telephone number through which the Contact Point can be contacted."))
contactpoint_contactPage: Property = Property(name="contactPage", type=AnyType, metadata=Metadata(uri="http://data.europa.eu/m8g/contactPage", description="A web page that could be used to reach out the Contact Point."))
# ContactPoint class definition
contactpoint: Class = Class(name="ContactPoint", attributes={contactpoint_hasEmail, contactpoint_hasTelephone, contactpoint_contactPage}, metadata=Metadata(uri="http://data.europa.eu/m8g/ContactPoint" , description="Information (e.g. e-mail address, telephone number) of a person or department through which the user can get in touch with."))

# Address attributes definition
address_postName: Property = Property(name="postName", type=StringType, metadata=Metadata(uri="http://www.w3.org/ns/locn#postName", description="A name created and maintained for postal purposes to identify a subdivision of addresses and postal delivery points."))
address_postCode: Property = Property(name="postCode", type=IntegerType, metadata=Metadata(uri="http://www.w3.org/ns/locn#postCode", description="The code created and maintained for postal purposes to identify a subdivision of addresses and postal delivery points."))
# Address class definition
address: Class = Class(name="Address", attributes={address_postName, address_postCode}, metadata=Metadata(uri="http://www.w3.org/ns/locn#Address", description="A spatial object that in a human-readable way identifies a fixed location."))

# Person-ContactPoint association definition
person_contactpoint_contactpoint: Property = Property(name="contactPoint", owner=person, type=contactpoint, multiplicity=Multiplicity(0, "*"), metadata=Metadata(uri="http://data.europa.eu/m8g/contactPoint", description="	The main contact information of the resource."))
contactpoint_person_has: Property = Property(name="has", type=person, multiplicity=Multiplicity(0, "*"))
person_contactpoint_association: Association = Association(name="contactPoint_test", ends={ person_contactpoint_contactpoint, contactpoint_person_has })

# Person-Address association definition
person_address_domicile: Property = Property(name="domicile", type=address, multiplicity=Multiplicity(0, "*"), metadata=Metadata(uri="http://data.europa.eu/m8g/domicile", description="	The place that the Person treats as permanent home." ))
address_person_has: Property = Property(name="", owner=None, type=person, multiplicity=Multiplicity(0, "*"))
person_address_association: Association = Association(name="domicile_test", ends={person_address_domicile, address_person_has})

# Domain model definition
library_model: DomainModel = DomainModel(name="Library_model", types={person, contactpoint, address},
                                         associations={person_contactpoint_association, person_address_association})

# Getting the attributes of the Person class
for attribute in person.attributes:
    print(attribute.name)

# Code Generation
rdf = RDFGenerator(model=library_model)
rdf.generate()