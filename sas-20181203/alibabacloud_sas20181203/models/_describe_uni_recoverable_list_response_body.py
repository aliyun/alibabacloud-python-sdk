# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUniRecoverableListResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        database: str = None,
        page_size: int = None,
        recoverable_info_list: List[main_models.DescribeUniRecoverableListResponseBodyRecoverableInfoList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The name of the database.
        self.database = database
        # The number of entries returned per page.
        self.page_size = page_size
        # An array that consists of the backup snapshots.
        self.recoverable_info_list = recoverable_info_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.recoverable_info_list:
            for v1 in self.recoverable_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.database is not None:
            result['Database'] = self.database

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['RecoverableInfoList'] = []
        if self.recoverable_info_list is not None:
            for k1 in self.recoverable_info_list:
                result['RecoverableInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.recoverable_info_list = []
        if m.get('RecoverableInfoList') is not None:
            for k1 in m.get('RecoverableInfoList'):
                temp_model = main_models.DescribeUniRecoverableListResponseBodyRecoverableInfoList()
                self.recoverable_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeUniRecoverableListResponseBodyRecoverableInfoList(DaraModel):
    def __init__(
        self,
        first_time: int = None,
        last_time: int = None,
        reset_scn: str = None,
        reset_time: int = None,
        restore_info: str = None,
    ):
        # The timestamp of the first backup. Unit: milliseconds.
        self.first_time = first_time
        # The timestamp of the last backup. Unit: milliseconds.
        self.last_time = last_time
        # The identifier of the point in time for restoration in the backup version that is used. The database is an Oracle database.
        self.reset_scn = reset_scn
        # The point in time for restoration in the backup version that is used. The database is an Oracle database.
        self.reset_time = reset_time
        # The information about the database. This parameter is available when the database is a Microsoft SQL Server (MSSQL) database. The value is a JSON string. Valid values:
        # 
        # *   **name**: the name of the database
        # *   **files**: the path to the database files
        self.restore_info = restore_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.reset_scn is not None:
            result['ResetScn'] = self.reset_scn

        if self.reset_time is not None:
            result['ResetTime'] = self.reset_time

        if self.restore_info is not None:
            result['RestoreInfo'] = self.restore_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('ResetScn') is not None:
            self.reset_scn = m.get('ResetScn')

        if m.get('ResetTime') is not None:
            self.reset_time = m.get('ResetTime')

        if m.get('RestoreInfo') is not None:
            self.restore_info = m.get('RestoreInfo')

        return self

