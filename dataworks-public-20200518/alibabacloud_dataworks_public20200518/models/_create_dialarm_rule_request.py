# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class CreateDIAlarmRuleRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        notification_settings: main_models.CreateDIAlarmRuleRequestNotificationSettings = None,
        trigger_conditions: List[main_models.CreateDIAlarmRuleRequestTriggerConditions] = None,
    ):
        # The ID of the task with which the alert rule is associated.
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # The description of the task.
        self.description = description
        # Specifies whether to enable the alert rule. By default, the alert rule is disabled.
        self.enabled = enabled
        # The metric type in the alert rule. Valid values:
        # 
        # *   Heartbeat
        # *   FailoverCount
        # *   Delay
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The alert notification settings.
        # 
        # This parameter is required.
        self.notification_settings = notification_settings
        # The conditions that are used to trigger the alert rule.
        # 
        # This parameter is required.
        self.trigger_conditions = trigger_conditions

    def validate(self):
        if self.notification_settings:
            self.notification_settings.validate()
        if self.trigger_conditions:
            for v1 in self.trigger_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.notification_settings is not None:
            result['NotificationSettings'] = self.notification_settings.to_map()

        result['TriggerConditions'] = []
        if self.trigger_conditions is not None:
            for k1 in self.trigger_conditions:
                result['TriggerConditions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('NotificationSettings') is not None:
            temp_model = main_models.CreateDIAlarmRuleRequestNotificationSettings()
            self.notification_settings = temp_model.from_map(m.get('NotificationSettings'))

        self.trigger_conditions = []
        if m.get('TriggerConditions') is not None:
            for k1 in m.get('TriggerConditions'):
                temp_model = main_models.CreateDIAlarmRuleRequestTriggerConditions()
                self.trigger_conditions.append(temp_model.from_map(k1))

        return self

class CreateDIAlarmRuleRequestTriggerConditions(DaraModel):
    def __init__(
        self,
        duration: int = None,
        severity: str = None,
        threshold: int = None,
    ):
        # The time interval for alert calculation. Unit: minutes.
        self.duration = duration
        # The severity level. Valid values:
        # 
        # *   Warning
        # *   Critical
        self.severity = severity
        # The alert threshold.
        # 
        # *   If the alert rule is for task status, you do not need to specify a threshold.
        # *   If the alert rule is for failovers, specify the number of failovers.
        # *   If the alert rule is for latency, the threshold is the latency duration, in seconds.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class CreateDIAlarmRuleRequestNotificationSettings(DaraModel):
    def __init__(
        self,
        inhibition_interval: int = None,
        notification_channels: List[main_models.CreateDIAlarmRuleRequestNotificationSettingsNotificationChannels] = None,
        notification_receivers: List[main_models.CreateDIAlarmRuleRequestNotificationSettingsNotificationReceivers] = None,
    ):
        # The duration of the alert suppression interval. Default value: 5. Unit: minutes.
        self.inhibition_interval = inhibition_interval
        # The alert notification methods.
        # 
        # This parameter is required.
        self.notification_channels = notification_channels
        # The settings of alert notification recipients.
        # 
        # This parameter is required.
        self.notification_receivers = notification_receivers

    def validate(self):
        if self.notification_channels:
            for v1 in self.notification_channels:
                 if v1:
                    v1.validate()
        if self.notification_receivers:
            for v1 in self.notification_receivers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inhibition_interval is not None:
            result['InhibitionInterval'] = self.inhibition_interval

        result['NotificationChannels'] = []
        if self.notification_channels is not None:
            for k1 in self.notification_channels:
                result['NotificationChannels'].append(k1.to_map() if k1 else None)

        result['NotificationReceivers'] = []
        if self.notification_receivers is not None:
            for k1 in self.notification_receivers:
                result['NotificationReceivers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InhibitionInterval') is not None:
            self.inhibition_interval = m.get('InhibitionInterval')

        self.notification_channels = []
        if m.get('NotificationChannels') is not None:
            for k1 in m.get('NotificationChannels'):
                temp_model = main_models.CreateDIAlarmRuleRequestNotificationSettingsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.CreateDIAlarmRuleRequestNotificationSettingsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class CreateDIAlarmRuleRequestNotificationSettingsNotificationReceivers(DaraModel):
    def __init__(
        self,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The recipient type. Valid values: AliyunUid and DingToken.
        # 
        # *   If the alert notification method is Mail, Phone, or Sms, set this parameter to **AliyunUid**, which specifies the Alibaba Cloud account ID.
        # *   If the alert notification method is Ding, set this parameter to **DingToken**, which indicates the DingTalk chatbot token.
        self.receiver_type = receiver_type
        # The recipients.
        self.receiver_values = receiver_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type

        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')

        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')

        return self

class CreateDIAlarmRuleRequestNotificationSettingsNotificationChannels(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        severity: str = None,
    ):
        # The alert notification methods.
        self.channels = channels
        # The severity level. Valid values:
        # 
        # *   Warning
        # *   Critical
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels

        if self.severity is not None:
            result['Severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        return self

