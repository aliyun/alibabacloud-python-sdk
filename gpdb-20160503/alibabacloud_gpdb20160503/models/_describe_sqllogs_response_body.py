# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLLogsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeSQLLogsResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
    ):
        # The queried SQL execution logs.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
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
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSQLLogsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSQLLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbname: str = None,
        dbrole: str = None,
        execute_cost: float = None,
        execute_state: str = None,
        operation_class: str = None,
        operation_execute_time: str = None,
        operation_type: str = None,
        return_row_counts: int = None,
        sqlplan: str = None,
        sqltext: str = None,
        scan_row_counts: int = None,
        source_ip: str = None,
        source_port: int = None,
    ):
        # The database account that executes the SQL statement.
        self.account_name = account_name
        # The name of the database.
        self.dbname = dbname
        # The role of the database.
        self.dbrole = dbrole
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
        # The total number of entries returned.
        self.return_row_counts = return_row_counts
        # The SQL execution plan.
        self.sqlplan = sqlplan
        # The SQL statement.
        self.sqltext = sqltext
        # The number of entries scanned.
        self.scan_row_counts = scan_row_counts
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

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.sqlplan is not None:
            result['SQLPlan'] = self.sqlplan

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.scan_row_counts is not None:
            result['ScanRowCounts'] = self.scan_row_counts

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

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('SQLPlan') is not None:
            self.sqlplan = m.get('SQLPlan')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('ScanRowCounts') is not None:
            self.scan_row_counts = m.get('ScanRowCounts')

        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        return self

