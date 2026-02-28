# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLeniPrivateIpAddressesRequest(DaraModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        ip_name: str = None,
        page_number: int = None,
        page_size: int = None,
        private_ip_address: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        # Lingjun Elastic Network Interface ID.
        self.elastic_network_interface_id = elastic_network_interface_id
        # Lingjun Elastic Network Interface secondary private IP unique identifier.
        self.ip_name = ip_name
        # The page number returned.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # Lingjun Elastic Network Interface secondary private IP.
        self.private_ip_address = private_ip_address
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The status of the image build command risk.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id

        if self.ip_name is not None:
            result['IpName'] = self.ip_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')

        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

