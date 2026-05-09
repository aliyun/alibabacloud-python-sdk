# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBatchTaskResponseBody(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        request_id: str = None,
        status: str = None,
        sub_tasks: List[main_models.DescribeBatchTaskResponseBodySubTasks] = None,
        success_count: int = None,
        task_begin: str = None,
        task_end: str = None,
        task_name: str = None,
        task_type: str = None,
        total_count: int = None,
    ):
        self.batch_id = batch_id
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.sub_tasks = sub_tasks
        self.success_count = success_count
        self.task_begin = task_begin
        self.task_end = task_end
        self.task_name = task_name
        self.task_type = task_type
        self.total_count = total_count

    def validate(self):
        if self.sub_tasks:
            for v1 in self.sub_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k1 in self.sub_tasks:
                result['SubTasks'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.task_begin is not None:
            result['TaskBegin'] = self.task_begin

        if self.task_end is not None:
            result['TaskEnd'] = self.task_end

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k1 in m.get('SubTasks'):
                temp_model = main_models.DescribeBatchTaskResponseBodySubTasks()
                self.sub_tasks.append(temp_model.from_map(k1))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TaskBegin') is not None:
            self.task_begin = m.get('TaskBegin')

        if m.get('TaskEnd') is not None:
            self.task_end = m.get('TaskEnd')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBatchTaskResponseBodySubTasks(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        instance_id: str = None,
        status: str = None,
        task_begin: str = None,
        task_end: str = None,
        task_id: str = None,
    ):
        self.error_msg = error_msg
        self.instance_id = instance_id
        self.status = status
        self.task_begin = task_begin
        self.task_end = task_end
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_begin is not None:
            result['TaskBegin'] = self.task_begin

        if self.task_end is not None:
            result['TaskEnd'] = self.task_end

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskBegin') is not None:
            self.task_begin = m.get('TaskBegin')

        if m.get('TaskEnd') is not None:
            self.task_end = m.get('TaskEnd')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

