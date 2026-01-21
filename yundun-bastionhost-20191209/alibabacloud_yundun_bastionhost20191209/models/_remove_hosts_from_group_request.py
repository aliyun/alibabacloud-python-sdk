# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveHostsFromGroupRequest(DaraModel):
    def __init__(
        self,
        host_group_id: str = None,
        host_ids: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the asset group from which you want to remove hosts.
        # 
        # >  You can call the [ListHostGroups](https://help.aliyun.com/document_detail/201307.html) operation to query the asset group ID.
        # 
        # This parameter is required.
        self.host_group_id = host_group_id
        # The IDs of the hosts that you want to remove from the host group. Specify a JSON string. You can specify up to 100 host IDs.
        # 
        # >  You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query the host IDs.
        # 
        # This parameter is required.
        self.host_ids = host_ids
        # The ID of the bastion host whose asset group you want to manage.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host whose asset group you want to manage.
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
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id

        if self.host_ids is not None:
            result['HostIds'] = self.host_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')

        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

