# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class DeleteMemorySkillResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.DeleteMemorySkillResponseBodyResult = None,
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
            temp_model = main_models.DeleteMemorySkillResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class DeleteMemorySkillResponseBodyResult(DaraModel):
    def __init__(
        self,
        message: str = None,
        skill_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.skill_id = skill_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.skill_id is not None:
            result['skill_id'] = self.skill_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('skill_id') is not None:
            self.skill_id = m.get('skill_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

