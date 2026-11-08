# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateGroupMonitoringAgentProcessRequest(DaraModel):
    def __init__(
        self,
        alert_config: List[main_models.CreateGroupMonitoringAgentProcessRequestAlertConfig] = None,
        group_id: str = None,
        match_express: List[main_models.CreateGroupMonitoringAgentProcessRequestMatchExpress] = None,
        match_express_filter_relation: str = None,
        process_name: str = None,
        region_id: str = None,
    ):
        # The list of alert rule configurations.
        # 
        # Valid values of N: 1 to 3.
        # 
        # This parameter is required.
        self.alert_config = alert_config
        # The application group ID.
        # 
        # For information about how to obtain the application group ID, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The list of match conditional expressions.
        # 
        # Valid values of N: 1 to 3.
        self.match_express = match_express
        # The logical relation for matching instances. Valid values:
        # 
        # - all: all.
        # - and: AND.
        # - or: OR.
        self.match_express_filter_relation = match_express_filter_relation
        # The process name.
        # 
        # This parameter is required.
        self.process_name = process_name
        self.region_id = region_id

    def validate(self):
        if self.alert_config:
            for v1 in self.alert_config:
                 if v1:
                    v1.validate()
        if self.match_express:
            for v1 in self.match_express:
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

        result['MatchExpress'] = []
        if self.match_express is not None:
            for k1 in self.match_express:
                result['MatchExpress'].append(k1.to_map() if k1 else None)

        if self.match_express_filter_relation is not None:
            result['MatchExpressFilterRelation'] = self.match_express_filter_relation

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k1 in m.get('AlertConfig'):
                temp_model = main_models.CreateGroupMonitoringAgentProcessRequestAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.match_express = []
        if m.get('MatchExpress') is not None:
            for k1 in m.get('MatchExpress'):
                temp_model = main_models.CreateGroupMonitoringAgentProcessRequestMatchExpress()
                self.match_express.append(temp_model.from_map(k1))

        if m.get('MatchExpressFilterRelation') is not None:
            self.match_express_filter_relation = m.get('MatchExpressFilterRelation')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateGroupMonitoringAgentProcessRequestMatchExpress(DaraModel):
    def __init__(
        self,
        function: str = None,
        name: str = None,
        value: str = None,
    ):
        # The match condition. Valid values:
        # 
        # - all: matches all. This is the default value.
        # - startWith: matches the prefix.
        # - endWith: matches the suffix.
        # - contains: contains the specified string.
        # - notContains: does not contain the specified string.
        # - equals: exactly matches.
        # 
        # Valid values of N: 1 to 3.
        self.function = function
        # The type of the match condition.
        # 
        # Valid values of N: 1 to 3.
        # 
        # > Only Name, which indicates the instance name, is supported.
        self.name = name
        # The name of the matched instance.
        # 
        # Valid values of N: 1 to 3.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateGroupMonitoringAgentProcessRequestAlertConfig(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        effective_interval: str = None,
        escalations_level: str = None,
        no_effective_interval: str = None,
        silence_time: str = None,
        statistics: str = None,
        target_list: List[main_models.CreateGroupMonitoringAgentProcessRequestAlertConfigTargetList] = None,
        threshold: str = None,
        times: str = None,
        webhook: str = None,
    ):
        # The comparison operator for the threshold. Valid values:
        # 
        # - GreaterThanOrEqualToThreshold: greater than or equal to.
        # - GreaterThanThreshold: greater than.
        # - LessThanOrEqualToThreshold: less than or equal to.
        # - LessThanThreshold: less than.
        # - NotEqualToThreshold: not equal to.
        # - GreaterThanYesterday: greater than the value at the same time yesterday.
        # - LessThanYesterday: less than the value at the same time yesterday.
        # - GreaterThanLastWeek: greater than the value at the same time last week.
        # - LessThanLastWeek: less than the value at the same time last week.
        # - GreaterThanLastPeriod: greater than the value in the previous period.
        # - LessThanLastPeriod: less than the value in the previous period.
        # 
        # Valid values of N: 1 to 3.
        # 
        # This parameter is required.
        self.comparison_operator = comparison_operator
        # The effective period of the alert rule.
        # 
        # Valid values of N: 1 to 3.
        self.effective_interval = effective_interval
        # The alert level. Valid values:
        # 
        # - critical: critical. This is the default value.
        # - warn: warning.
        # - info: informational.
        # 
        # Valid values of N: 1 to 3.
        # 
        # This parameter is required.
        self.escalations_level = escalations_level
        # **[Deprecated]** This parameter is deprecated and no longer requires attention.
        self.no_effective_interval = no_effective_interval
        # The mute period. Unit: seconds. Minimum value: 3600, which indicates 1 hour. Default value: 86400, which indicates 1 day.
        # 
        # Valid values of N: 1 to 3.
        # 
        # > If the monitoring data continuously exceeds the alert rule threshold, the system sends only one alert notification within each mute period.
        self.silence_time = silence_time
        # The statistical method for alerts.
        # 
        # Valid values of N: 1 to 3.
        # 
        # > Only Average is supported.
        # 
        # This parameter is required.
        self.statistics = statistics
        # The list of alert targets.
        self.target_list = target_list
        # The alert threshold.
        # 
        # Valid values of N: 1 to 3.
        # 
        # Unit: count.
        # 
        # This parameter is required.
        self.threshold = threshold
        # The number of consecutive times the alert level is triggered. Default value: 3.
        # 
        # Valid values of N: 1 to 3.
        # 
        # > An alert is triggered only when the alert level is reached for the specified number of consecutive times and the alert threshold is met.
        # 
        # This parameter is required.
        self.times = times
        # The webhook URL for alert callbacks.
        # 
        # Valid values of N: 1 to 3.
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
                temp_model = main_models.CreateGroupMonitoringAgentProcessRequestAlertConfigTargetList()
                self.target_list.append(temp_model.from_map(k1))

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class CreateGroupMonitoringAgentProcessRequestAlertConfigTargetList(DaraModel):
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
        # The ARN is in the following format: `acs:{service abbreviation}:{regionId}:{userId}:/{resource type}/{resource name}/message`. Example: `acs:mns:cn-hangzhou:120886317861****:/queues/test123/message`. The parameters are described as follows:
        # 
        # - {service abbreviation}: the abbreviation of the cloud service. Only Simple Message Queue (formerly MNS) is supported.
        # 
        # - {userId}: the Alibaba Cloud account ID.
        # 
        # - {regionId}: the region where the Simple Message Queue (formerly MNS) queue or topic resides.
        # 
        # - {resource type}: the type of the resource that receives alert notifications. Valid values:
        #   
        #     - **queues**: queue.
        #     - **topics**: topic.
        # 
        # - {resource name}: the name of the resource.
        # 
        #     - If the resource type is **queues**, the resource name is the queue name.
        #     - If the resource type is **topics**, the resource name is the topic name.
        self.arn = arn
        # The ID of the alert target.
        # 
        # For information about how to obtain the ID of an alert target, see [DescribeMetricRuleTargets](https://help.aliyun.com/document_detail/121592.html).
        self.id = id
        # The JSON-formatted parameters for the alert callback.
        self.json_params = json_params
        # The alert level. Valid values:
        # 
        # - INFO: informational.
        # - WARN: warning.
        # - CRITICAL: critical.
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

