# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateMemoryStoreRequest(DaraModel):
    def __init__(
        self,
        custom_extraction_strategies: List[main_models.CustomExtractionStrategy] = None,
        description: str = None,
        extraction_strategies: List[str] = None,
        memory_store_name: str = None,
        short_term_ttl: int = None,
        source_type: str = None,
        trace_source_config: main_models.CreateMemoryStoreRequestTraceSourceConfig = None,
    ):
        # A list of custom extraction strategies.
        self.custom_extraction_strategies = custom_extraction_strategies
        # The description of the MemoryStore.
        self.description = description
        # The extraction strategies to use. Valid values include `Episodic`, `Summary`, and `Fact`.
        self.extraction_strategies = extraction_strategies
        # The name of the MemoryStore. The name must be unique within the workspace.
        # 
        # This parameter is required.
        self.memory_store_name = memory_store_name
        # The short-term TTL, which is the number of conversation rounds to retain.
        # 
        # This parameter is required.
        self.short_term_ttl = short_term_ttl
        # The source type of the memory. Valid values are `None` and `Trace`.
        self.source_type = source_type
        # Configuration for the trace source. Required if `sourceType` is `Trace`.
        self.trace_source_config = trace_source_config

    def validate(self):
        if self.custom_extraction_strategies:
            for v1 in self.custom_extraction_strategies:
                 if v1:
                    v1.validate()
        if self.trace_source_config:
            self.trace_source_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.short_term_ttl is not None:
            result['shortTermTtl'] = self.short_term_ttl

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.trace_source_config is not None:
            result['traceSourceConfig'] = self.trace_source_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('shortTermTtl') is not None:
            self.short_term_ttl = m.get('shortTermTtl')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('traceSourceConfig') is not None:
            temp_model = main_models.CreateMemoryStoreRequestTraceSourceConfig()
            self.trace_source_config = temp_model.from_map(m.get('traceSourceConfig'))

        return self

class CreateMemoryStoreRequestTraceSourceConfig(DaraModel):
    def __init__(
        self,
        include_output: bool = None,
        query: str = None,
        workspace: str = None,
    ):
        # Specifies whether to include the output in the trace.
        self.include_output = include_output
        # The query to filter traces.
        self.query = query
        # The name of the workspace that contains the trace source.
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

