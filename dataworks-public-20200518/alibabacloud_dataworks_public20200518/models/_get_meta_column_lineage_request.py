# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaColumnLineageRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        column_guid: str = None,
        column_name: str = None,
        data_source_type: str = None,
        database_name: str = None,
        direction: str = None,
        page_num: int = None,
        page_size: int = None,
        table_name: str = None,
    ):
        # The ID of the E-MapReduce (EMR) cluster. Configure this parameter only when you query data in an EMR compute engine instance.
        self.cluster_id = cluster_id
        # The unique identifier of the field.
        self.column_guid = column_guid
        # The name of the field.
        self.column_name = column_name
        # The type of the data source. Valid values: odps and emr.
        self.data_source_type = data_source_type
        # The name of the database.
        self.database_name = database_name
        # Specifies whether to query the ancestor or descendant lineage of the field. The value up indicates the ancestor lineage. The value down indicates the descendant lineage.
        # 
        # This parameter is required.
        self.direction = direction
        # The number of the page to return.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
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

        if self.column_guid is not None:
            result['ColumnGuid'] = self.column_guid

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ColumnGuid') is not None:
            self.column_guid = m.get('ColumnGuid')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

