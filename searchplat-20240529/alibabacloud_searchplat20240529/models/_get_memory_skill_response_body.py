# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetMemorySkillResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetMemorySkillResponseBodyResult = None,
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
            temp_model = main_models.GetMemorySkillResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetMemorySkillResponseBodyResult(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        files: str = None,
        name: str = None,
        skill_id: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.files = files
        self.name = name
        self.skill_id = skill_id
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

        if self.files is not None:
            result['files'] = self.files

        if self.name is not None:
            result['name'] = self.name

        if self.skill_id is not None:
            result['skill_id'] = self.skill_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('files') is not None:
            self.files = m.get('files')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('skill_id') is not None:
            self.skill_id = m.get('skill_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

