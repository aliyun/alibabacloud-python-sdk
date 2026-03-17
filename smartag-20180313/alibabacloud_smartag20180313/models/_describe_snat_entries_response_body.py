# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSnatEntriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snat_entries: main_models.DescribeSnatEntriesResponseBodySnatEntries = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.snat_entries = snat_entries
        # The total number of SNAT entries.
        self.total_count = total_count

    def validate(self):
        if self.snat_entries:
            self.snat_entries.validate()

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

        if self.snat_entries is not None:
            result['SnatEntries'] = self.snat_entries.to_map()

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

        if m.get('SnatEntries') is not None:
            temp_model = main_models.DescribeSnatEntriesResponseBodySnatEntries()
            self.snat_entries = temp_model.from_map(m.get('SnatEntries'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSnatEntriesResponseBodySnatEntries(DaraModel):
    def __init__(
        self,
        snat_entry: List[main_models.DescribeSnatEntriesResponseBodySnatEntriesSnatEntry] = None,
    ):
        self.snat_entry = snat_entry

    def validate(self):
        if self.snat_entry:
            for v1 in self.snat_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnatEntry'] = []
        if self.snat_entry is not None:
            for k1 in self.snat_entry:
                result['SnatEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snat_entry = []
        if m.get('SnatEntry') is not None:
            for k1 in m.get('SnatEntry'):
                temp_model = main_models.DescribeSnatEntriesResponseBodySnatEntriesSnatEntry()
                self.snat_entry.append(temp_model.from_map(k1))

        return self

class DescribeSnatEntriesResponseBodySnatEntriesSnatEntry(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        create_time: int = None,
        instance_id: str = None,
        snat_ip: str = None,
    ):
        self.cidr_block = cidr_block
        self.create_time = create_time
        self.instance_id = instance_id
        self.snat_ip = snat_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        return self

