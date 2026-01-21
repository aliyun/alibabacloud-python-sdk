# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVpcEndpointAttributeRequest(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
        region_id: str = None,
    ):
        # The ID of the endpoint whose attributes you want to query.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The region ID of the endpoint whose attributes you want to query.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/448570.html) operation to query the most recent region list.
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
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

