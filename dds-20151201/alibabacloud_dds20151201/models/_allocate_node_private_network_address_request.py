# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateNodePrivateNetworkAddressRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dbinstance_id: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The username of the account.
        # 
        # > 
        # 
        # *   The username must be 4 to 16 characters in length and can contain lowercase letters, digits, and underscores (_). The username must start with a lowercase letter.
        # 
        # *   You must configure the account and password only when you apply for the endpoint of a shard or Configserver node for the first time. The account and password are required for all shard and Configserver nodes.
        # 
        # *   The permissions of this account are fixed to read-only.
        self.account_name = account_name
        # The password for the account.
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `! # $ % ^ & * ( ) _ + - =`
        # *   The password must be 8 to 32 characters in length.
        self.account_password = account_password
        # The ID of the sharded cluster instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the shard or Configserver node.
        # 
        # >  You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to query the ID of the shard or Configserver node.
        # 
        # This parameter is required.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the zone to which the instance belongs.
        # 
        # >  You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to query the zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

