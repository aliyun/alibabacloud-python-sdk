# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceGroupInspectReportDetailRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        report_id: str = None,
        report_type: str = None,
    ):
        # The ID of the agent that the user purchased.
        self.agent_id = agent_id
        # The ID of the operations report.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The type of the report.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        return self

