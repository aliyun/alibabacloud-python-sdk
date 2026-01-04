# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyBlockStatusRequest(DaraModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        lines: List[str] = None,
        status: str = None,
    ):
        # The blocking period. Valid values: **15** to **43200**. Unit: minutes.
        # 
        # > If you set **Status** to **do**, you must also specify this parameter.
        self.duration = duration
        # The ID of the Anti-DDoS Proxy (Chinese Mainland) instance to manage.
        # 
        # >  You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all Anti-DDoS Proxy instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # An array consisting of the Internet service provider (ISP) lines from which traffic is blocked.
        # 
        # This parameter is required.
        self.lines = lines
        # Specifies the status of the Diversion from Origin Server policy. Valid values:
        # 
        # *   **do**: enables the policy.
        # *   **undo**: disables the policy.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lines is not None:
            result['Lines'] = self.lines

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lines') is not None:
            self.lines = m.get('Lines')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

