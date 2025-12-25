# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DownloadDataTrackResultRequest(DaraModel):
    def __init__(
        self,
        column_filter: main_models.DownloadDataTrackResultRequestColumnFilter = None,
        event_id_list: List[int] = None,
        filter_end_time: str = None,
        filter_start_time: str = None,
        filter_table_list: List[str] = None,
        filter_type_list: List[str] = None,
        order_id: int = None,
        rollback_sqltype: str = None,
        tid: int = None,
    ):
        # The condition to filter columns.
        self.column_filter = column_filter
        # The IDs of the events.
        self.event_id_list = event_id_list
        # The end time of the time range in which you want to track data operations. The time must be specified in the yyyy-MM-dd HH:mm:ss format.
        self.filter_end_time = filter_end_time
        # The start time of the time range in which you want to track data operations. The time must be specified in the yyyy-MM-dd HH:mm:ss format.
        self.filter_start_time = filter_start_time
        # The names of the tables for which you want to track data operations.
        self.filter_table_list = filter_table_list
        # The types of data operations that you want to track.
        self.filter_type_list = filter_type_list
        # The ID of the ticket. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to obtain the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The type of the SQL statement.
        # 
        # *   **REVERSE**: undoes or rolls back an executed SQL statement, which is equivalent to the UNDO SQL statement.
        # *   **FORWARD**: redoes or re-executes an SQL statement that failed to be executed, which is equivalent to the REDO SQL statement.
        # 
        # This parameter is required.
        self.rollback_sqltype = rollback_sqltype
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        if self.column_filter:
            self.column_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_filter is not None:
            result['ColumnFilter'] = self.column_filter.to_map()

        if self.event_id_list is not None:
            result['EventIdList'] = self.event_id_list

        if self.filter_end_time is not None:
            result['FilterEndTime'] = self.filter_end_time

        if self.filter_start_time is not None:
            result['FilterStartTime'] = self.filter_start_time

        if self.filter_table_list is not None:
            result['FilterTableList'] = self.filter_table_list

        if self.filter_type_list is not None:
            result['FilterTypeList'] = self.filter_type_list

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.rollback_sqltype is not None:
            result['RollbackSQLType'] = self.rollback_sqltype

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnFilter') is not None:
            temp_model = main_models.DownloadDataTrackResultRequestColumnFilter()
            self.column_filter = temp_model.from_map(m.get('ColumnFilter'))

        if m.get('EventIdList') is not None:
            self.event_id_list = m.get('EventIdList')

        if m.get('FilterEndTime') is not None:
            self.filter_end_time = m.get('FilterEndTime')

        if m.get('FilterStartTime') is not None:
            self.filter_start_time = m.get('FilterStartTime')

        if m.get('FilterTableList') is not None:
            self.filter_table_list = m.get('FilterTableList')

        if m.get('FilterTypeList') is not None:
            self.filter_type_list = m.get('FilterTypeList')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RollbackSQLType') is not None:
            self.rollback_sqltype = m.get('RollbackSQLType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class DownloadDataTrackResultRequestColumnFilter(DaraModel):
    def __init__(
        self,
        between_end: str = None,
        between_start: str = None,
        column_name: str = None,
        in_list: List[str] = None,
        operator: str = None,
        value: str = None,
    ):
        # The end value of the range used in the filter condition. This parameter takes effect only when Operator is set to BETWEEN.
        self.between_end = between_end
        # The start value of the range used in the filter condition. This parameter takes effect only when Operator is set to BETWEEN.
        self.between_start = between_start
        # The name of the column.
        self.column_name = column_name
        # The IN list used in the filter condition.
        self.in_list = in_list
        # The type of the operator used to configure the filter condition. Valid values:
        # 
        # *   **EQUAL**: retrieves the column whose value is equal to the specified value.
        # *   **NOT_EQUAL**: retrieves the column whose value is not equal to the specified value.
        # *   **IN**: retrieves the column whose value is in the IN list.
        # *   **BETWEEN**: retrieves the column whose value is in the specified range.
        # *   **LESS**: retrieves the column whose value is less than the specified value.
        # *   **MORE**: retrieves the column whose value is greater than the specified value.
        # *   **NOT_IN**: retrieves the column whose value is not in the IN list.
        self.operator = operator
        # The value used in the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.between_end is not None:
            result['BetweenEnd'] = self.between_end

        if self.between_start is not None:
            result['BetweenStart'] = self.between_start

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.in_list is not None:
            result['InList'] = self.in_list

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BetweenEnd') is not None:
            self.between_end = m.get('BetweenEnd')

        if m.get('BetweenStart') is not None:
            self.between_start = m.get('BetweenStart')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('InList') is not None:
            self.in_list = m.get('InList')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

