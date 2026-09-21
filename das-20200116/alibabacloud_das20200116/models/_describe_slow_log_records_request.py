# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowLogRecordsRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        end_time: int = None,
        filters: List[main_models.DescribeSlowLogRecordsRequestFilters] = None,
        instance_id: str = None,
        node_id: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # Specifies whether to sort the results in ascending order. Default value: **true**.
        # 
        # - **true**: Sort in ascending order.
        # - **false**: Sort in descending order.
        self.asc = asc
        # The end time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The list of filter conditions.
        self.filters = filters
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        self.node_id = node_id
        # - **Common to all engines** 
        #   - QueryTimeSeconds: query duration (seconds).
        #   - Timestamp: timestamp.
        # 
        # - **SQL-based engines (MySQL / PolarDB for MySQL / PostgreSQL / PolarDB for PostgreSQL / PolarDB for Oracle / PolarDB-X DN)**
        #   - LockTimeSeconds: lock time (seconds).
        #   - RowsExamined: rows examined.
        #   - RowsSent: rows returned.
        # 
        # - **MongoDB**
        #   - KeysExamined: number of indexes scanned.
        #   - DocExamined: number of documents scanned.
        #   - ReturnNum: rows returned.
        # 
        # - **SQL Server**
        #   - CPUTimeSeconds: CPU time.
        #   - IOWrites: number of I/O writes.
        #   - LastRowsCountAffected: last rows affected.
        #   - LogicalIOReads: logical I/O reads.
        #   - PhysicalIOReads: physical I/O reads.
        #   - RowsCountAffected: rows affected.
        # 
        # - **PolarDB-X CN**
        #   - RowsSent: rows returned or updated.
        #   - Frows: rows fetched.
        #   - Scnt: number of physical SQL statements.
        self.order_by = order_by
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The start time.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['Asc'] = self.asc

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeSlowLogRecordsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeSlowLogRecordsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter parameter.
        # 
        # > For more information, refer to the supplementary description.
        self.key = key
        # The value of the filter parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

