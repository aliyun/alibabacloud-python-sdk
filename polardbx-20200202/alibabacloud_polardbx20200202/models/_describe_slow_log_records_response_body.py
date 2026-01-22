# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        items: List[main_models.DescribeSlowLogRecordsResponseBodyItems] = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSlowLogRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSlowLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        cnname: str = None,
        dbname: str = None,
        extension: str = None,
        fail: str = None,
        frows: str = None,
        host_address: str = None,
        ins_name: str = None,
        is_bind: str = None,
        lock_time_ms: str = None,
        params: str = None,
        parse_row_counts: str = None,
        query_start_time: str = None,
        query_time: str = None,
        query_time_ms: str = None,
        return_row_counts: str = None,
        rows: str = None,
        scnt: str = None,
        sqlhash: str = None,
        sqltext: str = None,
        sql_type: str = None,
        template_id: str = None,
        too_long: str = None,
        trace_id: str = None,
        transaction_policy: str = None,
        trx_id: str = None,
        wt: str = None,
    ):
        self.cnname = cnname
        self.dbname = dbname
        self.extension = extension
        self.fail = fail
        self.frows = frows
        self.host_address = host_address
        self.ins_name = ins_name
        self.is_bind = is_bind
        self.lock_time_ms = lock_time_ms
        self.params = params
        self.parse_row_counts = parse_row_counts
        self.query_start_time = query_start_time
        self.query_time = query_time
        self.query_time_ms = query_time_ms
        self.return_row_counts = return_row_counts
        self.rows = rows
        self.scnt = scnt
        self.sqlhash = sqlhash
        self.sqltext = sqltext
        self.sql_type = sql_type
        self.template_id = template_id
        self.too_long = too_long
        self.trace_id = trace_id
        self.transaction_policy = transaction_policy
        self.trx_id = trx_id
        self.wt = wt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnname is not None:
            result['CNname'] = self.cnname

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.fail is not None:
            result['Fail'] = self.fail

        if self.frows is not None:
            result['Frows'] = self.frows

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        if self.is_bind is not None:
            result['IsBind'] = self.is_bind

        if self.lock_time_ms is not None:
            result['LockTimeMS'] = self.lock_time_ms

        if self.params is not None:
            result['Params'] = self.params

        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.query_time_ms is not None:
            result['QueryTimeMS'] = self.query_time_ms

        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.scnt is not None:
            result['SCNT'] = self.scnt

        if self.sqlhash is not None:
            result['SQLHash'] = self.sqlhash

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.too_long is not None:
            result['TooLong'] = self.too_long

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.transaction_policy is not None:
            result['TransactionPolicy'] = self.transaction_policy

        if self.trx_id is not None:
            result['TrxId'] = self.trx_id

        if self.wt is not None:
            result['WT'] = self.wt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CNname') is not None:
            self.cnname = m.get('CNname')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('Frows') is not None:
            self.frows = m.get('Frows')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        if m.get('IsBind') is not None:
            self.is_bind = m.get('IsBind')

        if m.get('LockTimeMS') is not None:
            self.lock_time_ms = m.get('LockTimeMS')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('QueryTimeMS') is not None:
            self.query_time_ms = m.get('QueryTimeMS')

        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('SCNT') is not None:
            self.scnt = m.get('SCNT')

        if m.get('SQLHash') is not None:
            self.sqlhash = m.get('SQLHash')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TooLong') is not None:
            self.too_long = m.get('TooLong')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('TransactionPolicy') is not None:
            self.transaction_policy = m.get('TransactionPolicy')

        if m.get('TrxId') is not None:
            self.trx_id = m.get('TrxId')

        if m.get('WT') is not None:
            self.wt = m.get('WT')

        return self

