# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLLogsV2ResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        items: List[main_models.DescribeSQLLogsV2ResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The queried SQL execution logs.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSQLLogsV2ResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSQLLogsV2ResponseBodyItems(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbname: str = None,
        dbrole: str = None,
        error_code: str = None,
        error_msg: str = None,
        execute_cost: float = None,
        execute_state: str = None,
        operation_class: str = None,
        operation_execute_time: str = None,
        operation_type: str = None,
        query_id: str = None,
        return_row_counts: int = None,
        sqltext: str = None,
        scan_row_counts: int = None,
        session_id: str = None,
        source_ip: str = None,
        source_port: int = None,
    ):
        # The database account that executes the SQL statement.
        self.account_name = account_name
        # The name of the database.
        self.dbname = dbname
        # The role of the database.
        self.dbrole = dbrole
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The execution duration of the SQL statement.
        self.execute_cost = execute_cost
        # The execution status of the SQL statement. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.execute_state = execute_state
        # The type of the query language.
        self.operation_class = operation_class
        # The time when the SQL statement was executed.
        self.operation_execute_time = operation_execute_time
        # The type of the SQL statement.
        self.operation_type = operation_type
        # The query ID.
        self.query_id = query_id
        # The number of entries returned.
        self.return_row_counts = return_row_counts
        # The SQL statement.
        self.sqltext = sqltext
        # The number of entries scanned.
        self.scan_row_counts = scan_row_counts
        # The ID of the session.
        self.session_id = session_id
        # The source IP address.
        self.source_ip = source_ip
        # The number of the source port.
        self.source_port = source_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbrole is not None:
            result['DBRole'] = self.dbrole

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost

        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state

        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class

        if self.operation_execute_time is not None:
            result['OperationExecuteTime'] = self.operation_execute_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBRole') is not None:
            self.dbrole = m.get('DBRole')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')

        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')

        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')

        if m.get('OperationExecuteTime') is not None:
            self.operation_execute_time = m.get('OperationExecuteTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        return self

