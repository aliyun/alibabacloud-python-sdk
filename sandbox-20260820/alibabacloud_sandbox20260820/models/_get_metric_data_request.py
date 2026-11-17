# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetMetricDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        group_by: List[str] = None,
        metric_names: List[str] = None,
        period: int = None,
        sandbox_id: str = None,
        sandbox_plan: str = None,
        start_time: str = None,
        team_id: str = None,
        template_id: str = None,
        time: str = None,
    ):
        # The end time of the time series query. This time is excluded from the query range. Specify the UTC time accurate to seconds. The end time must be later than the start time. You can query metrics for a maximum of 7 days at a time. The time range must include at least one time point aligned with the period, and these time points cannot be later than the current time.
        self.end_time = end_time
        # Groups metrics by a specific key. For example, you can group metrics by teamID to view the metrics of each team separately. You can combine up to four different grouping keys. The available keys vary by metric. If you do not specify this parameter, the overall results within the query scope are returned.
        self.group_by = group_by
        # The names of the metrics to query. You can query 1 to 16 different metrics at a time. For available metrics and query scopes, see the metric catalog.
        # 
        # This parameter is required.
        self.metric_names = metric_names
        # The time interval for time series queries, in seconds. Valid values: 60, 300, 900, 1800, 3600, and 86400. A value of 60 corresponds to full minutes, and 86400 corresponds to midnight UTC every day. The calculation duration of some statistical metrics varies with the interval.
        # 
        # This parameter is required.
        self.period = period
        # The ID of the sandbox to query. You must also specify the teamID and templateID to which the sandbox belongs, and select a metric that supports sandbox-level queries.
        self.sandbox_id = sandbox_id
        # Queries the number of sandboxes by sandbox plan. This parameter applies only to sandboxCount. Valid values: eco, std, pro, and ent.
        self.sandbox_plan = sandbox_plan
        # The start time of the time series query. This time is included in the query range. Specify the UTC time accurate to seconds and also specify endTime.
        self.start_time = start_time
        # The ID of the team to query. If you leave this parameter empty, the metrics of the current account are queried.
        self.team_id = team_id
        # The ID of the template to query. You must also specify the teamID to which the template belongs.
        self.template_id = template_id
        # The specific point in time to query. If you query metrics at a specific point in time, specify only this parameter. Specify the current or past UTC time accurate to seconds. If you omit all time parameters, the metrics at the current time are queried.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.metric_names is not None:
            result['metricNames'] = self.metric_names

        if self.period is not None:
            result['period'] = self.period

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.sandbox_plan is not None:
            result['sandboxPlan'] = self.sandbox_plan

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('metricNames') is not None:
            self.metric_names = m.get('metricNames')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('sandboxPlan') is not None:
            self.sandbox_plan = m.get('sandboxPlan')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

