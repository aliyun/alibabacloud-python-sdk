# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLniPrivateIpAddressRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        enable_page: bool = None,
        ip: str = None,
        ip_name: str = None,
        network_interface_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The description of the variable.
        self.description = description
        # Whether pagination is required
        self.enable_page = enable_page
        # network interface controller IP address
        self.ip = ip
        # IP unique identifier
        self.ip_name = ip_name
        # Lingjun network interface controller ID
        self.network_interface_id = network_interface_id
        # The page number of the returned page.
        self.page_number = page_number
        # Obtain the index number of the current mouse click for an animation
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

