# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceIpAddressRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ddos_region_id: str = None,
        ddos_status: str = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_name: str = None,
        instance_type: str = None,
        page_size: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The DDoS mitigation status of the asset. Valid values:
        # 
        # - **defense**: queries assets for which traffic scrubbing is performed.
        # 
        # - **blackhole**: queries assets for which blackhole filtering is triggered.
        self.ddos_status = ddos_status
        # The ID of the instance to which the asset is added.
        self.instance_id = instance_id
        # The IP address of the asset.
        self.instance_ip = instance_ip
        # The name of the asset.
        self.instance_name = instance_name
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
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

