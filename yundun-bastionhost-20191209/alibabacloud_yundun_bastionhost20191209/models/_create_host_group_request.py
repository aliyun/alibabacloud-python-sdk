# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHostGroupRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        host_group_name: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The remarks of the asset group. The remarks can be up to 500 characters in length.
        self.comment = comment
        # The name of the asset group. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.host_group_name = host_group_name
        # The ID of the bastion host on which you want to create an asset group.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host on which you want to create an asset group.
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
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

