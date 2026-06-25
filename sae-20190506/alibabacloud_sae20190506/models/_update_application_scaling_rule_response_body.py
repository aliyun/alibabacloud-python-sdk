# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationScalingRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateApplicationScalingRuleResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code or a POP error code.
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: A client-side error occurred.
        # 
        # - **5xx**: A server-side error occurred.
        self.code = code
        # The response data.
        self.data = data
        # The error code.
        # 
        # - This parameter is returned only if the request fails.
        # 
        # - For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The response message.
        # 
        # - **success** is returned if the request is successful.
        # 
        # - An error message is returned if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Specifies whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID used to query call details.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class UpdateApplicationScalingRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        enable_idle: bool = None,
        last_disable_time: int = None,
        metric: main_models.UpdateApplicationScalingRuleResponseBodyDataMetric = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: main_models.UpdateApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The time when the scaling policy was created, in milliseconds.
        self.create_time = create_time
        # Specifies whether to enable idle mode.
        self.enable_idle = enable_idle
        # The time when the scaling policy was last disabled, in milliseconds.
        self.last_disable_time = last_disable_time
        # The configuration for metric-based scaling.
        self.metric = metric
        # Specifies whether the scaling policy is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.scale_rule_enabled = scale_rule_enabled
        # The name of the scaling policy.
        self.scale_rule_name = scale_rule_name
        # The type of the scaling policy. Valid values:
        # 
        # - **timing**: scheduled scaling
        # 
        # - **metric**: metric-based scaling
        # 
        # - **mix**: hybrid scaling
        self.scale_rule_type = scale_rule_type
        # The configuration for scheduled scaling.
        self.timer = timer
        # The time when the scaling policy was updated, in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_idle is not None:
            result['EnableIdle'] = self.enable_idle

        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time

        if self.metric is not None:
            result['Metric'] = self.metric.to_map()

        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled

        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name

        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type

        if self.timer is not None:
            result['Timer'] = self.timer.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableIdle') is not None:
            self.enable_idle = m.get('EnableIdle')

        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')

        if m.get('Metric') is not None:
            temp_model = main_models.UpdateApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m.get('Metric'))

        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')

        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')

        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')

        if m.get('Timer') is not None:
            temp_model = main_models.UpdateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m.get('Timer'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class UpdateApplicationScalingRuleResponseBodyDataTimer(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[main_models.UpdateApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        # The start date of the short-term scheduled scaling policy.
        # 
        # - If **BeginDate** and **EndDate** are both set to **null**, the policy is long-term by default.
        # 
        # - If you specify a date range, for example, **BeginDate** is set to 2021-03-25 and **EndDate** is set to 2021-04-25, the policy is effective for one month.
        self.begin_date = begin_date
        # The end date of the short-term scheduled scaling policy.
        # 
        # - If **BeginDate** and **EndDate** are both set to **null**, the policy is long-term by default.
        # 
        # - If you specify a date range, for example, **BeginDate** is set to 2021-03-25 and **EndDate** is set to 2021-04-25, the policy is effective for one month.
        self.end_date = end_date
        # The recurrence schedule for the scaling policy.
        # 
        # - **\\* \\* \\***: The policy runs at a specified time every day.
        # 
        # - **\\* \\* Fri,Mon**: The policy runs at a specified time on specific days of a week. You can select multiple days. The time is in the GMT+8 time zone. Valid values:
        # 
        #   - **Sun**: Sunday
        # 
        #   - **Mon**: Monday
        # 
        #   - **Tue**: Tuesday
        # 
        #   - **Wed**: Wednesday
        # 
        #   - **Thu**: Thursday
        # 
        #   - **Fri**: Friday
        # 
        #   - **Sat**: Saturday
        # 
        # - **1,2,3,28,31 \\* \\***: The policy runs at a specified time on specific days of a month. You can select multiple days. If a month does not have a specific day, such as the 31st, the policy skips that day.
        self.period = period
        # The schedules for the scaling policy.
        self.schedules = schedules

    def validate(self):
        if self.schedules:
            for v1 in self.schedules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.period is not None:
            result['Period'] = self.period

        result['Schedules'] = []
        if self.schedules is not None:
            for k1 in self.schedules:
                result['Schedules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        self.schedules = []
        if m.get('Schedules') is not None:
            for k1 in m.get('Schedules'):
                temp_model = main_models.UpdateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k1))

        return self

class UpdateApplicationScalingRuleResponseBodyDataTimerSchedules(DaraModel):
    def __init__(
        self,
        at_time: str = None,
        max_replicas: int = None,
        min_replicas: int = None,
        target_replicas: int = None,
    ):
        # The time at which the scaling action is triggered. Format: **HH:mm**.
        self.at_time = at_time
        # The maximum number of instances.
        self.max_replicas = max_replicas
        # The minimum number of instances.
        self.min_replicas = min_replicas
        # The target number of instances.
        self.target_replicas = target_replicas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.at_time is not None:
            result['AtTime'] = self.at_time

        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')

        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')

        return self

class UpdateApplicationScalingRuleResponseBodyDataMetric(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[main_models.UpdateApplicationScalingRuleResponseBodyDataMetricMetrics] = None,
        min_replicas: int = None,
    ):
        # The maximum number of instances.
        self.max_replicas = max_replicas
        # The metrics that trigger scaling actions.
        self.metrics = metrics
        # The minimum number of instances.
        self.min_replicas = min_replicas

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.UpdateApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        return self

class UpdateApplicationScalingRuleResponseBodyDataMetricMetrics(DaraModel):
    def __init__(
        self,
        metric_target_average_utilization: int = None,
        metric_type: str = None,
        slb_id: str = None,
        slb_logstore: str = None,
        slb_project: str = None,
        vport: str = None,
    ):
        # The target value for the specified metric. The unit varies based on the metric type.
        # 
        # - Target CPU utilization, in percentage.
        # 
        # - Target memory usage, in percentage.
        # 
        # - Target queries per second (QPS).
        # 
        # - Target response time, in milliseconds.
        # 
        # - The target number of active TCP connections.
        # 
        # - Target QPS for the public-facing SLB instance.
        # 
        # - Target response time of the public-facing SLB instance, in milliseconds.
        # 
        # - Target QPS for the internal SLB instance.
        # 
        # - Target response time of the internal SLB instance, in milliseconds.
        self.metric_target_average_utilization = metric_target_average_utilization
        # The metric that triggers the scaling policy. Valid values:
        # 
        # - **CPU**: CPU utilization.
        # 
        # - **MEMORY**: memory usage.
        # 
        # - **QPS**: The average queries per second (QPS) per instance over the last minute. This applies only to Java applications.
        # 
        # - **RT**: The average response time (RT) of all service interfaces in the application over the last minute. This applies only to Java applications.
        # 
        # - **tcpActiveConn**: The average number of active TCP connections per instance over the last 30 seconds.
        # 
        # - **SLB_QPS**: The average QPS from the public-facing SLB, per instance, over the last 15 seconds.
        # 
        # - **SLB_RT**: The average response time of a public-facing SLB instance over the last 15 seconds.
        # 
        # - **INTRANET_SLB_QPS**: The average QPS from the internal SLB, per instance, over the last 15 seconds.
        # 
        # - **INTRANET_SLB_RT**: The average response time of an internal SLB instance over the last 15 seconds.
        self.metric_type = metric_type
        # The SLB instance ID.
        self.slb_id = slb_id
        # The name of the Logstore for SLB access logs.
        self.slb_logstore = slb_logstore
        # The name of the Log Service Project for SLB access logs.
        self.slb_project = slb_project
        # The SLB port.
        self.vport = vport

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_logstore is not None:
            result['SlbLogstore'] = self.slb_logstore

        if self.slb_project is not None:
            result['SlbProject'] = self.slb_project

        if self.vport is not None:
            result['Vport'] = self.vport

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbLogstore') is not None:
            self.slb_logstore = m.get('SlbLogstore')

        if m.get('SlbProject') is not None:
            self.slb_project = m.get('SlbProject')

        if m.get('Vport') is not None:
            self.vport = m.get('Vport')

        return self

