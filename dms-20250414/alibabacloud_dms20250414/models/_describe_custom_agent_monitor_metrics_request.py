# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomAgentMonitorMetricsRequest(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        end_time: int = None,
        granularity: str = None,
        query_type: str = None,
        start_time: int = None,
        workspace_id: str = None,
    ):
        # The custom agent ID.
        # - Required only when QueryType is set to CustomAgent.
        self.custom_agent_id = custom_agent_id
        # The end time of the statistical period (epoch millis).
        # - Note: The maximum time range is 3 months.
        self.end_time = end_time
        # The aggregation granularity. Valid values:
        # - DAY: daily. The maximum supported time range is 3 months.
        # - HOUR: hourly. The maximum supported time range is 72 hours.
        self.granularity = granularity
        # The statistical scope. Default value: All. Valid values:
        # - Default: default DataAgent sessions.
        # - CustomAgent: specified custom agent sessions.
        # - All: all sessions in the workspace.
        self.query_type = query_type
        # The start time of the statistical period (epoch millis).
        # - Note: The maximum time range is 3 months.
        self.start_time = start_time
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

