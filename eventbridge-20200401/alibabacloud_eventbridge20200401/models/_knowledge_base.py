# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBase(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        chunk_configuration: main_models.KnowledgeBaseChunkConfiguration = None,
        created_at: str = None,
        description: str = None,
        embedding_dimension: int = None,
        embedding_model: str = None,
        failure_reason: str = None,
        knowledge_base_name: str = None,
        metadata_schema: List[main_models.MetadataSchemaField] = None,
        namespace: str = None,
        search_configuration: main_models.KnowledgeBaseSearchConfiguration = None,
        status: str = None,
        updated_at: str = None,
    ):
        # The EventHouse data catalog to which the knowledge base belongs. This value cannot be modified after the knowledge base is created.
        self.catalog = catalog
        # The default chunking strategy of the knowledge base. This configuration takes effect only for documents uploaded after the configuration is updated. Existing documents are not re-chunked.
        self.chunk_configuration = chunk_configuration
        # The time when the knowledge base was created.
        self.created_at = created_at
        # The description of the knowledge base.
        self.description = description
        # The embedding vector dimension specified during creation or the default dimension of the model. This value cannot be modified after the knowledge base is created.
        self.embedding_dimension = embedding_dimension
        # The embedding model specified during creation. This value cannot be modified after the knowledge base is created.
        self.embedding_model = embedding_model
        # The brief reason for the most recent creation or deletion failure. This parameter is returned only when the status is CREATE_FAILED or DELETE_FAILED.
        self.failure_reason = failure_reason
        # The name of the knowledge base, which is unique within the namespace.
        self.knowledge_base_name = knowledge_base_name
        # The metadata fields declared when the knowledge base was created. These fields cannot be modified after the knowledge base is created.
        self.metadata_schema = metadata_schema
        # The EventHouse namespace to which the knowledge base belongs. This value cannot be modified after the knowledge base is created.
        self.namespace = namespace
        # The default search configuration at the knowledge base level. This configuration takes effect when the corresponding parameters are not specified in a search request. You can modify this configuration by calling the UpdateKnowledgeBase operation.
        self.search_configuration = search_configuration
        # The current status of the knowledge base. Valid values:
        # - CREATING: The knowledge base is being created.
        # - ACTIVE: The knowledge base is available.
        # - CREATE_FAILED: The knowledge base failed to be created.
        # - DELETING: The knowledge base is being deleted.
        # - DELETE_FAILED: The knowledge base failed to be deleted.
        self.status = status
        # The time when the knowledge base was last updated.
        self.updated_at = updated_at

    def validate(self):
        if self.chunk_configuration:
            self.chunk_configuration.validate()
        if self.metadata_schema:
            for v1 in self.metadata_schema:
                 if v1:
                    v1.validate()
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

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        result['MetadataSchema'] = []
        if self.metadata_schema is not None:
            for k1 in self.metadata_schema:
                result['MetadataSchema'].append(k1.to_map() if k1 else None)

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.search_configuration is not None:
            result['SearchConfiguration'] = self.search_configuration.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ChunkConfiguration') is not None:
            temp_model = main_models.KnowledgeBaseChunkConfiguration()
            self.chunk_configuration = temp_model.from_map(m.get('ChunkConfiguration'))

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        self.metadata_schema = []
        if m.get('MetadataSchema') is not None:
            for k1 in m.get('MetadataSchema'):
                temp_model = main_models.MetadataSchemaField()
                self.metadata_schema.append(temp_model.from_map(k1))

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchConfiguration') is not None:
            temp_model = main_models.KnowledgeBaseSearchConfiguration()
            self.search_configuration = temp_model.from_map(m.get('SearchConfiguration'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

class KnowledgeBaseSearchConfiguration(DaraModel):
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
        # The retrieval mode. Valid values:
        # - KEYWORD: keyword retrieval.
        # - VECTOR: vector retrieval.
        # - HYBRID: hybrid retrieval.
        self.mode = mode
        # The fusion algorithm for hybrid search. This parameter takes effect only in hybrid search mode. Valid values:
        # - RRF: reciprocal rank fusion.
        # - WEIGHTED: weighted normalization fusion. Use this value together with VectorWeight.
        # 
        # Default value: RRF.
        self.rank_algorithm = rank_algorithm
        # Specifies whether reranking is enabled by default. This parameter takes effect for all search modes (KEYWORD, VECTOR, and HYBRID). This default value is used when the Rerank parameter is not specified in a search request.
        self.rerank_enabled = rerank_enabled
        # The default reranking model used when the RerankModel parameter is not specified in a search request. Valid values: qwen3-rerank, gte-rerank-v2, and qwen3-vl-rerank. Default value: qwen3-rerank. Score distributions vary across models and cannot be compared. Use the same model consistently within a knowledge base.
        self.rerank_model = rerank_model
        # The k parameter of the RRF fusion algorithm. The value must be greater than 0. Default value: 60.
        self.rrf_k = rrf_k
        # The maximum number of results returned by default for a search request.
        self.top_k = top_k
        # The weight of the vector path in the WEIGHTED fusion algorithm. Valid values: 0 to 1. The keyword path weight equals 1 minus this value. Default value: 0.7.
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

class KnowledgeBaseChunkConfiguration(DaraModel):
    def __init__(
        self,
        heading_level: int = None,
        max_chunk_size: int = None,
        overlap_size: int = None,
        preprocess_rules: main_models.KnowledgeBaseChunkConfigurationPreprocessRules = None,
        separator: str = None,
        strategy: str = None,
    ):
        # The heading level (1 to 6) used for splitting in the BY_HEADING strategy. Headings at or above this level serve as split boundaries. Deeper-level headings are retained in the chunk body.
        self.heading_level = heading_level
        # The maximum character length of a single chunk. Starting from revision 22, this value is character-based. Valid values: 1 to 6000.
        self.max_chunk_size = max_chunk_size
        # The overlap character length between adjacent chunks. This parameter takes effect only for the BY_LENGTH strategy. When the value is greater than 0, the beginning of the next chunk repeats the content from the end of the previous chunk within this window. The overlap does not cause a chunk to exceed MaxChunkSize. A value of 0 indicates no overlap.
        self.overlap_size = overlap_size
        # The preprocessing rules that take effect during document parsing.
        self.preprocess_rules = preprocess_rules
        # The separator used in the BY_SEPARATOR strategy. The separator is matched as a literal string (not a regular expression). The maximum length is 32 characters.
        self.separator = separator
        # The chunking strategy. Valid values:
        # - AUTO: intelligent splitting (heading-aware + paragraph packing).
        # - BY_LENGTH: sliding window splitting by length. You can specify OverlapSize.
        # - BY_SEPARATOR: splitting by separator. You must specify Separator.
        # - BY_HEADING: splitting by heading level. You must specify HeadingLevel.
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
            temp_model = main_models.KnowledgeBaseChunkConfigurationPreprocessRules()
            self.preprocess_rules = temp_model.from_map(m.get('PreprocessRules'))

        if m.get('Separator') is not None:
            self.separator = m.get('Separator')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class KnowledgeBaseChunkConfigurationPreprocessRules(DaraModel):
    def __init__(
        self,
        remove_urls_and_emails: bool = None,
        replace_consecutive_whitespace: bool = None,
    ):
        # Specifies whether to remove URLs and email addresses during parsing.
        self.remove_urls_and_emails = remove_urls_and_emails
        # Specifies whether to replace consecutive whitespace characters (spaces, line breaks, and tab characters) with a single space.
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

