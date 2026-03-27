# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetMemoryStoreResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        custom_extraction_strategies: List[main_models.CustomExtractionStrategy] = None,
        description: str = None,
        extraction_strategies: List[str] = None,
        memory_store_name: str = None,
        region_id: str = None,
        request_id: str = None,
        short_term_storage: main_models.GetMemoryStoreResponseBodyShortTermStorage = None,
        short_term_ttl: int = None,
        source_type: str = None,
        trace_source_config: main_models.GetMemoryStoreResponseBodyTraceSourceConfig = None,
        update_time: str = None,
        workspace: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.custom_extraction_strategies = custom_extraction_strategies
        self.description = description
        self.extraction_strategies = extraction_strategies
        self.memory_store_name = memory_store_name
        self.region_id = region_id
        self.request_id = request_id
        self.short_term_storage = short_term_storage
        self.short_term_ttl = short_term_ttl
        self.source_type = source_type
        self.trace_source_config = trace_source_config
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        self.workspace = workspace

    def validate(self):
        if self.custom_extraction_strategies:
            for v1 in self.custom_extraction_strategies:
                 if v1:
                    v1.validate()
        if self.short_term_storage:
            self.short_term_storage.validate()
        if self.trace_source_config:
            self.trace_source_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        result['customExtractionStrategies'] = []
        if self.custom_extraction_strategies is not None:
            for k1 in self.custom_extraction_strategies:
                result['customExtractionStrategies'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.extraction_strategies is not None:
            result['extractionStrategies'] = self.extraction_strategies

        if self.memory_store_name is not None:
            result['memoryStoreName'] = self.memory_store_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.short_term_storage is not None:
            result['shortTermStorage'] = self.short_term_storage.to_map()

        if self.short_term_ttl is not None:
            result['shortTermTtl'] = self.short_term_ttl

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.trace_source_config is not None:
            result['traceSourceConfig'] = self.trace_source_config.to_map()

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        self.custom_extraction_strategies = []
        if m.get('customExtractionStrategies') is not None:
            for k1 in m.get('customExtractionStrategies'):
                temp_model = main_models.CustomExtractionStrategy()
                self.custom_extraction_strategies.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extractionStrategies') is not None:
            self.extraction_strategies = m.get('extractionStrategies')

        if m.get('memoryStoreName') is not None:
            self.memory_store_name = m.get('memoryStoreName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('shortTermStorage') is not None:
            temp_model = main_models.GetMemoryStoreResponseBodyShortTermStorage()
            self.short_term_storage = temp_model.from_map(m.get('shortTermStorage'))

        if m.get('shortTermTtl') is not None:
            self.short_term_ttl = m.get('shortTermTtl')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('traceSourceConfig') is not None:
            temp_model = main_models.GetMemoryStoreResponseBodyTraceSourceConfig()
            self.trace_source_config = temp_model.from_map(m.get('traceSourceConfig'))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetMemoryStoreResponseBodyTraceSourceConfig(DaraModel):
    def __init__(
        self,
        include_output: bool = None,
        query: str = None,
        workspace: str = None,
    ):
        self.include_output = include_output
        self.query = query
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_output is not None:
            result['includeOutput'] = self.include_output

        if self.query is not None:
            result['query'] = self.query

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeOutput') is not None:
            self.include_output = m.get('includeOutput')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetMemoryStoreResponseBodyShortTermStorage(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

