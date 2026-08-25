# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class CreateAccessAssignmentResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: main_models.CreateAccessAssignmentResponseBodyTask = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried task.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task is not None:
            result['Task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Task') is not None:
            temp_model = main_models.CreateAccessAssignmentResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self



class CreateAccessAssignmentResponseBodyTask(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        origin_target_id: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
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
        # The ID of the CloudSSO identity.
        self.principal_id = principal_id
        # The name of the CloudSSO identity.
        self.principal_name = principal_name
        # The type of the CloudSSO identity. Valid values:
        # 
        # - User
        # 
        # - Group
        self.principal_type = principal_type
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
        # The ID of the job.
        self.task_id = task_id
        # The task type. The value is fixed as CreateAccessAssignment, which indicates that access permissions on an account in your resource directory are assigned.
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

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

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

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

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

