# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyMetricRuleTemplateRequest(DaraModel):
    def __init__(
        self,
        append_mode: str = None,
        apply_mode: str = None,
        dry_run: bool = None,
        enable_end_time: int = None,
        enable_start_time: int = None,
        group_id: int = None,
        notify_level: int = None,
        silence_time: int = None,
        template_ids: str = None,
        webhook: str = None,
    ):
        # The application policy of the template. Valid values:
        # 
        # - all: deletes all rules created by using alert templates on the selected group and then creates new alert rules based on the template. This is the default value.
        # 
        # - append: deletes the rules created by using the current alert template on the selected group and then creates new alert rules based on the current template.
        self.append_mode = append_mode
        # The application mode of the template. Valid values:
        # 
        # - GROUP_INSTANCE_FIRST: application group instances take precedence. When the alert template is applied, the instances in the application group take precedence. If an instance specified in the template does not exist in the application group, the rule for the instance in the template is ignored.
        # 
        # - ALARM_TEMPLATE_FIRST: alert template instances take precedence. When the alert template is applied, alert rules are created regardless of whether the instances exist in the application group.
        self.apply_mode = apply_mode
        # Specifies whether to perform a dry run on the request. Valid values:
        # - **true**: performs a dry run and does not bind a security group to the instance. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the request fails the dry run, an error is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false**: performs a normal request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run
        # The end time of the effective period for the alert, in hours. The value is a two-digit string, such as "00", "18", or "23". Valid values: 00 to 23. The value specifies the hour of the end time, and the actual effective period ends at the 59th minute of the hour. For example, "23" indicates that the effective period ends at 23:59. The default time zone is UTC+8.
        self.enable_end_time = enable_end_time
        # The start time of the effective period for the alert, in hours. The value is a two-digit string, such as "00", "09", or "23". Valid values: 00 to 23, which represent 00:00 to 23:00. The default time zone is UTC+8.
        self.enable_start_time = enable_start_time
        # The ID of the application group.
        # 
        # For more information about how to obtain the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The alert notification method. Valid values:
        # 
        # <props="china">- 2: phone call, text message, mailbox, TradeManager, and DingTalk chatbot.
        # 
        # <props="china">- 3: text message, mailbox, TradeManager, and DingTalk chatbot.
        # 
        # <props="china">- 4: TradeManager and DingTalk chatbot.
        # 
        # 
        # <props="intl">4: TradeManager and DingTalk chatbot.
        # 
        # <props="partner">4: TradeManager and DingTalk chatbot.
        self.notify_level = notify_level
        # The mute for. Unit: seconds. Default value: 86400.
        # 
        # > If the monitoring data continuously exceeds the threshold of the alert rule, the system sends only one alert notification within each epoch.
        self.silence_time = silence_time
        # The ID of the alert template.
        # 
        # For more information about how to obtain the ID of an alert template, see [DescribeMetricRuleTemplateList](https://help.aliyun.com/document_detail/114982.html).
        # 
        # This parameter is required.
        self.template_ids = template_ids
        # The webhook URL to which a POST request is sent when an alert is triggered.
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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

