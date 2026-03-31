# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryTunnelMetricDetailRequest(DaraModel):
    def __init__(
        self,
        asc_order: bool = None,
        group_list: List[str] = None,
        limit: int = None,
        operation_list: List[str] = None,
        order_column: str = None,
        project: str = None,
        quota_nickname: str = None,
        table_list: List[str] = None,
        end_time: int = None,
        start_time: int = None,
    ):
        self.asc_order = asc_order
        self.group_list = group_list
        self.limit = limit
        self.operation_list = operation_list
        self.order_column = order_column
        self.project = project
        self.quota_nickname = quota_nickname
        self.table_list = table_list
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order

        if self.group_list is not None:
            result['groupList'] = self.group_list

        if self.limit is not None:
            result['limit'] = self.limit

        if self.operation_list is not None:
            result['operationList'] = self.operation_list

        if self.order_column is not None:
            result['orderColumn'] = self.order_column

        if self.project is not None:
            result['project'] = self.project

        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname

        if self.table_list is not None:
            result['tableList'] = self.table_list

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')

        if m.get('groupList') is not None:
            self.group_list = m.get('groupList')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('operationList') is not None:
            self.operation_list = m.get('operationList')

        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')

        if m.get('tableList') is not None:
            self.table_list = m.get('tableList')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

