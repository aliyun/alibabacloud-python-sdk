# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribePrefixListsResponseBody(DaraModel):
    def __init__(
        self,
        prefix_list: List[main_models.DescribePrefixListsResponseBodyPrefixList] = None,
        request_id: str = None,
    ):
        # Details about the prefix lists.
        self.prefix_list = prefix_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.prefix_list:
            for v1 in self.prefix_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrefixList'] = []
        if self.prefix_list is not None:
            for k1 in self.prefix_list:
                result['PrefixList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prefix_list = []
        if m.get('PrefixList') is not None:
            for k1 in m.get('PrefixList'):
                temp_model = main_models.DescribePrefixListsResponseBodyPrefixList()
                self.prefix_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePrefixListsResponseBodyPrefixList(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        association_count: int = None,
        creation_time: str = None,
        description: str = None,
        max_entries: int = None,
        prefix_list_id: str = None,
        prefix_list_name: str = None,
    ):
        # The IP address family of the prefix list. Valid values:
        # 
        # *   IPv4
        # *   IPv6
        self.address_family = address_family
        # The number of associated resources.
        self.association_count = association_count
        # The creation time.
        self.creation_time = creation_time
        # The description.
        self.description = description
        # The maximum number of entries in the prefix list.
        self.max_entries = max_entries
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The name of the prefix list.
        self.prefix_list_name = prefix_list_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family

        if self.association_count is not None:
            result['AssociationCount'] = self.association_count

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

        if m.get('AssociationCount') is not None:
            self.association_count = m.get('AssociationCount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')

        return self

