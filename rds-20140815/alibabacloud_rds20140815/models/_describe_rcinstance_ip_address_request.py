# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCInstanceIpAddressRequest(DaraModel):
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
        region_id: str = None,
        resource_type: str = None,
    ):
        # The page number of the page to return. Default value: 1, which indicates that the first page is returned.
        self.current_page = current_page
        # The region ID of the assets that are assigned public IP addresses to query.
        self.ddos_region_id = ddos_region_id
        # The DDoS mitigation status of the assets that are assigned public IP addresses to query. Valid values:
        # 
        # - **defense**: Cleaning. Assets that are assigned public IP addresses for which Anti-DDoS Origin scrubs traffic are queried.
        # - **blackhole**: Black Hole Activated. Assets that are assigned public IP addresses that are in the blackhole filtering status are queried.
        self.ddos_status = ddos_status
        # The instance ID of the Custom instance to which the assets that are assigned public IP addresses belong.
        self.instance_id = instance_id
        # The IP address of the assets that are assigned public IP addresses to query.
        self.instance_ip = instance_ip
        # The name of the Custom instance to which the assets that are assigned public IP addresses belong.
        self.instance_name = instance_name
        # The instance type of the assets that are assigned public IP addresses to query. Set the value to **ecs**.
        self.instance_type = instance_type
        # Settings for paged query. The number of instances to return on each page for paging.
        self.page_size = page_size
        # The region ID of the Custom instance.
        self.region_id = region_id
        # The resource type. Set the value to **ecs**.
        self.resource_type = resource_type

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

