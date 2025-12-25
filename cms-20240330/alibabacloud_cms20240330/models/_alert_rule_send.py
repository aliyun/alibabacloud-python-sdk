# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleSend(DaraModel):
    def __init__(
        self,
        action: main_models.AlertRuleAction = None,
        notification: main_models.AlertRuleNotification = None,
        notify_strategies: List[str] = None,
        send_to_arms: bool = None,
    ):
        self.action = action
        self.notification = notification
        self.notify_strategies = notify_strategies
        self.send_to_arms = send_to_arms

    def validate(self):
        if self.action:
            self.action.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action.to_map()

        if self.notification is not None:
            result['notification'] = self.notification.to_map()

        if self.notify_strategies is not None:
            result['notifyStrategies'] = self.notify_strategies

        if self.send_to_arms is not None:
            result['sendToArms'] = self.send_to_arms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            temp_model = main_models.AlertRuleAction()
            self.action = temp_model.from_map(m.get('action'))

        if m.get('notification') is not None:
            temp_model = main_models.AlertRuleNotification()
            self.notification = temp_model.from_map(m.get('notification'))

        if m.get('notifyStrategies') is not None:
            self.notify_strategies = m.get('notifyStrategies')

        if m.get('sendToArms') is not None:
            self.send_to_arms = m.get('sendToArms')

        return self

