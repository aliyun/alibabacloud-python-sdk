# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStatementResultRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        id: str = None,
        owner_id: int = None,
        region_id: str = None,
        secret_arn: str = None,
    ):
        # The instance ID. You can call DescribeDBInstances to obtain the ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name.
        self.database = database
        # The task ID of the asynchronous SQL execution.
        # 
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The access credential. Created by calling the CreateSecret operation.
        # 
        # > When you access this operation by using a RAM user, you must have the UseSecret or GetSecretValue permission on this SecretArn.
        # 
        # This parameter is required.
        self.secret_arn = secret_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database is not None:
            result['Database'] = self.database

        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')

        return self

