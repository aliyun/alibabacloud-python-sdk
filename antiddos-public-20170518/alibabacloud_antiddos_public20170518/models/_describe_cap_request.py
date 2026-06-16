# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCapRequest(DaraModel):
    def __init__(
        self,
        beg_time: int = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
    ):
        # The start time of the DDoS attack event. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > You can call the [DescribeDdosEventList](https://help.aliyun.com/document_detail/354236.html) operation to query the start time of each DDoS attack event that occurred on an asset.
        # 
        # This parameter is required.
        self.beg_time = beg_time
        # The region ID of the asset that is under DDoS attacks. The asset is assigned a public IP address.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The ID of the asset that is under DDoS attacks.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset that is under DDoS attacks. The asset is assigned a public IP address. Valid values:
        # 
        # - **ecs**: an Elastic Compute Service (ECS) instance.
        # 
        # - **slb**: a Server Load Balancer (SLB) instance.
        # 
        # - **eip**: an elastic IP address (EIP).
        # 
        # - **ipv6**: an IPv6 gateway.
        # 
        # - **swas**: a simple application server.
        # 
        # - **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # 
        # - **ga_basic**: a Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The public IP address of the asset that is under DDoS attacks.
        self.internet_ip = internet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beg_time is not None:
            result['BegTime'] = self.beg_time

        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BegTime') is not None:
            self.beg_time = m.get('BegTime')

        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        return self

