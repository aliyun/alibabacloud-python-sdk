# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBlackholeStatusRequest(DaraModel):
    def __init__(
        self,
        blackhole_status: str = None,
        instance_id: str = None,
    ):
        # The action that you want to perform on the instance. Set the value to **undo**, which indicates that you want to deactivate blackhole filtering.
        # 
        # This parameter is required.
        self.blackhole_status = blackhole_status
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blackhole_status is not None:
            result['BlackholeStatus'] = self.blackhole_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackholeStatus') is not None:
            self.blackhole_status = m.get('BlackholeStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

