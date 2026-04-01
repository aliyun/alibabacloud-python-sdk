# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecretRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        db_instance_id: str = None,
        db_names: str = None,
        description: str = None,
        engine: str = None,
        owner_id: int = None,
        password: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_name: str = None,
        username: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the generated token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the instance. You can call the DescribeDBInstances operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # The name of the database.
        self.db_names = db_names
        # The description of the credential.
        self.description = description
        # The engine of the database.
        # 
        # > Only MySQL is supported.
        # 
        # This parameter is required.
        self.engine = engine
        self.owner_id = owner_id
        # The password that is used to access the database.
        # 
        # This parameter is required.
        self.password = password
        # The region ID of the instance. You can call the DescribeDBInstanceAttribute operation to query the region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. You can call the DescribeDBInstanceAttribute operation to query the ID of the resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the credential.
        self.secret_name = secret_name
        # The username that is used to access the database.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_names is not None:
            result['DbNames'] = self.db_names

        if self.description is not None:
            result['Description'] = self.description

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

