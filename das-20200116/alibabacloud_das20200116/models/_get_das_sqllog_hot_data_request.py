# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDasSQLLogHotDataRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        child_dbinstance_ids: str = None,
        dbname: str = None,
        end: int = None,
        fail: str = None,
        host_address: str = None,
        instance_id: str = None,
        logical_operator: str = None,
        max_latancy: int = None,
        max_records_per_page: int = None,
        max_rows: int = None,
        max_scan_rows: int = None,
        max_spill_cnt: int = None,
        min_latancy: int = None,
        min_rows: int = None,
        min_scan_rows: int = None,
        min_spill_cnt: int = None,
        page_numbers: int = None,
        query_keyword: str = None,
        role: str = None,
        sort_key: str = None,
        sort_method: str = None,
        sql_type: str = None,
        start: int = None,
        state: str = None,
        thread_id: str = None,
        trace_id: str = None,
        transaction_id: str = None,
    ):
        # The database account.
        # 
        # > You can specify multiple database accounts. Separate multiple accounts with a space. For example: `user1 user2 user3`.
        self.account_name = account_name
        # The node ID.
        # 
        # > This parameter is required if the database instance is a PolarDB for MySQL cluster.
        self.child_dbinstance_ids = child_dbinstance_ids
        # The database name.
        # 
        # > You can specify multiple database names. Separate multiple names with a space. For example: `DB1 DB2 DB3`.
        self.dbname = dbname
        # The end of the time range to query. This value must be a Unix timestamp in milliseconds.
        # 
        # > The end time must be later than the start time. The time range cannot exceed one day.
        # 
        # This parameter is required.
        self.end = end
        # The SQL execution error code. You can call the [GetAsyncErrorRequestStatByCode](https://help.aliyun.com/document_detail/409804.html) operation to obtain the error code.
        self.fail = fail
        # The client IP address.
        # 
        # > You can specify multiple client IP addresses. Separate multiple IP addresses with a space. For example: `IP1 IP2 IP3`.
        self.host_address = host_address
        # The ID of the database instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The logical operator to use with multiple keywords. Valid values:
        # 
        # - **or**
        # 
        # - **and**
        self.logical_operator = logical_operator
        # The maximum execution time in microseconds. Returns SQL statements that have an execution time less than this value.
        self.max_latancy = max_latancy
        # The maximum number of entries per page. Valid values: 5 to 100.
        self.max_records_per_page = max_records_per_page
        # A reserved parameter.
        self.max_rows = max_rows
        # The maximum number of scanned rows. Returns SQL statements that scanned fewer than this number of rows.
        self.max_scan_rows = max_scan_rows
        # A reserved parameter.
        self.max_spill_cnt = max_spill_cnt
        # The minimum execution time in microseconds. Returns SQL statements with an execution time greater than or equal to this value.
        self.min_latancy = min_latancy
        # A reserved parameter.
        self.min_rows = min_rows
        # The minimum number of scanned rows. Returns SQL statements that scanned at least this number of rows.
        self.min_scan_rows = min_scan_rows
        # A reserved parameter.
        self.min_spill_cnt = min_spill_cnt
        # The page number to return. Pages start from 1. The default value is 1.
        self.page_numbers = page_numbers
        # The query keyword.
        # 
        # > Fuzzy search is supported. You can specify up to 10 keywords. Separate multiple keywords with a space. For example: a1 b2 c3.
        self.query_keyword = query_keyword
        # A reserved parameter.
        self.role = role
        # The sort key. Valid values:
        # 
        # - **ScanRows**: scanned rows.
        # 
        # - **UpdateRows**: updated rows.
        # 
        # - **Consume**: execution time.
        # 
        # - **OriginTime**: The execution start time.
        # 
        # - **ReturnRows**: returned rows.
        self.sort_key = sort_key
        # The sort order. Valid values:
        # 
        # - **ASC**: ascending
        # 
        # - **DESC**: descending
        self.sort_method = sort_method
        # The SQL type.
        self.sql_type = sql_type
        # The start of the time range to query. This value must be a Unix timestamp in milliseconds.
        # 
        # > You can query only data that is generated after you enable DAS Enterprise Edition. The start time cannot be earlier than seven days before the current time.
        # 
        # This parameter is required.
        self.start = start
        # The execution state. Set this parameter to **0** to query for successfully executed SQL statements. You can also specify an error code to query for the corresponding SQL statements.
        self.state = state
        # The thread ID.
        # 
        # > You can specify multiple thread IDs. Separate multiple IDs with a space. For example: `657 658 659`.
        self.thread_id = thread_id
        # A reserved parameter.
        self.trace_id = trace_id
        # The transaction ID.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.child_dbinstance_ids is not None:
            result['ChildDBInstanceIDs'] = self.child_dbinstance_ids

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.end is not None:
            result['End'] = self.end

        if self.fail is not None:
            result['Fail'] = self.fail

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator

        if self.max_latancy is not None:
            result['MaxLatancy'] = self.max_latancy

        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page

        if self.max_rows is not None:
            result['MaxRows'] = self.max_rows

        if self.max_scan_rows is not None:
            result['MaxScanRows'] = self.max_scan_rows

        if self.max_spill_cnt is not None:
            result['MaxSpillCnt'] = self.max_spill_cnt

        if self.min_latancy is not None:
            result['MinLatancy'] = self.min_latancy

        if self.min_rows is not None:
            result['MinRows'] = self.min_rows

        if self.min_scan_rows is not None:
            result['MinScanRows'] = self.min_scan_rows

        if self.min_spill_cnt is not None:
            result['MinSpillCnt'] = self.min_spill_cnt

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword

        if self.role is not None:
            result['Role'] = self.role

        if self.sort_key is not None:
            result['SortKey'] = self.sort_key

        if self.sort_method is not None:
            result['SortMethod'] = self.sort_method

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start is not None:
            result['Start'] = self.start

        if self.state is not None:
            result['State'] = self.state

        if self.thread_id is not None:
            result['ThreadID'] = self.thread_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ChildDBInstanceIDs') is not None:
            self.child_dbinstance_ids = m.get('ChildDBInstanceIDs')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')

        if m.get('MaxLatancy') is not None:
            self.max_latancy = m.get('MaxLatancy')

        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')

        if m.get('MaxRows') is not None:
            self.max_rows = m.get('MaxRows')

        if m.get('MaxScanRows') is not None:
            self.max_scan_rows = m.get('MaxScanRows')

        if m.get('MaxSpillCnt') is not None:
            self.max_spill_cnt = m.get('MaxSpillCnt')

        if m.get('MinLatancy') is not None:
            self.min_latancy = m.get('MinLatancy')

        if m.get('MinRows') is not None:
            self.min_rows = m.get('MinRows')

        if m.get('MinScanRows') is not None:
            self.min_scan_rows = m.get('MinScanRows')

        if m.get('MinSpillCnt') is not None:
            self.min_spill_cnt = m.get('MinSpillCnt')

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')

        if m.get('SortMethod') is not None:
            self.sort_method = m.get('SortMethod')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('ThreadID') is not None:
            self.thread_id = m.get('ThreadID')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

