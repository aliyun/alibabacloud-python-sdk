# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableProducingTasksRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_source_type: str = None,
        db_name: str = None,
        schema_name: str = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        # The ID of the EMR cluster. This parameter takes effect only if the DataSourceType parameter is set to emr.
        self.cluster_id = cluster_id
        # The type of the metatable. Valid values: odps and emr. The value odps indicates that the metatable is a MaxCompute metatable. The value emr indicates that the metatable is an E-MapReduce (EMR) metatable.
        self.data_source_type = data_source_type
        # The name of the database.
        self.db_name = db_name
        # The name of the schema.
        self.schema_name = schema_name
        # The GUID of the MaxCompute metatable.
        # 
        # This parameter is required.
        self.table_guid = table_guid
        # The name of the metatable.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

