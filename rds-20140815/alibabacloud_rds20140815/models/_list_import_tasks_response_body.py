# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ListImportTasksResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListImportTasksResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListImportTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListImportTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        db_version: str = None,
        status: str = None,
        target_instance_name: str = None,
        task_id: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        self.created_time = created_time
        self.db_version = db_version
        self.status = status
        self.target_instance_name = target_instance_name
        self.task_id = task_id
        self.task_name = task_name
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.status is not None:
            result['Status'] = self.status

        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

