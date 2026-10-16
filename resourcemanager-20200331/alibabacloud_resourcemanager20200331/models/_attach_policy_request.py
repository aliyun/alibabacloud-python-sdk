# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        # Policy Name of the access policy.
        # 
        # Policy Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the access policy. Valid values:
        # 
        # - Custom: custom access policy.
        # - System: system access policy.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The name of the authorization object. The format varies based on the object type:
        # 
        # - Resource Access Management (RAM) user: <UserName>@<AccountAlias>.onaliyun.com, where <UserName> is the RAM username and <AccountAlias> is the account alias.
        # - RAM user group: <GroupName>@group.<AccountAlias>.onaliyun.com, where <GroupName> is the RAM user group name and <AccountAlias> is the account alias.
        # - RAM role: <RoleName>@role.<AccountAlias>.onaliyunservice.com, where <RoleName> is the RAM role name and <AccountAlias> is the account alias.
        # 
        # > The account alias is part of the default domain name. Invoke [GetDefaultDomain](https://help.aliyun.com/document_detail/186720.html) to obtain the account alias.
        # 
        # This parameter is required.
        self.principal_name = principal_name
        # The authorization object type. Valid values:
        # 
        # - IMSUser: Resource Access Management (RAM) user.
        # - IMSGroup: RAM user group.
        # - ServiceRole: RAM role.
        # 
        # This parameter is required.
        self.principal_type = principal_type
        # The authorization scope. Valid values:
        # 
        # - Resource group ID: The permissions take effect within the specified resource group.
        # - Alibaba Cloud account ID: The ID of the Alibaba Cloud account to which the principal belongs. The permissions take effect within the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

