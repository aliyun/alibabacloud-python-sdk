# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIpDdosThresholdRequest(DaraModel):
    def __init__(
        self,
        ddos_region_id: str = None,
        ddos_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
    ):
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The type of the threshold. Valid values:
        # 
        # - **defense**: traffic scrubbing threshold
        # 
        # - **blackhole**: DDoS mitigation threshold
        # 
        # This parameter is required.
        self.ddos_type = ddos_type
        # The ID of the asset.
        # 
        # > You can call the [DescribeInstanceIpAddress](https://help.aliyun.com/document_detail/429562.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset that is assigned a public IP address. Valid values:
        # 
        # - **ecs**: ECS instances.
        # 
        # - **slb**: SLB instances.
        # 
        # - **eip**: EIPs.
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
        # The IP address of the asset.
        # 
        # This parameter is required.
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        return self

