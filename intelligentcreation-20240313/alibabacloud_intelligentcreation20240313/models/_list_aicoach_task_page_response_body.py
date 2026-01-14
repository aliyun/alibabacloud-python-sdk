# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class ListAICoachTaskPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[main_models.ListAICoachTaskPageResponseBodyTaskList] = None,
        total: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task_list = task_list
        self.total = total

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['taskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['taskList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.task_list = []
        if m.get('taskList') is not None:
            for k1 in m.get('taskList'):
                temp_model = main_models.ListAICoachTaskPageResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAICoachTaskPageResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        finish_time: str = None,
        gmt_create: str = None,
        status: str = None,
        student_id: str = None,
        task_id: str = None,
    ):
        self.finish_time = finish_time
        self.gmt_create = gmt_create
        self.status = status
        self.student_id = student_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.status is not None:
            result['status'] = self.status

        if self.student_id is not None:
            result['studentId'] = self.student_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('studentId') is not None:
            self.student_id = m.get('studentId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

