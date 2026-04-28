# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class CreateMemorySkillResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.CreateMemorySkillResponseBodyResult = None,
        status: str = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latency is not None:
            result['latency'] = self.latency

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('result') is not None:
            temp_model = main_models.CreateMemorySkillResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class CreateMemorySkillResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.CreateMemorySkillResponseBodyResultData] = None,
        imported_count: int = None,
    ):
        self.data = data
        self.imported_count = imported_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.imported_count is not None:
            result['imported_count'] = self.imported_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.CreateMemorySkillResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('imported_count') is not None:
            self.imported_count = m.get('imported_count')

        return self

class CreateMemorySkillResponseBodyResultData(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        name: str = None,
        owner: str = None,
        resource_paths: List[str] = None,
        tags: List[str] = None,
        triggers: List[str] = None,
        updated_at: str = None,
        version: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.owner = owner
        self.resource_paths = resource_paths
        self.tags = tags
        self.triggers = triggers
        self.updated_at = updated_at
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.resource_paths is not None:
            result['resource_paths'] = self.resource_paths

        if self.tags is not None:
            result['tags'] = self.tags

        if self.triggers is not None:
            result['triggers'] = self.triggers

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('resource_paths') is not None:
            self.resource_paths = m.get('resource_paths')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('triggers') is not None:
            self.triggers = m.get('triggers')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

