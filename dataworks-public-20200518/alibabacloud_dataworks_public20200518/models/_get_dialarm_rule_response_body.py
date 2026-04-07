# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDIAlarmRuleResponseBody(DaraModel):
    def __init__(
        self,
        dialarm_rule: main_models.GetDIAlarmRuleResponseBodyDIAlarmRule = None,
        request_id: str = None,
    ):
        # The details of the alert rule.
        self.dialarm_rule = dialarm_rule
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dialarm_rule:
            self.dialarm_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialarm_rule is not None:
            result['DIAlarmRule'] = self.dialarm_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRule') is not None:
            temp_model = main_models.GetDIAlarmRuleResponseBodyDIAlarmRule()
            self.dialarm_rule = temp_model.from_map(m.get('DIAlarmRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDIAlarmRuleResponseBodyDIAlarmRule(DaraModel):
    def __init__(
        self,
        created_time: int = None,
        created_uid: str = None,
        dialarm_rule_id: int = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        notification_settings: main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettings = None,
        trigger_conditions: List[main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleTriggerConditions] = None,
        updated_time: int = None,
        updated_uid: str = None,
    ):
        # The timestamp when the alert rule was created. Unit: seconds.
        self.created_time = created_time
        # The ID of the user who creates the alert rule.
        self.created_uid = created_uid
        # The alert rule ID.
        self.dialarm_rule_id = dialarm_rule_id
        # The ID of the task with which the alert rule is associated.
        self.dijob_id = dijob_id
        # The description of the alert rule.
        self.description = description
        # Indicates whether the alert rule is enabled.
        self.enabled = enabled
        # The metric type in the alert rule. Valid values:
        # 
        # *   Heartbeat
        # *   FailoverCount
        # *   Delay
        self.metric_type = metric_type
        # The alert notification settings.
        self.notification_settings = notification_settings
        # The conditions that are used to trigger the alert rule.
        self.trigger_conditions = trigger_conditions
        # The timestamp when the alert rule was last updated. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the user who last updates the alert rule.
        self.updated_uid = updated_uid

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
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.created_uid is not None:
            result['CreatedUid'] = self.created_uid

        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id

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

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.updated_uid is not None:
            result['UpdatedUid'] = self.updated_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreatedUid') is not None:
            self.created_uid = m.get('CreatedUid')

        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')

        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('NotificationSettings') is not None:
            temp_model = main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettings()
            self.notification_settings = temp_model.from_map(m.get('NotificationSettings'))

        self.trigger_conditions = []
        if m.get('TriggerConditions') is not None:
            for k1 in m.get('TriggerConditions'):
                temp_model = main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleTriggerConditions()
                self.trigger_conditions.append(temp_model.from_map(k1))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('UpdatedUid') is not None:
            self.updated_uid = m.get('UpdatedUid')

        return self

class GetDIAlarmRuleResponseBodyDIAlarmRuleTriggerConditions(DaraModel):
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
        # *   If the alert rule is for task status, no threshold is used.
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

class GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettings(DaraModel):
    def __init__(
        self,
        inhibition_interval: int = None,
        notification_channels: List[main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettingsNotificationChannels] = None,
        notification_receivers: List[main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettingsNotificationReceivers] = None,
    ):
        # The duration of the alert suppression interval. Unit: minutes.
        self.inhibition_interval = inhibition_interval
        # The alert notification methods.
        self.notification_channels = notification_channels
        # The alert notification recipients.
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
                temp_model = main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettingsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettingsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettingsNotificationReceivers(DaraModel):
    def __init__(
        self,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The recipient type. Valid values: AliyunUid and DingToken.
        # 
        # *   If the alert notification method is Mail, Phone, or Sms, the value of this parameter is **AliyunUid**, which indicates the Alibaba Cloud account ID.
        # *   If the alert notification method is Ding, the value of this parameter is **DingToken**, which indicates the DingTalk chatbot token.
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

class GetDIAlarmRuleResponseBodyDIAlarmRuleNotificationSettingsNotificationChannels(DaraModel):
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

