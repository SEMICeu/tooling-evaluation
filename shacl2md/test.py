from shacl2md import ShaclMarkdownGenerator
sh_md = ShaclMarkdownGenerator(
    languages=["nl", "en", "fr"],
    output_dir="./",
    shacl_shacl_validation=True,
    version_directory=True,
    crosslink_between_graphs=True,
    ontology_graphs=[
        "core-person-ap-SHACL.ttl",

    ]
)
sh_md.generate(terms="core-person-ap-SHACL.ttl",)