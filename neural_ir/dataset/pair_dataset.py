from tqdm import tqdm
from pathlib import Path
from torch.utils.data import Dataset
from neural_ir.utils.dataset_utils import read_pairs
import json
from collections import defaultdict
from ir_measures import read_trec_run


class PairDataset(Dataset):
    """
    PairDataset stores pairs of query and document needed to be score in the re-ranking step.
    Attributes
    ----------
    collection: dict
        a dictionary maps document id to text
    queries: dict
        a dictionary maps query id to text 
    pairs: list
        a list of (query, document) pairs for re-ranking
    qrels: dict
        a dictionary storing the ground-truth query relevancy.
    top_k: int
        an integer storing the number of documents to rerank per query

    HINT: - make sure to implement and use the functions defined in utils/dataset_utils.py
          - check out the documentation of ir_measures at https://ir-measur.es/en/latest/
          - the read_trec_run method returns a generator that yields the following object:
            `yield ScoredDoc(query_id=query_id, doc_id=doc_id, score=float(score))`
            (i.e., you can use pair.query_id and pair.doc_id by iterating through the generator)

    """

    # TODO: implement this method
    def __init__(
        self,
        collection_path: str,
        queries_path: str,
        query_doc_pair_path: str,
        qrels_path: str = None,
        top_k: int = 100,
    ):
        """
        Constructing PairDataset
        Parameters
        ----------
        collection_path: str
            path to a tsv file where each line store document id and text separated by a tab character 
        queries_path: str
            path to a tsv file where each line store query id and text separated by a tab character 
        query_doc_pair_path: str
            path to a trec run file (containing query-doc pairs) to re-rank
        qrels_path: str (optional)
            path to a qrel json file expected be formated as {query_id: {doc_id: relevance, ...}, ...}
        """
        # BEGIN SOLUTION
        self.collection = dict(read_pairs(collection_path))
        self.queries = dict(read_pairs(queries_path))
        generator = read_trec_run(query_doc_pair_path)
        self.pairs = [(pair.query_id, pair.doc_id) for pair in generator]
        self.top_k = top_k

        if qrels_path:
            with open(qrels_path, 'r') as file:
                self.qrels = json.load(file)
        else:
            self.qrels = None
            
        # END SOLUTION

    # TODO: implement this method
    def __len__(self):
        """
        Return the number of pairs to re-rank
        """
        # BEGIN SOLUTION
        return len(self.pairs)
        # END SOLUTION

    # TODO: implement this method
    def __getitem__(self, idx):
        """
        Return the idx-th pair of the dataset in the format of (qid, docid, query_text, doc_text)
        """
        # BEGIN SOLUTION
        qid, docid = self.pairs[idx]
        query_text = self.queries[qid]
        doc_text = self.collection[docid]
        return (qid, docid, query_text, doc_text)
        # END SOLUTION
