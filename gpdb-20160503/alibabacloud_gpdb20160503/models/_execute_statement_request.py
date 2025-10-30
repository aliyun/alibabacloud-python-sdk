# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ExecuteStatementRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        owner_id: int = None,
        parameters: List[Any] = None,
        rag_workspace_collection: main_models.ExecuteStatementRequestRagWorkspaceCollection = None,
        region_id: str = None,
        run_type: str = None,
        secret_arn: str = None,
        sql: str = None,
        sqls: List[str] = None,
        statement_name: str = None,
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
        # The configuration parameters.
        self.parameters = parameters
        self.rag_workspace_collection = rag_workspace_collection
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution type. Valid values:
        # 
        # *   synchronous
        # *   asynchronous (not supported)
        self.run_type = run_type
        # The Alibaba Cloud Resource Name (ARN) of the access credential for the created Data API account. You can call the CreateSecret operation to create an access credential.
        # 
        # >  To call the ExecuteStatement operation as a Resource Access Management (RAM) user, the RAM user must have the permissions to call the UseSecret or GetSecretValue operation on the ARN of the access credential.
        # 
        # This parameter is required.
        self.secret_arn = secret_arn
        # The SQL statements that you want to execute.
        self.sql = sql
        # The SQL statements.
        self.sqls = sqls
        # The name of the set of SQL statements that you want to execute. This parameter takes effect when the RunType parameter is set to asynchronous.
        self.statement_name = statement_name
        self.workspace_id = workspace_id

    def validate(self):
        if self.rag_workspace_collection:
            self.rag_workspace_collection.validate()

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

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.rag_workspace_collection is not None:
            result['RagWorkspaceCollection'] = self.rag_workspace_collection.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.run_type is not None:
            result['RunType'] = self.run_type

        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.sqls is not None:
            result['Sqls'] = self.sqls

        if self.statement_name is not None:
            result['StatementName'] = self.statement_name

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

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RagWorkspaceCollection') is not None:
            temp_model = main_models.ExecuteStatementRequestRagWorkspaceCollection()
            self.rag_workspace_collection = temp_model.from_map(m.get('RagWorkspaceCollection'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RunType') is not None:
            self.run_type = m.get('RunType')

        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('Sqls') is not None:
            self.sqls = m.get('Sqls')

        if m.get('StatementName') is not None:
            self.statement_name = m.get('StatementName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ExecuteStatementRequestRagWorkspaceCollection(DaraModel):
    def __init__(
        self,
        collection: str = None,
        namespace: str = None,
    ):
        self.collection = collection
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

