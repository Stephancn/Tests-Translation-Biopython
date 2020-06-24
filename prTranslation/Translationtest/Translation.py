from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Alphabet import generic_dna

def translatecommondna (seq):
    coding_dna = Seq(seq, IUPAC.unambiguous_dna)
    Protein = coding_dna.translate()
    return (Protein)

def translateMitocondrialdna (seq):
    coding_dna = Seq(seq, IUPAC.unambiguous_dna)
    Protein = coding_dna.translate(table=2)
    return (Protein)

def translaterna (seq):
    coding_rna = Seq(seq, IUPAC.unambiguous_rna)
    Protein = coding_rna.translate()
    return (Protein)

def translateStop (seq):
    coding_dna = Seq(seq, IUPAC.unambiguous_dna)
    Protein = coding_dna.translate(to_stop=True)
    return (Protein)

def translateBacterial(seq):
    dna_bacterial = Seq(seq, generic_dna)
    Protein = dna_bacterial.translate(table="Bacterial", cds=True)
    return (Protein)