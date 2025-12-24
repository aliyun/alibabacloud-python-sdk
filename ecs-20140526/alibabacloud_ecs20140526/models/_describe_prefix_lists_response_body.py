# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePrefixListsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        prefix_lists: main_models.DescribePrefixListsResponseBodyPrefixLists = None,
        request_id: str = None,
    ):
        # The query token that is returned in this call. If the return value is empty, no more data is returned.
        self.next_token = next_token
        # Details about the prefix lists.
        self.prefix_lists = prefix_lists
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.prefix_lists:
            self.prefix_lists.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.prefix_lists is not None:
            result['PrefixLists'] = self.prefix_lists.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PrefixLists') is not None:
            temp_model = main_models.DescribePrefixListsResponseBodyPrefixLists()
            self.prefix_lists = temp_model.from_map(m.get('PrefixLists'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePrefixListsResponseBodyPrefixLists(DaraModel):
    def __init__(
        self,
        prefix_list: List[main_models.DescribePrefixListsResponseBodyPrefixListsPrefixList] = None,
    ):
        self.prefix_list = prefix_list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prefix_list = []
        if m.get('PrefixList') is not None:
            for k1 in m.get('PrefixList'):
                temp_model = main_models.DescribePrefixListsResponseBodyPrefixListsPrefixList()
                self.prefix_list.append(temp_model.from_map(k1))

        return self

class DescribePrefixListsResponseBodyPrefixListsPrefixList(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        association_count: int = None,
        creation_time: str = None,
        description: str = None,
        max_entries: int = None,
        prefix_list_id: str = None,
        prefix_list_name: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribePrefixListsResponseBodyPrefixListsPrefixListTags = None,
    ):
        # The IP address family of the prefix list. Valid values:
        # 
        # *   IPv4
        # *   IPv6
        self.address_family = address_family
        # The number of associated resources.
        self.association_count = association_count
        # The time when the prefix list was created.
        self.creation_time = creation_time
        # The description of the prefix list.
        self.description = description
        # The maximum number of entries that the prefix list can contain.
        self.max_entries = max_entries
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The name of the prefix list.
        self.prefix_list_name = prefix_list_name
        # The ID of the resource group to which the prefix list belongs.
        self.resource_group_id = resource_group_id
        # The tags of the prefix list.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribePrefixListsResponseBodyPrefixListsPrefixListTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribePrefixListsResponseBodyPrefixListsPrefixListTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribePrefixListsResponseBodyPrefixListsPrefixListTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribePrefixListsResponseBodyPrefixListsPrefixListTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribePrefixListsResponseBodyPrefixListsPrefixListTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag value. A prefix list can have 1 to 20 tags. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http:// or https://`.
        self.tag_key = tag_key
        # The tag key. A prefix list can have 1 to 20 tags. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

