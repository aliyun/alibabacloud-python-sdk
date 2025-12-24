# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class QueryPredictiveTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_infos: main_models.QueryPredictiveTaskInfoResponseBodyTaskInfos = None,
    ):
        self.request_id = request_id
        self.task_infos = task_infos

    def validate(self):
        if self.task_infos:
            self.task_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_infos is not None:
            result['TaskInfos'] = self.task_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskInfos') is not None:
            temp_model = main_models.QueryPredictiveTaskInfoResponseBodyTaskInfos()
            self.task_infos = temp_model.from_map(m.get('TaskInfos'))

        return self

class QueryPredictiveTaskInfoResponseBodyTaskInfos(DaraModel):
    def __init__(
        self,
        task_info: List[main_models.QueryPredictiveTaskInfoResponseBodyTaskInfosTaskInfo] = None,
    ):
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            for v1 in self.task_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskInfo'] = []
        if self.task_info is not None:
            for k1 in self.task_info:
                result['TaskInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_info = []
        if m.get('TaskInfo') is not None:
            for k1 in m.get('TaskInfo'):
                temp_model = main_models.QueryPredictiveTaskInfoResponseBodyTaskInfosTaskInfo()
                self.task_info.append(temp_model.from_map(k1))

        return self

class QueryPredictiveTaskInfoResponseBodyTaskInfosTaskInfo(DaraModel):
    def __init__(
        self,
        max_value: int = None,
        min_value: int = None,
        time: str = None,
    ):
        self.max_value = max_value
        self.min_value = min_value
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

