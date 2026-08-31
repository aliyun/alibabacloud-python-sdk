# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityArchiveTablesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListQualityArchiveTablesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The result of querying the anomaly archived table list.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListQualityArchiveTablesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListQualityArchiveTablesResponseBodyData(DaraModel):
    def __init__(
        self,
        archive_table_list: List[main_models.ListQualityArchiveTablesResponseBodyDataArchiveTableList] = None,
        total_count: int = None,
    ):
        # The list of anomaly archived tables.
        self.archive_table_list = archive_table_list
        # The number of custom anomaly archived tables.
        self.total_count = total_count

    def validate(self):
        if self.archive_table_list:
            for v1 in self.archive_table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ArchiveTableList'] = []
        if self.archive_table_list is not None:
            for k1 in self.archive_table_list:
                result['ArchiveTableList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.archive_table_list = []
        if m.get('ArchiveTableList') is not None:
            for k1 in m.get('ArchiveTableList'):
                temp_model = main_models.ListQualityArchiveTablesResponseBodyDataArchiveTableList()
                self.archive_table_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQualityArchiveTablesResponseBodyDataArchiveTableList(DaraModel):
    def __init__(
        self,
        archive_table_id: int = None,
        archive_table_name: str = None,
        ddl: str = None,
        is_default: bool = None,
        lifecycle: int = None,
        max_archive_count: int = None,
    ):
        # The ID of the archived table. This ID is used when you update, switch to active, or delete the archived table.
        self.archive_table_id = archive_table_id
        # The full table name in the format of project_name.table_name.
        self.archive_table_name = archive_table_name
        # The DDL statement for creating the archived table, which includes dataphin_quality_* system fields and the dataphin_quality_validate_date partition field definition.
        self.ddl = ddl
        # Indicates whether this is the active archived table. At least one active archived table must exist under the same monitored object.
        self.is_default = is_default
        # The lifecycle in days. An empty value indicates no lifecycle is configured.
        self.lifecycle = lifecycle
        # The maximum number of records to archive per validation. A value of -1 indicates full archiving.
        self.max_archive_count = max_archive_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_table_id is not None:
            result['ArchiveTableId'] = self.archive_table_id

        if self.archive_table_name is not None:
            result['ArchiveTableName'] = self.archive_table_name

        if self.ddl is not None:
            result['Ddl'] = self.ddl

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle

        if self.max_archive_count is not None:
            result['MaxArchiveCount'] = self.max_archive_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveTableId') is not None:
            self.archive_table_id = m.get('ArchiveTableId')

        if m.get('ArchiveTableName') is not None:
            self.archive_table_name = m.get('ArchiveTableName')

        if m.get('Ddl') is not None:
            self.ddl = m.get('Ddl')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')

        if m.get('MaxArchiveCount') is not None:
            self.max_archive_count = m.get('MaxArchiveCount')

        return self

