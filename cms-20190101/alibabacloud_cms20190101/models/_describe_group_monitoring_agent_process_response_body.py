# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupMonitoringAgentProcessResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: str = None,
        page_size: str = None,
        processes: main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcesses = None,
        request_id: str = None,
        success: bool = None,
        total: str = None,
    ):
        # The HTTP status codes.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The page number. Default value: 1
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The process monitoring tasks.
        self.processes = processes
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: Valid values: true and false.
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.processes:
            self.processes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.processes is not None:
            result['Processes'] = self.processes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Processes') is not None:
            temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcesses()
            self.processes = temp_model.from_map(m.get('Processes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeGroupMonitoringAgentProcessResponseBodyProcesses(DaraModel):
    def __init__(
        self,
        process: List[main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcess] = None,
    ):
        self.process = process

    def validate(self):
        if self.process:
            for v1 in self.process:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Process'] = []
        if self.process is not None:
            for k1 in self.process:
                result['Process'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.process = []
        if m.get('Process') is not None:
            for k1 in m.get('Process'):
                temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcess()
                self.process.append(temp_model.from_map(k1))

        return self

class DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcess(DaraModel):
    def __init__(
        self,
        alert_config: main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfig = None,
        group_id: str = None,
        id: str = None,
        match_express: main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessMatchExpress = None,
        match_express_filter_relation: str = None,
        process_name: str = None,
    ):
        # The alert rule configurations.
        self.alert_config = alert_config
        # The ID of the application group.
        self.group_id = group_id
        # The ID of the process monitoring task.
        self.id = id
        # The matching conditions.
        # 
        # >  Only the instances that meet the conditional expressions are monitored by the process monitoring task.
        self.match_express = match_express
        # The logical operator used between conditional expressions that are used to match instances. Valid values:
        # 
        # *   all
        # *   and
        # *   or
        self.match_express_filter_relation = match_express_filter_relation
        # The process name.
        self.process_name = process_name

    def validate(self):
        if self.alert_config:
            self.alert_config.validate()
        if self.match_express:
            self.match_express.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config.to_map()

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.match_express is not None:
            result['MatchExpress'] = self.match_express.to_map()

        if self.match_express_filter_relation is not None:
            result['MatchExpressFilterRelation'] = self.match_express_filter_relation

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfig') is not None:
            temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfig()
            self.alert_config = temp_model.from_map(m.get('AlertConfig'))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchExpress') is not None:
            temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessMatchExpress()
            self.match_express = temp_model.from_map(m.get('MatchExpress'))

        if m.get('MatchExpressFilterRelation') is not None:
            self.match_express_filter_relation = m.get('MatchExpressFilterRelation')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        return self

class DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessMatchExpress(DaraModel):
    def __init__(
        self,
        match_express: List[main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessMatchExpressMatchExpress] = None,
    ):
        self.match_express = match_express

    def validate(self):
        if self.match_express:
            for v1 in self.match_express:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MatchExpress'] = []
        if self.match_express is not None:
            for k1 in self.match_express:
                result['MatchExpress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.match_express = []
        if m.get('MatchExpress') is not None:
            for k1 in m.get('MatchExpress'):
                temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessMatchExpressMatchExpress()
                self.match_express.append(temp_model.from_map(k1))

        return self

class DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessMatchExpressMatchExpress(DaraModel):
    def __init__(
        self,
        function: str = None,
        name: str = None,
        value: str = None,
    ):
        # The matching condition. Valid values:
        # 
        # *   all (default): matches all
        # *   startWith: starts with a prefix
        # *   endWith: ends with a suffix
        # *   contains: contains
        # *   notContains: excludes
        # *   equals: equals
        # 
        # >  The matched instances are monitored by the process monitoring task.
        self.function = function
        # The criteria based on which the instances are matched.
        # 
        # >  Set the value to `name`. The value name indicates that the instances are matched based on the instance name.
        self.name = name
        # The keyword used to match the instance name.
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

class DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfig(DaraModel):
    def __init__(
        self,
        alert_config: List[main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfig] = None,
    ):
        self.alert_config = alert_config

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_config = []
        if m.get('AlertConfig') is not None:
            for k1 in m.get('AlertConfig'):
                temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfig()
                self.alert_config.append(temp_model.from_map(k1))

        return self

class DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfig(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        effective_interval: str = None,
        escalations_level: str = None,
        no_effective_interval: str = None,
        silence_time: str = None,
        statistics: str = None,
        target_list: main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfigTargetList = None,
        threshold: str = None,
        times: str = None,
        webhook: str = None,
    ):
        # The comparison operator that is used to compare the metric value with the threshold. Valid values:
        # 
        # *   GreaterThanOrEqualToThreshold: greater than or equal to the threshold
        # *   GreaterThanThreshold: greater than the threshold
        # *   LessThanOrEqualToThreshold: less than or equal to the threshold
        # *   LessThanThreshold: less than the threshold
        # *   NotEqualToThreshold: not equal to the threshold
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday.
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        self.comparison_operator = comparison_operator
        # The time period during which the alert rule is effective.
        self.effective_interval = effective_interval
        # The level of the alert. Valid values:
        # 
        # *   critical
        # *   warn
        # *   Info
        self.escalations_level = escalations_level
        # The time period during which the alert rule is ineffective.
        self.no_effective_interval = no_effective_interval
        # The mute period during which new alert notifications are not sent even if the trigger conditions are met. Unit: seconds. Minimum value: 3600, which is equivalent to one hour. Default value: 86400, which is equivalent to one day.
        # 
        # >  Only one alert notification is sent during each mute period even if the metric value exceeds the alert threshold several times.
        self.silence_time = silence_time
        # The method used to calculate metric values that trigger alerts.
        self.statistics = statistics
        # The resources for which alerts are triggered.
        self.target_list = target_list
        # The alert threshold.
        self.threshold = threshold
        # The number of times for which the threshold can be consecutively exceeded.
        # 
        # >  A metric triggers an alert only after the metric value reaches the threshold consecutively for the specified times.
        self.times = times
        # The callback URL to which a POST request is sent when an alert is triggered based on the alert rule.
        self.webhook = webhook

    def validate(self):
        if self.target_list:
            self.target_list.validate()

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

        if self.target_list is not None:
            result['TargetList'] = self.target_list.to_map()

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

        if m.get('TargetList') is not None:
            temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfigTargetList()
            self.target_list = temp_model.from_map(m.get('TargetList'))

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')

        return self

class DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfigTargetList(DaraModel):
    def __init__(
        self,
        target: List[main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfigTargetListTarget] = None,
    ):
        self.target = target

    def validate(self):
        if self.target:
            for v1 in self.target:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Target'] = []
        if self.target is not None:
            for k1 in self.target:
                result['Target'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target = []
        if m.get('Target') is not None:
            for k1 in m.get('Target'):
                temp_model = main_models.DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfigTargetListTarget()
                self.target.append(temp_model.from_map(k1))

        return self

class DescribeGroupMonitoringAgentProcessResponseBodyProcessesProcessAlertConfigAlertConfigTargetListTarget(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        json_parmas: str = None,
        level: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the resource. Format: acs:{Service name abbreviation}:{regionId}:{userId}:/{Resource type}/{Resource name}/message. Example: acs:mns:cn-hangzhou:120886317861\\*\\*\\*\\*:/queues/test123/message. Fields:
        # 
        # *   {Service name abbreviation}: the abbreviation of the service name. Set the value to Simple Message Queue (formerly MNS) (SMQ).
        # 
        # *   {userId}: the ID of the Alibaba Cloud account.
        # 
        # *   {regionId}: the region ID of the SMQ queue or topic.
        # 
        # *   {Resource type}: the type of the resource for which alerts are triggered. Valid values:
        # 
        #     *   **queues**
        #     *   **topics**
        # 
        # *   {Resource name}: the resource name.
        # 
        #     *   If the resource type is **queues**, the resource name is the queue name.
        #     *   If the resource type is **topics**, the resource name is the topic name.
        self.arn = arn
        # The ID of the resource for which alerts are triggered.
        self.id = id
        # The parameters of the alert callback. The parameters are in the JSON format.
        self.json_parmas = json_parmas
        # The alert level. Valid values:
        # 
        # *   INFO
        # *   WARN
        # *   CRITICAL
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

        if self.json_parmas is not None:
            result['JsonParmas'] = self.json_parmas

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JsonParmas') is not None:
            self.json_parmas = m.get('JsonParmas')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

