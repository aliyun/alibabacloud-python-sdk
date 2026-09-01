# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeKnowledgeBaseFilesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeKnowledgeBaseFilesResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.page_size = page_size
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeKnowledgeBaseFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        file_id: str = None,
        file_name: str = None,
        file_size: int = None,
        file_type: str = None,
        inherit_space_strategy: bool = None,
        knowledge_base_id: str = None,
        knowledge_space_id: str = None,
        metadata: Dict[str, Any] = None,
        osspath: str = None,
        shard_count: int = None,
        sharding_strategy_config: main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfig = None,
        source_type: str = None,
        status: str = None,
        updated_at: str = None,
        upload_time: str = None,
    ):
        self.error_message = error_message
        self.file_id = file_id
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.inherit_space_strategy = inherit_space_strategy
        self.knowledge_base_id = knowledge_base_id
        self.knowledge_space_id = knowledge_space_id
        self.metadata = metadata
        self.osspath = osspath
        self.shard_count = shard_count
        self.sharding_strategy_config = sharding_strategy_config
        self.source_type = source_type
        self.status = status
        self.updated_at = updated_at
        self.upload_time = upload_time

    def validate(self):
        if self.sharding_strategy_config:
            self.sharding_strategy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.inherit_space_strategy is not None:
            result['InheritSpaceStrategy'] = self.inherit_space_strategy

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.osspath is not None:
            result['OSSPath'] = self.osspath

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.sharding_strategy_config is not None:
            result['ShardingStrategyConfig'] = self.sharding_strategy_config.to_map()

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('InheritSpaceStrategy') is not None:
            self.inherit_space_strategy = m.get('InheritSpaceStrategy')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('OSSPath') is not None:
            self.osspath = m.get('OSSPath')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('ShardingStrategyConfig') is not None:
            temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfig()
            self.sharding_strategy_config = temp_model.from_map(m.get('ShardingStrategyConfig'))

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        return self

class DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfig(DaraModel):
    def __init__(
        self,
        default_strategy: main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigDefaultStrategy = None,
        rules: List[main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRules] = None,
    ):
        self.default_strategy = default_strategy
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
            temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigDefaultStrategy()
            self.default_strategy = temp_model.from_map(m.get('DefaultStrategy'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRules(DaraModel):
    def __init__(
        self,
        match: main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesMatch = None,
        strategy: main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesStrategy = None,
    ):
        self.match = match
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
            temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesMatch()
            self.match = temp_model.from_map(m.get('Match'))

        if m.get('Strategy') is not None:
            temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesStrategyParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
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
            temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesStrategyParameters(DaraModel):
    def __init__(
        self,
        markdown_tables: str = None,
        max_tokens: int = None,
    ):
        self.markdown_tables = markdown_tables
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

class DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigRulesMatch(DaraModel):
    def __init__(
        self,
        content_type: str = None,
    ):
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

class DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigDefaultStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigDefaultStrategyParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
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
            temp_model = main_models.DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigDefaultStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeKnowledgeBaseFilesResponseBodyItemsShardingStrategyConfigDefaultStrategyParameters(DaraModel):
    def __init__(
        self,
        max_tokens: int = None,
        merge_peers: bool = None,
    ):
        self.max_tokens = max_tokens
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

