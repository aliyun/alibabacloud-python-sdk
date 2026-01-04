# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetVpcPrefixListEntriesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        next_token: str = None,
        prefix_list_entry: List[main_models.GetVpcPrefixListEntriesResponseBodyPrefixListEntry] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries.
        self.count = count
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value indicates the token that is used for the next request to retrieve a new page of results.
        self.next_token = next_token
        # The information about the prefix list.
        self.prefix_list_entry = prefix_list_entry
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.prefix_list_entry:
            for v1 in self.prefix_list_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PrefixListEntry'] = []
        if self.prefix_list_entry is not None:
            for k1 in self.prefix_list_entry:
                result['PrefixListEntry'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.prefix_list_entry = []
        if m.get('PrefixListEntry') is not None:
            for k1 in m.get('PrefixListEntry'):
                temp_model = main_models.GetVpcPrefixListEntriesResponseBodyPrefixListEntry()
                self.prefix_list_entry.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetVpcPrefixListEntriesResponseBodyPrefixListEntry(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
        prefix_list_id: str = None,
        region_id: str = None,
    ):
        # The CIDR blocks specified in the prefix list.
        self.cidr = cidr
        # The description of the prefix list.
        self.description = description
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The region ID of the prefix list.
        self.region_id = region_id

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

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

