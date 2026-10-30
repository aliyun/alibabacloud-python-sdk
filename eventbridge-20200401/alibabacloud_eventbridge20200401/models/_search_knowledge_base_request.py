# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        knowledge_base_name: str = None,
        metadata_filter: str = None,
        mode: str = None,
        namespace: str = None,
        query: str = None,
        rank_algorithm: str = None,
        rerank: bool = None,
        rerank_model: str = None,
        rrf_k: int = None,
        top_k: int = None,
        vector_weight: float = None,
    ):
        # The data catalog to which the knowledge base belongs. This parameter, together with Namespace and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListCatalogs to obtain the value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The name of the knowledge base. The name must be unique within the namespace. The name is specified upon creation and cannot be modified.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # Filters search results by document metadata. The value is a JSON expression tree. Nodes are divided into two types: logical nodes and leaf conditions. Logical nodes include {"AndAll": [child nodes...]} (all conditions met), {"OrAll": [child nodes...]} (any condition met), and {"NotAll": [child nodes...]} (no conditions met). Arbitrary nesting is supported. Leaf conditions are in the format of {"Key": field name, "Operator": operator, "Value": value}. For the In and NotIn operators, use "Values": [values...]. Valid values for Operator: Equals, NotEquals, In, NotIn, GreaterThan, GreaterThanOrEqual, LessThan, and LessThanOrEqual (the last four range operators apply only to LONG, DOUBLE, and DATETIME fields), StartsWith, and StringContains (applies only to STRING fields). The field must be declared in the knowledge base schema. The nesting depth cannot exceed 5, and the total number of leaf conditions cannot exceed 20. Valid formats for DATETIME field values: ISO-8601 with time zone, yyyy-MM-dd HH:mm:ss, or yyyy-MM-dd.
        self.metadata_filter = metadata_filter
        # The retrieve mode. Valid values:
        # - KEYWORD: keyword retrieve.
        # - VECTOR: AISearch.
        # - HYBRID: hybrid retrieve.
        self.mode = mode
        # The namespace to which the knowledge base belongs. The namespace must belong to the specified data catalog. This parameter, together with Catalog and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListNamespaces to obtain the value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The retrieve text. Both keyword retrieve and AISearch are based on this text.
        # 
        # This parameter is required.
        self.query = query
        # Optional. Overrides the fusion algorithm configured for the knowledge base in this request. This parameter takes effect only in HYBRID search mode. Valid values: RRF for reciprocal rank fusion, and WEIGHTED for weighted normalization fusion (used with VectorWeight). If you set this parameter to WEIGHTED in KEYWORD or VECTOR single mode, the InvalidParameter error is returned.
        self.rank_algorithm = rank_algorithm
        # Specifies whether to enable reranking for search results. Default value: false.
        self.rerank = rerank
        # Optional. Overrides the reranking model configured for the knowledge base in this request. This parameter takes effect when reranking is enabled across all search modes. Valid values: qwen3-rerank, gte-rerank-v2, and qwen3-vl-rerank. If this parameter is not specified, the value configured for the knowledge base is used. If no value is configured, the default value is qwen3-rerank. Score distributions of different models cannot be compared horizontally. We recommend that you use a fixed model for each knowledge base.
        self.rerank_model = rerank_model
        # Optional. Overrides the RRF fusion parameter k configured for the knowledge base in this request. This parameter takes effect only in HYBRID search mode and must be greater than 0.
        self.rrf_k = rrf_k
        # The number of most relevant results to return. Default value: 10. Maximum value: 100.
        self.top_k = top_k
        # Optional. The vector path weight for the WEIGHTED fusion algorithm. Valid values: 0 to 1. The keyword path weight is 1 minus this value. If this parameter is not specified, the value configured for the knowledge base is used. If no value is configured, the default value is 0.7.
        self.vector_weight = vector_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.metadata_filter is not None:
            result['MetadataFilter'] = self.metadata_filter

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.query is not None:
            result['Query'] = self.query

        if self.rank_algorithm is not None:
            result['RankAlgorithm'] = self.rank_algorithm

        if self.rerank is not None:
            result['Rerank'] = self.rerank

        if self.rerank_model is not None:
            result['RerankModel'] = self.rerank_model

        if self.rrf_k is not None:
            result['RrfK'] = self.rrf_k

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.vector_weight is not None:
            result['VectorWeight'] = self.vector_weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('MetadataFilter') is not None:
            self.metadata_filter = m.get('MetadataFilter')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RankAlgorithm') is not None:
            self.rank_algorithm = m.get('RankAlgorithm')

        if m.get('Rerank') is not None:
            self.rerank = m.get('Rerank')

        if m.get('RerankModel') is not None:
            self.rerank_model = m.get('RerankModel')

        if m.get('RrfK') is not None:
            self.rrf_k = m.get('RrfK')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('VectorWeight') is not None:
            self.vector_weight = m.get('VectorWeight')

        return self

