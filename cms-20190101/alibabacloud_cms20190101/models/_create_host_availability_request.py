# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateHostAvailabilityRequest(DaraModel):
    def __init__(
        self,
        alert_config: main_models.CreateHostAvailabilityRequestAlertConfig = None,
        task_option: main_models.CreateHostAvailabilityRequestTaskOption = None,
        alert_config_escalation_list: List[main_models.CreateHostAvailabilityRequestAlertConfigEscalationList] = None,
        alert_config_target_list: List[main_models.CreateHostAvailabilityRequestAlertConfigTargetList] = None,
        group_id: int = None,
        instance_list: List[str] = None,
        region_id: str = None,
        task_name: str = None,
        task_scope: str = None,
        task_type: str = None,
    ):
        self.alert_config = alert_config
        self.task_option = task_option
        # None
        # 
        # This parameter is required.
        self.alert_config_escalation_list = alert_config_escalation_list
        # The resources for which alerts are triggered.
        self.alert_config_target_list = alert_config_target_list
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ECS instances that are monitored. Valid values of N: 1 to 21.
        # 
        # > This parameter must be specified when `TaskScope` is set to `GROUP_SPEC_INSTANCE`.
        self.instance_list = instance_list
        self.region_id = region_id
        # The name of the availability monitoring task. The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.task_name = task_name
        # The range of instances that are monitored by the availability monitoring task. Valid values:
        # 
        # *   GROUP: All ECS instances in the application group are monitored.
        # *   GROUP_SPEC_INSTANCE: Specified ECS instances in the application group are monitored. The TaskScope parameter must be used in combination with the InstanceList parameter. The InstanceList parameter specifies the ECS instances to be monitored.
        self.task_scope = task_scope
        # The monitoring type of the availability monitoring task. Valid values:
        # 
        # *   PING
        # *   TELNET
        # *   HTTP
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        if self.alert_config:
            self.alert_config.validate()
        if self.task_option:
            self.task_option.validate()
        if self.alert_config_escalation_list:
            for v1 in self.alert_config_escalation_list:
                 if v1:
                    v1.validate()
        if self.alert_config_target_list:
            for v1 in self.alert_config_target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_config is not None:
            result['AlertConfig'] = self.alert_config.to_map()

        if self.task_option is not None:
            result['TaskOption'] = self.task_option.to_map()

        result['AlertConfigEscalationList'] = []
        if self.alert_config_escalation_list is not None:
            for k1 in self.alert_config_escalation_list:
                result['AlertConfigEscalationList'].append(k1.to_map() if k1 else None)

        result['AlertConfigTargetList'] = []
        if self.alert_config_target_list is not None:
            for k1 in self.alert_config_target_list:
                result['AlertConfigTargetList'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_scope is not None:
            result['TaskScope'] = self.task_scope

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConfig') is not None:
            temp_model = main_models.CreateHostAvailabilityRequestAlertConfig()
            self.alert_config = temp_model.from_map(m.get('AlertConfig'))

        if m.get('TaskOption') is not None:
            temp_model = main_models.CreateHostAvailabilityRequestTaskOption()
            self.task_option = temp_model.from_map(m.get('TaskOption'))

        self.alert_config_escalation_list = []
        if m.get('AlertConfigEscalationList') is not None:
            for k1 in m.get('AlertConfigEscalationList'):
                temp_model = main_models.CreateHostAvailabilityRequestAlertConfigEscalationList()
                self.alert_config_escalation_list.append(temp_model.from_map(k1))

        self.alert_config_target_list = []
        if m.get('AlertConfigTargetList') is not None:
            for k1 in m.get('AlertConfigTargetList'):
                temp_model = main_models.CreateHostAvailabilityRequestAlertConfigTargetList()
                self.alert_config_target_list.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskScope') is not None:
            self.task_scope = m.get('TaskScope')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class CreateHostAvailabilityRequestAlertConfigTargetList(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        json_params: str = None,
        level: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the resource. Format: `acs:{Service name abbreviation}:{regionId}:{userId}:/{Resource type}/{Resource name}/message`. Example: `acs:mns:cn-hangzhou:120886317861****:/queues/test123/message`. Fields:
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

class CreateHostAvailabilityRequestAlertConfigEscalationList(DaraModel):
    def __init__(
        self,
        aggregate: str = None,
        metric_name: str = None,
        operator: str = None,
        times: int = None,
        value: str = None,
    ):
        # The method used to calculate the metric values that trigger alerts. Valid values of N: 1 to 21. Valid values:
        # 
        # *   HttpStatus: Value
        # *   HttpLatency: Average
        # *   TelnetStatus: Value
        # *   TelnetLatency: Average
        # *   PingLostRate: Average
        # 
        # > The value Value indicates the original value and is used for metrics such as status codes. The value Average indicates the average value and is used for metrics such as the latency and packet loss rate.
        self.aggregate = aggregate
        # The metric for which the alert feature is enabled. Valid values of N: 1 to 21. Valid values:
        # 
        # *   HttpStatus: HTTP status code
        # *   HttpLatency: HTTP response time
        # *   TelnetStatus: Telnet status code
        # *   TelnetLatency: Telnet response time
        # *   PingLostRate: Ping packet loss rate
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The comparison operator that is used in the alert rule. Valid values of N: 1 to 21. Valid values:
        # 
        # *   `>`
        # *   `>=`
        # *   `<`
        # *   `<=`
        # *   `=`
        self.operator = operator
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered. Valid values of N: 1 to 21.
        self.times = times
        # The alert threshold. Valid values of N: 1 to 21.
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

class CreateHostAvailabilityRequestTaskOption(DaraModel):
    def __init__(
        self,
        http_header: str = None,
        http_method: str = None,
        http_negative: bool = None,
        http_post_content: str = None,
        http_response_charset: str = None,
        http_response_match_content: str = None,
        http_uri: str = None,
        interval: int = None,
        telnet_or_ping_host: str = None,
    ):
        # The header of the HTTP request. Format: `Parameter name:Parameter value`. Separate multiple parameters with carriage return characters. Example:
        # 
        #     params1:value1
        #     params2:value2
        self.http_header = http_header
        # The HTTP request method. Valid values:
        # 
        # *   GET
        # *   POST
        # *   HEAD
        # 
        # > This parameter must be specified when TaskType is set to HTTP.
        self.http_method = http_method
        # The method to trigger an alert. The alert can be triggered based on whether the specified alert rule is included in the response body. Valid values:
        # 
        # *   true: If the HTTP response body includes the alert rule, an alert is triggered.
        # *   false: If the HTTP response does not include the alert rule, an alert is triggered.
        # 
        # > This parameter must be specified when TaskType is set to HTTP.
        self.http_negative = http_negative
        # The content of the HTTP POST request.
        self.http_post_content = http_post_content
        # The character set that is used in the HTTP response.
        # 
        # > Only UTF-8 is supported.
        self.http_response_charset = http_response_charset
        # The response to the HTTP request.
        self.http_response_match_content = http_response_match_content
        # The URI that you want to monitor. This parameter is required if the TaskType parameter is set to HTTP or Telnet.
        self.http_uri = http_uri
        # The interval at which detection requests are sent. Unit: seconds. Valid values: 15, 30, 60, 120, 300, 900, 1800, and 3600.
        # 
        # > This parameter is available only for the CloudMonitor agent V3.5.1 or later.
        self.interval = interval
        # The domain name or IP address that you want to monitor.
        # 
        # >  This parameter is required if the TaskType parameter is set to PING.
        self.telnet_or_ping_host = telnet_or_ping_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_header is not None:
            result['HttpHeader'] = self.http_header

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.http_negative is not None:
            result['HttpNegative'] = self.http_negative

        if self.http_post_content is not None:
            result['HttpPostContent'] = self.http_post_content

        if self.http_response_charset is not None:
            result['HttpResponseCharset'] = self.http_response_charset

        if self.http_response_match_content is not None:
            result['HttpResponseMatchContent'] = self.http_response_match_content

        if self.http_uri is not None:
            result['HttpURI'] = self.http_uri

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.telnet_or_ping_host is not None:
            result['TelnetOrPingHost'] = self.telnet_or_ping_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpHeader') is not None:
            self.http_header = m.get('HttpHeader')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('HttpNegative') is not None:
            self.http_negative = m.get('HttpNegative')

        if m.get('HttpPostContent') is not None:
            self.http_post_content = m.get('HttpPostContent')

        if m.get('HttpResponseCharset') is not None:
            self.http_response_charset = m.get('HttpResponseCharset')

        if m.get('HttpResponseMatchContent') is not None:
            self.http_response_match_content = m.get('HttpResponseMatchContent')

        if m.get('HttpURI') is not None:
            self.http_uri = m.get('HttpURI')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('TelnetOrPingHost') is not None:
            self.telnet_or_ping_host = m.get('TelnetOrPingHost')

        return self

class CreateHostAvailabilityRequestAlertConfig(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        notify_type: int = None,
        silence_time: int = None,
        start_time: int = None,
        web_hook: str = None,
    ):
        # The end of the time range during which the alert rule is effective. Valid values: 0 to 23.
        # 
        # For example, if the `AlertConfig.StartTime` parameter is set to 0 and the `AlertConfig.EndTime` parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00.
        # 
        # > Alert notifications are sent based on the specified threshold only if the alert rule is effective.
        self.end_time = end_time
        # The alert notification methods. Valid values:
        # 
        # 0: Alert notifications are sent by using emails and DingTalk chatbots.
        # 
        # This parameter is required.
        self.notify_type = notify_type
        # The mute period during which new alerts are not sent even if the trigger conditions are met. Unit: seconds. Default value: 86400. The default value indicates one day.
        self.silence_time = silence_time
        # The beginning of the time range during which the alert rule is effective. Valid values: 0 to 23.
        # 
        # For example, if the `AlertConfig.StartTime` parameter is set to 0 and the `AlertConfig.EndTime` parameter is set to 22, the alert rule is effective from 00:00:00 to 22:00:00.
        # 
        # > Alert notifications are sent based on the specified threshold only if the alert rule is effective.
        self.start_time = start_time
        # The callback URL.
        self.web_hook = web_hook

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.web_hook is not None:
            result['WebHook'] = self.web_hook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')

        return self

