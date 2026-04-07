# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckMetaPartitionRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_source_type: str = None,
        database_name: str = None,
        partition: str = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        # This parameter is deprecated.
        self.cluster_id = cluster_id
        # The type of the data source. Set the value to odps.
        self.data_source_type = data_source_type
        # The name of the metadatabase.
        self.database_name = database_name
        # The name of the partition in the MaxCompute metatable.
        # 
        # This parameter is required.
        self.partition = partition
        # The GUID of the MaxCompute metatable.
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

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.partition is not None:
            result['Partition'] = self.partition

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

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

