# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartNisTrafficRankingShrinkRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter_shrink: str = None,
        group_by_shrink: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        region_no: str = None,
        sort: str = None,
        storage_interval: int = None,
        top_n: int = None,
        traffic_analyzer_id: str = None,
        traffic_scenario: str = None,
        tuple_dimension: str = None,
    ):
        # This parameter is required.
        self.begin_time = begin_time
        # This parameter is required.
        self.direction = direction
        # This parameter is required.
        self.end_time = end_time
        self.filter_shrink = filter_shrink
        self.group_by_shrink = group_by_shrink
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.order_by = order_by
        # This parameter is required.
        self.region_no = region_no
        self.sort = sort
        self.storage_interval = storage_interval
        self.top_n = top_n
        # This parameter is required.
        self.traffic_analyzer_id = traffic_analyzer_id
        # This parameter is required.
        self.traffic_scenario = traffic_scenario
        self.tuple_dimension = tuple_dimension

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.group_by_shrink is not None:
            result['GroupBy'] = self.group_by_shrink

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.storage_interval is not None:
            result['StorageInterval'] = self.storage_interval

        if self.top_n is not None:
            result['TopN'] = self.top_n

        if self.traffic_analyzer_id is not None:
            result['TrafficAnalyzerId'] = self.traffic_analyzer_id

        if self.traffic_scenario is not None:
            result['TrafficScenario'] = self.traffic_scenario

        if self.tuple_dimension is not None:
            result['TupleDimension'] = self.tuple_dimension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('GroupBy') is not None:
            self.group_by_shrink = m.get('GroupBy')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StorageInterval') is not None:
            self.storage_interval = m.get('StorageInterval')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        if m.get('TrafficAnalyzerId') is not None:
            self.traffic_analyzer_id = m.get('TrafficAnalyzerId')

        if m.get('TrafficScenario') is not None:
            self.traffic_scenario = m.get('TrafficScenario')

        if m.get('TupleDimension') is not None:
            self.tuple_dimension = m.get('TupleDimension')

        return self

