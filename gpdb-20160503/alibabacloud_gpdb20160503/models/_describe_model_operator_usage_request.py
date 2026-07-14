# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeModelOperatorUsageRequest(DaraModel):
    def __init__(
        self,
        api_key_ids: List[int] = None,
        end_time: str = None,
        group_by: str = None,
        keys: List[str] = None,
        model_names: List[str] = None,
        period: int = None,
        start_time: str = None,
    ):
        # The list of API key IDs. Separate multiple IDs with commas (,). If this parameter is not specified, all API key IDs under the instance ID are used by default.
        # 
        # > The list can contain up to 50 items.
        self.api_key_ids = api_key_ids
        # The end time of the query. Specify the time in the <i>YYYY-MM-DDThh:mmZ</i> format (UTC).
        # 
        # > The end time must be later than the start time, and the interval between the start time and end time cannot exceed 7 days.
        self.end_time = end_time
        # The dimension by which to split the series. Separate multiple dimensions with commas (,). The order is not significant. Valid values:
        # 
        # - model (default): splits by model.
        # - api_key: splits by API key.
        # - model,api_key: splits by model and API key.
        self.group_by = group_by
        # The list of metrics. Separate multiple metrics with commas (,). Valid values:
        # 
        # - request_count: the number of requests.
        # - success_count: the number of successful requests.
        # - error_count: the number of failed requests.
        # - success_rate: the request success rate.
        # - input_token: the number of input tokens.
        # - output_token: the number of output tokens.
        # - total_token: the total number of tokens.
        self.keys = keys
        # The list of model names. Separate multiple names with commas (,).
        self.model_names = model_names
        # The time bucket size in seconds. Valid values: 1, 5, 15, 60, 300, and 3600.
        # 
        # >
        # > - 1. If Period is not specified, the default value is determined by the following rules:
        # > - - Window range ≤ 1 hour: Period = 1.
        # > - - Window range ≤ 1 day: Period = 60.
        # > - - Window range ≤ 7 days: Period = 60.
        # > - 2. When Period is set to 1, the window must be ≤ 1 day.
        self.period = period
        # The start time of the query. Specify the time in the <i>YYYY-MM-DDThh:mmZ</i> format (UTC).
        # 
        # > Only metrics within the last 30 days can be queried.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_ids is not None:
            result['ApiKeyIds'] = self.api_key_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.keys is not None:
            result['Keys'] = self.keys

        if self.model_names is not None:
            result['ModelNames'] = self.model_names

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyIds') is not None:
            self.api_key_ids = m.get('ApiKeyIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        if m.get('ModelNames') is not None:
            self.model_names = m.get('ModelNames')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

