# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutCustomMetricRuleRequest(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        contact_groups: str = None,
        effective_interval: str = None,
        email_subject: str = None,
        evaluation_count: int = None,
        group_id: str = None,
        level: str = None,
        metric_name: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: int = None,
        statistics: str = None,
        threshold: str = None,
        webhook: str = None,
    ):
        # The operator that is used to compare the metric value with the threshold. Valid values:
        # 
        # *   `>=`
        # *   `=`
        # *   `<=`
        # *   `>`
        # *   `<`
        # *   `!=`
        # 
        # This parameter is required.
        self.comparison_operator = comparison_operator
        # The alert contact groups. Separate multiple alert contact groups with commas (,).
        # 
        # This parameter is required.
        self.contact_groups = contact_groups
        # The period of time during which the alert rule is effective. Valid values: 00:00 to 23:59.
        self.effective_interval = effective_interval
        # The subject of the alert notification email.
        self.email_subject = email_subject
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered.
        # 
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # The ID of the application group to which the custom monitoring data belongs.
        # 
        # >  The value 0 indicates that the reported custom monitoring data does not belong to an application group.
        self.group_id = group_id
        # The alert level. Valid values:
        # 
        # *   CRITICAL
        # *   WARN
        # *   INFO
        # 
        # This parameter is required.
        self.level = level
        # The metric name.
        # 
        # >  For more information about how to obtain the metric name, see [DescribeCustomMetricList](https://help.aliyun.com/document_detail/115005.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The cycle that is used to aggregate custom monitoring data. Unit: seconds Set the value to an integral multiple of 60. The original reporting cycle of custom monitoring data is used by default.
        self.period = period
        # The custom monitoring data to which the alert rule applies. The value includes the application group ID to which the custom monitoring data belongs and the dimension to which the metric belongs.
        # 
        # This parameter is required.
        self.resources = resources
        # The ID of the alert rule.
        # 
        # >  You can specify an existing ID to modify the corresponding alert rule or specify a new ID to create an alert rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # The mute period during which new alert notifications are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400, which is equivalent to one day.
        # 
        # >  Only one alert notification is sent during each mute period even if the metric value exceeds the alert threshold several times.
        self.silence_time = silence_time
        # The method used to calculate the metric value based on which alerts are triggered.
        # 
        # This parameter is required.
        self.statistics = statistics
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
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.email_subject is not None:
            result['EmailSubject'] = self.email_subject

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.level is not None:
            result['Level'] = self.level

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.period is not None:
            result['Period'] = self.period

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EmailSubject') is not None:
            self.email_subject = m.get('EmailSubject')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

