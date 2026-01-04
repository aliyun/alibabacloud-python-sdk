# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSnatTableEntriesRequest(DaraModel):
    def __init__(
        self,
        nat_gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        snat_ips: List[str] = None,
        source_cidr: str = None,
    ):
        # The ID of the Network Address Translation (NAT) gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The page number. Pages start from page **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. The maximum value is **100**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The ID of the SNAT entry.
        self.snat_entry_id = snat_entry_id
        # The name of the SNAT entry.
        self.snat_entry_name = snat_entry_name
        # The elastic IP address (EIP) specified in the SNAT entry.
        self.snat_ip = snat_ip
        # The information about the EIP specified in the SNAT entry.
        self.snat_ips = snat_ips
        # The source CIDR block specified in the SNAT entry.
        self.source_cidr = source_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.snat_ips is not None:
            result['SnatIps'] = self.snat_ips

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SnatIps') is not None:
            self.snat_ips = m.get('SnatIps')

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        return self

