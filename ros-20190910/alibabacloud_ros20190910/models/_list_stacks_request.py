# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListStacksRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_stack_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        show_nested_stack: bool = None,
        stack_id: str = None,
        stack_ids: List[str] = None,
        stack_name: List[str] = None,
        start_time: str = None,
        status: List[str] = None,
        tag: List[main_models.ListStacksRequestTag] = None,
    ):
        # The end of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the parent stack.
        self.parent_stack_id = parent_stack_id
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.\\
        # For more information about resource groups, see the "Resource Group" section of the [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html) topic.
        self.resource_group_id = resource_group_id
        # Specifies whether to return nested stacks. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # > If you specify ParentStackId, you must set ShowNestedStack to true.
        self.show_nested_stack = show_nested_stack
        # The stack ID. You can specify this parameter to query only the stack ID. If you want to query the detailed information about the stack, call the GetStack operation.
        self.stack_id = stack_id
        # The IDs of the stacks.
        self.stack_ids = stack_ids
        # The names of the stacks.
        self.stack_name = stack_name
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time
        # The status of the stack.
        self.status = status
        # The tags of the stack.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.show_nested_stack is not None:
            result['ShowNestedStack'] = self.show_nested_stack

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_ids is not None:
            result['StackIds'] = self.stack_ids

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShowNestedStack') is not None:
            self.show_nested_stack = m.get('ShowNestedStack')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackIds') is not None:
            self.stack_ids = m.get('StackIds')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListStacksRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListStacksRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.\\
        # Valid values of N: 1 to 20.
        self.key = key
        # The value of tag N.\\
        # Valid values of N: 1 to 20.
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

