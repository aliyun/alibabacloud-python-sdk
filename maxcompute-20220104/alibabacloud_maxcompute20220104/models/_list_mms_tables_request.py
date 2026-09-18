# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsTablesRequest(DaraModel):
    def __init__(
        self,
        sorter: main_models.ListMmsTablesRequestSorter = None,
        db_id: int = None,
        db_name: str = None,
        dst_name: str = None,
        dst_project_name: str = None,
        dst_schema_name: str = None,
        has_partitions: bool = None,
        last_ddl_time_end: str = None,
        last_ddl_time_start: str = None,
        name: str = None,
        only_name: bool = None,
        page_num: int = None,
        page_size: int = None,
        status: List[str] = None,
        type: str = None,
    ):
        self.sorter = sorter
        # The ID of the database.
        self.db_id = db_id
        # The name of the database.
        self.db_name = db_name
        # The name of the destination MaxCompute table.
        self.dst_name = dst_name
        # The name of the destination MaxCompute project.
        self.dst_project_name = dst_project_name
        # The name of the destination MaxCompute schema. This parameter is null if the destination MaxCompute project does not have a schema layer.
        self.dst_schema_name = dst_schema_name
        # The partitioned table.
        self.has_partitions = has_partitions
        # The end of the time range for lastDdlTime.
        self.last_ddl_time_end = last_ddl_time_end
        # The start of the time range for lastDdlTime.
        self.last_ddl_time_start = last_ddl_time_start
        # The name of the table.
        self.name = name
        # Specifies whether to return only the names of the tables.
        self.only_name = only_name
        # The page number.
        self.page_num = page_num
        # The number of entries to return on each page.
        self.page_size = page_size
        # The migration status.
        self.status = status
        # The table type.
        self.type = type

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()

        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.dst_name is not None:
            result['dstName'] = self.dst_name

        if self.dst_project_name is not None:
            result['dstProjectName'] = self.dst_project_name

        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name

        if self.has_partitions is not None:
            result['hasPartitions'] = self.has_partitions

        if self.last_ddl_time_end is not None:
            result['lastDdlTimeEnd'] = self.last_ddl_time_end

        if self.last_ddl_time_start is not None:
            result['lastDdlTimeStart'] = self.last_ddl_time_start

        if self.name is not None:
            result['name'] = self.name

        if self.only_name is not None:
            result['onlyName'] = self.only_name

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = main_models.ListMmsTablesRequestSorter()
            self.sorter = temp_model.from_map(m.get('sorter'))

        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('dstName') is not None:
            self.dst_name = m.get('dstName')

        if m.get('dstProjectName') is not None:
            self.dst_project_name = m.get('dstProjectName')

        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')

        if m.get('hasPartitions') is not None:
            self.has_partitions = m.get('hasPartitions')

        if m.get('lastDdlTimeEnd') is not None:
            self.last_ddl_time_end = m.get('lastDdlTimeEnd')

        if m.get('lastDdlTimeStart') is not None:
            self.last_ddl_time_start = m.get('lastDdlTimeStart')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('onlyName') is not None:
            self.only_name = m.get('onlyName')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListMmsTablesRequestSorter(DaraModel):
    def __init__(
        self,
        last_ddl_time: str = None,
        num_rows: str = None,
        size: str = None,
    ):
        # The sort order for lastDdlTime.
        self.last_ddl_time = last_ddl_time
        # The sort order for the number of rows.
        self.num_rows = num_rows
        # The sort order for the data size.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time

        if self.num_rows is not None:
            result['numRows'] = self.num_rows

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')

        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

