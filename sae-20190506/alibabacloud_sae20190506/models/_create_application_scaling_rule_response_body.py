# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationScalingRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateApplicationScalingRuleResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code or the error code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The returned result.
        self.data = data
        # The status code. Value values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The message returned. The following limits are imposed on the ID:
        # 
        # *   If the request was successful, **success** is returned.
        # *   An error code is returned when a request failed.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the application instances were restarted. Valid values:
        # 
        # *   **true**: The application instances were restarted.
        # *   **false**: The application instances failed to be restarted.
        self.success = success
        # The ID of the trace. The ID is used to query the details of a request.
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
            temp_model = main_models.CreateApplicationScalingRuleResponseBodyData()
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

class CreateApplicationScalingRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        enable_idle: bool = None,
        last_disable_time: int = None,
        metric: main_models.CreateApplicationScalingRuleResponseBodyDataMetric = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: main_models.CreateApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        # null
        self.app_id = app_id
        # null null
        self.create_time = create_time
        self.enable_idle = enable_idle
        # null
        self.last_disable_time = last_disable_time
        # The details of the metric-based auto scaling policy.
        self.metric = metric
        # null null
        # 
        # *   **null**
        # *   **null**
        self.scale_rule_enabled = scale_rule_enabled
        # The name of the auto scaling policy.
        self.scale_rule_name = scale_rule_name
        # null null
        # 
        # *   **null**
        # *   **metric**: a metric-based auto scaling policy.
        # *   **mix**: a hybrid auto scaling policy.
        self.scale_rule_type = scale_rule_type
        # The details of the scheduled auto scaling policy.
        self.timer = timer
        # null null
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
            temp_model = main_models.CreateApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m.get('Metric'))

        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')

        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')

        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')

        if m.get('Timer') is not None:
            temp_model = main_models.CreateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m.get('Timer'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class CreateApplicationScalingRuleResponseBodyDataTimer(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[main_models.CreateApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        # The start date of the validity period of the scheduled auto scaling policy.
        # 
        # *   **null** (default): If you set **BeginDate** and **EndDate** to null, the scheduled auto scaling policy can always be triggered.
        # *   If the two parameters are set to specific dates, the scheduled auto scaling policy can be triggered during the period between the two dates. For example, if **BeginDate** is set to 2021-03-25 and **EndDate** is set to 2021-04-25, the auto scaling policy is valid for one month.
        self.begin_date = begin_date
        # The end date of the validity period of the scheduled auto scaling policy.
        # 
        # *   **null** (default): If you set **BeginDate** and **EndDate** to null, the scheduled auto scaling policy can always be triggered.
        # *   If the two parameters are set to specific dates, the scheduled auto scaling policy can be triggered during the period between the two dates. For example, if **BeginDate** is set to 2021-03-25 and **EndDate** is set to 2021-04-25, the auto scaling policy is valid for one month.
        self.end_date = end_date
        # The days on which the scheduled auto scaling policy takes effect. Valid values:
        # 
        # *   **\\* \\* \\***: The scheduled auto scaling policy is executed at a specified point in time every day.
        # 
        # *   **\\* \\* Fri,Mon**: The scheduled auto scaling policy is executed at a specified point in time on one or more days every week. The time must be in GMT+8. Valid values:
        # 
        #     *   **Sun**: Sunday
        #     *   **Mon**: Monday
        #     *   **Tue**: Tuesday
        #     *   **Wed**: Wednesday
        #     *   **Thu**: Thursday
        #     *   **Fri**: Friday
        #     *   **Sat**: Saturday
        # 
        # *   **1,2,3,28,31 \\* \\***: The scheduled auto scaling policy is executed at a specified point in time on one or more dates of each month. Valid values: 1 to 31. If a month does not have the 31st day, the auto scaling policy is executed on the specified days other than the 31st day.
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
                temp_model = main_models.CreateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k1))

        return self

class CreateApplicationScalingRuleResponseBodyDataTimerSchedules(DaraModel):
    def __init__(
        self,
        at_time: str = None,
        max_replicas: int = None,
        min_replicas: int = None,
        target_replicas: int = None,
    ):
        # The point in time. Format: **Hour:Minute**.
        self.at_time = at_time
        # The maximum number of instances.
        self.max_replicas = max_replicas
        # The minimum number of instances.
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

class CreateApplicationScalingRuleResponseBodyDataMetric(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[main_models.CreateApplicationScalingRuleResponseBodyDataMetricMetrics] = None,
        min_replicas: int = None,
    ):
        # The maximum number of Elastic Compute Service (ECS) instances supported by the node pool.
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
                temp_model = main_models.CreateApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        return self

class CreateApplicationScalingRuleResponseBodyDataMetricMetrics(DaraModel):
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
        # *   The limit on the queries per second (QPS). Unit: seconds.
        # *   The limit on the response time. Unit: milliseconds.
        # *   The limit on the average number of active TCP connections per second.
        # *   The limit on the QPS of the Internet-facing SLB instance.
        # *   The limit on the response time of the Internet-facing SLB instance. Unit: milliseconds.
        # *   The limit on the QPS of the internal-facing SLB instance.
        # *   The limit on the response time of the internal-facing SLB instance. Unit: milliseconds.
        self.metric_target_average_utilization = metric_target_average_utilization
        # The metric that is used to trigger the auto scaling policy. Valid values:
        # 
        # *   **CPU**: the CPU utilization.
        # *   **MEMORY**: the memory usage.
        # *   **QPS**: the average QPS within 1 minute per Java application instance.
        # *   **RT**: the average response time of all API operations within 1 minute in the Java application.
        # *   **tcpActiveConn**: the average number of active TCP connections within 30 seconds per instance.
        # *   **SLB_QPS**: the average QPS of the Internet-facing SLB instance within 15 seconds per instance.
        # *   **SLB_RT**: the average response time of the Internet-facing SLB instance within 15 seconds.
        # *   **INTRANET_SLB_QPS**: the average QPS of the internal-facing SLB instance within 15 seconds per instance.
        # *   **INTRANET_SLB_RT**: the average response time of the internal-facing SLB instance within 15 seconds.
        self.metric_type = metric_type
        # The ID of the SLB instance.
        self.slb_id = slb_id
        # The Logstore that stores the SLB access logs.
        self.slb_logstore = slb_logstore
        # The project that stores the SLB access logs.
        self.slb_project = slb_project
        # The port number of the SLB instance.
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

