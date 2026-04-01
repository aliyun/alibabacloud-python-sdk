# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAccountNameAvailableRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        client_token: str = None,
        dbinstance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        # The username of the account.
        # 
        # *   The value must be unique.
        # 
        # *   The value must start with a lowercase letter, and end with a lowercase letter or a digit.
        # 
        # *   The value can contain lowercase letters, digits, and underscores (_).
        # 
        # *   The length of the value must meet the following requirements:
        # 
        #     *   If the instance runs MySQL 5.7 or MySQL 8.0, the value must be 2 to 32 characters in length.
        #     *   If the instance runs MySQL 5.6, the value must be 2 to 16 characters in length.
        #     *   If the instance runs SQL Server, the value must be 2 to 64 characters in length.
        #     *   If the instance runs PostgreSQL with cloud disks, the value must be 2 to 63 characters in length.
        #     *   If the instance runs PostgreSQL with local disks, the value must be 2 to 16 characters in length.
        #     *   If the instance runs MariaDB, the value must be 2 to 16 characters in length.
        # 
        # *   For more information about invalid characters, see [Forbidden keywords table](https://help.aliyun.com/document_detail/26317.html).
        # 
        # This parameter is required.
        self.account_name = account_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self

