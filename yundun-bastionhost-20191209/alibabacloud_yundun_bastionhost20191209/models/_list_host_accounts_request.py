# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHostAccountsRequest(DaraModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        host_ids: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        protocol_name: str = None,
        region_id: str = None,
    ):
        # The name of the host account that you want to query. The name can be up to 128 characters in length. Only exact match is supported.
        self.host_account_name = host_account_name
        # The ID of the specified host whose accounts you want to query.
        # 
        # >  You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query the ID of the host.
        # 
        # This parameter is required.
        self.host_id = host_id
        self.host_ids = host_ids
        # The ID of the bastion host in which you want to query accounts of the specified host.
        # 
        # >  You can call the DescribeInstances operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The protocol used by the host whose accounts you want to query.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.protocol_name = protocol_name
        # The region ID of the bastion host in which you want to query accounts of the specified host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.host_ids is not None:
            result['HostIds'] = self.host_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

