# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportNodesStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        end_time: str = None,
        issue_category: str = None,
        nodes_shrink: str = None,
        reason: str = None,
        start_time: str = None,
    ):
        self.description = description
        self.end_time = end_time
        self.issue_category = issue_category
        self.nodes_shrink = nodes_shrink
        self.reason = reason
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.issue_category is not None:
            result['IssueCategory'] = self.issue_category

        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IssueCategory') is not None:
            self.issue_category = m.get('IssueCategory')

        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

