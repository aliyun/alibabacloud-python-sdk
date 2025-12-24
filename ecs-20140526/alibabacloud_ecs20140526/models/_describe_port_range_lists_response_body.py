# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePortRangeListsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        port_range_lists: List[main_models.DescribePortRangeListsResponseBodyPortRangeLists] = None,
        request_id: str = None,
    ):
        # A pagination token. If the return value is empty, no more data is returned.
        self.next_token = next_token
        # Details of the port lists.
        self.port_range_lists = port_range_lists
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.port_range_lists:
            for v1 in self.port_range_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PortRangeLists'] = []
        if self.port_range_lists is not None:
            for k1 in self.port_range_lists:
                result['PortRangeLists'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.port_range_lists = []
        if m.get('PortRangeLists') is not None:
            for k1 in m.get('PortRangeLists'):
                temp_model = main_models.DescribePortRangeListsResponseBodyPortRangeLists()
                self.port_range_lists.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortRangeListsResponseBodyPortRangeLists(DaraModel):
    def __init__(
        self,
        association_count: int = None,
        creation_time: str = None,
        description: str = None,
        max_entries: int = None,
        port_range_list_id: str = None,
        port_range_list_name: str = None,
        resource_group_id: str = None,
        tags: List[main_models.DescribePortRangeListsResponseBodyPortRangeListsTags] = None,
    ):
        # The number of associated resources.
        self.association_count = association_count
        # The time when the port list was created.
        self.creation_time = creation_time
        # The description of the port list.
        self.description = description
        # The maximum number of entries in the port list.
        self.max_entries = max_entries
        # The ID of the port list.
        self.port_range_list_id = port_range_list_id
        # The name of the port list.
        self.port_range_list_name = port_range_list_name
        # The ID of the resource group to which to assign the port list.
        self.resource_group_id = resource_group_id
        # The tags of the port list.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_count is not None:
            result['AssociationCount'] = self.association_count

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries

        if self.port_range_list_id is not None:
            result['PortRangeListId'] = self.port_range_list_id

        if self.port_range_list_name is not None:
            result['PortRangeListName'] = self.port_range_list_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationCount') is not None:
            self.association_count = m.get('AssociationCount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('PortRangeListId') is not None:
            self.port_range_list_id = m.get('PortRangeListId')

        if m.get('PortRangeListName') is not None:
            self.port_range_list_name = m.get('PortRangeListName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribePortRangeListsResponseBodyPortRangeListsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribePortRangeListsResponseBodyPortRangeListsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of tag N.
        self.tag_key = tag_key
        # The value of tag N.
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

