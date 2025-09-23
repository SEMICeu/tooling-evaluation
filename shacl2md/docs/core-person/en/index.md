---
layout: "default"
title: "Core Person Vocabulary"
parent: "index"
nav_order: 1
nav_exclude: False
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Core Person Vocabulary
====================

**Version:** None

**Previous version:** 

**Created:** None

**Last modified:** None

**SHACL file:** [core-person.shacl.ttl](core-person.shacl.ttl)

**Other languages:**

**Authors:**


This a description

<div id="zoom" class="table-wrapper">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" preserveAspectRatio="none" version="1.1" viewBox="0 0 238 74" zoomAndPan="magnify"><defs/><g><a href="#ex%3APerson" target="_top" title="#ex%3APerson" xlink:actuate="onRequest" xlink:href="#ex%3APerson" xlink:show="new" xlink:title="#ex%3APerson" xlink:type="simple"><g id="elem_ex_Person"><rect codeLine="15" fill="#F1F1F1" height="53.2188" id="ex_Person" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="217" x="7" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="50" x="52" y="26.5332">Person</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="102" y="26.5332"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="73" x="106" y="26.5332">(ex:Person)</text><line style="stroke:#181818;stroke-width:0.5;" x1="8" x2="223" y1="34.6094" y2="34.6094"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="13" y="53.1426">family</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="49" y="53.1426"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="35" x="53" y="53.1426">name</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="88" y="53.1426"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="92" y="53.1426">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="96" y="53.1426"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="85" x="100" y="53.1426">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="185" y="53.1426"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="29" x="189" y="53.1426">[0..*]</text></g></a></g></svg>
</div>

## Namespaces

| Prefix | URI      |
| :----- | :------- |
| dct     | [http://purl.org/dc/terms/](http://purl.org/dc/terms/) |
| ex     | [http://example.org/](http://example.org/) |
| foaf     | [http://xmlns.com/foaf/0.1/](http://xmlns.com/foaf/0.1/) |
| owl     | [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#) |
| rdf     | [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#) |
| rdfs     | [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#) |
| sh     | [http://www.w3.org/ns/shacl#](http://www.w3.org/ns/shacl#) |

## Classes & Properties

**Classes:** 
 [Person](#ex%3APerson)
## <a id="ex%3APerson"></a>Person <small>[(ex:Person)](http://example.org/Person)</small>




| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='foaf%3AfamilyName'></a>family name <br> <small>[(foaf:familyName)](http://xmlns.com/foaf/0.1/familyName)</small> | The hereditary surname of a family. | `0..*` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |

[^1]: Unique language tags required
<style>
#zoom {
  height: 60vh;
  padding: 5px;
}

#zoom > svg {
    width: 100%;
    height: 100%;
}

.svg-external-link {
  width: 16px;
  height: 16px;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.5.0/dist/svg-pan-zoom.min.js"></script>
<script>
window.onload = (event) => {
  svgPanZoom('#zoom > svg', {controlIconsEnabled: true})
};
</script>
