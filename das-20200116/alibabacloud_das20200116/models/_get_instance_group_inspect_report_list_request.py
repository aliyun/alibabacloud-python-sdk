# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceGroupInspectReportListRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        end_time: int = None,
        group_id: str = None,
        report_type: str = None,
        start_time: int = None,
    ):
        # Optional. The default agent is used by default. Alternatively, you can specify an agent that was generated after DAS Agent was activated or manually created.
        self.agent_id = agent_id
        # The end time of the query, which is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The reserved parameter.
        self.group_id = group_id
        # The type of the inspection report.
        self.report_type = report_type
        # The start time of the query, which is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

