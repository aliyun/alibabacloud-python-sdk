# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHostGroupsForUserGroupRequest(DaraModel):
    def __init__(
        self,
        host_group_name: str = None,
        instance_id: str = None,
        mode: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: int = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The name of the host group to query. Only exact match is supported.
        self.host_group_name = host_group_name
        # The instance ID of the Bastionhost instance to which the user group belongs.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The mode of the host group list to query. Valid values:
        # - **Authorized**: Authorized host groups. This is the default value.
        # - **Unauthorized**: Unauthorized host groups.
        self.mode = mode
        # The page number of the current page when paging in a paged query. Default value: **1**.
        self.page_number = page_number
        # The maximum number of entries to return on each page when paging in a paged query.  
        # The maximum value of the PageSize parameter is 100. The default value is 20. If this parameter is left empty, 20 entries are returned by default.
        # > Specify a value for the PageSize parameter.
        self.page_size = page_size
        # The project ID.
        self.project_id = project_id
        # The region ID of the Bastionhost instance to which the user group belongs.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user group to query.
        # > You can call the [ListUserGroups](https://help.aliyun.com/document_detail/204509.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id

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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

