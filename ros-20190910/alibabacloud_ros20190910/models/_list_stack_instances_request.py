# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStackInstancesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_instance_account_id: str = None,
        stack_instance_region_id: str = None,
    ):
        # The number of the page to return.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # *   Valid values: 1 to 50.
        # *   Default value: 10.
        self.page_size = page_size
        # The region ID of the stack group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the stack group. The name must be unique within a region.\\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or letter.
        # 
        # This parameter is required.
        self.stack_group_name = stack_group_name
        # The ID of the destination account to which the stack belongs.
        # 
        # *   If the stack group is granted self-managed permissions, the stack belongs to an Alibaba Cloud account.
        # *   If the stack group is granted service-managed permissions, the stack belongs to a member in a resource directory.
        # 
        # > For more information about the destination account, see [Overview](https://help.aliyun.com/document_detail/154578.html).
        self.stack_instance_account_id = stack_instance_account_id
        # The region ID of the stack.
        self.stack_instance_region_id = stack_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.stack_instance_account_id is not None:
            result['StackInstanceAccountId'] = self.stack_instance_account_id

        if self.stack_instance_region_id is not None:
            result['StackInstanceRegionId'] = self.stack_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = m.get('StackInstanceAccountId')

        if m.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = m.get('StackInstanceRegionId')

        return self

