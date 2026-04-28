# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class CreateMemoryResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.CreateMemoryResponseBodyResult = None,
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
            temp_model = main_models.CreateMemoryResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class CreateMemoryResponseBodyResult(DaraModel):
    def __init__(
        self,
        memory: main_models.CreateMemoryResponseBodyResultMemory = None,
        skill: main_models.CreateMemoryResponseBodyResultSkill = None,
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
            temp_model = main_models.CreateMemoryResponseBodyResultMemory()
            self.memory = temp_model.from_map(m.get('memory'))

        if m.get('skill') is not None:
            temp_model = main_models.CreateMemoryResponseBodyResultSkill()
            self.skill = temp_model.from_map(m.get('skill'))

        return self

class CreateMemoryResponseBodyResultSkill(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

class CreateMemoryResponseBodyResultMemory(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

