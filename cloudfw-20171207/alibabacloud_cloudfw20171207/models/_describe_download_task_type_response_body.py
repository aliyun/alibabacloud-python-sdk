# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeDownloadTaskTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_type_array: List[main_models.DescribeDownloadTaskTypeResponseBodyTaskTypeArray] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The task types.
        self.task_type_array = task_type_array
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.task_type_array:
            for v1 in self.task_type_array:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskTypeArray'] = []
        if self.task_type_array is not None:
            for k1 in self.task_type_array:
                result['TaskTypeArray'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_type_array = []
        if m.get('TaskTypeArray') is not None:
            for k1 in m.get('TaskTypeArray'):
                temp_model = main_models.DescribeDownloadTaskTypeResponseBodyTaskTypeArray()
                self.task_type_array.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDownloadTaskTypeResponseBodyTaskTypeArray(DaraModel):
    def __init__(
        self,
        task_name: str = None,
        task_type: str = None,
    ):
        # The name of the task type.
        self.task_name = task_name
        # The type of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

