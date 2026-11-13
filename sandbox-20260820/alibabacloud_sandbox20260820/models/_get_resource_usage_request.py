# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetResourceUsageRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        granularity: str = None,
        group_by: List[str] = None,
        sandbox_plan: str = None,
        start_time: str = None,
        team_id: str = None,
        template_id: str = None,
        usage_names: List[str] = None,
    ):
        # The end time of the query. This time is exclusive. Specify the time on the hour in UTC. The latest allowed end time is the start of the current hour. You can query data for a maximum of 7 days at a time. The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The granularity at which usage data is aggregated. Set this parameter to All to view the cumulative usage over the entire query interval, to Hour to view the hourly usage, or to Day to aggregate the usage every 24 hours from the start time. The last interval can be less than 24 hours.
        # 
        # This parameter is required.
        self.granularity = granularity
        # The grouping keys. You can group the results by any combination of teamID, templateID, and sandboxPlan. Each key can be specified only once. If you do not specify this parameter, the results are aggregated over the entire query scope.
        self.group_by = group_by
        # The sandbox edition to query. Valid values: eco, std, pro, and ent.
        self.sandbox_plan = sandbox_plan
        # The start time of the query. This time is inclusive. Specify the time on the hour in UTC, such as 00:00 UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the team to query. If you do not specify this parameter, the usage of the current account is queried.
        self.team_id = team_id
        # The ID of the template to query. You must also specify the teamID to which the template belongs.
        self.template_id = template_id
        # The usage items to query. You can query 1 to 6 different usage items at a time. CPU usage items include cpuActive and cpuIdle. Memory usage items include memoryActive and memoryIdle. Disk usage items include disk and diskDeepSleep. The disk item includes the usage of disks in deep sleep mode.
        # 
        # This parameter is required.
        self.usage_names = usage_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.sandbox_plan is not None:
            result['sandboxPlan'] = self.sandbox_plan

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.usage_names is not None:
            result['usageNames'] = self.usage_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('sandboxPlan') is not None:
            self.sandbox_plan = m.get('sandboxPlan')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('usageNames') is not None:
            self.usage_names = m.get('usageNames')

        return self

