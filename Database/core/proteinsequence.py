import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Systematic name of the protein.",
    )

    amino_acid_sequence: str = Field(
        ...,
        description="The amino acid sequence of the protein sequence object.",
    )

    ncbi_taxonomy_id: str = Field(
        ...,
        description="NCBI Taxonomy ID to identify the organism",
    )

    uniprot_id: Optional[str] = Field(
        description="Identifier for the UniProt database",
        default=None,
    )

    organism: Optional[str] = Field(
        description="Name of the host organism",
        default=None,
    )

    amino_acid_sequence_length: Optional[str] = Field(
        description="Number of amino acids",
        default=None,
    )

    protein_mass: List[str] = Field(
        description="Protein mass in Da",
        default_factory=ListPlus,
    )

    domain: Optional[str] = Field(
        description="Taxonomy of the host organism (domain)",
        default=None,
    )

    kingdom_phylum: Optional[str] = Field(
        description="Taxonomy of the host organism (kingdom or phylum)",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/TestDatabase-For-Lars.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="4f5e03752f63f52e9eac6d5b66d11e85ea6e5de5"
    )
