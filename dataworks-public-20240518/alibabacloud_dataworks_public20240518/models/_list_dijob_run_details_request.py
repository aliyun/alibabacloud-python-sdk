# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDIJobRunDetailsRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        instance_id: int = None,
        page_number: int = None,
        page_size: int = None,
        source_data_source_name: str = None,
        source_database_name: str = None,
        source_schema_name: str = None,
        source_table_name: str = None,
    ):
        # The ID of the synchronization task.
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # The instance ID.
        self.instance_id = instance_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The name of the source.
        self.source_data_source_name = source_data_source_name
        # The name of the database in the source.
        self.source_database_name = source_database_name
        # The name of the schema of the source.
        self.source_schema_name = source_schema_name
        # The name of the table in the source.
        self.source_table_name = source_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_data_source_name is not None:
            result['SourceDataSourceName'] = self.source_data_source_name

        if self.source_database_name is not None:
            result['SourceDatabaseName'] = self.source_database_name

        if self.source_schema_name is not None:
            result['SourceSchemaName'] = self.source_schema_name

        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceDataSourceName') is not None:
            self.source_data_source_name = m.get('SourceDataSourceName')

        if m.get('SourceDatabaseName') is not None:
            self.source_database_name = m.get('SourceDatabaseName')

        if m.get('SourceSchemaName') is not None:
            self.source_schema_name = m.get('SourceSchemaName')

        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')

        return self

