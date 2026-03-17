# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQosAttributeRequest(DaraModel):
    def __init__(
        self,
        qos_id: str = None,
        region_id: str = None,
    ):
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The ID of the region where the QoS policy is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

