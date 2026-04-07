# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTableRequest(DaraModel):
    def __init__(
        self,
        app_guid: str = None,
        env_type: int = None,
        project_id: int = None,
        schema: str = None,
        table_name: str = None,
    ):
        # The globally unique identifier (GUID) of the MaxCompute project. Specify the GUID in the odps.{projectName} format.
        self.app_guid = app_guid
        # The type of the compute engine or data source. Valid values:
        # 
        # *   cdh
        # *   analyticdb_for_mysql
        # *   odps
        # *   emr
        # *   hadoop
        # *   holodb
        # *   hybriddb_for_postgresql
        self.env_type = env_type
        # The ID of the DataWorks workspace.
        self.project_id = project_id
        # The schema information of the table. You need to enter the schema information of the table if you enable the table schema in MaxCompute.
        self.schema = schema
        # The name of the MaxCompute table.
        # 
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_guid is not None:
            result['AppGuid'] = self.app_guid

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGuid') is not None:
            self.app_guid = m.get('AppGuid')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

