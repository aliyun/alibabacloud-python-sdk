# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ChatWithKnowledgeBaseStreamRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        include_knowledge_base_results: bool = None,
        knowledge_params: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParams = None,
        model_params: main_models.ChatWithKnowledgeBaseStreamRequestModelParams = None,
        owner_id: int = None,
        prompt_params: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to return recall results. Default value: false.
        self.include_knowledge_base_results = include_knowledge_base_results
        # The knowledge retrieval parameter object. If this parameter is not specified, only chat is performed.
        self.knowledge_params = knowledge_params
        # The large language model (LLM) invocation parameter object.
        # 
        # This parameter is required.
        self.model_params = model_params
        self.owner_id = owner_id
        # The system prompt template. The template must include {{ text_chunks }}, {{ user_system_prompt }}, {{ graph_entities }}, and {{ graph_relations }}. If not specified, this part does not take effect.
        self.prompt_params = prompt_params
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.knowledge_params:
            self.knowledge_params.validate()
        if self.model_params:
            self.model_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.include_knowledge_base_results is not None:
            result['IncludeKnowledgeBaseResults'] = self.include_knowledge_base_results

        if self.knowledge_params is not None:
            result['KnowledgeParams'] = self.knowledge_params.to_map()

        if self.model_params is not None:
            result['ModelParams'] = self.model_params.to_map()

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prompt_params is not None:
            result['PromptParams'] = self.prompt_params

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IncludeKnowledgeBaseResults') is not None:
            self.include_knowledge_base_results = m.get('IncludeKnowledgeBaseResults')

        if m.get('KnowledgeParams') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParams()
            self.knowledge_params = temp_model.from_map(m.get('KnowledgeParams'))

        if m.get('ModelParams') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestModelParams()
            self.model_params = temp_model.from_map(m.get('ModelParams'))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PromptParams') is not None:
            self.prompt_params = m.get('PromptParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ChatWithKnowledgeBaseStreamRequestModelParams(DaraModel):
    def __init__(
        self,
        max_tokens: int = None,
        messages: List[main_models.ChatWithKnowledgeBaseStreamRequestModelParamsMessages] = None,
        model: str = None,
        n: int = None,
        presence_penalty: float = None,
        seed: int = None,
        stop: List[str] = None,
        temperature: float = None,
        tools: List[main_models.ChatWithKnowledgeBaseStreamRequestModelParamsTools] = None,
        top_p: float = None,
    ):
        # The maximum number of tokens to generate.
        self.max_tokens = max_tokens
        # The message list.
        # 
        # This parameter is required.
        self.messages = messages
        # The name of the large language model to use. For valid values, see [Model Studio documentation](https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope#eadfc13038jd5).
        # 
        # This parameter is required.
        self.model = model
        # The number of candidate responses to generate.
        self.n = n
        # The presence penalty coefficient. Valid values: -2.0 to 2.0.
        self.presence_penalty = presence_penalty
        # The random seed.
        self.seed = seed
        # The list of stop words.
        self.stop = stop
        # The sampling temperature. Valid values: 0 to 2.
        self.temperature = temperature
        # The tool list.
        self.tools = tools
        # The nucleus sampling probability threshold. Valid values: 0 to 1.
        self.top_p = top_p

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.model is not None:
            result['Model'] = self.model

        if self.n is not None:
            result['N'] = self.n

        if self.presence_penalty is not None:
            result['PresencePenalty'] = self.presence_penalty

        if self.seed is not None:
            result['Seed'] = self.seed

        if self.stop is not None:
            result['Stop'] = self.stop

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        result['Tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['Tools'].append(k1.to_map() if k1 else None)

        if self.top_p is not None:
            result['TopP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.ChatWithKnowledgeBaseStreamRequestModelParamsMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('N') is not None:
            self.n = m.get('N')

        if m.get('PresencePenalty') is not None:
            self.presence_penalty = m.get('PresencePenalty')

        if m.get('Seed') is not None:
            self.seed = m.get('Seed')

        if m.get('Stop') is not None:
            self.stop = m.get('Stop')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.ChatWithKnowledgeBaseStreamRequestModelParamsTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        return self

class ChatWithKnowledgeBaseStreamRequestModelParamsTools(DaraModel):
    def __init__(
        self,
        function: main_models.ChatWithKnowledgeBaseStreamRequestModelParamsToolsFunction = None,
    ):
        # The function information.
        self.function = function

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestModelParamsToolsFunction()
            self.function = temp_model.from_map(m.get('Function'))

        return self

class ChatWithKnowledgeBaseStreamRequestModelParamsToolsFunction(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: Any = None,
    ):
        # The description of the function tool.
        self.description = description
        # The name of the function tool.
        self.name = name
        # The JSON Schema of the function parameters.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

class ChatWithKnowledgeBaseStreamRequestModelParamsMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # The message content.
        # 
        # This parameter is required.
        self.content = content
        # The message role. Valid values:
        # 
        # - system
        # - user
        # - assistant.
        # 
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

class ChatWithKnowledgeBaseStreamRequestKnowledgeParams(DaraModel):
    def __init__(
        self,
        merge_method: str = None,
        merge_method_args: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgs = None,
        rerank_factor: float = None,
        rerank_model: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsRerankModel = None,
        source_collection: List[main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollection] = None,
        top_k: int = None,
    ):
        # The method for merging results from multiple knowledge bases. Default value: RRF. Valid values:
        # - RRF
        # - Weight.
        self.merge_method = merge_method
        # The parameters for merging results from multiple knowledge bases.
        self.merge_method_args = merge_method_args
        # The reranking factor. If this value is not empty, the AISearch retrieve results are reranked. Valid values: 1 < RerankFactor <= 5.
        # > - Reranking is slow when document chunks are sparse.
        # > - The recommended number of reranked items (TopK × Factor, rounded up) should not exceed 50.
        self.rerank_factor = rerank_factor
        # The reranking model parameters for performing an additional reranking on the merged results from multiple retrieval paths.
        self.rerank_model = rerank_model
        # The knowledge base.
        # 
        # This parameter is required.
        self.source_collection = source_collection
        # The number of top results to return after merging recall results from multiple vector collections.
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
        if self.merge_method is not None:
            result['MergeMethod'] = self.merge_method

        if self.merge_method_args is not None:
            result['MergeMethodArgs'] = self.merge_method_args.to_map()

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
        if m.get('MergeMethod') is not None:
            self.merge_method = m.get('MergeMethod')

        if m.get('MergeMethodArgs') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgs()
            self.merge_method_args = temp_model.from_map(m.get('MergeMethodArgs'))

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        if m.get('RerankModel') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsRerankModel()
            self.rerank_model = temp_model.from_map(m.get('RerankModel'))

        self.source_collection = []
        if m.get('SourceCollection') is not None:
            for k1 in m.get('SourceCollection'):
                temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollection()
                self.source_collection.append(temp_model.from_map(k1))

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollection(DaraModel):
    def __init__(
        self,
        collection: str = None,
        namespace: str = None,
        namespace_password: str = None,
        query_params: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParams = None,
    ):
        # The name of the collection to recall.
        # 
        # This parameter is required.
        self.collection = collection
        # The namespace.
        # 
        # > You can call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to query the list.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # > This value is specified in the CreateNamespace operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The parameters related to retrieval from this knowledge base.
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
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParams()
            self.query_params = temp_model.from_map(m.get('QueryParams'))

        return self

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParams(DaraModel):
    def __init__(
        self,
        filter: str = None,
        graph_enhance: bool = None,
        graph_search_args: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParamsGraphSearchArgs = None,
        hybrid_search: str = None,
        hybrid_search_args: Dict[str, Any] = None,
        metrics: str = None,
        recall_window: List[int] = None,
        rerank_factor: float = None,
        rerank_model: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParamsRerankModel = None,
        top_k: int = None,
        use_full_text_retrieval: bool = None,
    ):
        # The filter condition for the data to update, in SQL WHERE clause format.
        self.filter = filter
        # Specifies whether to enable knowledge graph enhancement. Default value: false.
        self.graph_enhance = graph_enhance
        # The knowledge graph retrieval parameters.
        self.graph_search_args = graph_search_args
        # The multi-channel recall algorithm. Default value: empty (AISearch and full-text index scores are directly compared and sorted).
        # 
        # Valid values:
        # 
        # - RRF: Reciprocal rank fusion. A parameter k controls the fusion effect. For more information, see HybridSearchArgs.
        # - Weight: Weighted reranking. A parameter alpha controls the score weight between AISearch and full-text index results, then performs reranking. For more information, see HybridSearchArgs.
        # - Cascaded: Full-text index retrieve is performed first, followed by AISearch retrieve on the full-text index results.
        self.hybrid_search = hybrid_search
        # The algorithm parameters for multi-channel recall. RRF and Weight are supported:
        # 
        # - RRF: The k constant in the score calculation formula `1/(k+rank_i)`. The value must be a positive integer greater than 1. Format:
        # ```
        # { 
        #    "RRF": {
        #     "k": 60
        #    }
        # }
        # ```
        # 
        # - Weight: The calculation formula is `alpha * vector_score + (1-alpha) * text_score`. The parameter alpha specifies the score weight between vector and full-text retrieval. Valid values: 0 to 1, where 0 indicates full-text only and 1 indicates vector only:
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```.
        self.hybrid_search_args = hybrid_search_args
        # The method used to build the vector index. Valid values:
        # - l2: Euclidean distance.
        # - ip: inner product distance.
        # - cosine: cosine similarity.
        self.metrics = metrics
        # The recall window. If this value is not empty, additional context is returned for retrieval results. The format is a two-element array: List<A, B>, where -10 <= A <= 0 and 0 <= B <= 10.
        # > - Use this parameter when documents are segmented too finely and retrieval may lose contextual information.
        # > - Reranking takes priority over windowing. Reranking is performed first, followed by windowing.
        self.recall_window = recall_window
        # The reranking factor. If this value is not empty, the AISearch retrieve results are reranked. Valid values: 1 < RerankFactor <= 5.
        # > - Reranking is slow when document chunks are sparse.
        # > - The recommended number of reranked items (TopK × Factor, rounded up) should not exceed 50.
        self.rerank_factor = rerank_factor
        # The reranking model parameters.
        self.rerank_model = rerank_model
        # The number of top results to return.
        self.top_k = top_k
        # Specifies whether to use full-text index (multi-channel recall). Default value: false. Only AISearch retrieve is used.
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
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParamsGraphSearchArgs()
            self.graph_search_args = temp_model.from_map(m.get('GraphSearchArgs'))

        if m.get('HybridSearch') is not None:
            self.hybrid_search = m.get('HybridSearch')

        if m.get('HybridSearchArgs') is not None:
            self.hybrid_search_args = m.get('HybridSearchArgs')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('RecallWindow') is not None:
            self.recall_window = m.get('RecallWindow')

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        if m.get('RerankModel') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParamsRerankModel()
            self.rerank_model = temp_model.from_map(m.get('RerankModel'))

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')

        return self

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParamsRerankModel(DaraModel):
    def __init__(
        self,
        instruct: str = None,
        name: str = None,
        rerank_metadata_fields: str = None,
    ):
        # This parameter can be set when RerankModel.Name is set to qwen3-rerank. Specifies a custom ranking task type description to guide the model to adopt different ranking strategies.
        self.instruct = instruct
        # The reranking model name. Valid values: qwen3-rerank, gte-rerank-v2.
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

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsSourceCollectionQueryParamsGraphSearchArgs(DaraModel):
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

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsRerankModel(DaraModel):
    def __init__(
        self,
        instruct: str = None,
        name: str = None,
    ):
        # This parameter can be set when RerankModel.Name is set to qwen3-rerank. Specifies a custom ranking task type description to guide the model to adopt different ranking strategies.
        self.instruct = instruct
        # The reranking model name. Valid values: qwen3-rerank, gte-rerank-v2.
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

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgs(DaraModel):
    def __init__(
        self,
        rrf: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgsRrf = None,
        weight: main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgsWeight = None,
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
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgsRrf()
            self.rrf = temp_model.from_map(m.get('Rrf'))

        if m.get('Weight') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgsWeight()
            self.weight = temp_model.from_map(m.get('Weight'))

        return self

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgsWeight(DaraModel):
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

class ChatWithKnowledgeBaseStreamRequestKnowledgeParamsMergeMethodArgsRrf(DaraModel):
    def __init__(
        self,
        k: int = None,
    ):
        # The k constant in the score calculation formula `1/(k+rank_i)`. The value must be a positive integer greater than 1.
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

