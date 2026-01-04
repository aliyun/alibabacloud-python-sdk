# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIPv6TranslatorEntriesResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6translator_entries: main_models.DescribeIPv6TranslatorEntriesResponseBodyIpv6TranslatorEntries = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The IPv6 mapping entries that are queried.
        self.ipv_6translator_entries = ipv_6translator_entries
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipv_6translator_entries:
            self.ipv_6translator_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6translator_entries is not None:
            result['Ipv6TranslatorEntries'] = self.ipv_6translator_entries.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6TranslatorEntries') is not None:
            temp_model = main_models.DescribeIPv6TranslatorEntriesResponseBodyIpv6TranslatorEntries()
            self.ipv_6translator_entries = temp_model.from_map(m.get('Ipv6TranslatorEntries'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIPv6TranslatorEntriesResponseBodyIpv6TranslatorEntries(DaraModel):
    def __init__(
        self,
        ipv_6translator_entry: List[main_models.DescribeIPv6TranslatorEntriesResponseBodyIpv6TranslatorEntriesIpv6TranslatorEntry] = None,
    ):
        self.ipv_6translator_entry = ipv_6translator_entry

    def validate(self):
        if self.ipv_6translator_entry:
            for v1 in self.ipv_6translator_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6TranslatorEntry'] = []
        if self.ipv_6translator_entry is not None:
            for k1 in self.ipv_6translator_entry:
                result['Ipv6TranslatorEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6translator_entry = []
        if m.get('Ipv6TranslatorEntry') is not None:
            for k1 in m.get('Ipv6TranslatorEntry'):
                temp_model = main_models.DescribeIPv6TranslatorEntriesResponseBodyIpv6TranslatorEntriesIpv6TranslatorEntry()
                self.ipv_6translator_entry.append(temp_model.from_map(k1))

        return self

class DescribeIPv6TranslatorEntriesResponseBodyIpv6TranslatorEntriesIpv6TranslatorEntry(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_status: str = None,
        acl_type: str = None,
        allocate_ipv_6addr: str = None,
        allocate_ipv_6port: int = None,
        backend_ipv_4addr: str = None,
        backend_ipv_4port: str = None,
        entry_bandwidth: str = None,
        entry_description: str = None,
        entry_name: str = None,
        entry_status: str = None,
        ipv_6translator_entry_id: str = None,
        ipv_6translator_id: str = None,
        region_id: str = None,
        trans_protocol: str = None,
    ):
        # The ID of the associated ACL.
        self.acl_id = acl_id
        # Indicates whether ACLs are enabled.
        self.acl_status = acl_status
        # The ACL type.
        # 
        # *   **white**: a whitelist. IPv6 addresses in the ACL are allowed to access backend services.
        # *   **black**: a blacklist. IPv6 addresses in the ACL are not allowed to access backend services.
        self.acl_type = acl_type
        # The IPv6 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_6addr = allocate_ipv_6addr
        # The port used by the IPv6 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_6port = allocate_ipv_6port
        # The public IP address of the backend IPv4 server.
        self.backend_ipv_4addr = backend_ipv_4addr
        # The public IPv4 port used by the IPv4 server that needs to provide IPv6 access.
        self.backend_ipv_4port = backend_ipv_4port
        # The bandwidth specified in the IPv6 mapping entry.
        self.entry_bandwidth = entry_bandwidth
        # The description of the IPv6 mapping entry.
        self.entry_description = entry_description
        # The name of the IPv6 mapping entry.
        self.entry_name = entry_name
        # The status of the IPv6 mapping entry.
        self.entry_status = entry_status
        # The ID of the IPv6 mapping entry.
        self.ipv_6translator_entry_id = ipv_6translator_entry_id
        # The ID of the IPv6 Translation Service instance to which the IPv6 mapping entry belongs.
        self.ipv_6translator_id = ipv_6translator_id
        # The region of the IPv6 Translation Service instance.
        self.region_id = region_id
        # The protocol.
        self.trans_protocol = trans_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.allocate_ipv_6addr is not None:
            result['AllocateIpv6Addr'] = self.allocate_ipv_6addr

        if self.allocate_ipv_6port is not None:
            result['AllocateIpv6Port'] = self.allocate_ipv_6port

        if self.backend_ipv_4addr is not None:
            result['BackendIpv4Addr'] = self.backend_ipv_4addr

        if self.backend_ipv_4port is not None:
            result['BackendIpv4Port'] = self.backend_ipv_4port

        if self.entry_bandwidth is not None:
            result['EntryBandwidth'] = self.entry_bandwidth

        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description

        if self.entry_name is not None:
            result['EntryName'] = self.entry_name

        if self.entry_status is not None:
            result['EntryStatus'] = self.entry_status

        if self.ipv_6translator_entry_id is not None:
            result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id

        if self.ipv_6translator_id is not None:
            result['Ipv6TranslatorId'] = self.ipv_6translator_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.trans_protocol is not None:
            result['TransProtocol'] = self.trans_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('AllocateIpv6Addr') is not None:
            self.allocate_ipv_6addr = m.get('AllocateIpv6Addr')

        if m.get('AllocateIpv6Port') is not None:
            self.allocate_ipv_6port = m.get('AllocateIpv6Port')

        if m.get('BackendIpv4Addr') is not None:
            self.backend_ipv_4addr = m.get('BackendIpv4Addr')

        if m.get('BackendIpv4Port') is not None:
            self.backend_ipv_4port = m.get('BackendIpv4Port')

        if m.get('EntryBandwidth') is not None:
            self.entry_bandwidth = m.get('EntryBandwidth')

        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')

        if m.get('EntryName') is not None:
            self.entry_name = m.get('EntryName')

        if m.get('EntryStatus') is not None:
            self.entry_status = m.get('EntryStatus')

        if m.get('Ipv6TranslatorEntryId') is not None:
            self.ipv_6translator_entry_id = m.get('Ipv6TranslatorEntryId')

        if m.get('Ipv6TranslatorId') is not None:
            self.ipv_6translator_id = m.get('Ipv6TranslatorId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TransProtocol') is not None:
            self.trans_protocol = m.get('TransProtocol')

        return self

