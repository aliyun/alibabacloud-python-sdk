# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserGroupsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_name: str = None,
    ):
        # The ID of the bastion host on which you want to query user groups.
        #  >You can call the [DescribeInstances ](https://help.aliyun.com/document_detail/462953.html)operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        self.page_size = page_size
        # The region ID of the bastion host on which you want to query user groups.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/462924.html).
        self.region_id = region_id
        # The name of the user group that you want to query. Only exact match is supported.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

