# PyEED Data Model



PyEED is a Python-encoded data model of an Enzyme Engineering Database. It supports the scalable and reproducible analysis of sequence and structure data of protein families, and makes data and processes findable, accessible, interoperable, and reusable according to the FAIR data principles.



### ProteinSequence

- __uniprot_id__
  - Type: string
  - Description: Identifier for the UniProt database
- __name__
  - Type: string
  - Description: Systematic name of the protein.
- __organism__
  - Type: string
  - Description: Name of the host organism
- __amino_acid_sequence__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.
- __amino_acid_sequence_length__
  - Type: string
  - Description: Number of amino acids
- __protein_mass__
  - Type: string
  - Description: Protein mass in Da
- __domain__
  - Type: string
  - Description: Taxonomy of the host organism (domain)
- __kingdom_phylum__
  - Type: string
  - Description: Taxonomy of the host organism (kingdom or phylum)
- __ncbi_taxonomy_id__
  - Type: string
  - Description: NCBI Taxonomy ID to identify the organism


