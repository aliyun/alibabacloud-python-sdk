# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RerankRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        documents: List[str] = None,
        max_chunks_per_doc: int = None,
        model: str = None,
        owner_id: int = None,
        query: str = None,
        region_id: str = None,
        return_documents: bool = None,
        top_k: int = None,
    ):
        # Instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) API to view details of all AnalyticDB PostgreSQL instances in the target region, including the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # List of documents to be re-ordered.
        self.documents = documents
        # Maximum number of chunks allowed when the text exceeds the model window:
        # - bge-reranker-v2-m3: default value is 10.
        # - bge-reranker-v2-minicpm-layerwise: default value is 5:
        # 
        # > Example of splitting
        # > - If using the bge-reranker-v2-minicpm-layerwise model, the maximum single inference window is 2048 tokens. If the query is 48 tokens and the content of a single document parameter is 9000 tokens, it will be divided as follows: 1-2000 for the first, 2001-4000 for the second, and so on. If the number of splits exceeds MaxChunksPerDoc, the remaining sentences will be discarded.
        self.max_chunks_per_doc = max_chunks_per_doc
        # Rerank model, currently supports:
        # - bge-reranker-v2-m3: (default), better performance, supports 8192 tokens per inference, if exceeded, it will be split, which may reduce the effect.
        # - bge-reranker-v2-minicpm-layerwise: better performance than v2-m3, supports 2048 tokens per inference, if exceeded, it will be split, which may reduce the effect.
        self.model = model
        self.owner_id = owner_id
        # Query statement for Rerank.
        self.query = query
        # Region ID where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # If set to false, does not return the Documents text, only returns the index of the document order and the rerank score.
        self.return_documents = return_documents
        # Number of most relevant documents to return.
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.documents is not None:
            result['Documents'] = self.documents

        if self.max_chunks_per_doc is not None:
            result['MaxChunksPerDoc'] = self.max_chunks_per_doc

        if self.model is not None:
            result['Model'] = self.model

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.return_documents is not None:
            result['ReturnDocuments'] = self.return_documents

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Documents') is not None:
            self.documents = m.get('Documents')

        if m.get('MaxChunksPerDoc') is not None:
            self.max_chunks_per_doc = m.get('MaxChunksPerDoc')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReturnDocuments') is not None:
            self.return_documents = m.get('ReturnDocuments')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

