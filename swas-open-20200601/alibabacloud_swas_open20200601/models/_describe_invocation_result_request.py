# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvocationResultRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        invoke_id: str = None,
        region_id: str = None,
    ):
        # The instance ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The command execution ID. You can call the [DescribeInvocations](https://help.aliyun.com/document_detail/439368.html) operation to query the InvokeId.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

