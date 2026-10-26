# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddHostsToGroupRequest(DaraModel):
    def __init__(
        self,
        host_group_id: str = None,
        host_ids: str = None,
        instance_id: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The ID of the asset group to which you want to add hosts.
        # > You can call the [ListHostGroups](https://help.aliyun.com/document_detail/201307.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.host_group_id = host_group_id
        # The IDs of the hosts that you want to add to the asset group. This parameter is a JSON-formatted string. You can add up to 100 host IDs.
        # > You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query host IDs.
        # 
        # This parameter is required.
        self.host_ids = host_ids
        # The instance ID of the bastion host where the asset group to which you want to add hosts resides.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The project ID.
        self.project_id = project_id
        # The region ID of the bastion host instance where the asset group to which you want to add hosts resides.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

