# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutCustomEventRuleRequest(DaraModel):
    def __init__(
        self,
        contact_groups: str = None,
        effective_interval: str = None,
        email_subject: str = None,
        event_name: str = None,
        group_id: str = None,
        level: str = None,
        period: str = None,
        rule_id: str = None,
        rule_name: str = None,
        threshold: str = None,
        webhook: str = None,
    ):
        # The alert contact group that receives alert notifications. Separate multiple contact groups with commas (,).
        # 
        # This parameter is required.
        self.contact_groups = contact_groups
        # The time period during which the alert rule is effective. Valid values: 00:00 to 23:59.
        self.effective_interval = effective_interval
        # The subject of the alert notification email.
        self.email_subject = email_subject
        # The name of the custom event. For more information about how to obtain the event name, see [DescribeCustomEventAttribute](https://help.aliyun.com/document_detail/115262.html).
        # 
        # This parameter is required.
        self.event_name = event_name
        # The ID of the application group. For more information about how to obtain the group ID, see [DescribeCustomEventAttribute](https://help.aliyun.com/document_detail/115262.html).
        # 
        # >  The value 0 indicates that the reported custom event does not belong to any application Group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The level of the alert. Valid values:
        # 
        # *   CRITICAL: critical issue
        # *   WARN: warning
        # *   INFO: information
        # 
        # This parameter is required.
        self.level = level
        # The cycle that is used to aggregate monitoring data of the custom event. Unit: seconds. Set the value to an integral multiple of 60. Default value: 300.
        self.period = period
        # The ID of the alert rule.
        # 
        # >  You can specify an existing ID to modify the corresponding alert rule or specify a new ID to create an alert rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the alert rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The alert threshold.
        # 
        # This parameter is required.
        self.threshold = threshold
        # The callback URL to which a POST request is sent when an alert is triggered based on the alert rule.
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.email_subject is not None:
            result['EmailSubject'] = self.email_subject

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.level is not None:
            result['Level'] = self.level

        if self.period is not None:
            result['Period'] = self.period

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

