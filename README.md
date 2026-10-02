# GraphOSINT

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

Link analysis tool for OSINT. Create, connect, and organize entities
on an interactive graph in the browser. Works for people-centric cases
(identities, accounts, emails, locations) and for corporate ones
(companies, domains, netblocks, servers, IPs, certificates).

## Features

Create entities and links, label links, search (including notes and
tags), merge duplicate entities, undo/redo, local autosave, colored
tags, photo attachments, filter by entity type, directed links,
neighbor highlight on hover, minimap, light/dark theme, graph stats,
CSV/JSON import, PNG/SVG export, CSV asset inventory export.

## Importing a case

`Import JSON` takes a GraphOSINT export, or a foreign case export whose
nodes are described by `key` / `type` / `label` / `notes` / `status`.
Types are mapped onto the built-in ones (`employer` and `org` become
companies, `cidr` and `asn` become netblocks, unknown types become
notes), `status` becomes a colored tag, and links come from an `edges`
array when present. Without one, reference fields such as
`"domain": "example.com"` are followed and anything left unreferenced
is attached to the case target.

`examples/` holds two fictional fixtures covering both paths:
`person-case.json` (identities, aliases, accounts, family, with an
explicit `edges` array) and `company-case.json` (subsidiaries, domains,
netblocks, servers, certificates, structure rebuilt from reference
fields alone).

## Usage

`index.html` is standalone, open it directly in a browser.

Or run through Streamlit:

```
pip install streamlit
streamlit run app.py
```

## Stack

HTML, CSS, JavaScript, vis-network, Phosphor Icons.
