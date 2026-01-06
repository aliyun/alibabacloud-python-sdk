# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogHistogramAsyncResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSlowLogHistogramAsyncResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        # AsyncResult<Histogram>。
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.DescribeSlowLogHistogramAsyncResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSlowLogHistogramAsyncResponseBodyData(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSlowLogHistogramAsyncResponseBodyDataData = None,
        error_code: int = None,
        is_finish: bool = None,
        message: str = None,
        request_key: str = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.is_finish = is_finish
        self.message = message
        self.request_key = request_key
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish

        if self.message is not None:
            result['Message'] = self.message

        if self.request_key is not None:
            result['RequestKey'] = self.request_key

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.state is not None:
            result['State'] = self.state

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSlowLogHistogramAsyncResponseBodyDataData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestKey') is not None:
            self.request_key = m.get('RequestKey')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class DescribeSlowLogHistogramAsyncResponseBodyDataData(DaraModel):
    def __init__(
        self,
        avg_cputime: List[float] = None,
        avg_doc_examined: List[float] = None,
        avg_frows: List[float] = None,
        avg_iowrites: List[float] = None,
        avg_keys_examined: List[float] = None,
        avg_last_rows_count_affected: List[float] = None,
        avg_lock_time: List[float] = None,
        avg_logical_ioreads: List[float] = None,
        avg_physical_ioreads: List[float] = None,
        avg_return_num: List[float] = None,
        avg_rows: List[float] = None,
        avg_rows_count_affected: List[float] = None,
        avg_rows_examined: List[float] = None,
        avg_rows_sent: List[float] = None,
        avg_rt: List[float] = None,
        avg_scnt: List[float] = None,
        cputime: List[float] = None,
        count: List[int] = None,
        doc_examined: List[int] = None,
        frows: List[int] = None,
        iowrites: List[int] = None,
        item: List[main_models.DescribeSlowLogHistogramAsyncResponseBodyDataDataItem] = None,
        keys_examined: List[int] = None,
        last_rows_count_affected: List[int] = None,
        lock_time: List[float] = None,
        logical_ioreads: List[int] = None,
        max_cputime: List[float] = None,
        max_doc_examined: List[int] = None,
        max_frows: List[int] = None,
        max_iowrites: List[int] = None,
        max_keys_examined: List[int] = None,
        max_last_rows_count_affected: List[int] = None,
        max_lock_time: List[float] = None,
        max_logical_ioreads: List[int] = None,
        max_physical_ioreads: List[int] = None,
        max_return_num: List[int] = None,
        max_rows: List[int] = None,
        max_rows_count_affected: List[int] = None,
        max_rows_examined: List[int] = None,
        max_rows_sent: List[int] = None,
        max_rt: List[float] = None,
        max_scnt: List[int] = None,
        physical_ioreads: List[int] = None,
        return_num: List[int] = None,
        rows: List[int] = None,
        rows_count_affected: List[int] = None,
        rows_examined: List[int] = None,
        rows_sent: List[int] = None,
        rt: List[float] = None,
        scnt: List[int] = None,
        total: int = None,
        total_count: int = None,
        ts: List[int] = None,
        ts_end: List[int] = None,
    ):
        self.avg_cputime = avg_cputime
        self.avg_doc_examined = avg_doc_examined
        self.avg_frows = avg_frows
        self.avg_iowrites = avg_iowrites
        self.avg_keys_examined = avg_keys_examined
        self.avg_last_rows_count_affected = avg_last_rows_count_affected
        self.avg_lock_time = avg_lock_time
        self.avg_logical_ioreads = avg_logical_ioreads
        self.avg_physical_ioreads = avg_physical_ioreads
        self.avg_return_num = avg_return_num
        self.avg_rows = avg_rows
        self.avg_rows_count_affected = avg_rows_count_affected
        self.avg_rows_examined = avg_rows_examined
        self.avg_rows_sent = avg_rows_sent
        self.avg_rt = avg_rt
        self.avg_scnt = avg_scnt
        self.cputime = cputime
        self.count = count
        self.doc_examined = doc_examined
        self.frows = frows
        self.iowrites = iowrites
        self.item = item
        self.keys_examined = keys_examined
        self.last_rows_count_affected = last_rows_count_affected
        self.lock_time = lock_time
        self.logical_ioreads = logical_ioreads
        self.max_cputime = max_cputime
        self.max_doc_examined = max_doc_examined
        self.max_frows = max_frows
        self.max_iowrites = max_iowrites
        self.max_keys_examined = max_keys_examined
        self.max_last_rows_count_affected = max_last_rows_count_affected
        self.max_lock_time = max_lock_time
        self.max_logical_ioreads = max_logical_ioreads
        self.max_physical_ioreads = max_physical_ioreads
        self.max_return_num = max_return_num
        self.max_rows = max_rows
        self.max_rows_count_affected = max_rows_count_affected
        self.max_rows_examined = max_rows_examined
        self.max_rows_sent = max_rows_sent
        self.max_rt = max_rt
        self.max_scnt = max_scnt
        self.physical_ioreads = physical_ioreads
        self.return_num = return_num
        self.rows = rows
        self.rows_count_affected = rows_count_affected
        self.rows_examined = rows_examined
        self.rows_sent = rows_sent
        self.rt = rt
        self.scnt = scnt
        self.total = total
        self.total_count = total_count
        self.ts = ts
        self.ts_end = ts_end

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_cputime is not None:
            result['AvgCPUTime'] = self.avg_cputime

        if self.avg_doc_examined is not None:
            result['AvgDocExamined'] = self.avg_doc_examined

        if self.avg_frows is not None:
            result['AvgFrows'] = self.avg_frows

        if self.avg_iowrites is not None:
            result['AvgIOWrites'] = self.avg_iowrites

        if self.avg_keys_examined is not None:
            result['AvgKeysExamined'] = self.avg_keys_examined

        if self.avg_last_rows_count_affected is not None:
            result['AvgLastRowsCountAffected'] = self.avg_last_rows_count_affected

        if self.avg_lock_time is not None:
            result['AvgLockTime'] = self.avg_lock_time

        if self.avg_logical_ioreads is not None:
            result['AvgLogicalIOReads'] = self.avg_logical_ioreads

        if self.avg_physical_ioreads is not None:
            result['AvgPhysicalIOReads'] = self.avg_physical_ioreads

        if self.avg_return_num is not None:
            result['AvgReturnNum'] = self.avg_return_num

        if self.avg_rows is not None:
            result['AvgRows'] = self.avg_rows

        if self.avg_rows_count_affected is not None:
            result['AvgRowsCountAffected'] = self.avg_rows_count_affected

        if self.avg_rows_examined is not None:
            result['AvgRowsExamined'] = self.avg_rows_examined

        if self.avg_rows_sent is not None:
            result['AvgRowsSent'] = self.avg_rows_sent

        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt

        if self.avg_scnt is not None:
            result['AvgScnt'] = self.avg_scnt

        if self.cputime is not None:
            result['CPUTime'] = self.cputime

        if self.count is not None:
            result['Count'] = self.count

        if self.doc_examined is not None:
            result['DocExamined'] = self.doc_examined

        if self.frows is not None:
            result['Frows'] = self.frows

        if self.iowrites is not None:
            result['IOWrites'] = self.iowrites

        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        if self.keys_examined is not None:
            result['KeysExamined'] = self.keys_examined

        if self.last_rows_count_affected is not None:
            result['LastRowsCountAffected'] = self.last_rows_count_affected

        if self.lock_time is not None:
            result['LockTime'] = self.lock_time

        if self.logical_ioreads is not None:
            result['LogicalIOReads'] = self.logical_ioreads

        if self.max_cputime is not None:
            result['MaxCPUTime'] = self.max_cputime

        if self.max_doc_examined is not None:
            result['MaxDocExamined'] = self.max_doc_examined

        if self.max_frows is not None:
            result['MaxFrows'] = self.max_frows

        if self.max_iowrites is not None:
            result['MaxIOWrites'] = self.max_iowrites

        if self.max_keys_examined is not None:
            result['MaxKeysExamined'] = self.max_keys_examined

        if self.max_last_rows_count_affected is not None:
            result['MaxLastRowsCountAffected'] = self.max_last_rows_count_affected

        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time

        if self.max_logical_ioreads is not None:
            result['MaxLogicalIOReads'] = self.max_logical_ioreads

        if self.max_physical_ioreads is not None:
            result['MaxPhysicalIOReads'] = self.max_physical_ioreads

        if self.max_return_num is not None:
            result['MaxReturnNum'] = self.max_return_num

        if self.max_rows is not None:
            result['MaxRows'] = self.max_rows

        if self.max_rows_count_affected is not None:
            result['MaxRowsCountAffected'] = self.max_rows_count_affected

        if self.max_rows_examined is not None:
            result['MaxRowsExamined'] = self.max_rows_examined

        if self.max_rows_sent is not None:
            result['MaxRowsSent'] = self.max_rows_sent

        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt

        if self.max_scnt is not None:
            result['MaxScnt'] = self.max_scnt

        if self.physical_ioreads is not None:
            result['PhysicalIOReads'] = self.physical_ioreads

        if self.return_num is not None:
            result['ReturnNum'] = self.return_num

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.rows_count_affected is not None:
            result['RowsCountAffected'] = self.rows_count_affected

        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined

        if self.rows_sent is not None:
            result['RowsSent'] = self.rows_sent

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.scnt is not None:
            result['Scnt'] = self.scnt

        if self.total is not None:
            result['Total'] = self.total

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.ts is not None:
            result['Ts'] = self.ts

        if self.ts_end is not None:
            result['TsEnd'] = self.ts_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgCPUTime') is not None:
            self.avg_cputime = m.get('AvgCPUTime')

        if m.get('AvgDocExamined') is not None:
            self.avg_doc_examined = m.get('AvgDocExamined')

        if m.get('AvgFrows') is not None:
            self.avg_frows = m.get('AvgFrows')

        if m.get('AvgIOWrites') is not None:
            self.avg_iowrites = m.get('AvgIOWrites')

        if m.get('AvgKeysExamined') is not None:
            self.avg_keys_examined = m.get('AvgKeysExamined')

        if m.get('AvgLastRowsCountAffected') is not None:
            self.avg_last_rows_count_affected = m.get('AvgLastRowsCountAffected')

        if m.get('AvgLockTime') is not None:
            self.avg_lock_time = m.get('AvgLockTime')

        if m.get('AvgLogicalIOReads') is not None:
            self.avg_logical_ioreads = m.get('AvgLogicalIOReads')

        if m.get('AvgPhysicalIOReads') is not None:
            self.avg_physical_ioreads = m.get('AvgPhysicalIOReads')

        if m.get('AvgReturnNum') is not None:
            self.avg_return_num = m.get('AvgReturnNum')

        if m.get('AvgRows') is not None:
            self.avg_rows = m.get('AvgRows')

        if m.get('AvgRowsCountAffected') is not None:
            self.avg_rows_count_affected = m.get('AvgRowsCountAffected')

        if m.get('AvgRowsExamined') is not None:
            self.avg_rows_examined = m.get('AvgRowsExamined')

        if m.get('AvgRowsSent') is not None:
            self.avg_rows_sent = m.get('AvgRowsSent')

        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')

        if m.get('AvgScnt') is not None:
            self.avg_scnt = m.get('AvgScnt')

        if m.get('CPUTime') is not None:
            self.cputime = m.get('CPUTime')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DocExamined') is not None:
            self.doc_examined = m.get('DocExamined')

        if m.get('Frows') is not None:
            self.frows = m.get('Frows')

        if m.get('IOWrites') is not None:
            self.iowrites = m.get('IOWrites')

        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeSlowLogHistogramAsyncResponseBodyDataDataItem()
                self.item.append(temp_model.from_map(k1))

        if m.get('KeysExamined') is not None:
            self.keys_examined = m.get('KeysExamined')

        if m.get('LastRowsCountAffected') is not None:
            self.last_rows_count_affected = m.get('LastRowsCountAffected')

        if m.get('LockTime') is not None:
            self.lock_time = m.get('LockTime')

        if m.get('LogicalIOReads') is not None:
            self.logical_ioreads = m.get('LogicalIOReads')

        if m.get('MaxCPUTime') is not None:
            self.max_cputime = m.get('MaxCPUTime')

        if m.get('MaxDocExamined') is not None:
            self.max_doc_examined = m.get('MaxDocExamined')

        if m.get('MaxFrows') is not None:
            self.max_frows = m.get('MaxFrows')

        if m.get('MaxIOWrites') is not None:
            self.max_iowrites = m.get('MaxIOWrites')

        if m.get('MaxKeysExamined') is not None:
            self.max_keys_examined = m.get('MaxKeysExamined')

        if m.get('MaxLastRowsCountAffected') is not None:
            self.max_last_rows_count_affected = m.get('MaxLastRowsCountAffected')

        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')

        if m.get('MaxLogicalIOReads') is not None:
            self.max_logical_ioreads = m.get('MaxLogicalIOReads')

        if m.get('MaxPhysicalIOReads') is not None:
            self.max_physical_ioreads = m.get('MaxPhysicalIOReads')

        if m.get('MaxReturnNum') is not None:
            self.max_return_num = m.get('MaxReturnNum')

        if m.get('MaxRows') is not None:
            self.max_rows = m.get('MaxRows')

        if m.get('MaxRowsCountAffected') is not None:
            self.max_rows_count_affected = m.get('MaxRowsCountAffected')

        if m.get('MaxRowsExamined') is not None:
            self.max_rows_examined = m.get('MaxRowsExamined')

        if m.get('MaxRowsSent') is not None:
            self.max_rows_sent = m.get('MaxRowsSent')

        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')

        if m.get('MaxScnt') is not None:
            self.max_scnt = m.get('MaxScnt')

        if m.get('PhysicalIOReads') is not None:
            self.physical_ioreads = m.get('PhysicalIOReads')

        if m.get('ReturnNum') is not None:
            self.return_num = m.get('ReturnNum')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RowsCountAffected') is not None:
            self.rows_count_affected = m.get('RowsCountAffected')

        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')

        if m.get('RowsSent') is not None:
            self.rows_sent = m.get('RowsSent')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('Scnt') is not None:
            self.scnt = m.get('Scnt')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        if m.get('TsEnd') is not None:
            self.ts_end = m.get('TsEnd')

        return self

class DescribeSlowLogHistogramAsyncResponseBodyDataDataItem(DaraModel):
    def __init__(
        self,
        count: List[int] = None,
        ins_items: List[main_models.DescribeSlowLogHistogramAsyncResponseBodyDataDataItemInsItems] = None,
        ins_role: str = None,
        node_id: str = None,
        total_count: int = None,
    ):
        self.count = count
        self.ins_items = ins_items
        self.ins_role = ins_role
        self.node_id = node_id
        self.total_count = total_count

    def validate(self):
        if self.ins_items:
            for v1 in self.ins_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['InsItems'] = []
        if self.ins_items is not None:
            for k1 in self.ins_items:
                result['InsItems'].append(k1.to_map() if k1 else None)

        if self.ins_role is not None:
            result['InsRole'] = self.ins_role

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ins_items = []
        if m.get('InsItems') is not None:
            for k1 in m.get('InsItems'):
                temp_model = main_models.DescribeSlowLogHistogramAsyncResponseBodyDataDataItemInsItems()
                self.ins_items.append(temp_model.from_map(k1))

        if m.get('InsRole') is not None:
            self.ins_role = m.get('InsRole')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSlowLogHistogramAsyncResponseBodyDataDataItemInsItems(DaraModel):
    def __init__(
        self,
        count: List[int] = None,
        ins_id: str = None,
        ins_role: str = None,
        total_count: int = None,
    ):
        self.count = count
        self.ins_id = ins_id
        self.ins_role = ins_role
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.ins_id is not None:
            result['InsId'] = self.ins_id

        if self.ins_role is not None:
            result['InsRole'] = self.ins_role

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('InsId') is not None:
            self.ins_id = m.get('InsId')

        if m.get('InsRole') is not None:
            self.ins_role = m.get('InsRole')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

