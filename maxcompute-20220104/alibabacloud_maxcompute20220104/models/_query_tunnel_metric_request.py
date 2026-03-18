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
        # A list of HTTP status codes for requests.
        self.code_list = code_list
        # A list of grouping criteria.
        self.group_list = group_list
        # A list of operation types.
        self.operation_list = operation_list
        # The name of the project.
        self.project = project
        # The nickname of the level-2 Tunnel quota.
        # 
        # The nickname of a shared quota is `default`.
        # 
        # The format of a dedicated quota nickname is `quotaNickname#subQuotaNickname`.
        self.quota_nickname = quota_nickname
        # A list of table names.
        # 
        # The tables belong to a project. Therefore, if `tableList` is not empty, `project` cannot be empty.
        self.table_list = table_list
        # The maximum number of data entries to return.
        # 
        # This parameter takes effect when the grouping criterion includes `table` or `ip`.
        # 
        # The default value is 10. The maximum value is 100.
        self.top_n = top_n
        # The end of the time range for the query.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start of the time range for the query.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The data aggregation policy. The default value is `max`.
        # 
        # Data is collected at a frequency of 1 minute. If you query data over a long time range, the automatic step size for data display may exceed 1 minute. In this case, metrics are aggregated. This parameter specifies the aggregation logic.
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

