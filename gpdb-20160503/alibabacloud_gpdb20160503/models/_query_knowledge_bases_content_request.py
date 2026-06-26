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
        # The text content used for retrieval.
        # 
        # This parameter is required.
        self.content = content
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The method used to merge results from multiple knowledge bases. Default value: RRF. Valid values:
        # - RRF
        # - Weight.
        self.merge_method = merge_method
        # The parameters for the merge method of each SourceCollection.
        self.merge_method_args = merge_method_args
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The reranking factor. If this parameter is not empty, the vector retrieval results are reranked. Valid values: 1 < RerankFactor <= 5.
        # > - Reranking is slow when document chunks are sparse.
        # > - The recommended reranking count (TopK × Factor, rounded up) should not exceed 50.
        self.rerank_factor = rerank_factor
        # The reranking model parameters for performing an additional reranking on the overall results after multi-channel merging.
        self.rerank_model = rerank_model
        # The information about the multiple collections to retrieve.
        # 
        # This parameter is required.
        self.source_collection = source_collection
        # The number of top results to return after multi-channel recall merging.
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
        # The name of the document collection.
        # 
        # > The document collection is created by calling the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. You can call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to view existing document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The namespace.
        # 
        # > You can create a namespace by calling the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation and view the list by calling the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # > This value is specified by the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The filter conditions for the data to query, in SQL WHERE clause format.
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
        # The filter conditions for the data to query, in SQL WHERE clause format. This is an expression that returns a Boolean value (true or false). The conditions can be simple comparison operators such as equal to (=), not equal to (<> or !=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=). They can also be more complex expressions combined with logical operators (AND, OR, NOT), as well as conditions that use keywords such as IN, BETWEEN, and LIKE.
        # 
        # > 
        # > - For detailed syntax, refer to: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/.
        self.filter = filter
        # Specifies whether to enable knowledge graph enhancement. Default value: false.
        self.graph_enhance = graph_enhance
        # The number of top entities and relationship edges to return. Default value: 60.
        self.graph_search_args = graph_search_args
        # The multi-channel recall algorithm. Default value: empty (the scores from dense vectors and full-text retrieval are directly compared and sorted).
        # 
        # Valid values:
        # 
        # - RRF: reciprocal rank fusion. A parameter k controls the fusion effect. For more information, see the HybridSearchArgs configuration.
        # - Weight: weighted ranking. Parameters control the score weights of vector retrieval and full-text retrieval before sorting. For more information, see the HybridSearchArgs configuration.
        # - Cascaded: full-text retrieval is performed first, followed by vector retrieval on the full-text results.
        self.hybrid_search = hybrid_search
        # The algorithm parameters for multi-channel recall. RRF and Weight are supported. HybridPathsSetting specifies the recall paths: dense vectors (dense), sparse vectors (sparse), and full-text retrieval (fulltext). If this value is empty, dense vectors (dense) and full-text retrieval (fulltext) are used by default.
        # 
        # - RRF: specifies the k constant in the scoring algorithm `1/(k+rank_i)`. The value must be a positive integer greater than 1. Format:
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
        # - Weight: 
        #    - Dual-path recall (without specifying HybridPathsSetting, only specifying alpha):
        #       - Formula: alpha * dense_score + (1-alpha) * fulltext_score. The alpha parameter specifies the score weight between dense vectors and full-text retrieval. Valid values: 0 to 1, where 0 indicates full-text retrieval only and 1 indicates dense vectors only:
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```
        #   - Three-path recall pattern:
        #      - Formula: normalized_dense * dense_score + normalized_sparse * sparse_score + normalized_fulltext * fulltext_score. dense, sparse, and fulltext represent the weights for dense vectors, sparse vectors, and full-text retrieval respectively. Valid values: greater than or equal to 0. The system automatically performs normalization on the weights to 0 to 1 (normalized_x = x / (dense + sparse + fulltext)).
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
        # The method used to build the vector index. Valid values:
        # - l2: Euclidean distance.
        # - ip: inner product distance.
        # - cosine: cosine similarity.
        self.metrics = metrics
        # The offset for paging query.
        self.offset = offset
        # The field used for sorting. Default value: empty.
        # 
        # The field must belong to metadata or a default field in the table, such as id. Supported formats:
        # 
        # A single field, such as chunk_id.
        # Multiple fields separated by commas, such as block_id, chunk_id.
        # Descending order is supported, such as block_id DESC, chunk_id DESC.
        self.order_by = order_by
        # The recall window. If this value is not empty, the context of the retrieval results is included. The format is a two-element array: List<A, B>, where -10 <= A <= 0 and 0 <= B <= 10.
        # > - Use this parameter when document chunks are too small and retrieval may lose context information.
        # > - Reranking takes priority over windowing. Reranking is performed first, followed by windowing.
        self.recall_window = recall_window
        # The reranking factor. If this parameter is not empty, the vector retrieval results are reranked. Valid values: 1 < RerankFactor <= 5.
        # > - Reranking is slow when document chunks are sparse.
        # > - The recommended reranking count (TopK × Factor, rounded up) should not exceed 50.
        self.rerank_factor = rerank_factor
        # The reranking model parameters.
        self.rerank_model = rerank_model
        # The number of top results to return.
        self.top_k = top_k
        # Specifies whether to use full-text retrieval (dual-path recall). Default value: false, which indicates that only vector retrieval is used.
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
        rerank_metadata_fields: str = None,
    ):
        # This parameter can be set when RerankModel.Name is set to qwen3-rerank. Specifies a custom ranking task type description that guides the model to adopt different ranking strategies.
        self.instruct = instruct
        # The name of the reranking model. Valid values: qwen3-rerank, gte-rerank-v2.
        self.name = name
        self.rerank_metadata_fields = rerank_metadata_fields

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

        if self.rerank_metadata_fields is not None:
            result['RerankMetadataFields'] = self.rerank_metadata_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instruct') is not None:
            self.instruct = m.get('Instruct')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RerankMetadataFields') is not None:
            self.rerank_metadata_fields = m.get('RerankMetadataFields')

        return self

class QueryKnowledgeBasesContentRequestSourceCollectionQueryParamsGraphSearchArgs(DaraModel):
    def __init__(
        self,
        graph_top_k: int = None,
    ):
        # The number of top entities and relationship edges to return. Default value: 60.
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
        # This parameter can be set when RerankModel.Name is set to qwen3-rerank. Specifies a custom ranking task type description that guides the model to adopt different ranking strategies.
        self.instruct = instruct
        # The name of the reranking model. Valid values: qwen3-rerank, gte-rerank-v2.
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
        # The configurable parameters when MergeMethod is set to RRF.
        self.rrf = rrf
        # The configurable parameters when MergeMethod is set to Weight.
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
        # The weight array for each SourceCollection.
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
        # The k constant in the scoring algorithm `1/(k+rank_i)`. The value must be a positive integer greater than 1.
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

