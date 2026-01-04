# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeSnatTableEntriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snat_table_entries: main_models.DescribeSnatTableEntriesResponseBodySnatTableEntries = None,
        total_count: int = None,
    ):
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details of SNAT entries.
        self.snat_table_entries = snat_table_entries
        # The number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.snat_table_entries:
            self.snat_table_entries.validate()

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

        if self.snat_table_entries is not None:
            result['SnatTableEntries'] = self.snat_table_entries.to_map()

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

        if m.get('SnatTableEntries') is not None:
            temp_model = main_models.DescribeSnatTableEntriesResponseBodySnatTableEntries()
            self.snat_table_entries = temp_model.from_map(m.get('SnatTableEntries'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSnatTableEntriesResponseBodySnatTableEntries(DaraModel):
    def __init__(
        self,
        snat_table_entry: List[main_models.DescribeSnatTableEntriesResponseBodySnatTableEntriesSnatTableEntry] = None,
    ):
        self.snat_table_entry = snat_table_entry

    def validate(self):
        if self.snat_table_entry:
            for v1 in self.snat_table_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnatTableEntry'] = []
        if self.snat_table_entry is not None:
            for k1 in self.snat_table_entry:
                result['SnatTableEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snat_table_entry = []
        if m.get('SnatTableEntry') is not None:
            for k1 in m.get('SnatTableEntry'):
                temp_model = main_models.DescribeSnatTableEntriesResponseBodySnatTableEntriesSnatTableEntry()
                self.snat_table_entry.append(temp_model.from_map(k1))

        return self

class DescribeSnatTableEntriesResponseBodySnatTableEntriesSnatTableEntry(DaraModel):
    def __init__(
        self,
        eip_affinity: str = None,
        nat_gateway_id: str = None,
        network_interface_id: str = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        snat_table_id: str = None,
        source_cidr: str = None,
        source_vswitch_id: str = None,
        status: str = None,
    ):
        self.eip_affinity = eip_affinity
        # The ID of the NAT gateway to which the SNAT entry belongs.
        self.nat_gateway_id = nat_gateway_id
        self.network_interface_id = network_interface_id
        # The ID of the SNAT entry.
        self.snat_entry_id = snat_entry_id
        # The name of the SNAT entry.
        self.snat_entry_name = snat_entry_name
        # *   When you query SNAT entries of Internet NAT gateways, this parameter indicates the EIP in an SNAT entry.
        # *   When you query SNAT entries of VPC NAT gateways, this parameter indicates the NAT IP address in an SNAT entry.
        self.snat_ip = snat_ip
        # The ID of the SNAT table to which the SNAT entry belongs.
        self.snat_table_id = snat_table_id
        # The source CIDR block specified in the SNAT entry.
        self.source_cidr = source_cidr
        # *   When you query SNAT entries of Internet NAT gateways, this parameter indicates the ID of the vSwitch that uses SNAT to access the Internet.
        # *   When you query SNAT entries of VPC NAT gateways, this parameter indicates the ID of the vSwitch that uses SNAT to access external networks.
        self.source_vswitch_id = source_vswitch_id
        # The status of the SNAT entry. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        # *   **Deleting**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_affinity is not None:
            result['EipAffinity'] = self.eip_affinity

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        if self.source_vswitch_id is not None:
            result['SourceVSwitchId'] = self.source_vswitch_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        if m.get('SourceVSwitchId') is not None:
            self.source_vswitch_id = m.get('SourceVSwitchId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

