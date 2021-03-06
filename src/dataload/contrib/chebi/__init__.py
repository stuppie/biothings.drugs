from .chebi_parser import load_data as _load_data

__METADATA__ = {
    "src_name": 'ChEBI',
    "src_url": 'https://www.ebi.ac.uk/chebi/',    
    "field": "chebi"
}

CHEBI_INPUT_FILE = '/home/jadesara/ENV/chebi/ChEBI_complete.sdf'

def load_data():
    chebi_data = _load_data(CHEBI_INPUT_FILE)
    return chebi_data

def get_id_for_merging(doc, src, db):
    _flag = 0
    
    if 'inchikey' in doc[src]:
        _id = doc[src]['inchikey']       
    else:                
        if 'drugbank_database_links' in doc[src]:            
            d = db.drugbank.find_one({'_id':doc[src]['drugbank_database_links']})
            if d != None:                
                try:
                    _id = d['drugbank']['inchi_key']
                except:
                    _id = d['_id']                
            else:                           
                _flag = 1
        else:                       
            _flag = 1
            
        if _flag:
            _flag = 0
            d = db.chembl.find_one({'chembl.chebi_par_id':doc['_id'][6:]},no_cursor_timeout=True)
            if d != None:
                try:
                    _id = d['chembl']['inchi_key']
                except:
                    _id = d['_id']
            else:                
                d = db.drugbank.find_one({'drugbank.chebi':doc['_id'][6:]})
                if d != None:
                    try:
                        _id = d['chembl']['inchi_key']
                    except:
                        _id = d['_id']                                   
                else:
                    _id = doc['_id']    
    return _id

def get_mapping():
    mapping = {
        "chebi" : {
            "properties" : {
                "chebi_id" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "chebi_name" : {
                    "type":"string"
                    },
                "star" : {
                    "type":"integer"
                    },
                "definition" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "secondary_chebi_id" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "smiles" : {
                    "type" : "string",
                    "analyzer":"string_lowercase"
                    },
                "inchi" : {
                    "type" : "string",
                    "analyzer":"string_lowercase"
                    },
                "inchikey" : {
                    "type" : "string",
                    "analyzer":"string_lowercase"
                    },
                "formulae" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "charge" : {
                    "type":"integer"
                    },
                "mass" : {
                    "type":"float"
                    },
                "monoisotopic_mass" : {
                    "type":"float"
                    },
                "iupac_names" : {
                    "type":"string"
                    },
                "synonyms" : {
                    "type":"string"
                    },                
                "kegg_compound_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "lipid_maps_instance_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "pubchem_database_links" : {
                    "type" : "string"
                    },
                "pubmed_citation_links" : {
                    "type" : "string"
                    },
                "uniprot_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "last_modified" : {
                    "type" : "string"
                    },
                "inn" : {
                    "type" : "string",
                    "analyzer":"string_lowercase"
                    },
                "beilstein_registry_numbers" : {
                    "type" : "string"
                    },
                "gmelin_registry_numbers" : {
                    "type" : "string"
                    },
                "drugbank_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "kegg_drug_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "patent_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "sabio_rk_database_links" : {
                    "type" : "string"
                    },
                "intenz_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "rhea_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "pdbechem_database_links" : {
                    "type":"string"
                    },
                "kegg_glycan_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "molbase_database_links" : {
                    "type":"string"
                    },
                "come_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "resid_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "um_bbd_compid_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "intact_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "biomodels_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "reactome_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    },
                "arrayexpress_database_links" : {
                    "type":"string",
                    "analyzer":"string_lowercase"
                    }
            }
        }
    }
    return mapping
