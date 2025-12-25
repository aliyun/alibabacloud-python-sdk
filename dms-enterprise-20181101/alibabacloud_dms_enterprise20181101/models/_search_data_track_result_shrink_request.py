# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchDataTrackResultShrinkRequest(DaraModel):
    def __init__(
        self,
        column_filter_shrink: str = None,
        filter_end_time: str = None,
        filter_start_time: str = None,
        filter_table_list_shrink: str = None,
        filter_type_list_shrink: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        # The condition to filter columns.
        self.column_filter_shrink = column_filter_shrink
        # The end time of the time range in which you want to track data operations. The time must be in the yyyy-MM-dd HH:mm:ss format.
        self.filter_end_time = filter_end_time
        # The start time of the time range in which you want to track data operations. The time must be in the yyyy-MM-dd HH:mm:ss format.
        self.filter_start_time = filter_start_time
        # The names of the tables for which you want to track data operations.
        self.filter_table_list_shrink = filter_table_list_shrink
        # The types of data operations that you want to track.
        self.filter_type_list_shrink = filter_type_list_shrink
        # The ID of the ticket. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to query the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_filter_shrink is not None:
            result['ColumnFilter'] = self.column_filter_shrink

        if self.filter_end_time is not None:
            result['FilterEndTime'] = self.filter_end_time

        if self.filter_start_time is not None:
            result['FilterStartTime'] = self.filter_start_time

        if self.filter_table_list_shrink is not None:
            result['FilterTableList'] = self.filter_table_list_shrink

        if self.filter_type_list_shrink is not None:
            result['FilterTypeList'] = self.filter_type_list_shrink

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnFilter') is not None:
            self.column_filter_shrink = m.get('ColumnFilter')

        if m.get('FilterEndTime') is not None:
            self.filter_end_time = m.get('FilterEndTime')

        if m.get('FilterStartTime') is not None:
            self.filter_start_time = m.get('FilterStartTime')

        if m.get('FilterTableList') is not None:
            self.filter_table_list_shrink = m.get('FilterTableList')

        if m.get('FilterTypeList') is not None:
            self.filter_type_list_shrink = m.get('FilterTypeList')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

