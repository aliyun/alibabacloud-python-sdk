# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTableRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        owner_id: int = None,
        region_id: str = None,
        schema: str = None,
        secret_arn: str = None,
        table: str = None,
        workspace_id: str = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        # 
        # This parameter is required.
        self.database = database
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the schema to which the table belongs.
        # 
        # This parameter is required.
        self.schema = schema
        # The Alibaba Cloud Resource Name (ARN) of the access credential for the created Data API account. You can call the CreateSecret operation to create an access credential.
        # 
        # >  To call the DescribeTable operation as a Resource Access Management (RAM) user, the RAM user must have the permissions to call the UseSecret or GetSecretValue operation on the ARN of the access credential.
        # 
        # This parameter is required.
        self.secret_arn = secret_arn
        # The name of the table.
        # 
        # This parameter is required.
        self.table = table
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

        if self.database is not None:
            result['Database'] = self.database

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn

        if self.table is not None:
            result['Table'] = self.table

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

