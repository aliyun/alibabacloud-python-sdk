# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridCloudSdkPullinStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mid: str = None,
        pullin_status: str = None,
    ):
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstanceInfo](https://help.aliyun.com/document_detail/140857.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the SDK.
        # 
        # This parameter is required.
        self.mid = mid
        # The status of traffic redirection. Valid values:
        # 
        # *   **on**
        # *   **off**
        # 
        # This parameter is required.
        self.pullin_status = pullin_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mid is not None:
            result['Mid'] = self.mid

        if self.pullin_status is not None:
            result['PullinStatus'] = self.pullin_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mid') is not None:
            self.mid = m.get('Mid')

        if m.get('PullinStatus') is not None:
            self.pullin_status = m.get('PullinStatus')

        return self

