# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetPolicyUserScopeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
        scope_type: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The bastion host ID.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # 
        # >  You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to query the control policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The scope of users to whom the control policy applies. Valid values:
        # 
        # * **All**: The control policy applies to all users.
        # * **User**: The control policy applies to specified users.
        # * **UserGroup**: The control policy applies to specified user groups.
        # 
        # This parameter is required.
        self.scope_type = scope_type
        # The user groups to which the control policy applies.
        # 
        # > This parameter is required if ScopeType is set to UserGroup. You can specify up to 100 user group IDs.
        self.user_group_ids = user_group_ids
        # The users to whom the control policy applies.
        # 
        # > This parameter is required if ScopeType is set to User. You can specify up to 500 user IDs.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

