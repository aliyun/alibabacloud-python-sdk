# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeHostAvailabilityListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_list: main_models.DescribeHostAvailabilityListResponseBodyTaskList = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The details of the availability monitoring tasks.
        self.task_list = task_list
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.task_list:
            self.task_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_list is not None:
            result['TaskList'] = self.task_list.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskList') is not None:
            temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskList()
            self.task_list = temp_model.from_map(m.get('TaskList'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeHostAvailabilityListResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        node_task_config: List[main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfig] = None,
    ):
        self.node_task_config = node_task_config

    def validate(self):
        if self.node_task_config:
            for v1 in self.node_task_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeTaskConfig'] = []
        if self.node_task_config is not None:
            for k1 in self.node_task_config:
                result['NodeTaskConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_task_config = []
        if m.get('NodeTaskConfig') is not None:
            for k1 in m.get('NodeTaskConfig'):
                temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfig()
                self.node_task_config.append(temp_model.from_map(k1))

        return self

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfig(DaraModel):
    def __init__(
        self,
        alert_config: main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfig = None,
        disabled: bool = None,
        group_id: int = None,
        group_name: str = None,
        id: int = None,
        instances: main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigInstances = None,
        task_name: str = None,
        task_option: main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigTaskOption = None,
        task_scope: str = None,
        task_type: str = None,
    ):
        # The configurations of the alert rule.
        self.alert_config = alert_config
        # Indicates whether the availability monitoring task is disabled. Valid values:
        # 
        # *   true: The availability monitoring task is disabled.
        # *   false: The availability monitoring task is enabled.
        self.disabled = disabled
        # The ID of the application group.
        self.group_id = group_id
        # The name of the application group.
        self.group_name = group_name
        # The ID of the availability monitoring task.
        self.id = id
        # The ECS instances that are monitored.
        self.instances = instances
        # The name of the availability monitoring task.
        self.task_name = task_name
        # The optional parameters of the availability monitoring task.
        self.task_option = task_option
        # The range of instances that are monitored by the availability monitoring task. Valid values:
        # 
        # *   GROUP: All ECS instances in the application group are monitored.
        # *   GROUP_SPEC_INSTANCE: Specified ECS instances in the application group are monitored.
        self.task_scope = task_scope
        # The task type. Valid values:
        # 
        # *   PING
        # *   TELNET
        # *   HTTP
        self.task_type = task_type

    def validate(self):
        if self.alert_config:
            self.alert_config.validate()
        if self.instances:
            self.instances.validate()
        if self.task_option:
            self.task_option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config.to_map()

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_option is not None:
            result['TaskOption'] = self.task_option.to_map()

        if self.task_scope is not None:
            result['TaskScope'] = self.task_scope

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfig') is not None:
            temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfig()
            self.alert_config = temp_model.from_map(m.get('AlertConfig'))

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Instances') is not None:
            temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskOption') is not None:
            temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigTaskOption()
            self.task_option = temp_model.from_map(m.get('TaskOption'))

        if m.get('TaskScope') is not None:
            self.task_scope = m.get('TaskScope')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigTaskOption(DaraModel):
    def __init__(
        self,
        http_keyword: str = None,
        http_method: str = None,
        http_negative: bool = None,
        http_post_content: str = None,
        http_response_charset: str = None,
        http_uri: str = None,
        interval: int = None,
        telnet_or_ping_host: str = None,
    ):
        # The response to the HTTP request.
        self.http_keyword = http_keyword
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        self.http_method = http_method
        # The method to trigger an alert. The alert can be triggered based on whether the specified alert rule is included in the response body. Valid values:
        # 
        # *   true: If the HTTP response body includes the alert rule, an alert is triggered.
        # *   false: If the HTTP response does not include the alert rule, an alert is triggered.
        self.http_negative = http_negative
        # The content of the HTTP POST request.
        self.http_post_content = http_post_content
        # The character set that is used in the HTTP response.
        self.http_response_charset = http_response_charset
        # The URI that you want to monitor. If the TaskType parameter is set to HTTP, this parameter is required.
        self.http_uri = http_uri
        # The interval at which detection requests are sent. Unit: seconds.
        self.interval = interval
        # The domain name or IP address that you want to monitor.
        self.telnet_or_ping_host = telnet_or_ping_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_keyword is not None:
            result['HttpKeyword'] = self.http_keyword

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.http_negative is not None:
            result['HttpNegative'] = self.http_negative

        if self.http_post_content is not None:
            result['HttpPostContent'] = self.http_post_content

        if self.http_response_charset is not None:
            result['HttpResponseCharset'] = self.http_response_charset

        if self.http_uri is not None:
            result['HttpURI'] = self.http_uri

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.telnet_or_ping_host is not None:
            result['TelnetOrPingHost'] = self.telnet_or_ping_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpKeyword') is not None:
            self.http_keyword = m.get('HttpKeyword')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('HttpNegative') is not None:
            self.http_negative = m.get('HttpNegative')

        if m.get('HttpPostContent') is not None:
            self.http_post_content = m.get('HttpPostContent')

        if m.get('HttpResponseCharset') is not None:
            self.http_response_charset = m.get('HttpResponseCharset')

        if m.get('HttpURI') is not None:
            self.http_uri = m.get('HttpURI')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('TelnetOrPingHost') is not None:
            self.telnet_or_ping_host = m.get('TelnetOrPingHost')

        return self

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigInstances(DaraModel):
    def __init__(
        self,
        instance: List[str] = None,
    ):
        self.instance = instance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

        return self

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfig(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        escalation_list: main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigEscalationList = None,
        notify_type: int = None,
        silence_time: int = None,
        start_time: int = None,
        target_list: main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigTargetList = None,
        web_hook: str = None,
    ):
        # The end of the time period during which the alert rule is effective. Valid values: 0 to 23.
        # 
        # For example, if the `AlertConfig.StartTime` parameter is set to 0 and the `AlertConfig.EndTime` parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00.
        # 
        # >  Alert notifications are sent based on the specified threshold only if the alert rule is effective.
        self.end_time = end_time
        # The trigger conditions of the alert rule.
        self.escalation_list = escalation_list
        # The alert notification methods. Valid values:
        # 
        # *   2: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   1: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   0: Alert notifications are sent by using emails and DingTalk chatbots.
        self.notify_type = notify_type
        # The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400.
        self.silence_time = silence_time
        # The beginning of the time period during which the alert rule is effective. Valid values: 0 to 23.
        # 
        # For example, if the `AlertConfig.StartTime` parameter is set to 0 and the `AlertConfig.EndTime` parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00.
        # 
        # >  Alert notifications are sent based on the specified threshold only if the alert rule is effective.
        self.start_time = start_time
        # The monitored resources.
        self.target_list = target_list
        # The callback URL.
        # 
        # CloudMonitor pushes an alert notification to the specified callback URL by sending an HTTP POST request. Only the HTTP protocol is supported.
        self.web_hook = web_hook

    def validate(self):
        if self.escalation_list:
            self.escalation_list.validate()
        if self.target_list:
            self.target_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.escalation_list is not None:
            result['EscalationList'] = self.escalation_list.to_map()

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target_list is not None:
            result['TargetList'] = self.target_list.to_map()

        if self.web_hook is not None:
            result['WebHook'] = self.web_hook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EscalationList') is not None:
            temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigEscalationList()
            self.escalation_list = temp_model.from_map(m.get('EscalationList'))

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TargetList') is not None:
            temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigTargetList()
            self.target_list = temp_model.from_map(m.get('TargetList'))

        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')

        return self

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigTargetList(DaraModel):
    def __init__(
        self,
        target: List[main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigTargetListTarget] = None,
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
                temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigTargetListTarget()
                self.target.append(temp_model.from_map(k1))

        return self

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigTargetListTarget(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        json_params: str = None,
        level: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the function.
        # 
        # Format: `arn:acs:${Service}:${Region}:${Account}:${ResourceType}/${ResourceId}`. Fields:
        # 
        # *   Service: the service code
        # *   Region: the region ID
        # *   Account: the ID of the Alibaba Cloud account
        # *   ResourceType: the resource type
        # *   ResourceId: the resource ID.
        self.arn = arn
        # The ID of the resource that triggers the alert.
        self.id = id
        # The JSON-formatted parameters of the alert callback.
        self.json_params = json_params
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

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigEscalationList(DaraModel):
    def __init__(
        self,
        escalation_list: List[main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigEscalationListEscalationList] = None,
    ):
        self.escalation_list = escalation_list

    def validate(self):
        if self.escalation_list:
            for v1 in self.escalation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['escalationList'] = []
        if self.escalation_list is not None:
            for k1 in self.escalation_list:
                result['escalationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalation_list = []
        if m.get('escalationList') is not None:
            for k1 in m.get('escalationList'):
                temp_model = main_models.DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigEscalationListEscalationList()
                self.escalation_list.append(temp_model.from_map(k1))

        return self

class DescribeHostAvailabilityListResponseBodyTaskListNodeTaskConfigAlertConfigEscalationListEscalationList(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        metric_name: str = None,
        operator: str = None,
        times: str = None,
        value: str = None,
    ):
        # The method used to calculate metric values that trigger alerts. Valid values:
        # 
        # *   Value: the value of the HTTP status code
        # *   Average: the average HTTP response time
        # *   Value: the value of the Telnet status code
        # *   TelnetLatency: the average Telnet response time
        # *   Average: the average Ping packet loss rate
        self.aggregate = aggregate
        # The name of the metric. Valid values:
        # 
        # *   HttpStatus
        # *   HttpLatency
        # *   TelnetStatus
        # *   TelnetLatency
        # *   PingLostRate
        self.metric_name = metric_name
        # The comparison operator that is used in the alert rule. Valid values:
        # 
        # *   `>`
        # *   `>=`
        # *   `<`
        # *   `<=`
        # *   `=`
        self.operator = operator
        # The consecutive number of times for which the metric value is measured before an alert is triggered.
        self.times = times
        # The alert threshold.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate is not None:
            result['Aggregate'] = self.aggregate

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.times is not None:
            result['Times'] = self.times

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregate') is not None:
            self.aggregate = m.get('Aggregate')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

