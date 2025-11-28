# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecretRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        description: str = None,
        owner_id: int = None,
        password: str = None,
        region_id: str = None,
        secret_name: str = None,
        test_connection: bool = None,
        username: str = None,
        workspace_id: str = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The description of the access credential.
        self.description = description
        self.owner_id = owner_id
        # The password of the database account that is used to access the instance.
        # 
        # This parameter is required.
        self.password = password
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the access credential. The name must be 1 to 16 characters in length and can contain letters, digits, and underscores (_). If you leave this parameter empty, the value of the Username parameter is used.
        self.secret_name = secret_name
        # Specifies whether to check the connectivity to the instance by using the name and password of the database account.
        self.test_connection = test_connection
        # The name of the database account that is used to access the instance.
        # 
        # This parameter is required.
        self.username = username
        # The ID of the workspace that consists of multiple AnalyticDB for PostgreSQL instances. You must specify one of the WorkspaceId and DBInstanceId parameters. If you specify both parameters, the WorkspaceId parameter takes precedence.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.test_connection is not None:
            result['TestConnection'] = self.test_connection

        if self.username is not None:
            result['Username'] = self.username

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('TestConnection') is not None:
            self.test_connection = m.get('TestConnection')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

