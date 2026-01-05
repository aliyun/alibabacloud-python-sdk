# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateDIAlarmRuleRequest(DaraModel):
    def __init__(
        self,
        dialarm_rule_id: int = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        id: int = None,
        metric_type: str = None,
        name: str = None,
        notification_settings: main_models.UpdateDIAlarmRuleRequestNotificationSettings = None,
        trigger_conditions: List[main_models.UpdateDIAlarmRuleRequestTriggerConditions] = None,
    ):
        # This parameter is deprecated. Use the Id parameter instead.
        self.dialarm_rule_id = dialarm_rule_id
        # The ID of the synchronization task.
        self.dijob_id = dijob_id
        # The description of the alert rule.
        self.description = description
        # Specifies whether to enable the alert rule. By default, the alert rule is disabled.
        self.enabled = enabled
        # The alert rule Id
        self.id = id
        # The metric type in the alert rule. Valid values:
        # 
        # *   Heartbeat
        # *   FailoverCount
        # *   Delay
        # *   DdlReport
        # *   ResourceUtilization
        self.metric_type = metric_type
        # The name of the alert rule.
        self.name = name
        # The alert notification settings.
        self.notification_settings = notification_settings
        # The conditions that can trigger the alert rule.
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
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id

        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

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
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')

        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotificationSettings') is not None:
            temp_model = main_models.UpdateDIAlarmRuleRequestNotificationSettings()
            self.notification_settings = temp_model.from_map(m.get('NotificationSettings'))

        self.trigger_conditions = []
        if m.get('TriggerConditions') is not None:
            for k1 in m.get('TriggerConditions'):
                temp_model = main_models.UpdateDIAlarmRuleRequestTriggerConditions()
                self.trigger_conditions.append(temp_model.from_map(k1))

        return self

class UpdateDIAlarmRuleRequestTriggerConditions(DaraModel):
    def __init__(
        self,
        ddl_report_tags: List[str] = None,
        ddl_types: List[str] = None,
        duration: int = None,
        severity: str = None,
        threshold: int = None,
    ):
        # This parameter is deprecated and replaced by the DdlTypes parameter.
        self.ddl_report_tags = ddl_report_tags
        # The types of DDL operations for which the alert rule takes effect.
        self.ddl_types = ddl_types
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
        # *   If the alert rule is for failovers, you must specify the number of failovers.
        # *   If the alert rule is for latency, you must specify the latency duration, in seconds.
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

class UpdateDIAlarmRuleRequestNotificationSettings(DaraModel):
    def __init__(
        self,
        inhibition_interval: int = None,
        mute_interval: int = None,
        notification_channels: List[main_models.UpdateDIAlarmRuleRequestNotificationSettingsNotificationChannels] = None,
        notification_receivers: List[main_models.UpdateDIAlarmRuleRequestNotificationSettingsNotificationReceivers] = None,
    ):
        # This parameter is deprecated and replaced by the MuteInterval parameter.
        self.inhibition_interval = inhibition_interval
        # The duration of the alert suppression interval. Default value: 5. Unit: minutes.
        self.mute_interval = mute_interval
        # The alert notification methods.
        self.notification_channels = notification_channels
        # The settings of alert notification recipients.
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
                temp_model = main_models.UpdateDIAlarmRuleRequestNotificationSettingsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k1))

        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k1 in m.get('NotificationReceivers'):
                temp_model = main_models.UpdateDIAlarmRuleRequestNotificationSettingsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k1))

        return self

class UpdateDIAlarmRuleRequestNotificationSettingsNotificationReceivers(DaraModel):
    def __init__(
        self,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        # The recipient type. Valid values: AliyunUid, DingToken, FeishuToken, and WebHookUrl.
        self.receiver_type = receiver_type
        # The recipient.
        # 
        # *   If the ReceiverType parameter is set to AliyunUid, set this parameter to the Alibaba Cloud account ID of a user.
        # *   If the ReceiverType parameter is set to DingToken, set this parameter to the token of a DingTalk chatbot.
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

class UpdateDIAlarmRuleRequestNotificationSettingsNotificationChannels(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        severity: str = None,
    ):
        # The alert notification method. Valid values:
        # 
        # *   Mail
        # *   Phone
        # *   Sms
        # *   Ding
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

