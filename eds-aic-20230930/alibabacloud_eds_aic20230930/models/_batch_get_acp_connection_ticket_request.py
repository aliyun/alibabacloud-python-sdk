# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class BatchGetAcpConnectionTicketRequest(DaraModel):
    def __init__(
        self,
        connection_mode: str = None,
        end_user_id: str = None,
        instance_group_id: str = None,
        instance_ids: List[str] = None,
        instance_tasks: List[main_models.BatchGetAcpConnectionTicketRequestInstanceTasks] = None,
        ports: List[str] = None,
    ):
        # The connection mode.
        self.connection_mode = connection_mode
        # The ID of the assigned user. If you do not specify this parameter, the system user assigned in the background is used to obtain the ticket.
        # 
        # <props="china">
        # The usage of this parameter varies based on the Cloud Phone edition and the instance streaming mode:
        # 
        # - Cloud Phone Instance Edition or Cloud Phone Matrix Edition (preemptive mode): You can obtain a `Ticket` only by using the same `EnduserId`.
        # - Cloud Phone Matrix Edition (collaborative mode): You can pass different `EnduserId` values to obtain `Ticket` values and stream for different users (up to 5) at the same time. You can pass only one `EnduserId` at a time.
        # 
        # > You can define the instance streaming mode by using the `StreamMode` parameter of the `ModifyCloudPhoneNode` operation.
        self.end_user_id = end_user_id
        # The instance group ID.
        self.instance_group_id = instance_group_id
        # The list of Cloud Phone instance IDs. You can specify 1 to 100 IDs.
        self.instance_ids = instance_ids
        # The instance connection tasks. This parameter is used to query whether the ticket retrieval task is completed.
        self.instance_tasks = instance_tasks
        # The list of custom connection ports.
        self.ports = ports

    def validate(self):
        if self.instance_tasks:
            for v1 in self.instance_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        result['InstanceTasks'] = []
        if self.instance_tasks is not None:
            for k1 in self.instance_tasks:
                result['InstanceTasks'].append(k1.to_map() if k1 else None)

        if self.ports is not None:
            result['Ports'] = self.ports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        self.instance_tasks = []
        if m.get('InstanceTasks') is not None:
            for k1 in m.get('InstanceTasks'):
                temp_model = main_models.BatchGetAcpConnectionTicketRequestInstanceTasks()
                self.instance_tasks.append(temp_model.from_map(k1))

        if m.get('Ports') is not None:
            self.ports = m.get('Ports')

        return self

class BatchGetAcpConnectionTicketRequestInstanceTasks(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

