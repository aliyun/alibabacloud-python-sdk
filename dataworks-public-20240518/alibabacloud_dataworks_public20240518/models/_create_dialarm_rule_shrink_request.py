# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDIAlarmRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        name: str = None,
        notification_settings_shrink: str = None,
        trigger_conditions_shrink: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the synchronization task with which the alert rule is associated.
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # The description of the alert rule.
        self.description = description
        # Specifies whether to enable the alert rule. By default, the alert rule is disabled.
        self.enabled = enabled
        # The metric type in the alert rule. Valid values:
        # 
        # *   Heartbeat
        # *   FailoverCount
        # *   Delay
        # *   DdlReport
        # *   ResourceUtilization
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The name of the alert rule.
        # 
        # This parameter is required.
        self.name = name
        # The alert notification settings.
        # 
        # This parameter is required.
        self.notification_settings_shrink = notification_settings_shrink
        # The conditions that can trigger the alert rule.
        # 
        # This parameter is required.
        self.trigger_conditions_shrink = trigger_conditions_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.name is not None:
            result['Name'] = self.name

        if self.notification_settings_shrink is not None:
            result['NotificationSettings'] = self.notification_settings_shrink

        if self.trigger_conditions_shrink is not None:
            result['TriggerConditions'] = self.trigger_conditions_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotificationSettings') is not None:
            self.notification_settings_shrink = m.get('NotificationSettings')

        if m.get('TriggerConditions') is not None:
            self.trigger_conditions_shrink = m.get('TriggerConditions')

        return self

