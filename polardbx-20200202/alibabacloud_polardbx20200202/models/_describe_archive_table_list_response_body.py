# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeArchiveTableListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeArchiveTableListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeArchiveTableListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeArchiveTableListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        paused_count: int = None,
        running_count: int = None,
        success_count: int = None,
        tables: List[main_models.DescribeArchiveTableListResponseBodyDataTables] = None,
        tobe_archived_conut: int = None,
        total: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.paused_count = paused_count
        self.running_count = running_count
        self.success_count = success_count
        self.tables = tables
        self.tobe_archived_conut = tobe_archived_conut
        self.total = total

    def validate(self):
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.paused_count is not None:
            result['PausedCount'] = self.paused_count

        if self.running_count is not None:
            result['RunningCount'] = self.running_count

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        if self.tobe_archived_conut is not None:
            result['TobeArchivedConut'] = self.tobe_archived_conut

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PausedCount') is not None:
            self.paused_count = m.get('PausedCount')

        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.DescribeArchiveTableListResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k1))

        if m.get('TobeArchivedConut') is not None:
            self.tobe_archived_conut = m.get('TobeArchivedConut')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeArchiveTableListResponseBodyDataTables(DaraModel):
    def __init__(
        self,
        archive_status: str = None,
        created_date: int = None,
        file_count: int = None,
        last_success_archive_time: int = None,
        schema_name: str = None,
        space_size: float = None,
        table_name: str = None,
    ):
        self.archive_status = archive_status
        self.created_date = created_date
        self.file_count = file_count
        self.last_success_archive_time = last_success_archive_time
        self.schema_name = schema_name
        self.space_size = space_size
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_status is not None:
            result['ArchiveStatus'] = self.archive_status

        if self.created_date is not None:
            result['CreatedDate'] = self.created_date

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.last_success_archive_time is not None:
            result['LastSuccessArchiveTime'] = self.last_success_archive_time

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.space_size is not None:
            result['SpaceSize'] = self.space_size

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveStatus') is not None:
            self.archive_status = m.get('ArchiveStatus')

        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('LastSuccessArchiveTime') is not None:
            self.last_success_archive_time = m.get('LastSuccessArchiveTime')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SpaceSize') is not None:
            self.space_size = m.get('SpaceSize')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

