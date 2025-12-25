# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProxySQLExecAuditLogRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        exec_state: str = None,
        op_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        sqltype: str = None,
        search_name: str = None,
        start_time: int = None,
        tid: int = None,
    ):
        # The end of the time range to query. The value of this parameter must be a timestamp that follows the UNIX time format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The execution status of the SQL statement. Valid values:
        # 
        # *   **FAIL**: The execution of the SQL statement fails.
        # *   **CANCEL**: The execution of the SQL statement is canceled.
        # *   **SUCCESS**: The SQL statement is executed.
        self.exec_state = exec_state
        # The alias of the user.
        self.op_user_name = op_user_name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum values: 100.
        self.page_size = page_size
        # The type of SQL statement. Valid values:
        # 
        # *   **SELECT**
        # *   **INSERT**
        # *   **DELETE**
        # *   **CREATE_TABLE**
        # 
        # >  You can choose Operation Audit > Secure Access Proxy in the top navigation bar of the DMS console to view more types of SQL statements.
        self.sqltype = sqltype
        # The name of the database instance.
        self.search_name = search_name
        # The beginning of the time range to query. The value of this parameter must be a timestamp that follows the UNIX time format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.exec_state is not None:
            result['ExecState'] = self.exec_state

        if self.op_user_name is not None:
            result['OpUserName'] = self.op_user_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sqltype is not None:
            result['SQLType'] = self.sqltype

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecState') is not None:
            self.exec_state = m.get('ExecState')

        if m.get('OpUserName') is not None:
            self.op_user_name = m.get('OpUserName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

