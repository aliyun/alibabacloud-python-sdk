# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetInstanceMissingIndexListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstanceMissingIndexListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetInstanceMissingIndexListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceMissingIndexListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetInstanceMissingIndexListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The returned data.
        self.list = list
        # The page number of the page returned.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetInstanceMissingIndexListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetInstanceMissingIndexListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        avg_total_user_cost: float = None,
        avg_user_impact: float = None,
        create_index: str = None,
        database_name: str = None,
        equality_columns: str = None,
        included_columns: str = None,
        index_count: int = None,
        inequality_columns: str = None,
        last_user_seek: int = None,
        object_name: str = None,
        reserved_pages: int = None,
        reserved_size: float = None,
        row_count: int = None,
        schema_name: str = None,
        system_scans: int = None,
        system_seeks: int = None,
        unique_compiles: int = None,
        user_scans: int = None,
        user_seeks: int = None,
    ):
        # The average cost savings.
        self.avg_total_user_cost = avg_total_user_cost
        # The performance improvement, in percentage.
        self.avg_user_impact = avg_user_impact
        # The statement used to create the missing indexes.
        self.create_index = create_index
        # The database name.
        self.database_name = database_name
        # The index columns included in the equal operation.
        self.equality_columns = equality_columns
        # The columns on which indexes are missing.
        self.included_columns = included_columns
        # The number of indexes.
        self.index_count = index_count
        # The index columns included in the not equal operation.
        self.inequality_columns = inequality_columns
        # The last seek time of a user.
        self.last_user_seek = last_user_seek
        # The object name.
        self.object_name = object_name
        # The total number of returned pages.
        self.reserved_pages = reserved_pages
        # The table size.
        self.reserved_size = reserved_size
        # The number of table rows.
        self.row_count = row_count
        # The schema name.
        self.schema_name = schema_name
        # The number of scans.
        self.system_scans = system_scans
        # The number of seeks.
        self.system_seeks = system_seeks
        # The number of compilations.
        self.unique_compiles = unique_compiles
        # The number of scans performed by users.
        self.user_scans = user_scans
        # The number of seeks performed by users.
        self.user_seeks = user_seeks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_total_user_cost is not None:
            result['AvgTotalUserCost'] = self.avg_total_user_cost

        if self.avg_user_impact is not None:
            result['AvgUserImpact'] = self.avg_user_impact

        if self.create_index is not None:
            result['CreateIndex'] = self.create_index

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.equality_columns is not None:
            result['EqualityColumns'] = self.equality_columns

        if self.included_columns is not None:
            result['IncludedColumns'] = self.included_columns

        if self.index_count is not None:
            result['IndexCount'] = self.index_count

        if self.inequality_columns is not None:
            result['InequalityColumns'] = self.inequality_columns

        if self.last_user_seek is not None:
            result['LastUserSeek'] = self.last_user_seek

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.reserved_pages is not None:
            result['ReservedPages'] = self.reserved_pages

        if self.reserved_size is not None:
            result['ReservedSize'] = self.reserved_size

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.system_scans is not None:
            result['SystemScans'] = self.system_scans

        if self.system_seeks is not None:
            result['SystemSeeks'] = self.system_seeks

        if self.unique_compiles is not None:
            result['UniqueCompiles'] = self.unique_compiles

        if self.user_scans is not None:
            result['UserScans'] = self.user_scans

        if self.user_seeks is not None:
            result['UserSeeks'] = self.user_seeks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgTotalUserCost') is not None:
            self.avg_total_user_cost = m.get('AvgTotalUserCost')

        if m.get('AvgUserImpact') is not None:
            self.avg_user_impact = m.get('AvgUserImpact')

        if m.get('CreateIndex') is not None:
            self.create_index = m.get('CreateIndex')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EqualityColumns') is not None:
            self.equality_columns = m.get('EqualityColumns')

        if m.get('IncludedColumns') is not None:
            self.included_columns = m.get('IncludedColumns')

        if m.get('IndexCount') is not None:
            self.index_count = m.get('IndexCount')

        if m.get('InequalityColumns') is not None:
            self.inequality_columns = m.get('InequalityColumns')

        if m.get('LastUserSeek') is not None:
            self.last_user_seek = m.get('LastUserSeek')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ReservedPages') is not None:
            self.reserved_pages = m.get('ReservedPages')

        if m.get('ReservedSize') is not None:
            self.reserved_size = m.get('ReservedSize')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SystemScans') is not None:
            self.system_scans = m.get('SystemScans')

        if m.get('SystemSeeks') is not None:
            self.system_seeks = m.get('SystemSeeks')

        if m.get('UniqueCompiles') is not None:
            self.unique_compiles = m.get('UniqueCompiles')

        if m.get('UserScans') is not None:
            self.user_scans = m.get('UserScans')

        if m.get('UserSeeks') is not None:
            self.user_seeks = m.get('UserSeeks')

        return self

