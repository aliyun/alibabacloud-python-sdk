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
        rerank_model: main_models.QueryKnowledgeBasesContentRequestRerankModel = None,
        source_collection: List[main_models.QueryKnowledgeBasesContentRequestSourceCollection] = None,
        top_k: int = None,
    ):
        # The text content to search for.
        # 
        # This parameter is required.
        self.content = content
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to view the details of all AnalyticDB for PostgreSQL instances in a specific region, including their instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The method for merging results from multiple knowledge bases. The default value is `RRF`. Valid values:
        # 
        # - RRF
        # 
        # - Weight
        self.merge_method = merge_method
        # The arguments for the specified `MergeMethod`.
        self.merge_method_args = merge_method_args
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The reranking factor. If specified, the system reranks the final merged results. Valid values: 1 < RerankFactor <= 5.
        # 
        # > - Sparse document chunking reduces reranking efficiency.
        # >
        # > - We recommend that the number of items to rerank (TopK × Factor, rounded up) does not exceed 50.
        self.rerank_factor = rerank_factor
        # Parameters for the rerank model applied to the final merged results.
        self.rerank_model = rerank_model
        # The source collections to search.
        # 
        # This parameter is required.
        self.source_collection = source_collection
        # The number of top results to return after the results from all recall paths are merged.
        self.top_k = top_k

    def validate(self):
        if self.merge_method_args:
            self.merge_method_args.validate()
        if self.rerank_model:
            self.rerank_model.validate()
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

        if self.rerank_model is not None:
            result['RerankModel'] = self.rerank_model.to_map()

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

        if m.get('RerankModel') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentRequestRerankModel()
            self.rerank_model = temp_model.from_map(m.get('RerankModel'))

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
        # The document collection name.
        # 
        # > To create a document collection, call the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. To view existing document collections, call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation.
        # 
        # This parameter is required.
        self.collection = collection
        # The namespace.
        # 
        # > You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace and call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to view existing namespaces.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # > You specify this value when you call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The query parameters for the source collection.
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
        rerank_model: main_models.QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsRerankModel = None,
        top_k: int = None,
        use_full_text_retrieval: bool = None,
    ):
        # A filter expression for the data to retrieve, formatted as a SQL `WHERE` clause. This is a Boolean expression that evaluates to `true` or `false`. The expression can include simple comparison operators (such as `=`, `<>`, `!=`, `>`, `<`, `>=`, and `<=`), logical operators (`AND`, `OR`, `NOT`), and keywords such as `IN`, `BETWEEN`, and `LIKE`.
        # 
        # > - For syntax details, see [PostgreSQL WHERE](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/).
        self.filter = filter
        # Specifies whether to enable knowledge graph enhancement. The default value is `false`.
        self.graph_enhance = graph_enhance
        # Parameters for the graph search.
        self.graph_search_args = graph_search_args
        # The hybrid search algorithm. If this parameter is not specified, the system directly compares and sorts the scores from dense vector and full-text searches.
        # 
        # Valid values:
        # 
        # - `RRF`: Reciprocal rank fusion. Uses a parameter `k` to control the fusion effect. For more information, see the `HybridSearchArgs` parameter.
        # 
        # - `Weight`: Weighted ranking. Uses parameters to control the score weights from different retrieval paths, such as dense vector and full-text searches, before sorting. For more information, see the `HybridSearchArgs` parameter.
        # 
        # - `Cascaded`: Performs a full-text search first, and then performs a vector search on the results.
        self.hybrid_search = hybrid_search
        # The parameters for the hybrid search algorithm. `RRF` and `Weight` are supported. `HybridPathsSetting` specifies the retrieval paths: dense vectors (`dense`), sparse vectors (`sparse`), and full-text search (`fulltext`). If this parameter is not specified, the default paths are `dense` and `fulltext`.
        # 
        # - `RRF`: Specifies the constant `k` in the scoring formula `1/(k+rank_i)`. `k` must be a positive integer greater than 1. Format:
        # 
        # ```
        # {
        #   "HybridPathsSetting": {
        #     "paths": "dense,fulltext"
        #   },
        #   "RRF": {
        #     "k": 60
        #   }
        # }
        # ```
        # 
        # - `Weight`:
        # 
        #   - Two-path retrieval (the default if you do not specify `HybridPathsSetting`):
        # 
        #     - Scoring formula: `alpha * dense_score + (1-alpha) * fulltext_score`. The `alpha` parameter represents the score weight of dense vectors relative to full-text search. The value must be in the range of [0, 1]. A value of 0 indicates full-text search only, and a value of 1 indicates dense vector search only.
        # 
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```
        # 
        # - Three-path retrieval:
        # 
        #   - Scoring formula: `normalized_dense * dense_score + normalized_sparse * sparse_score + normalized_fulltext * fulltext_score`. The `dense`, `sparse`, and `fulltext` parameters represent the weights for dense vectors, sparse vectors, and full-text search, respectively. The value of each weight must be greater than or equal to 0. The system automatically normalizes the weights to a range of [0, 1] (for example, `normalized_x = x / (dense + sparse + fulltext)`).
        # 
        # ```
        # {
        #   "HybridPathsSetting": {
        #      "paths": "dense,sparse,fulltext"
        #    },
        #   "Weight": {
        #     "dense": 0.5,
        #     "sparse": 0.3,
        #     "fulltext": 0.2
        #   }
        # }
        # ```
        self.hybrid_search_args = hybrid_search_args
        # The distance metric used for building the vector index. Valid values:
        # 
        # - `l2`: Euclidean distance.
        # 
        # - `ip`: Inner product distance.
        # 
        # - `cosine`: Cosine similarity.
        self.metrics = metrics
        # The offset for paged queries.
        self.offset = offset
        # Specifies the field by which to sort the results. By default, this parameter is empty.
        # 
        # The field must be a metadata field or a default field in the table, such as `id`. The following formats are supported:
        # 
        # A single field, such as `chunk_id`. Multiple fields separated by commas, such as `block_id, chunk_id`. Descending order, such as `block_id DESC, chunk_id DESC`.
        self.order_by = order_by
        # The recall window. If specified, adds context from surrounding document chunks to the search results. The format is a two-element array `[A, B]`, where `-10 <= A <= 0` and `0 <= B <= 10`.
        # 
        # > - This parameter is recommended for finely chunked documents where retrieval might otherwise lose context.
        # >
        # > - The system applies reranking before applying the recall window.
        self.recall_window = recall_window
        # The reranking factor. If specified, the system reranks the results from this source collection before they are merged. Valid values: 1 < RerankFactor <= 5.
        # 
        # > - Sparse document chunking reduces reranking efficiency.
        # >
        # > - We recommend that the number of items to rerank (TopK × Factor, rounded up) does not exceed 50.
        self.rerank_factor = rerank_factor
        # Parameters for the rerank model applied to the results from this specific source collection before the final merge.
        self.rerank_model = rerank_model
        # The number of top results to return from this source collection.
        self.top_k = top_k
        # Specifies whether to use full-text search, which enables two-path retrieval. The default value is `false`, which indicates that only vector retrieval is performed.
        self.use_full_text_retrieval = use_full_text_retrieval

    def validate(self):
        if self.graph_search_args:
            self.graph_search_args.validate()
        if self.rerank_model:
            self.rerank_model.validate()

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

        if self.rerank_model is not None:
            result['RerankModel'] = self.rerank_model.to_map()

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

        if m.get('RerankModel') is not None:
            temp_model = main_models.QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsRerankModel()
            self.rerank_model = temp_model.from_map(m.get('RerankModel'))

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')

        return self

class QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsRerankModel(DaraModel):
    def __init__(
        self,
        instruct: str = None,
        name: str = None,
    ):
        # This parameter can be set only when `RerankModel.Name` is `qwen3-rerank`. Use this parameter to provide a custom instruction that guides the model\\"s ranking strategy.
        self.instruct = instruct
        # The name of the rerank model. Valid values: `qwen3-rerank` and `gte-rerank-v2`.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instruct is not None:
            result['Instruct'] = self.instruct

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instruct') is not None:
            self.instruct = m.get('Instruct')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsGraphSearchArgs(DaraModel):
    def __init__(
        self,
        graph_top_k: int = None,
    ):
        # The number of top entities and relationship edges to return. The default value is 60.
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

class QueryKnowledgeBasesContentRequestRerankModel(DaraModel):
    def __init__(
        self,
        instruct: str = None,
        name: str = None,
    ):
        # This parameter can be set only when `RerankModel.Name` is `qwen3-rerank`. Use this parameter to provide a custom instruction that guides the model\\"s ranking strategy.
        self.instruct = instruct
        # The name of the rerank model. Valid values: `qwen3-rerank` and `gte-rerank-v2`.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instruct is not None:
            result['Instruct'] = self.instruct

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instruct') is not None:
            self.instruct = m.get('Instruct')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class QueryKnowledgeBasesContentRequestMergeMethodArgs(DaraModel):
    def __init__(
        self,
        rrf: main_models.QueryKnowledgeBasesContentRequestMergeMethodArgsRrf = None,
        weight: main_models.QueryKnowledgeBasesContentRequestMergeMethodArgsWeight = None,
    ):
        # The parameters that you can configure when `MergeMethod` is set to `RRF`.
        self.rrf = rrf
        # The parameters that you can configure when `MergeMethod` is set to `Weight`.
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
        # An array of weights for each source collection.
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
        # The constant `k` in the scoring formula `1/(k+rank_i)`. It must be a positive integer greater than 1.
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

