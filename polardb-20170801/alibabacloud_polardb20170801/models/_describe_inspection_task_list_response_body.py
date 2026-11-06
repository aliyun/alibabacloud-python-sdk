# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeInspectionTaskListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_lists: List[main_models.DescribeInspectionTaskListResponseBodyTaskLists] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of inspection tasks.
        self.task_lists = task_lists

    def validate(self):
        if self.task_lists:
            for v1 in self.task_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskLists'] = []
        if self.task_lists is not None:
            for k1 in self.task_lists:
                result['TaskLists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_lists = []
        if m.get('TaskLists') is not None:
            for k1 in m.get('TaskLists'):
                temp_model = main_models.DescribeInspectionTaskListResponseBodyTaskLists()
                self.task_lists.append(temp_model.from_map(k1))

        return self

class DescribeInspectionTaskListResponseBodyTaskLists(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        cron_expression: str = None,
        dbcluster_ids: str = None,
        expire_time: str = None,
        task_description: str = None,
        task_id: str = None,
    ):
        # The date when the task was last modified.
        self.create_time = create_time
        # The cron expression for periodic inspections.
        self.cron_expression = cron_expression
        # The IDs of the PolarDB clusters to be inspected. Separate multiple IDs with commas.
        self.dbcluster_ids = dbcluster_ids
        # The expiration date of the inspection task.
        self.expire_time = expire_time
        # The description of the inspection task.
        self.task_description = task_description
        # The ID of the inspection task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.task_description is not None:
            result['TaskDescription'] = self.task_description

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

