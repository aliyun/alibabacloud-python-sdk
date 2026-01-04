# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAsyncTaskRequest(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        task_params: str = None,
        task_type: int = None,
    ):
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The details of the asynchronous export task. The value is a JSON string. The field in the value varies with **TaskType**.
        # 
        # If **TaskType** is set to **1**, **3**, **4**, **5**, or **6**, the following filed is returned:
        # 
        # *   **instanceId**: the ID of the instance. This field is required and must be of the STRING type.
        # 
        # If **TaskType** is set to **2**, the following field is returned:
        # 
        # *   **domain**: the domain name of the website, which must be of the STRING type. If you do not specify this field, the forwarding rules of all websites are exported.
        # 
        # This parameter is required.
        self.task_params = task_params
        # The type of the asynchronous export task that you want to create. Valid values:
        # 
        # *   **1**: the task to export the port forwarding rules of an instance
        # *   **2**: the task to export the forwarding rules of a website protected by an instance
        # *   **3**: the task to export the session persistence and health check settings of an instance
        # *   **4**: the task to export the anti-DDoS mitigation policies of an instance
        # *   **5**: the task to download the blacklist for destination IP addresses of an instance
        # *   **6**: the task to download the whitelist for destination IP addresses of an instance
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.task_params is not None:
            result['TaskParams'] = self.task_params

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

