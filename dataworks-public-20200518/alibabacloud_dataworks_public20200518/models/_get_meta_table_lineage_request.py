# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableLineageRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_source_type: str = None,
        database_name: str = None,
        direction: str = None,
        next_primary_key: str = None,
        page_size: int = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        # The ID of the E-MapReduce (EMR) cluster. Configure this parameter only if you want to query the lineage of an EMR table.
        self.cluster_id = cluster_id
        # The type of the data source. Valid values: odps and emr.
        self.data_source_type = data_source_type
        # The name of the database.
        self.database_name = database_name
        # Specifies the ancestor or descendant lineage that you want to query for a field. Valid values: up and down. The value up indicates the ancestor lineage. The value down indicates the descendant lineage.
        # 
        # This parameter is required.
        self.direction = direction
        # The logic of paging. Configure this parameter based on the value of the response parameter NextPrimaryKey when the value of the response parameter HasNext is true in the previous request.
        self.next_primary_key = next_primary_key
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The unique identifier of the table.
        self.table_guid = table_guid
        # The name of the table.
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

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.next_primary_key is not None:
            result['NextPrimaryKey'] = self.next_primary_key

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('NextPrimaryKey') is not None:
            self.next_primary_key = m.get('NextPrimaryKey')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

