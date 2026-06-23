# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHostsForUserGroupRequest(DaraModel):
    def __init__(
        self,
        host_address: str = None,
        host_name: str = None,
        instance_id: str = None,
        mode: str = None,
        ostype: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        user_group_id: str = None,
    ):
        # The address of the host. You can set this parameter to a domain name or an IP address. Exact match is supported.
        self.host_address = host_address
        # The name of the host. Exact match is supported.
        self.host_name = host_name
        # The ID of the bastion host instance that contains the user group.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to query for authorized or unauthorized hosts. Valid values:
        # 
        # - **Authorized** (default)
        # 
        # - **Unauthorized**
        self.mode = mode
        # The operating system of the host. Valid values:
        # 
        # - **Linux**
        # 
        # - **Windows**
        self.ostype = ostype
        # The page number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.<br>Maximum value: 100. Default value: 20.<br>
        # 
        # > We recommend that you specify this parameter.
        self.page_size = page_size
        # The ID of the region where the bastion host instance is located.
        # 
        # > For more information about regions and their corresponding IDs, see [regions and availability zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user group whose hosts you want to list.
        # 
        # > You can call the [ListUserGroups](https://help.aliyun.com/document_detail/204509.html) operation to obtain the user group ID.
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
        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

