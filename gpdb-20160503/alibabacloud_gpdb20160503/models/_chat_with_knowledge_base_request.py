# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ChatWithKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        include_knowledge_base_results: bool = None,
        knowledge_params: main_models.ChatWithKnowledgeBaseRequestKnowledgeParams = None,
        model_params: main_models.ChatWithKnowledgeBaseRequestModelParams = None,
        owner_id: int = None,
        prompt_params: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Whether to return the retrieved result. Default value: false.
        self.include_knowledge_base_results = include_knowledge_base_results
        # The knowledge retrieval parameter object. If you do not specify this parameter, only chat mode is enabled.
        self.knowledge_params = knowledge_params
        # The Large Language Model (LLM) invocation parameter object.
        # 
        # This parameter is required.
        self.model_params = model_params
        self.owner_id = owner_id
        # The system prompt template, which should include {{ text_chunks }},{{ user_system_prompt }},{{ graph_entities },{{ graph_relations }}. If any of these placeholders are not specified, the corresponding section should have no effect.
        self.prompt_params = prompt_params
        # 实例所在的地域ID
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
            temp_model = main_models.ChatWithKnowledgeBaseRequestKnowledgeParams()
            self.knowledge_params = temp_model.from_map(m.get('KnowledgeParams'))

        if m.get('ModelParams') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseRequestModelParams()
            self.model_params = temp_model.from_map(m.get('ModelParams'))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PromptParams') is not None:
            self.prompt_params = m.get('PromptParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ChatWithKnowledgeBaseRequestModelParams(DaraModel):
    def __init__(
        self,
        max_tokens: int = None,
        messages: List[main_models.ChatWithKnowledgeBaseRequestModelParamsMessages] = None,
        model: str = None,
        n: int = None,
        presence_penalty: float = None,
        seed: int = None,
        stop: List[str] = None,
        temperature: float = None,
        tools: List[main_models.ChatWithKnowledgeBaseRequestModelParamsTools] = None,
        top_p: float = None,
    ):
        # Maximum number of tokens to generate.
        self.max_tokens = max_tokens
        # Message list.
        # 
        # This parameter is required.
        self.messages = messages
        # The model name. See [Model Studio Document](https://help.aliyun.com/zh/model-studio/compatibility-of-openai-with-dashscope?spm=a2c4g.11186623.help-menu-2400256.d_2_10_0.45b5516eZIciC8\\&scm=20140722.H_2833609._.OR_help-T_cn~zh-V_1#eadfc13038jd5) for the available models.
        # 
        # This parameter is required.
        self.model = model
        # The number of candidate responses to generate.
        self.n = n
        # Presence penalty coefficient (-2.0 to 2.0).
        self.presence_penalty = presence_penalty
        # The random seed.
        self.seed = seed
        # Stop words.
        self.stop = stop
        # Sampling temperature (0~2).
        self.temperature = temperature
        # Tools
        self.tools = tools
        # Top-p (nucleus) sampling threshold (0–1).
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
                temp_model = main_models.ChatWithKnowledgeBaseRequestModelParamsMessages()
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
                temp_model = main_models.ChatWithKnowledgeBaseRequestModelParamsTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        return self

class ChatWithKnowledgeBaseRequestModelParamsTools(DaraModel):
    def __init__(
        self,
        function: main_models.ChatWithKnowledgeBaseRequestModelParamsToolsFunction = None,
    ):
        # The information about a function.
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
            temp_model = main_models.ChatWithKnowledgeBaseRequestModelParamsToolsFunction()
            self.function = temp_model.from_map(m.get('Function'))

        return self

class ChatWithKnowledgeBaseRequestModelParamsToolsFunction(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: Any = None,
    ):
        # The description of the function.
        self.description = description
        # The name of the function.
        self.name = name
        # JSON Schema for function parameters.
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

class ChatWithKnowledgeBaseRequestModelParamsMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # The message content.
        self.content = content
        # The message role. Valid values:
        # 
        # *   system
        # *   user
        # *   assistant
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

class ChatWithKnowledgeBaseRequestKnowledgeParams(DaraModel):
    def __init__(
        self,
        merge_method: str = None,
        merge_method_args: main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgs = None,
        rerank_factor: float = None,
        source_collection: List[main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollection] = None,
        top_k: int = None,
    ):
        # The method used to merge multiple knowledge bases. Default value: RRF. Optional:
        # 
        # *   RRF
        # *   Weight
        self.merge_method = merge_method
        # Parameters for multi-knowledge-base fusion.
        self.merge_method_args = merge_method_args
        # The rerank factor. If you specify this parameter, the search result is reranked once again. Valid values: 1\\<RerankFactor<=5.
        # 
        # > 
        # 
        # *   If the document is segmented into sparse parts, reranking is inefficient.
        # 
        # *   We recommend that the number of reranked results (the ceiling of TopK × RerankFactor) not exceed 50.
        self.rerank_factor = rerank_factor
        # Knowledge base.
        # 
        # This parameter is required.
        self.source_collection = source_collection
        # Specifies the number of top results to return after merging retrieved results from multiple vector collections.
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
        if self.merge_method is not None:
            result['MergeMethod'] = self.merge_method

        if self.merge_method_args is not None:
            result['MergeMethodArgs'] = self.merge_method_args.to_map()

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
        if m.get('MergeMethod') is not None:
            self.merge_method = m.get('MergeMethod')

        if m.get('MergeMethodArgs') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgs()
            self.merge_method_args = temp_model.from_map(m.get('MergeMethodArgs'))

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        self.source_collection = []
        if m.get('SourceCollection') is not None:
            for k1 in m.get('SourceCollection'):
                temp_model = main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollection()
                self.source_collection.append(temp_model.from_map(k1))

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

class ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollection(DaraModel):
    def __init__(
        self,
        collection: str = None,
        namespace: str = None,
        namespace_password: str = None,
        query_params: main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollectionQueryParams = None,
    ):
        # The name of the collection to be recalled.
        # 
        # This parameter is required.
        self.collection = collection
        # The name of the namespace. Default value: public.
        # 
        # >  You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace and call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to query a list of namespaces.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # >  The value of this parameter is specified when you call the CreateNamespace operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # Parameters related to the knowledge base retrieval.
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
            temp_model = main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollectionQueryParams()
            self.query_params = temp_model.from_map(m.get('QueryParams'))

        return self

class ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollectionQueryParams(DaraModel):
    def __init__(
        self,
        filter: str = None,
        graph_enhance: bool = None,
        graph_search_args: main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollectionQueryParamsGraphSearchArgs = None,
        hybrid_search: str = None,
        hybrid_search_args: Dict[str, Any] = None,
        metrics: str = None,
        recall_window: List[int] = None,
        rerank_factor: float = None,
        top_k: int = None,
        use_full_text_retrieval: bool = None,
    ):
        # The condition that is used to filter the data to be updated. Specify this parameter in a format that is the same as the WHERE clause.
        self.filter = filter
        # Whether to enable knowledge graph enhancement. Default value: false.
        self.graph_enhance = graph_enhance
        # Returns the top number of entities and relationship edges. Default value: 60.
        self.graph_search_args = graph_search_args
        # The dual-path retrieval algorithm. This parameter is empty by default, which specifies that scores of vector retrieval and full-text retrieval are directly compared and sorted together.
        # 
        # Valid values:
        # 
        # *   RRF: The reciprocal rank fusion (RRF) algorithm uses a constant k to control the fusion effect. For more information, see the description of the HybridSearchArgs parameter.
        # *   Weight: This algorithm uses the alpha parameter to specify the proportion of the vector search score and the full-text search score and then sorts by weight. For more information, see the description of the HybridSearchArgs parameter.
        # *   Cascaded: This algorithm performs first full-text retrieval and then vector retrieval.
        self.hybrid_search = hybrid_search
        # The parameters of the dual-path retrieval algorithm. RRF and Weight are supported at this time:
        # 
        # *   RRF: Specifies the smoothing constant k in the formula to calculate the score: `1/(k + rank_i)`. The k constant must be a positive integer greater than 1. The format:
        # 
        # <!---->
        # 
        #     { 
        #        "RRF": {
        #         "k": 60
        #        }
        #     }
        # 
        # *   Weight: The score is computed as `alpha * vector_score + (1 - alpha) * text_score`. The parameter alpha controls the weighting between vector search and full-text search scores, with a valid range of [0, 1]. 0 specifies only full-text search score. 1 specifies only vector search score.
        # 
        # <!---->
        # 
        #     { 
        #        "Weight": {
        #         "alpha": 0.5
        #        }
        #     }
        self.hybrid_search_args = hybrid_search_args
        # The method that is used to create vector indexes. Valid values:
        # 
        # *   l2: Euclidean distance.
        # *   ip: Inner product distance.
        # *   cosine: Cosine similarity.
        self.metrics = metrics
        # The retrieval window. If you specify this parameter, the context of the retrieved result is added in the output. Format: List\\<A, B>. Valid values: -10<=A<=0 and 0<=B<=10.
        # 
        # > 
        # 
        # *   We recommend that you specify this parameter if the source document is segmented into large numbers of pieces, which may result in loss of contextual information during retrieval.
        # 
        # *   Perform re-ranking before windowing.
        self.recall_window = recall_window
        # The rerank factor. If you specify this parameter, the search result is reranked once again. Valid values: 1\\<RerankFactor<=5.
        # 
        # > 
        # 
        # *   If the document is segmented into sparse parts, reranking is inefficient.
        # 
        # *   We recommend that the number of reranked results (the ceiling of TopK × RerankFactor) not exceed 50.
        self.rerank_factor = rerank_factor
        # The number of top results.
        self.top_k = top_k
        # Specifies whether to use full-text retrieval (dual-path retrieval). The default value is false, which means only vector retrieval is used.
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
            temp_model = main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollectionQueryParamsGraphSearchArgs()
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

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')

        return self

class ChatWithKnowledgeBaseRequestKnowledgeParamsSourceCollectionQueryParamsGraphSearchArgs(DaraModel):
    def __init__(
        self,
        graph_top_k: int = None,
    ):
        # Returns the top number of entities and relationship edges. Default value: 60.
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

class ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgs(DaraModel):
    def __init__(
        self,
        rrf: main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgsRrf = None,
        weight: main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgsWeight = None,
    ):
        # The parameter that can be configured when the MergeMethod parameter is set to RRF.
        self.rrf = rrf
        # The parameter that you can configure when you set the MergeMethod parameter to Weight.
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
            temp_model = main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgsRrf()
            self.rrf = temp_model.from_map(m.get('Rrf'))

        if m.get('Weight') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgsWeight()
            self.weight = temp_model.from_map(m.get('Weight'))

        return self

class ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgsWeight(DaraModel):
    def __init__(
        self,
        weights: List[float] = None,
    ):
        # An array of weights for each SourceCollection.
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

class ChatWithKnowledgeBaseRequestKnowledgeParamsMergeMethodArgsRrf(DaraModel):
    def __init__(
        self,
        k: int = None,
    ):
        # The smoothing constant k in the formula to calculate the score: 1/(k + rank_i). It must be a positive integer greater than 1.
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

