# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetMemoryTaskResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetMemoryTaskResponseBodyResult = None,
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
            temp_model = main_models.GetMemoryTaskResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetMemoryTaskResponseBodyResult(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        memory_ids: List[str] = None,
        skill_ids: List[str] = None,
        status: str = None,
        task_id: str = None,
    ):
        self.error_message = error_message
        self.memory_ids = memory_ids
        self.skill_ids = skill_ids
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['error_message'] = self.error_message

        if self.memory_ids is not None:
            result['memory_ids'] = self.memory_ids

        if self.skill_ids is not None:
            result['skill_ids'] = self.skill_ids

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')

        if m.get('memory_ids') is not None:
            self.memory_ids = m.get('memory_ids')

        if m.get('skill_ids') is not None:
            self.skill_ids = m.get('skill_ids')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

