# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSQLExecAuditLogRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        exec_state: str = None,
        op_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_name: str = None,
        sql_type: str = None,
        start_time: str = None,
        tid: int = None,
    ):
        # The end of the time range to query.
        # 
        # >  The end time supports fuzzy match. Specify the time in the YYYY-MM-DD hh:mm:ss format. We recommend that you use the StartTime and EndTime parameters to specify a time range that does not exceed one day. The returned entries can be displayed by page to improve query efficiency.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The execution status of the SQL statement. Valid values:
        # 
        # *   **FAIL**: The SQL statement fails to be executed.
        # *   **NOEXE**: The SQL statement has not been executed.
        # *   **RUNNING**: The SQL statement is being executed.
        # *   **CANCEL**: The execution of the SQL statement is canceled.
        # *   **SUCCESS**: The SQL statement is executed.
        self.exec_state = exec_state
        # The nickname of the user who wrote the SQL statement.
        self.op_user_name = op_user_name
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. The value cannot exceed 100.
        self.page_size = page_size
        # The name of the database or instance based on which you want to query SQL statements.
        # 
        # >  If the SQL statements to be queried are at the instance level, you can set this parameter to an instance name. If the SQL statements to be queried are at the database level, you can set this parameter to a database name.
        self.search_name = search_name
        # The type of the SQL statement. Valid values:
        # 
        # *   **SELECT**: the SQL statement that is used to query data.
        # *   **INSERT**: the SQL statement that is used to insert data.
        # *   **DELETE**: the SQL statement that is used to delete data.
        # *   **CREATE_TABLE**: the SQL statement that is used to create tables.
        # 
        # >  To view more types of SQL statements, log on to the DMS console and click Security and Specifications. In the left-side navigation pane, click **Operation Audit**. Then, you can view all supported types of SQL statements from the **SQL type** drop-down list.
        self.sql_type = sql_type
        # The beginning of the time range to query.
        # 
        # >  The start time supports fuzzy match. Specify the time in the YYYY-MM-DD hh:mm:ss format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
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

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

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

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

