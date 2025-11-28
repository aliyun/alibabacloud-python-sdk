# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryKnowledgeBasesContentShrinkRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        dbinstance_id: str = None,
        merge_method: str = None,
        merge_method_args_shrink: str = None,
        owner_id: int = None,
        region_id: str = None,
        rerank_factor: float = None,
        source_collection_shrink: str = None,
        top_k: int = None,
    ):
        # The text content for retrieval.
        # 
        # This parameter is required.
        self.content = content
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The method used to merge multiple knowledge bases. Default value: RRF. Valid values:
        # 
        # *   RRF
        # *   Weight
        self.merge_method = merge_method
        # The parameters of the merge method for each SourceCollection.
        self.merge_method_args_shrink = merge_method_args_shrink
        self.owner_id = owner_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The rerank factor. If you specify this parameter, the vector retrieval results are reranked once more. Valid values: 1\\<RerankFactor<=5.
        # 
        # > 
        # 
        # *   If the document is segmented into sparse parts, reranking is inefficient.
        # 
        # *   We recommend that the number of reranked results (the ceiling of TopK × RerankFactor) not exceed 50.
        self.rerank_factor = rerank_factor
        # The information about collections to retrieve from.
        # 
        # This parameter is required.
        self.source_collection_shrink = source_collection_shrink
        # Set the number of top results to be returned after merging results from multiple path retrieval.
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.merge_method is not None:
            result['MergeMethod'] = self.merge_method

        if self.merge_method_args_shrink is not None:
            result['MergeMethodArgs'] = self.merge_method_args_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rerank_factor is not None:
            result['RerankFactor'] = self.rerank_factor

        if self.source_collection_shrink is not None:
            result['SourceCollection'] = self.source_collection_shrink

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('MergeMethod') is not None:
            self.merge_method = m.get('MergeMethod')

        if m.get('MergeMethodArgs') is not None:
            self.merge_method_args_shrink = m.get('MergeMethodArgs')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        if m.get('SourceCollection') is not None:
            self.source_collection_shrink = m.get('SourceCollection')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

