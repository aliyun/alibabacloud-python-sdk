# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeDnatEntriesResponseBody(DaraModel):
    def __init__(
        self,
        dnat_entries: main_models.DescribeDnatEntriesResponseBodyDnatEntries = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dnat_entries = dnat_entries
        # The page number of the returned page. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned per page. Default value: **10**. Maximum value: **50**.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dnat_entries:
            self.dnat_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dnat_entries is not None:
            result['DnatEntries'] = self.dnat_entries.to_map()

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
        if m.get('DnatEntries') is not None:
            temp_model = main_models.DescribeDnatEntriesResponseBodyDnatEntries()
            self.dnat_entries = temp_model.from_map(m.get('DnatEntries'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDnatEntriesResponseBodyDnatEntries(DaraModel):
    def __init__(
        self,
        dnat_entry: List[main_models.DescribeDnatEntriesResponseBodyDnatEntriesDnatEntry] = None,
    ):
        self.dnat_entry = dnat_entry

    def validate(self):
        if self.dnat_entry:
            for v1 in self.dnat_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DnatEntry'] = []
        if self.dnat_entry is not None:
            for k1 in self.dnat_entry:
                result['DnatEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dnat_entry = []
        if m.get('DnatEntry') is not None:
            for k1 in m.get('DnatEntry'):
                temp_model = main_models.DescribeDnatEntriesResponseBodyDnatEntriesDnatEntry()
                self.dnat_entry.append(temp_model.from_map(k1))

        return self

class DescribeDnatEntriesResponseBodyDnatEntriesDnatEntry(DaraModel):
    def __init__(
        self,
        dnat_entry_id: str = None,
        external_ip: str = None,
        external_port: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        sag_id: str = None,
        type: str = None,
    ):
        self.dnat_entry_id = dnat_entry_id
        self.external_ip = external_ip
        self.external_port = external_port
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.sag_id = sag_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dnat_entry_id is not None:
            result['DnatEntryId'] = self.dnat_entry_id

        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnatEntryId') is not None:
            self.dnat_entry_id = m.get('DnatEntryId')

        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

