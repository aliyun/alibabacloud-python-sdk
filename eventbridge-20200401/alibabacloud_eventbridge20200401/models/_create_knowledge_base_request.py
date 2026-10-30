# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        chunk_configuration: main_models.CreateKnowledgeBaseRequestChunkConfiguration = None,
        description: str = None,
        embedding_dimension: int = None,
        embedding_model: str = None,
        knowledge_base_name: str = None,
        metadata_schema: List[main_models.CreateKnowledgeBaseRequestMetadataSchema] = None,
        namespace: str = None,
        search_configuration: main_models.CreateKnowledgeBaseRequestSearchConfiguration = None,
    ):
        # The EventHouse catalog to which the knowledge base belongs. This parameter, together with Namespace and KnowledgeBaseName, uniquely identifies the knowledge base. This parameter cannot be modified after the knowledge base is created. You cannot bind a system catalog.
        # 
        # This parameter is required.
        self.catalog = catalog
        # Optional. The default chunking strategy for the knowledge base. This strategy applies only to documents uploaded after the configuration. If this parameter is not specified, the system default chunking strategy is used.
        self.chunk_configuration = chunk_configuration
        # The description of the knowledge base.
        self.description = description
        # Optional. The vector dimensions. This parameter is attached to the embedding model for validation. Valid values for text-embedding-v3: 64, 128, 256, 512, 768, and 1024. Valid values for text-embedding-v4: 64, 128, 256, 512, 768, 1024, 1536, and 2048. Valid values for qwen3.7-text-embedding: 256, 512, 768, 1024, 1536, 2048, and 2560. Valid values for qwen3.7-text-embedding-flash: 256, 512, 768, and 1024. If this parameter is not specified, the default dimension of the model, 1024, is used. This parameter cannot be modified after the knowledge base is created. To change the model, you must rebuild the knowledge base, even if the dimensions remain the same.
        self.embedding_dimension = embedding_dimension
        # Optional. The embedding model. This parameter cannot be modified after the knowledge base is created. Valid values: text-embedding-v3, text-embedding-v4, qwen3.7-text-embedding, and qwen3.7-text-embedding-flash. Only Qwen models provided by Model Studio are supported. Third-party models are not supported. Default value: text-embedding-v4.
        self.embedding_model = embedding_model
        # The name of the knowledge base. The name must be unique within the same namespace.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # Declares the metadata fields for the knowledge base. When you upload documents, the metadata can only contain the fields declared here. This parameter cannot be modified after the knowledge base is created.
        self.metadata_schema = metadata_schema
        # The EventHouse namespace to which the knowledge base belongs. The namespace must belong to the specified catalog. This parameter, together with Catalog and KnowledgeBaseName, uniquely identifies the knowledge base. This parameter cannot be modified after the knowledge base is created.
        # 
        # This parameter is required.
        self.namespace = namespace
        # Optional. The default search configuration at the knowledge base level. This configuration takes effect when the corresponding parameters are not specified in a search request. You can modify this configuration by calling UpdateKnowledgeBase after the knowledge base is created.
        self.search_configuration = search_configuration

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

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ChunkConfiguration') is not None:
            temp_model = main_models.CreateKnowledgeBaseRequestChunkConfiguration()
            self.chunk_configuration = temp_model.from_map(m.get('ChunkConfiguration'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        self.metadata_schema = []
        if m.get('MetadataSchema') is not None:
            for k1 in m.get('MetadataSchema'):
                temp_model = main_models.CreateKnowledgeBaseRequestMetadataSchema()
                self.metadata_schema.append(temp_model.from_map(k1))

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchConfiguration') is not None:
            temp_model = main_models.CreateKnowledgeBaseRequestSearchConfiguration()
            self.search_configuration = temp_model.from_map(m.get('SearchConfiguration'))

        return self

class CreateKnowledgeBaseRequestSearchConfiguration(DaraModel):
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
        # The search mode. KEYWORD indicates keyword retrieve. VECTOR indicates AISearch. HYBRID indicates hybrid retrieve. Valid values: KEYWORD, VECTOR, and HYBRID.
        self.mode = mode
        # Applies only to the hybrid search mode. RRF indicates reciprocal rank fusion. WEIGHTED indicates weighted normalization fusion, which is used together with VectorWeight. Default value: RRF.
        self.rank_algorithm = rank_algorithm
        # Applies only to the hybrid search mode. Specifies whether to enable reranking by default when a search request does not specify the Rerank parameter.
        self.rerank_enabled = rerank_enabled
        # The default rerank model used when a search request does not specify the RerankModel parameter. Valid value: qwen3-rerank. Default value: qwen3-rerank.
        self.rerank_model = rerank_model
        # The k parameter for the RRF fusion algorithm. The value must be greater than 0. Default value: 60.
        self.rrf_k = rrf_k
        # The default number of results to return.
        self.top_k = top_k
        # The vector weight for the WEIGHTED fusion algorithm. Valid values: 0 to 1. The keyword weight is 1 minus this value. Default value: 0.7.
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

class CreateKnowledgeBaseRequestMetadataSchema(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
        value_mode: str = None,
    ):
        # The name of the field.
        # 
        # This parameter is required.
        self.name = name
        # The type of the field. Valid values: STRING, LONG, DOUBLE, BOOLEAN, and DATETIME.
        # 
        # This parameter is required.
        self.type = type
        # The value configuration. If ValueMode is set to CONSTANT, this parameter specifies a fixed value. If it is left empty, you can assign a value during upload. If ValueMode is set to SYSTEM_VARIABLE, this parameter specifies a system variable name, such as DOCUMENT_NAME, FILE_TYPE, FILE_SIZE, DOCUMENT_UPLOAD_TIME, SOURCE_TYPE, SOURCE_URI, or SOURCE_MODIFIED_TIME.
        self.value = value
        # The value mode. CONSTANT indicates a constant. If Value is not empty, all documents use the fixed value. If Value is empty, you can assign a value during upload. SYSTEM_VARIABLE indicates a system variable. Value specifies the variable name, which is automatically generated by the system and cannot be overwritten during upload.
        # 
        # This parameter is required.
        self.value_mode = value_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.value_mode is not None:
            result['ValueMode'] = self.value_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueMode') is not None:
            self.value_mode = m.get('ValueMode')

        return self

class CreateKnowledgeBaseRequestChunkConfiguration(DaraModel):
    def __init__(
        self,
        heading_level: int = None,
        max_chunk_size: int = None,
        overlap_size: int = None,
        preprocess_rules: main_models.CreateKnowledgeBaseRequestChunkConfigurationPreprocessRules = None,
        separator: str = None,
        strategy: str = None,
    ):
        # Required for the BY_HEADING strategy. Valid values: 1 to 6. This parameter is ignored for other strategies. Headings at or above the specified level are used as chunking boundaries. For example, if you set this parameter to 2, both H1 and H2 headings are used as boundaries. Lower-level headings are not used as boundaries and are retained in the chunk text. If the section content exceeds MaxChunkSize, the system falls back to chunking by paragraph or sentence. For documents without headings, the system falls back to intelligent chunking.
        self.heading_level = heading_level
        # The maximum number of characters in a single chunk. Valid values: 1 to 6000. An error is reported if the limit is exceeded.
        self.max_chunk_size = max_chunk_size
        # Applies only to the BY_LENGTH strategy. This parameter is ignored for other strategies. The overlap size between adjacent chunks, in characters. If the value is greater than 0, the beginning of the next chunk repeats the content at the end of the previous chunk within this window. The overlap does not cause the chunk to exceed MaxChunkSize. Default value: 0, which indicates no overlap.
        self.overlap_size = overlap_size
        # The preprocessing rules.
        self.preprocess_rules = preprocess_rules
        # Required for the BY_SEPARATOR strategy. This parameter is ignored for other strategies. The literal string used to split the text. Regular expressions are not supported. The maximum length is 32 characters. Example: \\
        # \\
        #  for paragraph breaks.
        self.separator = separator
        # The chunking strategy. AUTO indicates intelligent chunking, which is heading-aware and groups paragraphs. BY_LENGTH indicates sliding window chunking by length, where you can specify OverlapSize. BY_SEPARATOR indicates chunking by separator, where you must specify Separator. BY_HEADING indicates chunking by heading level, where you must specify HeadingLevel. Valid values: AUTO, BY_LENGTH, BY_SEPARATOR, and BY_HEADING.
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
            temp_model = main_models.CreateKnowledgeBaseRequestChunkConfigurationPreprocessRules()
            self.preprocess_rules = temp_model.from_map(m.get('PreprocessRules'))

        if m.get('Separator') is not None:
            self.separator = m.get('Separator')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class CreateKnowledgeBaseRequestChunkConfigurationPreprocessRules(DaraModel):
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

