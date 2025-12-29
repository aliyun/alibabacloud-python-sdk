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
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The returned result.
        self.data = data
        # The error code returned. Take note of the following rules:
        # 
        # *   If the call is successful, **ErrorCode** is not returned.
        # *   If the call fails, **ErrorCode** is returned. For more information, see the "**Error codes**" section in this topic.
        self.error_code = error_code
        # The returned message. Take note of the following rules:
        # 
        # *   If the call is successful, **success** is returned.
        # *   If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Specifies whether the instances are successfully restarted. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The trace ID that is used to query the details of the request.
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
        # The time when the auto scaling policy was created. Unit: milliseconds.
        self.create_time = create_time
        self.enable_idle = enable_idle
        # The time when the auto scaling policy was last disabled.
        self.last_disable_time = last_disable_time
        # The details of the metric-based auto scaling policy.
        self.metric = metric
        # Specifies whether to enable the auto scaling policy. Valid values:
        # 
        # *   **true**: The auto scaling policy is enabled.
        # *   **false**: The auto scaling policy is disabled.
        self.scale_rule_enabled = scale_rule_enabled
        # The name of the auto scaling policy.
        self.scale_rule_name = scale_rule_name
        # The type of the auto scaling policy. Valid values:
        # 
        # *   **timing**: a scheduled auto scaling policy
        # *   **metric**: a metric-based auto scaling policy
        # *   **mix**: a hybrid auto scaling policy
        self.scale_rule_type = scale_rule_type
        # The details of the scheduled auto scaling policy.
        self.timer = timer
        # The time when the auto scaling policy was updated. Unit: milliseconds.
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
        # The start date of the validity period of the scheduled auto scaling policy. Parameter description:
        # 
        # *   If **BeginDate** and **EndDate** are set to **null**, the auto scaling policy is a long-term policy. Default values of the beginDate and endDate parameters: null.
        # *   If the two parameters are set to specific dates, the scheduled auto scaling policy can be triggered during the period between the two dates. For example, if **BeginDate** is set to 2021-03-25 and **EndDate** is set to 2021-04-25, the auto scaling policy is valid for one month.
        self.begin_date = begin_date
        # The end date of the validity period of the scheduled auto scaling policy. Take note of the following rules:
        # 
        # *   If **BeginDate** and **EndDate** are set to **null**, the auto scaling policy is a long-term policy. Default values of the beginDate and endDate parameters: null.
        # *   If the two parameters are set to specific dates, the scheduled auto scaling policy can be triggered during the period between the two dates. For example, if **BeginDate** is set to 2021-03-25 and **EndDate** is set to 2021-04-25, the auto scaling policy is valid for one month.
        self.end_date = end_date
        # The frequency at which the scheduled auto scaling policy is executed. Valid values:
        # 
        # *   **\\* \\* \\***: The scheduled auto scaling policy is executed at a specified point in time every day.
        # 
        # *   **\\* \\* Fri,Mon**: The scheduled auto scaling policy is executed at a specified point in time on one or more days of each week. GMT+8 is used. Valid values:
        # 
        #     *   **Sun**
        #     *   **Mon**
        #     *   **Tue**
        #     *   **Wed**
        #     *   **Thu**
        #     *   **Fri**
        #     *   **Sat**
        # 
        # *   **1,2,3,28,31 \\* \\***: The scheduled auto scaling policy is executed at a specified point in time on one or more days of each month. Valid values: 1 to 31. If the month does not have a 31st day, the auto scaling policy is executed on the specified days other than the 31st day.
        self.period = period
        # The points in time at which the auto scaling policy is triggered within one day.
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
        # The point in time. Format: **Hour:Minute**.
        self.at_time = at_time
        self.max_replicas = max_replicas
        self.min_replicas = min_replicas
        # The expected number of instances.
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
        # The metrics that are used to trigger the auto scaling policy.
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
        # The limit on the metric.
        # 
        # *   The limit on the CPU utilization. Unit: percentage.
        # *   The limit on the memory usage. Unit: percentage.
        # *   The limit on the average number of active TCP connections per second.
        # *   The limit on the QPS of the Internet-facing SLB instance.
        # *   The limit on the response time of the Internet-facing SLB instance. Unit: milliseconds.
        self.metric_target_average_utilization = metric_target_average_utilization
        # The metric that is used to trigger the auto scaling policy. Valid values:
        # 
        # *   **CPU**: the CPU utilization.
        # *   **MEMORY**: the memory usage.
        # *   **tcpActiveConn**: the average number of active TCP connections of an application instance within 30 seconds.
        # *   **SLB_QPS**: the average QPS of the Internet-facing SLB instance associated with an application instance within 15 seconds.
        # *   **SLB_RT**: the average response time of the Internet-facing SLB instance within 15 seconds.
        self.metric_type = metric_type
        self.slb_id = slb_id
        self.slb_logstore = slb_logstore
        self.slb_project = slb_project
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

