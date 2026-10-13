# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetaProfilingResultTablePageRequest(DaraModel):
    def __init__(
        self,
        component_type: int = None,
        data_range: str = None,
        data_size: float = None,
        data_unit: str = None,
        db_name: str = None,
        group_by: str = None,
        is_partitioned: int = None,
        is_summary: bool = None,
        migration_status: str = None,
        need_total_count: bool = None,
        order_by: str = None,
        order_direction: str = None,
        page_index: int = None,
        page_size: int = None,
        table_name: str = None,
        task_id: int = None,
        type: str = None,
    ):
        # The identifier of the component (data source) type.
        self.component_type = component_type
        # The filter condition for the data range.
        self.data_range = data_range
        # The threshold for filtering by data size. This parameter must be used together with dataUnit.
        self.data_size = data_size
        # The unit of data size, such as GB or TB. This parameter must be used together with dataSize.
        self.data_unit = data_unit
        # The name of the database, which is used to filter results by database.
        self.db_name = db_name
        # The name of the group-by field, which is used for aggregate statistics.
        self.group_by = group_by
        # Specifies whether to filter only partitioned tables.
        self.is_partitioned = is_partitioned
        # Specifies whether to return only summary statistics.
        self.is_summary = is_summary
        # The migration status, which is used to filter by migration progress or indicate the migration status of an object.
        self.migration_status = migration_status
        # Specifies whether to return the total number of records.
        self.need_total_count = need_total_count
        # The name of the order-by field.
        self.order_by = order_by
        # The sort direction, such as ascending (ASC) or descending (DESC).
        self.order_direction = order_direction
        # The current page number, starting from 1.
        self.page_index = page_index
        # The number of records to return on each page.
        self.page_size = page_size
        # The name of the table, which is used to filter results by table name.
        self.table_name = table_name
        # The ID of the metadata profiling task, which is used to locate the profiling task to which this query belongs.
        self.task_id = task_id
        # The identifier of the object type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.data_range is not None:
            result['dataRange'] = self.data_range

        if self.data_size is not None:
            result['dataSize'] = self.data_size

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.is_partitioned is not None:
            result['isPartitioned'] = self.is_partitioned

        if self.is_summary is not None:
            result['isSummary'] = self.is_summary

        if self.migration_status is not None:
            result['migrationStatus'] = self.migration_status

        if self.need_total_count is not None:
            result['needTotalCount'] = self.need_total_count

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('dataRange') is not None:
            self.data_range = m.get('dataRange')

        if m.get('dataSize') is not None:
            self.data_size = m.get('dataSize')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('isPartitioned') is not None:
            self.is_partitioned = m.get('isPartitioned')

        if m.get('isSummary') is not None:
            self.is_summary = m.get('isSummary')

        if m.get('migrationStatus') is not None:
            self.migration_status = m.get('migrationStatus')

        if m.get('needTotalCount') is not None:
            self.need_total_count = m.get('needTotalCount')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

