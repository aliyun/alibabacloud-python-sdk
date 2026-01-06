# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetEventSubscriptionRequest(DaraModel):
    def __init__(
        self,
        active: str = None,
        channel_type: str = None,
        contact_group_name: str = None,
        contact_name: str = None,
        dispatch_rule: str = None,
        event_context: str = None,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
        min_interval: str = None,
        severity: str = None,
    ):
        # Specifies whether to enable the event subscription feature. Valid values:
        # 
        # *   **0**: disables the event subscription feature.
        # *   **1**: enables the event subscription feature.
        self.active = active
        # The notification method. Valid values:
        # 
        # *   **hdm_alarm_sms**: text message.
        # *   **dingtalk**: DingTalk chatbot.
        # *   **hdm_alarm_sms_and_email**: text message and email.
        # *   **hdm_alarm_sms,dingtalk**: text message and DingTalk chatbot.
        self.channel_type = channel_type
        # The name of the contact group that receives alert notifications. Separate multiple names with commas (,).
        self.contact_group_name = contact_group_name
        # The name of the contact who receives alert notifications. Separate multiple names with commas (,).
        self.contact_name = contact_name
        # The notification rules based on the event type. If you leave this parameter empty, the values of **MinInterval** and **ChannelType** prevail.
        # 
        # Specify this parameter in the following format: `{"silenced": {"Event type 1":Specifies whether to enable adaptive silence, "Event type 2":Specify whether to enable adaptive silence},"min_interval": {"Event type 1":Minimum interval between event notifications, "Event type 2":Minimum interval between event notifications},"alert_type": {"Event type 1":"Notification method", "Event type 2":"Notification method"}}`.
        # 
        # *   **silenced**: specifies whether to enable adaptive silence. After you enable adaptive silence, the interval between consecutive alert notifications for an event is the greater one of the minimum interval specified by **min_interval** and one third of the event duration. Valid values:
        # 
        #     *   1: enables adaptive silence.
        #     *   2: disables adaptive silence.
        # 
        # *   **min_interval**: the minimum interval between event notifications. Unit: seconds.
        # 
        # *   **alert_type**: the notification method. Valid values:
        # 
        #     *   **hdm_alarm_sms**: text message.
        #     *   **dingtalk**: DingTalk chatbot.
        #     *   **hdm_alarm_sms_and_email**: text message and email.
        #     *   **hdm_alarm_sms,dingtalk**: text message and DingTalk chatbot.
        self.dispatch_rule = dispatch_rule
        # The supported event scenarios. You can set the value to **AllContext**, which indicates that all scenarios are supported.
        self.event_context = event_context
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of event notifications. You can set the value to **zh-CN**, which indicates that event notifications are sent in Chinese.
        self.lang = lang
        # The risk level of the events. Valid values:
        # 
        # *   **Notice**: events that trigger notifications, including events at the **Notice**, **Optimization**, **Warn**, and **Critical** levels.
        # *   **Optimization**: events that trigger optimizations, including events at the **Optimization**, **Warn**, and **Critical** levels.
        # *   **Warn**: events that trigger warnings, including events at the **Warn** and **Critical** levels.
        # *   **Critical**: events that trigger critical warnings.
        # 
        # The following content describes the events at each level in detail:
        # 
        # *   Notice: events that are related to database exceptions for which no suggestions are generated.
        # *   Optimization: events for which optimization suggestions are generated based on the status of the database.
        # *   Warn: events that may affect the running of the database.
        # *   Critical: events that affect the running of the database.
        self.level = level
        # The minimum interval between consecutive event notifications. Unit: seconds.
        self.min_interval = min_interval
        # The alert severity based on the event type.
        # 
        # Specify this parameter in the following format: `{"Event type 1":"Alert severity", "Event type 2":"Alert severity"}`.
        # 
        # Valid values of event types:
        # 
        # *   **AutoScale**: auto scaling event.
        # *   **SQLThrottle**: throttling event.
        # *   **TimeSeriesAbnormal**: event for detecting time series anomalies.
        # *   **SQLOptimize**: SQL optimization event.
        # *   **ResourceOptimize**: storage optimization event.
        # 
        # Valid values of alert severities:
        # 
        # *   **info**
        # *   **noticed**
        # *   **warning**
        # *   **critical**
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule

        if self.event_context is not None:
            result['EventContext'] = self.event_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.min_interval is not None:
            result['MinInterval'] = self.min_interval

        if self.severity is not None:
            result['Severity'] = self.severity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')

        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MinInterval') is not None:
            self.min_interval = m.get('MinInterval')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        return self

