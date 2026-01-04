# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListPrefixListsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix_lists: List[main_models.ListPrefixListsResponseBodyPrefixLists] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value indicates the token that is used for the next request to retrieve a new page of results.
        self.next_token = next_token
        # The information about the prefix lists.
        self.prefix_lists = prefix_lists
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.prefix_lists:
            for v1 in self.prefix_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PrefixLists'] = []
        if self.prefix_lists is not None:
            for k1 in self.prefix_lists:
                result['PrefixLists'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.prefix_lists = []
        if m.get('PrefixLists') is not None:
            for k1 in m.get('PrefixLists'):
                temp_model = main_models.ListPrefixListsResponseBodyPrefixLists()
                self.prefix_lists.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPrefixListsResponseBodyPrefixLists(DaraModel):
    def __init__(
        self,
        cidr_blocks: List[str] = None,
        creation_time: str = None,
        ip_version: str = None,
        max_entries: int = None,
        owner_id: str = None,
        prefix_list_description: str = None,
        prefix_list_id: str = None,
        prefix_list_name: str = None,
        prefix_list_status: str = None,
        prefix_list_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        status: str = None,
        tags: List[main_models.ListPrefixListsResponseBodyPrefixListsTags] = None,
    ):
        # The CIDR block specified in the prefix list.
        self.cidr_blocks = cidr_blocks
        # The time when the prefix list was created.
        self.creation_time = creation_time
        # The IP version of the prefix list. Valid values:
        # 
        # *   **IPV4**
        # *   **IPV6**
        self.ip_version = ip_version
        # The maximum number of CIDR blocks that you can specify in the prefix list.
        self.max_entries = max_entries
        # The Alibaba Cloud account to which the prefix list belongs.
        self.owner_id = owner_id
        # The description of the prefix list.
        self.prefix_list_description = prefix_list_description
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The name of the prefix list.
        self.prefix_list_name = prefix_list_name
        # The status of the prefix list. Valid values:
        # 
        # *   **Created**
        # *   **Deleted**
        # *   **Modifying**
        # 
        # >  This parameter is the same as the **Status** parameter.
        self.prefix_list_status = prefix_list_status
        # The type of the prefix list.
        self.prefix_list_type = prefix_list_type
        # The region ID of the prefix list.
        self.region_id = region_id
        # The ID of the resource group to which the prefix list belongs.
        self.resource_group_id = resource_group_id
        # Indicates whether the prefix list is shared. Valid values:
        # 
        # *   **Shared**: The prefix list is shared.
        # *   If an empty value is returned, the prefix list is not shared.
        self.share_type = share_type
        # The status of the prefix list. Valid values:
        # 
        # *   **Created**
        # *   **Deleted**
        # *   **Modifying**
        self.status = status
        # The tags.
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
        if self.cidr_blocks is not None:
            result['CidrBlocks'] = self.cidr_blocks

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix_list_description is not None:
            result['PrefixListDescription'] = self.prefix_list_description

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name

        if self.prefix_list_status is not None:
            result['PrefixListStatus'] = self.prefix_list_status

        if self.prefix_list_type is not None:
            result['PrefixListType'] = self.prefix_list_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlocks') is not None:
            self.cidr_blocks = m.get('CidrBlocks')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListDescription') is not None:
            self.prefix_list_description = m.get('PrefixListDescription')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')

        if m.get('PrefixListStatus') is not None:
            self.prefix_list_status = m.get('PrefixListStatus')

        if m.get('PrefixListType') is not None:
            self.prefix_list_type = m.get('PrefixListType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPrefixListsResponseBodyPrefixListsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListPrefixListsResponseBodyPrefixListsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

