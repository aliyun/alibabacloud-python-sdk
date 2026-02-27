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
        # The name of the permission policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the permission policy. Valid values:
        # 
        # *   Custom
        # *   System
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The name of the object to which you want to attach the permission policy.
        # 
        # *   If you want to attach the permission policy to a RAM user, specify the name in the @.onaliyun.com format. indicates the name of the RAM user, and indicates the alias of the Alibaba Cloud account to which the RAM user belongs.
        # *   If you want to attach the permission policy to a RAM user group, specify the name in the @group..onaliyun.com format. indicates the name of the RAM user group, and indicates the alias of the Alibaba Cloud account to which the RAM user group belongs.
        # *   If you want to attach the permission policy to a RAM role, specify the name in the @role..onaliyunservice.com format. indicates the name of the RAM role, and indicates the alias of the Alibaba Cloud account to which the RAM role belongs.
        # 
        # >  The alias of an Alibaba Cloud account is a part of the default domain name. You can call the [GetDefaultDomain](https://help.aliyun.com/document_detail/186720.html) operation to obtain the alias of an Alibaba Cloud account.
        # 
        # This parameter is required.
        self.principal_name = principal_name
        # The type of the object to which you want to attach the permission policy. Valid values:
        # 
        # *   IMSUser: RAM user
        # *   IMSGroup: RAM user group
        # *   ServiceRole: RAM role
        # 
        # This parameter is required.
        self.principal_type = principal_type
        # The effective scope of the permission policy. Valid values:
        # 
        # *   ID of a resource group: indicates that the permission policy takes effect for the resources in the resource group.
        # *   ID of the Alibaba Cloud account to which the authorized object belongs: indicates that the permission policy takes effect for the resources within the Alibaba Cloud account.
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

