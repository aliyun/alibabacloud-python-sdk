# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserGroupRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        region_id: str = None,
        user_group_name: str = None,
    ):
        # The description of the user group. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host for which you want to create a user group.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host for which you want to create a user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The name of the user group that you want to create. This name can be a up to 128 characters in length.
        # 
        # This parameter is required.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

