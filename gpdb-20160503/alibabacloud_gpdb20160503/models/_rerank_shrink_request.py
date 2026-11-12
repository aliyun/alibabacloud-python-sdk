# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RerankShrinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        documents_shrink: str = None,
        instruct: str = None,
        max_chunks_per_doc: int = None,
        model: str = None,
        owner_id: int = None,
        query: str = None,
        region_id: str = None,
        return_documents: bool = None,
        top_k: int = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to view the details of all AnalyticDB for PostgreSQL instances in the specified region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The list of documents to be reranked.
        self.documents_shrink = documents_shrink
        # The description of the custom ranking task type. This parameter can be set when RerankModel.Name is qwen3-rerank. It guides the model to use different ranking strategies.
        self.instruct = instruct
        # The maximum number of chunks allowed when the text exceeds the model window. Valid values:
        # - bge-reranker-v2-m3: 10. This is the default value.
        # - bge-reranker-v2-minicpm-layerwise: 5. This is the default value.
        # 
        # > Chunking example
        # > - If you use the bge-reranker-v2-minicpm-layerwise model, the maximum single inference window is 2,048 tokens. If the query is 48 tokens and a single document parameter contains 9,000 tokens, the document is split into chunks: tokens 1 to 2,000 form the first chunk, tokens 2,001 to 4,000 form the second chunk, and so on. If the number of chunks exceeds the value of MaxChunksPerDoc, the subsequent text is discarded.
        self.max_chunks_per_doc = max_chunks_per_doc
        # The rerank model. Valid values:
        # - bge-reranker-v2-m3: provides good performance and supports up to 8,192 tokens for a single inference. Text that exceeds this limit is split into chunks, which may degrade performance. This is the default value.
        # - bge-reranker-v2-minicpm-layerwise: provides better performance than bge-reranker-v2-m3 and supports up to 2,048 tokens for a single inference. Text that exceeds this limit is split into chunks, which may degrade performance.
        self.model = model
        self.owner_id = owner_id
        # The query statement for reranking.
        self.query = query
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to return the document text. If this parameter is set to false, the document text is not returned. Only the indexes and rerank scores of the sorted documents are returned.
        self.return_documents = return_documents
        # The number of most relevant documents to return.
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

        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink

        if self.instruct is not None:
            result['Instruct'] = self.instruct

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
            self.documents_shrink = m.get('Documents')

        if m.get('Instruct') is not None:
            self.instruct = m.get('Instruct')

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

