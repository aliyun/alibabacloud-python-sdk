# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class SearchMemoryResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.SearchMemoryResponseBodyResult = None,
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
            temp_model = main_models.SearchMemoryResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class SearchMemoryResponseBodyResult(DaraModel):
    def __init__(
        self,
        memory: main_models.SearchMemoryResponseBodyResultMemory = None,
        skill: main_models.SearchMemoryResponseBodyResultSkill = None,
    ):
        self.memory = memory
        self.skill = skill

    def validate(self):
        if self.memory:
            self.memory.validate()
        if self.skill:
            self.skill.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory is not None:
            result['memory'] = self.memory.to_map()

        if self.skill is not None:
            result['skill'] = self.skill.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memory') is not None:
            temp_model = main_models.SearchMemoryResponseBodyResultMemory()
            self.memory = temp_model.from_map(m.get('memory'))

        if m.get('skill') is not None:
            temp_model = main_models.SearchMemoryResponseBodyResultSkill()
            self.skill = temp_model.from_map(m.get('skill'))

        return self

class SearchMemoryResponseBodyResultSkill(DaraModel):
    def __init__(
        self,
        results: List[main_models.SearchMemoryResponseBodyResultSkillResults] = None,
        total: int = None,
    ):
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.SearchMemoryResponseBodyResultSkillResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class SearchMemoryResponseBodyResultSkillResults(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        description: str = None,
        name: str = None,
        skill_id: str = None,
        user_id: str = None,
        version: str = None,
    ):
        self.agent_id = agent_id
        self.description = description
        self.name = name
        self.skill_id = skill_id
        self.user_id = user_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.skill_id is not None:
            result['skill_id'] = self.skill_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('skill_id') is not None:
            self.skill_id = m.get('skill_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class SearchMemoryResponseBodyResultMemory(DaraModel):
    def __init__(
        self,
        results: List[main_models.SearchMemoryResponseBodyResultMemoryResults] = None,
        total: int = None,
    ):
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.SearchMemoryResponseBodyResultMemoryResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class SearchMemoryResponseBodyResultMemoryResults(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        memory: str = None,
        memory_id: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.memory = memory
        self.memory_id = memory_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.memory is not None:
            result['memory'] = self.memory

        if self.memory_id is not None:
            result['memory_id'] = self.memory_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('memory_id') is not None:
            self.memory_id = m.get('memory_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

