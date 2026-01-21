# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveDatabasesFromGroupRequest(DaraModel):
    def __init__(
        self,
        database_ids: List[str] = None,
        host_group_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The IDs of the databases that you want to remove.
        # 
        # This parameter is required.
        self.database_ids = database_ids
        # The ID of the asset group from which you want to remove databases.
        # 
        # > You can call the [ListHostGroups](https://help.aliyun.com/document_detail/201307.html) operation to query the asset group ID.
        # 
        # This parameter is required.
        self.host_group_id = host_group_id
        # The ID of the bastion host whose asset group you want to manage.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host whose asset group you want to manage.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids

        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')

        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

