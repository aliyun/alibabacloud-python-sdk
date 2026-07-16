# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeZonesRequest(DaraModel):
    def __init__(
        self,
        cross_region: bool = None,
        cross_region_side: str = None,
        region_id: str = None,
        service_resource_type: str = None,
    ):
        # Specifies whether this is a cross-region scenario. Default value: false.
        self.cross_region = cross_region
        # Specifies whether to query the active zones for the initiator side or the service side in a cross-region connection. Valid values:
        # - **Endpoint** (default): endpoint.
        # - **EndpointService**: endpoint service.
        # 
        # > This parameter takes effect only when CrossRegion is set to true.
        self.cross_region_side = cross_region_side
        # The ID of the region where the zones reside. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The zones supported by PrivateLink in a region depend on the backend service resource type. You can specify the service resource type when querying the zones supported by PrivateLink. Valid values:
        # 
        # - **slb** (default): Classic Load Balancer (CLB), the service resource type is classic load balancing.
        # - **alb**: Application Load Balancer (ALB), the service resource type is application load balancing.
        # - **nlb**: Network Load Balancer (NLB), the service resource type is network load balancing.
        # - **gwlb**: Gateway Load Balancer (GWLB), the service resource type is gateway load balancing.
        self.service_resource_type = service_resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_region is not None:
            result['CrossRegion'] = self.cross_region

        if self.cross_region_side is not None:
            result['CrossRegionSide'] = self.cross_region_side

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossRegion') is not None:
            self.cross_region = m.get('CrossRegion')

        if m.get('CrossRegionSide') is not None:
            self.cross_region_side = m.get('CrossRegionSide')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')

        return self

