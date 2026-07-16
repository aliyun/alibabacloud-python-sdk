# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDdosCountRequest(DaraModel):
    def __init__(
        self,
        ddos_region_id: str = None,
        instance_type: str = None,
    ):
        # The region ID of the asset to query.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The type of the asset to query. Valid values:
        # 
        # - **ecs**: Elastic Compute Service (ECS) instances.
        # 
        # - **slb**: Server Load Balancer (SLB) instances.
        # 
        # - **eip**: elastic IP addresses (EIPs).
        # 
        # - **ipv6**: IPv6 gateways.
        # 
        # - **swas**: simple application servers.
        # 
        # - **waf**: Web Application Firewall (WAF) instances of the Exclusive edition.
        # 
        # - **ga_basic**: Global Accelerator (GA) instances.
        # 
        # This parameter is required.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

