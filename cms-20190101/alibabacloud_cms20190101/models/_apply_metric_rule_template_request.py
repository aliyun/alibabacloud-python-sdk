# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyMetricRuleTemplateRequest(DaraModel):
    def __init__(
        self,
        append_mode: str = None,
        apply_mode: str = None,
        enable_end_time: int = None,
        enable_start_time: int = None,
        group_id: int = None,
        notify_level: int = None,
        silence_time: int = None,
        template_ids: str = None,
        webhook: str = None,
    ):
        # The template application policy. Valid values:
        # 
        # *   all (default): deletes all the rules that are created by using the alert template from the selected application group, and then creates alert rules based on the template.
        # *   append: deletes the rules that are created by using the alert template from the selected application group, and then creates alert rules based on the existing template.
        self.append_mode = append_mode
        # The mode in which the alert template is applied. Valid values:
        # 
        # *   GROUP_INSTANCE_FIRST: The metrics in the application group take precedence. If a metric specified in the alert template does not exist in the application group, the system does not generate an alert rule for the metric based on the alert template.
        # *   ALARM_TEMPLATE_FIRST: The metrics specified in the alert template take precedence. If a metric specified in the alert template does not exist in the application group, the system still generates an alert rule for the metric based on the alert template.
        self.apply_mode = apply_mode
        # The end of the time period during which the alert rule is effective. Valid values: 00 to 23. A value of 00 indicates 00:59 and a value of 23 indicates 23:59.
        self.enable_end_time = enable_end_time
        # The beginning of the time period during which the alert rule is effective. Valid values: 00 to 23. A value of 00 indicates 00:00 and a value of 23 indicates 23:00.
        self.enable_start_time = enable_start_time
        # The ID of the application group to which the alert template is applied.
        # 
        # For more information about how to query the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The alert notification method. Valid values:
        # 
        # Set the value to 4. A value of 4 indicates that alert notifications are sent by using TradeManager and DingTalk chatbots.
        self.notify_level = notify_level
        # The mute period during which notifications are not repeatedly sent for an alert. Unit: seconds. Default value: 86400.
        # 
        # >  Only one alert notification is sent during each mute period even if the metric value exceeds the alert threshold several times.
        self.silence_time = silence_time
        # The ID of the alert template.
        # 
        # For more information about how to query the IDs of alert templates, see [DescribeMetricRuleTemplateList](https://help.aliyun.com/document_detail/114982.html).
        # 
        # This parameter is required.
        self.template_ids = template_ids
        # The callback URL to which a POST request is sent when an alert is triggered based on the alert rule.
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.append_mode is not None:
            result['AppendMode'] = self.append_mode

        if self.apply_mode is not None:
            result['ApplyMode'] = self.apply_mode

        if self.enable_end_time is not None:
            result['EnableEndTime'] = self.enable_end_time

        if self.enable_start_time is not None:
            result['EnableStartTime'] = self.enable_start_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.notify_level is not None:
            result['NotifyLevel'] = self.notify_level

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppendMode') is not None:
            self.append_mode = m.get('AppendMode')

        if m.get('ApplyMode') is not None:
            self.apply_mode = m.get('ApplyMode')

        if m.get('EnableEndTime') is not None:
            self.enable_end_time = m.get('EnableEndTime')

        if m.get('EnableStartTime') is not None:
            self.enable_start_time = m.get('EnableStartTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NotifyLevel') is not None:
            self.notify_level = m.get('NotifyLevel')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

