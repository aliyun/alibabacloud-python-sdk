# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHostGroupsForUserRequest(DaraModel):
    def __init__(
        self,
        host_group_name: str = None,
        instance_id: str = None,
        mode: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The name of the host group to query. The name can be up to 128 characters in length. Only exact match is supported.
        self.host_group_name = host_group_name
        # The ID of the bastion host whose user you want to query.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The category of the host groups to query. Valid values:
        # 
        # *   **Authorized** (default): queries the host groups that the user is authorized to manage.
        # *   **Unauthorized**: queries the host groups that the user is not authorized to manage.
        self.mode = mode
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.\\
        # Valid values: 1 to 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host whose user you want to query.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The user ID.
        # 
        # >  You can call the [ListUsers](https://help.aliyun.com/document_detail/204522.html) operation to query the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

