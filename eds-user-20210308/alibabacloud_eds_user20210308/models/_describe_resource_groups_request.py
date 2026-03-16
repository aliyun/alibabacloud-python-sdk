# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeResourceGroupsRequest(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_ids: List[str] = None,
        business_channel: str = None,
        need_contain_resource_group_with_office_site: int = None,
        page_number: int = None,
        page_size: int = None,
        platform: str = None,
        resource_group_ids: List[str] = None,
        resource_group_name: str = None,
    ):
        self.aliyun_resource_group_ids = aliyun_resource_group_ids
        self.business_channel = business_channel
        # >  This parameter is not publicly available.
        self.need_contain_resource_group_with_office_site = need_contain_resource_group_with_office_site
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # >  Set the value to AliyunConsole.
        # 
        # *   This parameter is not publicly available on other platforms.
        self.platform = platform
        # The IDs of the resource groups that you want to query.
        self.resource_group_ids = resource_group_ids
        # The name of the resource group.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_resource_group_ids is not None:
            result['AliyunResourceGroupIds'] = self.aliyun_resource_group_ids

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.need_contain_resource_group_with_office_site is not None:
            result['NeedContainResourceGroupWithOfficeSite'] = self.need_contain_resource_group_with_office_site

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupIds') is not None:
            self.aliyun_resource_group_ids = m.get('AliyunResourceGroupIds')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('NeedContainResourceGroupWithOfficeSite') is not None:
            self.need_contain_resource_group_with_office_site = m.get('NeedContainResourceGroupWithOfficeSite')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

