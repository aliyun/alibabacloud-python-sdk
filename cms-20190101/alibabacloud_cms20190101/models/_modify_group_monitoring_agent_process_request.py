# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class ModifyGroupMonitoringAgentProcessRequest(DaraModel):
    def __init__(
        self,
        alert_config: List[main_models.ModifyGroupMonitoringAgentProcessRequestAlertConfig] = None,
        group_id: str = None,
        id: str = None,
        match_express_filter_relation: str = None,
        region_id: str = None,
    ):
        # The alert rule configurations.
        # 
        # This parameter is required.
        self.alert_config = alert_config
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the process monitoring task.
        # 
        # This parameter is required.
        self.id = id
        # The logical operator used between conditional expressions that are used to match instances. Valid values:
        # 
        # *   all
        # *   and
        # *   or
        self.match_express_filter_relation = match_express_filter_relation
        self.region_id = region_id

    def validate(self):
        if self.alert_config:
            for v1 in self.alert_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertConfig'] = []
        if self.alert_config is not None:
            for k1 in self.alert_config:
                result['AlertConfig'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.match_express_filter_relation is not None:
            result['MatchExpressFilterRelation'] = self.match_express_filter_relation

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k1 in m.get('AlertConfig'):
                temp_model = main_models.ModifyGroupMonitoringAgentProcessRequestAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchExpressFilterRelation') is not None:
            self.match_express_filter_relation = m.get('MatchExpressFilterRelation')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyGroupMonitoringAgentProcessRequestAlertConfig(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        effective_interval: str = None,
        escalations_level: str = None,
        no_effective_interval: str = None,
        silence_time: str = None,
        statistics: str = None,
        target_list: List[main_models.ModifyGroupMonitoringAgentProcessRequestAlertConfigTargetList] = None,
        threshold: str = None,
        times: str = None,
        webhook: str = None,
    ):
        # The comparison operator that is used to compare the metric value with the threshold. Valid values of N: 1 to 200. Valid values:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold.
        # *   NotEqualToThreshold: not equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday.
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        # 
        # This parameter is required.
        self.comparison_operator = comparison_operator
        # The time period during which the alert rule is effective. Valid values of N: 1 to 200.
        self.effective_interval = effective_interval
        # The level of the alert. Valid values of N: 1 to 200. Valid values:
        # 
        # *   critical (default value): critical
        # *   warn: warning
        # *   info: information
        # 
        # This parameter is required.
        self.escalations_level = escalations_level
        # The time period during which the alert rule is ineffective. Valid values of N: 1 to 200.
        self.no_effective_interval = no_effective_interval
        # The mute period during which new alerts are not sent even if the trigger conditions are met. Valid values of N: 1 to 200.
        # 
        # Unit: seconds. Minimum value: 3600, which is equivalent to one hour. Default value: 86400, which is equivalent to one day.
        # 
        # >  Only one alert notification is sent during a mute period even if the metric value exceeds the alert threshold during consecutive checks.
        self.silence_time = silence_time
        # The statistical aggregation method that is used to calculate the metric values. Valid values of N: 1 to 200.
        # 
        # >  Set the value to Average.
        self.statistics = statistics
        # The alert trigger.
        self.target_list = target_list
        # The alert threshold. Valid values of N: 1 to 200.
        # 
        # This parameter is required.
        self.threshold = threshold
        # The number of times for which the threshold can be consecutively exceeded. Valid values of N: 1 to 200. Default value: 3.
        # 
        # >  A metric triggers an alert only after the metric value reaches the threshold consecutively for the specified times.
        # 
        # This parameter is required.
        self.times = times
        # The callback URL to which a POST request is sent when an alert is triggered based on the alert rule. Valid values of N: 1 to 200.
        self.webhook = webhook

    def validate(self):
        if self.target_list:
            for v1 in self.target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval

        if self.escalations_level is not None:
            result['EscalationsLevel'] = self.escalations_level

        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        result['TargetList'] = []
        if self.target_list is not None:
            for k1 in self.target_list:
                result['TargetList'].append(k1.to_map() if k1 else None)

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.times is not None:
            result['Times'] = self.times

        if self.webhook is not None:
            result['Webhook'] = self.webhook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')

        if m.get('EscalationsLevel') is not None:
            self.escalations_level = m.get('EscalationsLevel')

        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        self.target_list = []
        if m.get('TargetList') is not None:
            for k1 in m.get('TargetList'):
                temp_model = main_models.ModifyGroupMonitoringAgentProcessRequestAlertConfigTargetList()
                self.target_list.append(temp_model.from_map(k1))

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class ModifyGroupMonitoringAgentProcessRequestAlertConfigTargetList(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        json_params: str = None,
        level: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the resource.
        # 
        # For information about how to obtain the ARN of a resource, see [DescribeMetricRuleTargets](https://help.aliyun.com/document_detail/121592.html).
        # 
        # Format: `acs:{Service name abbreviation}:{regionId}:{userId}:/{Resource type}/{Resource name}/message`. Example: `acs:mns:cn-hangzhou:120886317861****:/queues/test123/message`. Fields:
        # 
        # - {Service name abbreviation}: the abbreviation of the service name. Valid value: mns.
        # - {userId}: the ID of the Alibaba Cloud account.
        # - {regionId}: the region ID of the message queue or topic.
        # - {Resource type}: the type of the resource for which alerts are triggered. Valid values: 
        #     - **queues** 
        #     - **topics** 
        # - {Resourcename}: the name of the resource. 
        #   - If the resource type is set to **queues**, the resource name is the name of the message queue. 
        #   - If the resource type is set to **topics**, the resource name is the name of the topic.`
        self.arn = arn
        # The ID of the resource for which alerts are triggered.
        # 
        # For information about how to obtain the ID of a resource for which alerts are triggered, see [DescribeMetricRuleTargets](https://help.aliyun.com/document_detail/121592.html).
        self.id = id
        # The parameters of the alert callback. The parameters are in the JSON format.
        self.json_params = json_params
        # The level of the alert. Valid values:
        # 
        # *   INFO: information
        # *   WARN: warning
        # *   CRITICAL: critical
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.id is not None:
            result['Id'] = self.id

        if self.json_params is not None:
            result['JsonParams'] = self.json_params

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JsonParams') is not None:
            self.json_params = m.get('JsonParams')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

