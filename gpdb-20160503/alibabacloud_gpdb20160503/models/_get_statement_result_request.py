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
        # Instance ID. Can be obtained by calling DescribeDBInstances.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Database name.
        self.database = database
        # Task ID for asynchronous SQL execution.
        # 
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        # Region ID where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Access credential. Created through the CreateSecret interface.
        # 
        # > When accessing this interface with a sub-account, the sub-account must have the UseSecret or GetSecretValue permission for this SecretArn.
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

