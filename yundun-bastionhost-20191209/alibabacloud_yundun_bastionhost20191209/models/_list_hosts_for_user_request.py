# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHostsForUserRequest(DaraModel):
    def __init__(
        self,
        host_address: str = None,
        host_name: str = None,
        instance_id: str = None,
        mode: str = None,
        ostype: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: int = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The address of the host to query. You can use a domain name or an IP address. Only exact match is supported.
        self.host_address = host_address
        # The name of the host to query. Only exact match is supported.
        self.host_name = host_name
        # The ID of the Bastionhost instance to which the user belongs.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The mode of the host list to query. Valid values:
        # - **Authorized**: Authorized hosts. This is the default value.
        # - **Unauthorized**: Unauthorized hosts.
        self.mode = mode
        # The operating system type of the host to query. Valid values:
        # - **Linux**
        # - **Windows**
        self.ostype = ostype
        # The page number of the current page in a paging query. Default value: 1.
        self.page_number = page_number
        # The maximum number of entries to return on each page for a paging query.  
        # The maximum value of the PageSize parameter is 100. Default value: 20. If this parameter is left empty, 20 entries are returned by default.
        # > Specify a value for the PageSize parameter.
        self.page_size = page_size
        # The project ID.
        self.project_id = project_id
        # The region ID of the Bastionhost instance to which the user belongs.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user to query.
        # > You can call the [ListUsers](https://help.aliyun.com/document_detail/204522.html) operation to obtain this parameter.
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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

