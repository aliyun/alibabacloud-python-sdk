# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSensitiveDataAuditLogRequest(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        db_name: str = None,
        end_time: str = None,
        module_name: str = None,
        op_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        # The name of the column that contains sensitive data.
        self.column_name = column_name
        # The name of the database that stores the sensitive data.
        self.db_name = db_name
        # The end of the time range for which you want to query the audit logs for sensitive information. Specify the time in the yyyy-MM-DD HH:mm:ss format.
        self.end_time = end_time
        # The function module whose audit logs you want to query for sensitive data. If you do not specify this parameter, all audit logs are queried. Valid values:
        # 
        # *   **SQL_CONSOLE**: data query
        # *   **SQL_CONSOLE_EXPORT**: query result export
        # *   **DATA_CHANGE**: data change
        # *   **DATA_EXPORT**: data export
        self.module_name = module_name
        # The username of the requester.
        self.op_user_name = op_user_name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. Example: 100
        self.page_size = page_size
        # The beginning of the time range for which you want to query the audit logs for sensitive information. Specify the time in the yyyy-MM-DD HH:mm:ss format.
        self.start_time = start_time
        # The name of the table that stores the sensitive data.
        self.table_name = table_name
        # The ID of the tenant.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.op_user_name is not None:
            result['OpUserName'] = self.op_user_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('OpUserName') is not None:
            self.op_user_name = m.get('OpUserName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

