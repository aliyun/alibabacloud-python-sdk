# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class QueryKnowledgeBasesContentRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        dbinstance_id: str = None,
        merge_method: str = None,
        merge_method_args: main_models.QueryKnowledgeBasesContentRequestMergeMethodArgs = None,
        owner_id: int = None,
        region_id: str = None,
        rerank_factor: float = None,
        source_collection: List[main_models.QueryKnowledgeBasesContentRequestSourceCollection] = None,
        top_k: int = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.merge_method = merge_method
        self.merge_method_args = merge_method_args
        self.owner_id = owner_id
        # This parameter is required.
        self.region_id = region_id
        self.rerank_factor = rerank_factor
        # This parameter is required.
        self.source_collection = source_collection
        self.top_k = top_k

    def validate(self):
        if self.merge_method_args:
            self.merge_method_args.validate()
        if self.source_collection:
            for v1 in self.source_collection:
                 if v1:
                    v1.validate()

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

        if self.merge_method_args is not None:
            result['MergeMethodArgs'] = self.merge_method_args.to_map()

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rerank_factor is not None:
            result['RerankFactor'] = self.rerank_factor

        result['SourceCollection'] = []
        if self.source_collection is not None:
            for k1 in self.source_collection:
                result['SourceCollection'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.QueryKnowledgeBasesContentRequestMergeMethodArgs()
            self.merge_method_args = temp_model.from_map(m.get('MergeMethodArgs'))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        self.source_collection = []
        if m.get('SourceCollection') is not None:
            for k1 in m.get('SourceCollection'):
                temp_model = main_models.QueryKnowledgeBasesContentRequestSourceCollection()
                self.source_collection.append(temp_model.from_map(k1))

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

class QueryKnowledgeBasesContentRequestSourceCollection(DaraModel):
    def __init__(
        self,
        collection: str = None,
        namespace: str = None,
        namespace_password: str = None,
        query_params: main_models.QueryKnowledgeBasesContentRequestSourceCollectionQueryParams = None,
    ):
        # This parameter is required.
        self.collection = collection
        self.namespace = namespace
        # This parameter is required.
        self.namespace_password = namespace_password
        self.query_params = query_params

    def validate(self):
        if self.query_params:
            self.query_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.query_params is not None:
            result['QueryParams'] = self.query_params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('QueryParams') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentRequestSourceCollectionQueryParams()
            self.query_params = temp_model.from_map(m.get('QueryParams'))

        return self

class QueryKnowledgeBasesContentRequestSourceCollectionQueryParams(DaraModel):
    def __init__(
        self,
        filter: str = None,
        graph_enhance: bool = None,
        graph_search_args: main_models.QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsGraphSearchArgs = None,
        hybrid_search: str = None,
        hybrid_search_args: Dict[str, Any] = None,
        metrics: str = None,
        offset: int = None,
        order_by: str = None,
        recall_window: List[int] = None,
        rerank_factor: float = None,
        top_k: int = None,
        use_full_text_retrieval: bool = None,
    ):
        self.filter = filter
        self.graph_enhance = graph_enhance
        self.graph_search_args = graph_search_args
        self.hybrid_search = hybrid_search
        self.hybrid_search_args = hybrid_search_args
        self.metrics = metrics
        self.offset = offset
        self.order_by = order_by
        self.recall_window = recall_window
        self.rerank_factor = rerank_factor
        self.top_k = top_k
        self.use_full_text_retrieval = use_full_text_retrieval

    def validate(self):
        if self.graph_search_args:
            self.graph_search_args.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.graph_enhance is not None:
            result['GraphEnhance'] = self.graph_enhance

        if self.graph_search_args is not None:
            result['GraphSearchArgs'] = self.graph_search_args.to_map()

        if self.hybrid_search is not None:
            result['HybridSearch'] = self.hybrid_search

        if self.hybrid_search_args is not None:
            result['HybridSearchArgs'] = self.hybrid_search_args

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.recall_window is not None:
            result['RecallWindow'] = self.recall_window

        if self.rerank_factor is not None:
            result['RerankFactor'] = self.rerank_factor

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.use_full_text_retrieval is not None:
            result['UseFullTextRetrieval'] = self.use_full_text_retrieval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('GraphEnhance') is not None:
            self.graph_enhance = m.get('GraphEnhance')

        if m.get('GraphSearchArgs') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsGraphSearchArgs()
            self.graph_search_args = temp_model.from_map(m.get('GraphSearchArgs'))

        if m.get('HybridSearch') is not None:
            self.hybrid_search = m.get('HybridSearch')

        if m.get('HybridSearchArgs') is not None:
            self.hybrid_search_args = m.get('HybridSearchArgs')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RecallWindow') is not None:
            self.recall_window = m.get('RecallWindow')

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')

        return self

class QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsGraphSearchArgs(DaraModel):
    def __init__(
        self,
        graph_top_k: int = None,
    ):
        self.graph_top_k = graph_top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_top_k is not None:
            result['GraphTopK'] = self.graph_top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GraphTopK') is not None:
            self.graph_top_k = m.get('GraphTopK')

        return self

class QueryKnowledgeBasesContentRequestMergeMethodArgs(DaraModel):
    def __init__(
        self,
        rrf: main_models.QueryKnowledgeBasesContentRequestMergeMethodArgsRrf = None,
        weight: main_models.QueryKnowledgeBasesContentRequestMergeMethodArgsWeight = None,
    ):
        self.rrf = rrf
        self.weight = weight

    def validate(self):
        if self.rrf:
            self.rrf.validate()
        if self.weight:
            self.weight.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rrf is not None:
            result['Rrf'] = self.rrf.to_map()

        if self.weight is not None:
            result['Weight'] = self.weight.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rrf') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentRequestMergeMethodArgsRrf()
            self.rrf = temp_model.from_map(m.get('Rrf'))

        if m.get('Weight') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentRequestMergeMethodArgsWeight()
            self.weight = temp_model.from_map(m.get('Weight'))

        return self

class QueryKnowledgeBasesContentRequestMergeMethodArgsWeight(DaraModel):
    def __init__(
        self,
        weights: List[float] = None,
    ):
        self.weights = weights

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.weights is not None:
            result['Weights'] = self.weights

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Weights') is not None:
            self.weights = m.get('Weights')

        return self

class QueryKnowledgeBasesContentRequestMergeMethodArgsRrf(DaraModel):
    def __init__(
        self,
        k: int = None,
    ):
        self.k = k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.k is not None:
            result['K'] = self.k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K') is not None:
            self.k = m.get('K')

        return self

