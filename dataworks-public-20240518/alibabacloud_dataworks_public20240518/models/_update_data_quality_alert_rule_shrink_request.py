# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataQualityAlertRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        condition: str = None,
        id: int = None,
        notification_shrink: str = None,
        project_id: int = None,
        target_shrink: str = None,
    ):
        # The alert condition of the data quality monitoring rule.
        self.condition = condition
        # The ID of the alert rule.
        self.id = id
        # Alert notification configurations.
        self.notification_shrink = notification_shrink
        # The project ID.
        self.project_id = project_id
        # The monitored target of the data quality monitoring rule.
        self.target_shrink = target_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.id is not None:
            result['Id'] = self.id

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.target_shrink is not None:
            result['Target'] = self.target_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Target') is not None:
            self.target_shrink = m.get('Target')

        return self

