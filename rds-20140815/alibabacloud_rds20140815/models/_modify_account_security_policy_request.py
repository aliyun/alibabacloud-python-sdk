# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountSecurityPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        group_policy: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/2628785.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The custom password policy for the account of the ApsaraDB RDS for SQL Server instance. The following policies are supported:
        # 
        # *   `{"account security policy": {"MaximumPasswordAge": Specify the maximum password age}}`: You can configure only the maximum password age. After the maximum password age is reached, you must change the password.
        # *   `{"accountSecurityPolicy": {"MaximumPasswordAge": Specify the minimum password age}}`: You can configure only the minimum password age. During the specified period, you cannot change the password.
        # *   `{"accountSecurityPolicy": {"MaximumPasswordAge": Specify the maximum password age, "MinimumPasswordAge": Specify the minimum password age}}`: You can configure the maximum and minimum password age at the same time.
        # 
        # >  The minimum password age cannot be greater than the maximum password age. Valid values for the minimum password age: 0 to 998. Valid values for the maximum password age: 0 to 999.
        # 
        # This parameter is required.
        self.group_policy = group_policy
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.group_policy is not None:
            result['GroupPolicy'] = self.group_policy

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('GroupPolicy') is not None:
            self.group_policy = m.get('GroupPolicy')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

