# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryCubePerformanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryCubePerformanceResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Array of report objects
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryCubePerformanceResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCubePerformanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        cache_cost_time_avg: float = None,
        cache_query_count: int = None,
        cost_time_avg: float = None,
        cube_id: str = None,
        cube_name: str = None,
        query_count: int = None,
        query_count_avg: float = None,
        query_over_five_percent_num: float = None,
        query_over_five_sec_percent: str = None,
        query_over_ten_sec_percent: str = None,
        query_over_ten_sec_percent_num: float = None,
        query_timeout_count: int = None,
        query_timeout_count_percent: float = None,
        quick_index_cost_time_avg: float = None,
        quick_index_query_count: int = None,
        repeat_query_percent: str = None,
        repeat_query_percent_num: float = None,
        repeat_sql_query_count: int = None,
        repeat_sql_query_percent: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The average duration of cache hits.
        self.cache_cost_time_avg = cache_cost_time_avg
        # The number of cache hits.
        self.cache_query_count = cache_query_count
        # The average query duration associated with the SQL pattern.
        self.cost_time_avg = cost_time_avg
        # The dataset ID.
        self.cube_id = cube_id
        # The name of the dataset.
        self.cube_name = cube_name
        # The number of queries.
        self.query_count = query_count
        # The average number of queries.
        self.query_count_avg = query_count_avg
        # The percentage of the number of queries that exceed the 5S.
        self.query_over_five_percent_num = query_over_five_percent_num
        # Query the proportion of more than 5S.
        self.query_over_five_sec_percent = query_over_five_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent = query_over_ten_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent_num = query_over_ten_sec_percent_num
        # The number of times that the chart query times out.
        self.query_timeout_count = query_timeout_count
        # The percentage of timeout times for chart queries.
        self.query_timeout_count_percent = query_timeout_count_percent
        # The average time consumed by the Quick engine query.
        self.quick_index_cost_time_avg = quick_index_cost_time_avg
        # The number of times that the Quick engine is hit.
        self.quick_index_query_count = quick_index_query_count
        # The proportion of duplicate queries.
        self.repeat_query_percent = repeat_query_percent
        # The number of duplicate queries.
        self.repeat_query_percent_num = repeat_query_percent_num
        # The number of times the query is repeated.
        self.repeat_sql_query_count = repeat_sql_query_count
        # The proportion of duplicate queries.
        self.repeat_sql_query_percent = repeat_sql_query_percent
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the group.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_cost_time_avg is not None:
            result['CacheCostTimeAvg'] = self.cache_cost_time_avg

        if self.cache_query_count is not None:
            result['CacheQueryCount'] = self.cache_query_count

        if self.cost_time_avg is not None:
            result['CostTimeAvg'] = self.cost_time_avg

        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.cube_name is not None:
            result['CubeName'] = self.cube_name

        if self.query_count is not None:
            result['QueryCount'] = self.query_count

        if self.query_count_avg is not None:
            result['QueryCountAvg'] = self.query_count_avg

        if self.query_over_five_percent_num is not None:
            result['QueryOverFivePercentNum'] = self.query_over_five_percent_num

        if self.query_over_five_sec_percent is not None:
            result['QueryOverFiveSecPercent'] = self.query_over_five_sec_percent

        if self.query_over_ten_sec_percent is not None:
            result['QueryOverTenSecPercent'] = self.query_over_ten_sec_percent

        if self.query_over_ten_sec_percent_num is not None:
            result['QueryOverTenSecPercentNum'] = self.query_over_ten_sec_percent_num

        if self.query_timeout_count is not None:
            result['QueryTimeoutCount'] = self.query_timeout_count

        if self.query_timeout_count_percent is not None:
            result['QueryTimeoutCountPercent'] = self.query_timeout_count_percent

        if self.quick_index_cost_time_avg is not None:
            result['QuickIndexCostTimeAvg'] = self.quick_index_cost_time_avg

        if self.quick_index_query_count is not None:
            result['QuickIndexQueryCount'] = self.quick_index_query_count

        if self.repeat_query_percent is not None:
            result['RepeatQueryPercent'] = self.repeat_query_percent

        if self.repeat_query_percent_num is not None:
            result['RepeatQueryPercentNum'] = self.repeat_query_percent_num

        if self.repeat_sql_query_count is not None:
            result['RepeatSqlQueryCount'] = self.repeat_sql_query_count

        if self.repeat_sql_query_percent is not None:
            result['RepeatSqlQueryPercent'] = self.repeat_sql_query_percent

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostTimeAvg') is not None:
            self.cache_cost_time_avg = m.get('CacheCostTimeAvg')

        if m.get('CacheQueryCount') is not None:
            self.cache_query_count = m.get('CacheQueryCount')

        if m.get('CostTimeAvg') is not None:
            self.cost_time_avg = m.get('CostTimeAvg')

        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')

        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')

        if m.get('QueryCountAvg') is not None:
            self.query_count_avg = m.get('QueryCountAvg')

        if m.get('QueryOverFivePercentNum') is not None:
            self.query_over_five_percent_num = m.get('QueryOverFivePercentNum')

        if m.get('QueryOverFiveSecPercent') is not None:
            self.query_over_five_sec_percent = m.get('QueryOverFiveSecPercent')

        if m.get('QueryOverTenSecPercent') is not None:
            self.query_over_ten_sec_percent = m.get('QueryOverTenSecPercent')

        if m.get('QueryOverTenSecPercentNum') is not None:
            self.query_over_ten_sec_percent_num = m.get('QueryOverTenSecPercentNum')

        if m.get('QueryTimeoutCount') is not None:
            self.query_timeout_count = m.get('QueryTimeoutCount')

        if m.get('QueryTimeoutCountPercent') is not None:
            self.query_timeout_count_percent = m.get('QueryTimeoutCountPercent')

        if m.get('QuickIndexCostTimeAvg') is not None:
            self.quick_index_cost_time_avg = m.get('QuickIndexCostTimeAvg')

        if m.get('QuickIndexQueryCount') is not None:
            self.quick_index_query_count = m.get('QuickIndexQueryCount')

        if m.get('RepeatQueryPercent') is not None:
            self.repeat_query_percent = m.get('RepeatQueryPercent')

        if m.get('RepeatQueryPercentNum') is not None:
            self.repeat_query_percent_num = m.get('RepeatQueryPercentNum')

        if m.get('RepeatSqlQueryCount') is not None:
            self.repeat_sql_query_count = m.get('RepeatSqlQueryCount')

        if m.get('RepeatSqlQueryPercent') is not None:
            self.repeat_sql_query_percent = m.get('RepeatSqlQueryPercent')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

