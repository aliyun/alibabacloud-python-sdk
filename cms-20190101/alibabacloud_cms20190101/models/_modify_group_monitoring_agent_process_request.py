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
        # The configurations of the alert rule.
        # 
        # This parameter is required.
        self.alert_config = alert_config
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the process monitoring job for the application group.
        # 
        # This parameter is required.
        self.id = id
        # This parameter is deprecated. You can ignore it.
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
        # The comparison operator for the threshold of the Critical alert level. The value of N can be 1 to 200. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to
        # 
        # - GreaterThanThreshold: greater than
        # 
        # - LessThanOrEqualToThreshold: less than or equal to
        # 
        # - LessThanThreshold: less than
        # 
        # - NotEqualToThreshold: not equal to
        # 
        # - GreaterThanYesterday: greater than the value at the same time yesterday
        # 
        # - LessThanYesterday: less than the value at the same time yesterday
        # 
        # - GreaterThanLastWeek: greater than the value at the same time last week
        # 
        # - LessThanLastWeek: less than the value at the same time last week
        # 
        # - GreaterThanLastPeriod: greater than the value in the last monitoring cycle
        # 
        # - LessThanLastPeriod: less than the value in the last monitoring cycle
        # 
        # This parameter is required.
        self.comparison_operator = comparison_operator
        # The time period when the alert rule is effective. The value of N can be 1 to 200.
        self.effective_interval = effective_interval
        # The alert level. The value of N can be 1 to 200. Valid values:
        # 
        # - critical (default): critical
        # 
        # - warn: warning
        # 
        # - info: information
        # 
        # This parameter is required.
        self.escalations_level = escalations_level
        # This parameter is deprecated. You can ignore it.
        self.no_effective_interval = no_effective_interval
        # The mute period. The value of N can be 1 to 200.
        # 
        # Unit: seconds. Minimum value: 3600. Default value: 86400.
        # 
        # > If monitoring data continuously exceeds the alert threshold, an alert notification is sent only once during each mute period.
        self.silence_time = silence_time
        # The statistical method for alerts. The value of N can be 1 to 200.
        # 
        # > Only Average is supported.
        self.statistics = statistics
        # None.
        self.target_list = target_list
        # The alert threshold. The value of N can be 1 to 200.
        # 
        # This parameter is required.
        self.threshold = threshold
        # The number of consecutive times that the alert level is reached. The value of N can be 1 to 200. Default value: 3.
        # 
        # > An alert is triggered only when the alert level is reached the specified number of consecutive times and the threshold is met.
        # 
        # This parameter is required.
        self.times = times
        # The callback URL. A POST request is sent to this URL when an alert is triggered. The value of N can be 1 to 200.
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
        # For more information, see [DescribeMetricRuleTargets](https://help.aliyun.com/document_detail/121592.html).
        # 
        # The ARN of a resource is in the following format: `acs:{product-abbreviation}:{regionId}:{userId}:/{resource-type}/{resource-name}/message`. For example: `acs:mns:cn-hangzhou:120886317861****:/queues/test123/message`. The parameters are described as follows:
        # 
        # - {product-abbreviation}: Currently, only Simple Message Queue (formerly MNS) is supported.
        # 
        # - {userId}: The ID of your Alibaba Cloud account.
        # 
        # - {regionId}: The region where the Simple Message Queue (formerly MNS) queue or subject is located.
        # 
        # - {resource-type}: The type of the resource that receives alerts. Valid values:
        # 
        #   - **queues**: a queue.
        # 
        #   - **topics**: a subject.
        # 
        # - {resource-name}: The name of the resource.
        # 
        #   - If the resource type is **queues**, the resource name is the queue name.
        # 
        #   - If the resource type is **topics**, the resource name is the subject name.
        self.arn = arn
        # The ID of the alert-triggered target.
        # 
        # For more information, see [DescribeMetricRuleTargets](https://help.aliyun.com/document_detail/121592.html).
        self.id = id
        # The JSON-formatted parameters for the alert callback.
        self.json_params = json_params
        # The alert level. Valid values:
        # 
        # - INFO: information
        # 
        # - WARN: warning
        # 
        # - CRITICAL: critical
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

