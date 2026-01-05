# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlertRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        notification_shrink: str = None,
        owner: str = None,
        trigger_condition_shrink: str = None,
    ):
        # Specifies whether to enable the rule.
        self.enabled = enabled
        # The rule ID.
        self.id = id
        # The name of the rule.
        self.name = name
        # The configuration for the alert notification.
        self.notification_shrink = notification_shrink
        # The ID of the Alibaba Cloud account used by the owner of the rule.
        self.owner = owner
        # The alert triggering condition.
        self.trigger_condition_shrink = trigger_condition_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.trigger_condition_shrink is not None:
            result['TriggerCondition'] = self.trigger_condition_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TriggerCondition') is not None:
            self.trigger_condition_shrink = m.get('TriggerCondition')

        return self

