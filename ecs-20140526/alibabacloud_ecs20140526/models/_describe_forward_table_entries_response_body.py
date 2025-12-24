# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeForwardTableEntriesResponseBody(DaraModel):
    def __init__(
        self,
        forward_table_entries: main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntries = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.forward_table_entries = forward_table_entries
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.forward_table_entries:
            self.forward_table_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_table_entries is not None:
            result['ForwardTableEntries'] = self.forward_table_entries.to_map()

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
        if m.get('ForwardTableEntries') is not None:
            temp_model = main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntries()
            self.forward_table_entries = temp_model.from_map(m.get('ForwardTableEntries'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeForwardTableEntriesResponseBodyForwardTableEntries(DaraModel):
    def __init__(
        self,
        forward_table_entry: List[main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntriesForwardTableEntry] = None,
    ):
        self.forward_table_entry = forward_table_entry

    def validate(self):
        if self.forward_table_entry:
            for v1 in self.forward_table_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ForwardTableEntry'] = []
        if self.forward_table_entry is not None:
            for k1 in self.forward_table_entry:
                result['ForwardTableEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forward_table_entry = []
        if m.get('ForwardTableEntry') is not None:
            for k1 in m.get('ForwardTableEntry'):
                temp_model = main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntriesForwardTableEntry()
                self.forward_table_entry.append(temp_model.from_map(k1))

        return self

class DescribeForwardTableEntriesResponseBodyForwardTableEntriesForwardTableEntry(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_id: str = None,
        forward_table_id: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        status: str = None,
    ):
        self.external_ip = external_ip
        self.external_port = external_port
        self.forward_entry_id = forward_entry_id
        self.forward_table_id = forward_table_id
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id

        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')

        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

