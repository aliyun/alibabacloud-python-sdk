# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class UpdateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        chunk_configuration: main_models.UpdateKnowledgeBaseRequestChunkConfiguration = None,
        description: str = None,
        knowledge_base_name: str = None,
        namespace: str = None,
        search_configuration: main_models.UpdateKnowledgeBaseRequestSearchConfiguration = None,
    ):
        # The data catalog to which the knowledge base belongs. It is used together with Namespace and KnowledgeBaseName to locate the knowledge base. You can call ListCatalogs to obtain the value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # Optional. Updates the default chunking strategy of the knowledge base. This update takes effect only for newly uploaded documents and does not re-chunk existing documents. If this parameter is not specified, the strategy is not modified.
        self.chunk_configuration = chunk_configuration
        # Updates the description of the knowledge base. If this parameter is not specified, the description is not modified.
        self.description = description
        # The name of the knowledge base. The name must be unique within the namespace. It is specified during creation and cannot be modified.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The namespace to which the knowledge base belongs. The namespace must belong to the specified data catalog. It is used together with Catalog and KnowledgeBaseName to locate the knowledge base. You can call ListNamespaces to obtain the value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # Optional. Updates the default search configuration at the knowledge base level. The update takes effect immediately for subsequent search requests. If this parameter is not specified, the configuration is not modified.
        self.search_configuration = search_configuration

    def validate(self):
        if self.chunk_configuration:
            self.chunk_configuration.validate()
        if self.search_configuration:
            self.search_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.chunk_configuration is not None:
            result['ChunkConfiguration'] = self.chunk_configuration.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.search_configuration is not None:
            result['SearchConfiguration'] = self.search_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ChunkConfiguration') is not None:
            temp_model = main_models.UpdateKnowledgeBaseRequestChunkConfiguration()
            self.chunk_configuration = temp_model.from_map(m.get('ChunkConfiguration'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchConfiguration') is not None:
            temp_model = main_models.UpdateKnowledgeBaseRequestSearchConfiguration()
            self.search_configuration = temp_model.from_map(m.get('SearchConfiguration'))

        return self

class UpdateKnowledgeBaseRequestSearchConfiguration(DaraModel):
    def __init__(
        self,
        mode: str = None,
        rank_algorithm: str = None,
        rerank_enabled: bool = None,
        rerank_model: str = None,
        rrf_k: int = None,
        top_k: int = None,
        vector_weight: float = None,
    ):
        # The search mode. Valid values: KEYWORD: Keyword retrieve. VECTOR: AISearch. HYBRID: Hybrid retrieve.
        self.mode = mode
        # The hybrid search fusion algorithm. This parameter takes effect only in hybrid search mode. Valid values: RRF: Reciprocal rank fusion.
        self.rank_algorithm = rank_algorithm
        # Specifies whether to enable reranking by default. This parameter takes effect only in hybrid search mode and is used when a search request does not specify the Rerank parameter.
        self.rerank_enabled = rerank_enabled
        # The default rerank model used when a search request does not specify the RerankModel parameter. Valid values: qwen3-rerank. Default value: qwen3-rerank.
        self.rerank_model = rerank_model
        # The parameter k for the RRF fusion algorithm. The value must be greater than 0. Default value: 60.
        self.rrf_k = rrf_k
        # The default number of returned results.
        self.top_k = top_k
        # The weight of the vector path in the WEIGHTED fusion algorithm. Valid values: 0 to 1. The weight of the keyword path is 1 minus this value. Default value: 0.7.
        self.vector_weight = vector_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.rank_algorithm is not None:
            result['RankAlgorithm'] = self.rank_algorithm

        if self.rerank_enabled is not None:
            result['RerankEnabled'] = self.rerank_enabled

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
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RankAlgorithm') is not None:
            self.rank_algorithm = m.get('RankAlgorithm')

        if m.get('RerankEnabled') is not None:
            self.rerank_enabled = m.get('RerankEnabled')

        if m.get('RerankModel') is not None:
            self.rerank_model = m.get('RerankModel')

        if m.get('RrfK') is not None:
            self.rrf_k = m.get('RrfK')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('VectorWeight') is not None:
            self.vector_weight = m.get('VectorWeight')

        return self

class UpdateKnowledgeBaseRequestChunkConfiguration(DaraModel):
    def __init__(
        self,
        heading_level: int = None,
        max_chunk_size: int = None,
        overlap_size: int = None,
        preprocess_rules: main_models.UpdateKnowledgeBaseRequestChunkConfigurationPreprocessRules = None,
        separator: str = None,
        strategy: str = None,
    ):
        # Required for the BY_HEADING strategy. Valid values: 1 to 6. This parameter is ignored for other strategies. Headings at or above the specified level are used as split boundaries. For example, if you set this parameter to 2, both H1 and H2 headings are used for splitting. Deeper-level headings are not split and are retained in the chunk text. If the section content exceeds MaxChunkSize, the system falls back to splitting by paragraphs or sentences. For documents without headings, the system falls back to intelligent chunking.
        self.heading_level = heading_level
        # The maximum token length of a single chunk.
        self.max_chunk_size = max_chunk_size
        # The overlap token length between adjacent chunks.
        self.overlap_size = overlap_size
        # The preprocessing rules.
        self.preprocess_rules = preprocess_rules
        # The paragraph identifier for the LINE_BREAK strategy, such as a line break.
        self.separator = separator
        # The chunking strategy. Valid values: AUTO: Automatic chunking. LINE_BREAK: Chunking by paragraph identifier.
        # 
        # This parameter is required.
        self.strategy = strategy

    def validate(self):
        if self.preprocess_rules:
            self.preprocess_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.heading_level is not None:
            result['HeadingLevel'] = self.heading_level

        if self.max_chunk_size is not None:
            result['MaxChunkSize'] = self.max_chunk_size

        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size

        if self.preprocess_rules is not None:
            result['PreprocessRules'] = self.preprocess_rules.to_map()

        if self.separator is not None:
            result['Separator'] = self.separator

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeadingLevel') is not None:
            self.heading_level = m.get('HeadingLevel')

        if m.get('MaxChunkSize') is not None:
            self.max_chunk_size = m.get('MaxChunkSize')

        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')

        if m.get('PreprocessRules') is not None:
            temp_model = main_models.UpdateKnowledgeBaseRequestChunkConfigurationPreprocessRules()
            self.preprocess_rules = temp_model.from_map(m.get('PreprocessRules'))

        if m.get('Separator') is not None:
            self.separator = m.get('Separator')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class UpdateKnowledgeBaseRequestChunkConfigurationPreprocessRules(DaraModel):
    def __init__(
        self,
        remove_urls_and_emails: bool = None,
        replace_consecutive_whitespace: bool = None,
    ):
        # Specifies whether to remove URLs and email addresses during parsing.
        self.remove_urls_and_emails = remove_urls_and_emails
        # Specifies whether to replace consecutive whitespace characters, such as spaces, line breaks, and tabs, with a single space.
        self.replace_consecutive_whitespace = replace_consecutive_whitespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remove_urls_and_emails is not None:
            result['RemoveUrlsAndEmails'] = self.remove_urls_and_emails

        if self.replace_consecutive_whitespace is not None:
            result['ReplaceConsecutiveWhitespace'] = self.replace_consecutive_whitespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoveUrlsAndEmails') is not None:
            self.remove_urls_and_emails = m.get('RemoveUrlsAndEmails')

        if m.get('ReplaceConsecutiveWhitespace') is not None:
            self.replace_consecutive_whitespace = m.get('ReplaceConsecutiveWhitespace')

        return self

