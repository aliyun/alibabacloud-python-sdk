# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        service_resource_type: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The regions in which PrivateLink is available vary based on the service resource type. When you query the regions in which PrivateLink is available, you can specify a service resource type. Valid values:
        # 
        # - **slb** (default): indicates that the service resource type is Classic Load Balancer (CLB).
        # -  **alb**: indicates that the service resource type is Application Load Balancer (ALB).
        # - **nlb**: indicates that the service resource type is Network Load Balancer (NLB).
        # - **gwlb**: indicates that the service resource type is Gateway Load Balancer (GWLB).
        # 
        # - **ALL**: indicates all of the preceding service resource types.
        self.service_resource_type = service_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')

        return self

