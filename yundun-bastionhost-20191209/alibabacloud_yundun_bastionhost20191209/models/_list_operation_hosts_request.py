# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperationHostsRequest(DaraModel):
    def __init__(
        self,
        host_address: str = None,
        host_name: str = None,
        instance_id: str = None,
        ostype: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        # The address of the host. You can specify a domain name or an IP address. Only exact matches are supported.
        self.host_address = host_address
        # The name of the host. Only exact matches are supported.
        self.host_name = host_name
        # The ID of the Bastionhost instance.
        # 
        # > Call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The operating system of the host. Valid values:
        # 
        # - **Linux**
        # 
        # - **Windows**
        self.ostype = ostype
        # The number of the page to return. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page.<br> The maximum value is 100. The default value is 20. If you do not specify this parameter, the default value is used.<br>
        # 
        # > Specify a value for this parameter.
        self.page_size = page_size
        # The ID of the region where the Bastionhost instance resides.
        # 
        # > For more information about regions and zones, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The source of the host. Valid values:
        # 
        # - **Local**: a local host
        # 
        # - **Ecs**: an ECS instance
        self.source = source
        # The ID of the ECS instance. Only exact matches are supported.
        self.source_instance_id = source_instance_id
        # The state of the host. Valid values:
        # 
        # - **Normal**: The host is running.
        # 
        # - **Release**: The host is released.
        self.source_instance_state = source_instance_state

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

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')

        return self

