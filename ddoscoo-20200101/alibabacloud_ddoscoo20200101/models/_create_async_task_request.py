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
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management. If this parameter is empty, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The task parameter information. The value is a JSON-formatted string. The required task parameters vary based on the value of **TaskType**.
        # 
        # If **TaskType** is set to **1**, **3**, **4**, **5**, or **6**, the task parameters use the following structure:
        # - **instanceId**: String type. Required. The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # 
        # If **TaskType** is set to **2**, the task parameters use the following structure:
        # - **domain**: String type. Optional. The domain name of the website. If this parameter is not specified, the forwarding rules of all websites are exported.
        # 
        # This parameter is required.
        self.task_params = task_params
        # The type of the export task to create. Valid values:
        # 
        # - **1**: Layer 4 export task. Exports port forwarding rules of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **2**: Layer 7 export task. Exports website forwarding rules.
        # - **3**: Session persistence and health check export task. Exports session persistence and health check configurations of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **4**: DDoS mitigation policy export task. Exports DDoS mitigation policy configurations of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **5**: Blacklist (destination IP address-based) download task. Exports blacklisted IP addresses for the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # - **6**: Whitelist (destination IP address-based) download task. Exports whitelisted IP addresses for the Anti-DDoS Pro or Anti-DDoS Premium instance.
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

