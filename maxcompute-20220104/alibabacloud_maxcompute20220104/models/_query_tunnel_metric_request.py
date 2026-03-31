# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryTunnelMetricRequest(DaraModel):
    def __init__(
        self,
        code_list: List[int] = None,
        group_list: List[str] = None,
        operation_list: List[str] = None,
        project: str = None,
        quota_nickname: str = None,
        table_list: List[str] = None,
        top_n: int = None,
        end_time: int = None,
        start_time: int = None,
        strategy: str = None,
    ):
        self.code_list = code_list
        self.group_list = group_list
        self.operation_list = operation_list
        self.project = project
        self.quota_nickname = quota_nickname
        self.table_list = table_list
        self.top_n = top_n
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_list is not None:
            result['codeList'] = self.code_list

        if self.group_list is not None:
            result['groupList'] = self.group_list

        if self.operation_list is not None:
            result['operationList'] = self.operation_list

        if self.project is not None:
            result['project'] = self.project

        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname

        if self.table_list is not None:
            result['tableList'] = self.table_list

        if self.top_n is not None:
            result['topN'] = self.top_n

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.strategy is not None:
            result['strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeList') is not None:
            self.code_list = m.get('codeList')

        if m.get('groupList') is not None:
            self.group_list = m.get('groupList')

        if m.get('operationList') is not None:
            self.operation_list = m.get('operationList')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')

        if m.get('tableList') is not None:
            self.table_list = m.get('tableList')

        if m.get('topN') is not None:
            self.top_n = m.get('topN')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')

        return self

