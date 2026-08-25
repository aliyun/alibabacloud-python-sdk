# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class DeprovisionAccessConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.DeprovisionAccessConfigurationResponseBodyTasks] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task information.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.DeprovisionAccessConfigurationResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class DeprovisionAccessConfigurationResponseBodyTasks(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        origin_target_id: str = None,
        status: str = None,
        target_id: str = None,
        target_name: str = None,
        target_path: str = None,
        target_path_name: str = None,
        target_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        self.origin_target_id = origin_target_id
        # The task status. Valid values:
        # 
        # - InProgress: The task is running.
        # 
        # - Success: The task is successful.
        # 
        # - Failed: The task failed.
        self.status = status
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The path ID of the task object in the resource directory.
        self.target_path = target_path
        # The path name of the task object in the resource directory.
        self.target_path_name = target_path_name
        # The type of the task object. The value is fixed as RD-Account, which indicates the accounts in the resource directory.
        self.target_type = target_type
        # The task ID.
        self.task_id = task_id
        # The task type. The value is fixed as DeprovisionAccessConfiguration, which indicates that the access configuration is de-provisioned.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name

        if self.origin_target_id is not None:
            result['OriginTargetId'] = self.origin_target_id

        if self.status is not None:
            result['Status'] = self.status

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.target_path_name is not None:
            result['TargetPathName'] = self.target_path_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')

        if m.get('OriginTargetId') is not None:
            self.origin_target_id = m.get('OriginTargetId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('TargetPathName') is not None:
            self.target_path_name = m.get('TargetPathName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

