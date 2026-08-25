# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateDIAlarmRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        name: str = None,
        notification_settings: main_models.CreateDIAlarmRuleRequestNotificationSettings = None,
        trigger_conditions: List[main_models.CreateDIAlarmRuleRequestTriggerConditions] = None,
    ):
        # The idempotency parameter.
        self.client_token = client_token
        # The task ID associated with the alert rule.
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # The description of the alert rule.
        self.description = description
        # Specifies whether to enable the alert rule. By default, the alert rule is disabled.
        self.enabled = enabled
        # The alert metric type. Valid values:
        # - Heartbeat: task status alert.
        # - FailoverCount: failover count alert.
        # - Delay: task latency alert.
        # - DdlReport: DDL notification.
        # - ResourceUtilization: resource group utilization.
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
        self.notification_settings = notification_settings
        # The list of alert trigger conditions. Multiple conditions are supported.
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

        if self.notification_settings is not None:
            result['NotificationSettings'] = self.notification_settings.to_map()

        result['TriggerConditions'] = []
        if self.trigger_conditions is not None:
            for k1 in self.trigger_conditions:
                result['TriggerConditions'].append(k1.to_map() if k1 else None)

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
        ddl_report_tags: List[str] = None,
        ddl_types: List[str] = None,
        duration: int = None,
        severity: str = None,
        threshold: int = None,
    ):
        # **[Deprecated]** Use the DdlTypes parameter instead.
        self.ddl_report_tags = ddl_report_tags
        # The list of DDL types that take effect. This parameter takes effect only when the metric type is DDL notification.
        self.ddl_types = ddl_types
        # The time window for alert calculation. Unit: minutes.
        self.duration = duration
        # The severity level. Valid values:
        # - Warning
        # - Critical
        self.severity = severity
        # The alert threshold.
        # - Task status alert: no threshold is required.
        # - Failover count alert: the threshold is the number of failovers.
        # - Task latency alert: the threshold is the latency duration. Unit: seconds.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddl_report_tags is not None:
            result['DdlReportTags'] = self.ddl_report_tags

        if self.ddl_types is not None:
            result['DdlTypes'] = self.ddl_types

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdlReportTags') is not None:
            self.ddl_report_tags = m.get('DdlReportTags')

        if m.get('DdlTypes') is not None:
            self.ddl_types = m.get('DdlTypes')

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
        mute_interval: int = None,
        notification_channels: List[main_models.CreateDIAlarmRuleRequestNotificationSettingsNotificationChannels] = None,
        notification_receivers: List[main_models.CreateDIAlarmRuleRequestNotificationSettingsNotificationReceivers] = None,
    ):
        # **[Deprecated]** Use the MuteInterval parameter instead.
        self.inhibition_interval = inhibition_interval
        # The alert mute interval. Unit: minutes. Default value: 5.
        self.mute_interval = mute_interval
        # The alert notification channels.
        self.notification_channels = notification_channels
        # The alert notification receivers.
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

        if self.mute_interval is not None:
            result['MuteInterval'] = self.mute_interval

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

        if m.get('MuteInterval') is not None:
            self.mute_interval = m.get('MuteInterval')

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
        # The receiver type. Valid values: AliyunUid, DingToken, FeishuToken, and WebHookUrl.
        self.receiver_type = receiver_type
        # The receiver values.
        # - If the receiver type is AliyunUid, the value is the Alibaba Cloud account ID.
        # - If the receiver type is DingToken, the value is the DingTalk token.
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
        # The notification channel. Valid values:
        # - Mail: email.
        # - Phone: phone call.
        # - Sms: text message.
        # - Ding: DingTalk.
        self.channels = channels
        # The severity level. Valid values:
        # - Warning
        # - Critical
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

