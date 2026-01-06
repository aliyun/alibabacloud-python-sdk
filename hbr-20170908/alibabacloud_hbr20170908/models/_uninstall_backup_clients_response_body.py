# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class UninstallBackupClientsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_statuses: List[main_models.UninstallBackupClientsResponseBodyInstanceStatuses] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request is successful.
        self.code = code
        # The status of the ECS instance.
        self.instance_statuses = instance_statuses
        # The message that is returned. If the request is successful, a value of successful is returned. If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # *   true: The request is successful.
        # *   false: The request fails.
        self.success = success
        # The ID of the asynchronous job. You can call the DescribeTask operation to query the execution result of the asynchronous job.
        self.task_id = task_id

    def validate(self):
        if self.instance_statuses:
            for v1 in self.instance_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k1 in self.instance_statuses:
                result['InstanceStatuses'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k1 in m.get('InstanceStatuses'):
                temp_model = main_models.UninstallBackupClientsResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class UninstallBackupClientsResponseBodyInstanceStatuses(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        instance_id: str = None,
        valid_instance: bool = None,
    ):
        # The error code. Valid values:
        # 
        # *   If the value is empty, the request is successful.
        # *   **InstanceNotExists**: The ECS instance does not exist.
        # *   **InstanceNotRunning**: The ECS instance is not running.
        # *   **CloudAssistNotRunningOnInstance**: Cloud Assistant is unavailable.
        self.error_code = error_code
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # Indicates whether a backup client can be installed on the ECS instance.
        # 
        # *   true: A backup client can be installed on the ECS instance.
        # *   false: A backup client cannot be installed on the ECS instance.
        self.valid_instance = valid_instance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.valid_instance is not None:
            result['ValidInstance'] = self.valid_instance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ValidInstance') is not None:
            self.valid_instance = m.get('ValidInstance')

        return self

