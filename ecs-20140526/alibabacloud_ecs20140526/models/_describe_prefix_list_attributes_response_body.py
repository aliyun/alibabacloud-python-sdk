# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePrefixListAttributesResponseBody(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        creation_time: str = None,
        description: str = None,
        entries: main_models.DescribePrefixListAttributesResponseBodyEntries = None,
        max_entries: int = None,
        prefix_list_id: str = None,
        prefix_list_name: str = None,
        request_id: str = None,
    ):
        # The IP address family of the prefix list. Valid values:
        # 
        # *   IPv4
        # *   IPv6
        self.address_family = address_family
        # The time when the prefix list was created.
        self.creation_time = creation_time
        # The description of the prefix list.
        self.description = description
        # Details about the entries in the prefix list.
        self.entries = entries
        # The maximum number of entries in the prefix list.
        self.max_entries = max_entries
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The name of the prefix list.
        self.prefix_list_name = prefix_list_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            self.entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.entries is not None:
            result['Entries'] = self.entries.to_map()

        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Entries') is not None:
            temp_model = main_models.DescribePrefixListAttributesResponseBodyEntries()
            self.entries = temp_model.from_map(m.get('Entries'))

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePrefixListAttributesResponseBodyEntries(DaraModel):
    def __init__(
        self,
        entry: List[main_models.DescribePrefixListAttributesResponseBodyEntriesEntry] = None,
    ):
        self.entry = entry

    def validate(self):
        if self.entry:
            for v1 in self.entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entry'] = []
        if self.entry is not None:
            for k1 in self.entry:
                result['Entry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entry = []
        if m.get('Entry') is not None:
            for k1 in m.get('Entry'):
                temp_model = main_models.DescribePrefixListAttributesResponseBodyEntriesEntry()
                self.entry.append(temp_model.from_map(k1))

        return self

class DescribePrefixListAttributesResponseBodyEntriesEntry(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
    ):
        # The CIDR block in entry N.
        self.cidr = cidr
        # The description in entry N.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

