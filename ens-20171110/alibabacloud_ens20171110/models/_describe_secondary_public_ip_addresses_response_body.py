# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSecondaryPublicIpAddressesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        secondary_public_ip_addresses: List[main_models.DescribeSecondaryPublicIpAddressesResponseBodySecondaryPublicIpAddresses] = None,
        total_count: int = None,
    ):
        # The page number returned.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The array of returned secondary IP addresses.
        self.secondary_public_ip_addresses = secondary_public_ip_addresses
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.secondary_public_ip_addresses:
            for v1 in self.secondary_public_ip_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecondaryPublicIpAddresses'] = []
        if self.secondary_public_ip_addresses is not None:
            for k1 in self.secondary_public_ip_addresses:
                result['SecondaryPublicIpAddresses'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.secondary_public_ip_addresses = []
        if m.get('SecondaryPublicIpAddresses') is not None:
            for k1 in m.get('SecondaryPublicIpAddresses'):
                temp_model = main_models.DescribeSecondaryPublicIpAddressesResponseBodySecondaryPublicIpAddresses()
                self.secondary_public_ip_addresses.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSecondaryPublicIpAddressesResponseBodySecondaryPublicIpAddresses(DaraModel):
    def __init__(
        self,
        cidr_mask: int = None,
        creation_time: str = None,
        ens_region_id: str = None,
        gateway: str = None,
        ip_version: str = None,
        isp: str = None,
        secondary_public_ip_address: str = None,
        secondary_public_ip_id: str = None,
    ):
        # The subnet mask of the CIDR block.
        self.cidr_mask = cidr_mask
        # The time when the secondary public IP address was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The gateway.
        self.gateway = gateway
        # The version of the IP address. Valid values:
        # 
        # *   **ipv4**
        # *   **ipv6**
        self.ip_version = ip_version
        # The Internet service provider. Valid values:
        # 
        # *   cmcc: China Mobile.
        # *   unicom: China Unicom.
        # *   telecom: China Telecom.
        self.isp = isp
        # The secondary public IP address.
        self.secondary_public_ip_address = secondary_public_ip_address
        # The ID of the secondary public IP address.
        self.secondary_public_ip_id = secondary_public_ip_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_mask is not None:
            result['CidrMask'] = self.cidr_mask

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.secondary_public_ip_address is not None:
            result['SecondaryPublicIpAddress'] = self.secondary_public_ip_address

        if self.secondary_public_ip_id is not None:
            result['SecondaryPublicIpId'] = self.secondary_public_ip_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrMask') is not None:
            self.cidr_mask = m.get('CidrMask')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('SecondaryPublicIpAddress') is not None:
            self.secondary_public_ip_address = m.get('SecondaryPublicIpAddress')

        if m.get('SecondaryPublicIpId') is not None:
            self.secondary_public_ip_id = m.get('SecondaryPublicIpId')

        return self

