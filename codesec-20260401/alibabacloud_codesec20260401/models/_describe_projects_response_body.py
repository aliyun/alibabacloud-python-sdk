# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_codesec20260401 import models as main_models
from darabonba.model import DaraModel

class DescribeProjectsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeProjectsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

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
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DescribeProjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class DescribeProjectsResponseBodyItems(DaraModel):
    def __init__(
        self,
        config_revision: int = None,
        created_at: str = None,
        created_by: str = None,
        description: str = None,
        engines: main_models.DescribeProjectsResponseBodyItemsEngines = None,
        id: int = None,
        instruction_prompt: str = None,
        name: str = None,
        source: main_models.DescribeProjectsResponseBodyItemsSource = None,
        updated_at: str = None,
    ):
        self.config_revision = config_revision
        # 扫描项目创建时间（RFC3339）
        self.created_at = created_at
        self.created_by = created_by
        self.description = description
        self.engines = engines
        self.id = id
        self.instruction_prompt = instruction_prompt
        self.name = name
        self.source = source
        # 扫描项目更新时间（RFC3339）
        self.updated_at = updated_at

    def validate(self):
        if self.engines:
            self.engines.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_revision is not None:
            result['configRevision'] = self.config_revision

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.description is not None:
            result['description'] = self.description

        if self.engines is not None:
            result['engines'] = self.engines.to_map()

        if self.id is not None:
            result['id'] = self.id

        if self.instruction_prompt is not None:
            result['instructionPrompt'] = self.instruction_prompt

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configRevision') is not None:
            self.config_revision = m.get('configRevision')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('engines') is not None:
            temp_model = main_models.DescribeProjectsResponseBodyItemsEngines()
            self.engines = temp_model.from_map(m.get('engines'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instructionPrompt') is not None:
            self.instruction_prompt = m.get('instructionPrompt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            temp_model = main_models.DescribeProjectsResponseBodyItemsSource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class DescribeProjectsResponseBodyItemsSource(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self



class DescribeProjectsResponseBodyItemsEngines(DaraModel):
    def __init__(
        self,
        sast: bool = None,
        sca: bool = None,
    ):
        self.sast = sast
        self.sca = sca

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sast is not None:
            result['sast'] = self.sast

        if self.sca is not None:
            result['sca'] = self.sca

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sast') is not None:
            self.sast = m.get('sast')

        if m.get('sca') is not None:
            self.sca = m.get('sca')

        return self

