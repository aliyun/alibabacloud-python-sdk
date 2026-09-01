# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeKnowledgeSpaceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        aclmode: str = None,
        creation_time: str = None,
        dbcluster_id: str = None,
        dbname: str = None,
        dbtype: str = None,
        description: str = None,
        embedding_dimension: int = None,
        embedding_model: str = None,
        knowledge_base_count: int = None,
        knowledge_space_id: str = None,
        llmmodel: str = None,
        name: str = None,
        ossbucket: str = None,
        request_id: str = None,
        rerank_model: str = None,
        shard_size: int = None,
        sharding_strategy_config: main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfig = None,
        status: str = None,
        strategy: str = None,
        total_docs: int = None,
        total_size_bytes: int = None,
    ):
        # The access control list (ACL) mode of the knowledge space. Valid values:
        # - DISABLED
        # - ENFORCED
        self.aclmode = aclmode
        # The time when the knowledge space was created.
        self.creation_time = creation_time
        # The ID of the PolarDB instance.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.dbname = dbname
        # The type of the database engine. Valid values:
        # * MySQL
        # * PostgreSQL
        self.dbtype = dbtype
        # The description of the knowledge space.
        self.description = description
        # The vector dimensions.
        self.embedding_dimension = embedding_dimension
        # The embedding model.
        self.embedding_model = embedding_model
        # The total number of knowledge bases.
        self.knowledge_base_count = knowledge_base_count
        # The unique identifier of the knowledge space.
        self.knowledge_space_id = knowledge_space_id
        # The large language model.
        self.llmmodel = llmmodel
        # The name of the knowledge space.
        self.name = name
        # OSS Bucket
        self.ossbucket = ossbucket
        # Id of the request
        self.request_id = request_id
        # The reranking model.
        self.rerank_model = rerank_model
        # The chunk size in tokens.
        self.shard_size = shard_size
        # The default chunking strategy configuration of the knowledge space. This parameter may be empty if existing instances do not have the complete configuration saved.
        self.sharding_strategy_config = sharding_strategy_config
        # The instance status.
        self.status = status
        # The chunking strategy.
        self.strategy = strategy
        # The total number of documents.
        self.total_docs = total_docs
        # The total size in bytes.
        self.total_size_bytes = total_size_bytes

    def validate(self):
        if self.sharding_strategy_config:
            self.sharding_strategy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aclmode is not None:
            result['ACLMode'] = self.aclmode

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.knowledge_base_count is not None:
            result['KnowledgeBaseCount'] = self.knowledge_base_count

        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

        if self.llmmodel is not None:
            result['LLMModel'] = self.llmmodel

        if self.name is not None:
            result['Name'] = self.name

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rerank_model is not None:
            result['RerankModel'] = self.rerank_model

        if self.shard_size is not None:
            result['ShardSize'] = self.shard_size

        if self.sharding_strategy_config is not None:
            result['ShardingStrategyConfig'] = self.sharding_strategy_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.total_docs is not None:
            result['TotalDocs'] = self.total_docs

        if self.total_size_bytes is not None:
            result['TotalSizeBytes'] = self.total_size_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ACLMode') is not None:
            self.aclmode = m.get('ACLMode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('KnowledgeBaseCount') is not None:
            self.knowledge_base_count = m.get('KnowledgeBaseCount')

        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('LLMModel') is not None:
            self.llmmodel = m.get('LLMModel')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RerankModel') is not None:
            self.rerank_model = m.get('RerankModel')

        if m.get('ShardSize') is not None:
            self.shard_size = m.get('ShardSize')

        if m.get('ShardingStrategyConfig') is not None:
            temp_model = main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfig()
            self.sharding_strategy_config = temp_model.from_map(m.get('ShardingStrategyConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('TotalDocs') is not None:
            self.total_docs = m.get('TotalDocs')

        if m.get('TotalSizeBytes') is not None:
            self.total_size_bytes = m.get('TotalSizeBytes')

        return self

class DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfig(DaraModel):
    def __init__(
        self,
        default_strategy: main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigDefaultStrategy = None,
        rules: List[main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRules] = None,
    ):
        # The default chunking strategy. This strategy is used when no rule is matched.
        self.default_strategy = default_strategy
        # The list of override rules that are matched in order.
        self.rules = rules

    def validate(self):
        if self.default_strategy:
            self.default_strategy.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_strategy is not None:
            result['DefaultStrategy'] = self.default_strategy.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultStrategy') is not None:
            temp_model = main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigDefaultStrategy()
            self.default_strategy = temp_model.from_map(m.get('DefaultStrategy'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRules(DaraModel):
    def __init__(
        self,
        match: main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesMatch = None,
        strategy: main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesStrategy = None,
    ):
        # The content type. Currently, table is supported.
        self.match = match
        # The chunking strategy.
        self.strategy = strategy

    def validate(self):
        if self.match:
            self.match.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match is not None:
            result['Match'] = self.match.to_map()

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            temp_model = main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesMatch()
            self.match = temp_model.from_map(m.get('Match'))

        if m.get('Strategy') is not None:
            temp_model = main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesStrategyParameters = None,
        type: str = None,
    ):
        # The parameter details.
        self.parameters = parameters
        # The chunking strategy type used when a rule is matched.
        self.type = type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            temp_model = main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesStrategyParameters(DaraModel):
    def __init__(
        self,
        markdown_tables: str = None,
        max_tokens: int = None,
    ):
        # The Markdown table processing mode. Valid values: auto, on, or off.
        self.markdown_tables = markdown_tables
        # The maximum number of tokens in a single chunk for matched content.
        self.max_tokens = max_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.markdown_tables is not None:
            result['MarkdownTables'] = self.markdown_tables

        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkdownTables') is not None:
            self.markdown_tables = m.get('MarkdownTables')

        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        return self

class DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigRulesMatch(DaraModel):
    def __init__(
        self,
        content_type: str = None,
    ):
        # The content type. Currently, table is supported.
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        return self

class DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigDefaultStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigDefaultStrategyParameters = None,
        type: str = None,
    ):
        # The parameter details.
        self.parameters = parameters
        # The type of the default chunking strategy. Valid values: hybrid or hierarchical.
        self.type = type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            temp_model = main_models.DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigDefaultStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeKnowledgeSpaceAttributeResponseBodyShardingStrategyConfigDefaultStrategyParameters(DaraModel):
    def __init__(
        self,
        max_tokens: int = None,
        merge_peers: bool = None,
    ):
        # The maximum number of tokens in a single chunk.
        self.max_tokens = max_tokens
        # Specifies whether to merge adjacent small chunks under the same heading.
        self.merge_peers = merge_peers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        if self.merge_peers is not None:
            result['MergePeers'] = self.merge_peers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        if m.get('MergePeers') is not None:
            self.merge_peers = m.get('MergePeers')

        return self

