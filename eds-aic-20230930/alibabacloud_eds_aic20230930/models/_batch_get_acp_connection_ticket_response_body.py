# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class BatchGetAcpConnectionTicketResponseBody(DaraModel):
    def __init__(
        self,
        instance_connection_models: List[main_models.BatchGetAcpConnectionTicketResponseBodyInstanceConnectionModels] = None,
        request_id: str = None,
    ):
        # The results of the instance connection tasks.
        self.instance_connection_models = instance_connection_models
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_connection_models:
            for v1 in self.instance_connection_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceConnectionModels'] = []
        if self.instance_connection_models is not None:
            for k1 in self.instance_connection_models:
                result['InstanceConnectionModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_connection_models = []
        if m.get('InstanceConnectionModels') is not None:
            for k1 in m.get('InstanceConnectionModels'):
                temp_model = main_models.BatchGetAcpConnectionTicketResponseBodyInstanceConnectionModels()
                self.instance_connection_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchGetAcpConnectionTicketResponseBodyInstanceConnectionModels(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        error_code: str = None,
        instance_id: str = None,
        persistent_app_instance_id: str = None,
        task_id: str = None,
        task_status: str = None,
        ticket: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.error_code = error_code
        # The ID of the cloud phone instance.
        self.instance_id = instance_id
        self.persistent_app_instance_id = persistent_app_instance_id
        # The ID of the task.
        self.task_id = task_id
        # The state of the task.
        self.task_status = task_status
        # The ticket used to connect to the cloud phone instance.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.persistent_app_instance_id is not None:
            result['PersistentAppInstanceId'] = self.persistent_app_instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PersistentAppInstanceId') is not None:
            self.persistent_app_instance_id = m.get('PersistentAppInstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

