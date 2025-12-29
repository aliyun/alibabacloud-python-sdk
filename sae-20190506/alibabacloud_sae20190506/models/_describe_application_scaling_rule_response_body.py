# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationScalingRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationScalingRuleResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        # The data returned.
        self.data = data
        self.error_code = error_code
        self.message = message
        # The ID of the request.
        self.request_id = request_id
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
            temp_model = main_models.DescribeApplicationScalingRuleResponseBodyData()
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

class DescribeApplicationScalingRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        last_disable_time: int = None,
        metric: main_models.DescribeApplicationScalingRuleResponseBodyDataMetric = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: main_models.DescribeApplicationScalingRuleResponseBodyDataTimer = None,
        update_time: int = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The time when the auto scaling policy was created. Unit: milliseconds.
        self.create_time = create_time
        # The time when the auto scaling policy was last disabled.
        self.last_disable_time = last_disable_time
        # The details of the metric-based auto scaling policy.
        self.metric = metric
        # The ratio of the minimum number of available instances to the current number of instances. Valid values:
        # 
        # *   **-1** (default value): The minimum number of available instances is not determined based on this parameter.
        # *   **0 to 100**: The minimum number of available instances is calculated by using the following formula: Number of existing instances × Value of MinReadyInstanceRatio × 100%. The calculation result is rounded up to the nearest integer. For example, if the number of existing instances is 5 and MinReadyInstanceRatio is set to 50, the minimum number of available instances is 3.
        # 
        # >  If the **MinReadyInstanceRatio** and **MinReadyInstanceRatio** parameters are configured and the **MinReadyInstanceRatio** parameter is set to a number from 0 to 100, the value of the MinReadyInstanceRatio parameter takes precedence. For example, if the **MinReadyInstances** parameter is set to **5**, and the **MinReadyInstanceRatio** parameter is set to **50**, the minimum number of available instances is set to the nearest integer rounded up from the calculated result of the following formula: Nmber of existing instances × **50**.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Valid values:
        # 
        # *   If you set the value to **0**, business is interrupted when the application is updated.
        # *   If you set this property to -1, the system calculates a recommended value as the minimum number of available instances by using the following formula: Recommended value = Number of existing instances × 25%. The calculation result is rounded up to the nearest integer. For example, if the number of existing instances is 5, the recommended value is calculated by using the following formula: 5 × 25% = 1.25. In this case, the minimum number of available instances is 2.
        # 
        # >  To ensure business continuity, make sure that at least one instance is available during application deployment and rollback.
        self.min_ready_instances = min_ready_instances
        # Indicates whether the auto scaling policy is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.scale_rule_enabled = scale_rule_enabled
        # The name of the auto scaling policy.
        self.scale_rule_name = scale_rule_name
        # The type of the auto scaling policy. Valid values:
        # 
        # *   **timing**: the scheduled auto scaling policy.
        # *   **metric**: the metric-based auto scaling policy.
        # *   **mix**: the hybrid auto scaling policy.
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

        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time

        if self.metric is not None:
            result['Metric'] = self.metric.to_map()

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

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

        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')

        if m.get('Metric') is not None:
            temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m.get('Metric'))

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')

        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')

        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')

        if m.get('Timer') is not None:
            temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m.get('Timer'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeApplicationScalingRuleResponseBodyDataTimer(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[main_models.DescribeApplicationScalingRuleResponseBodyDataTimerSchedules] = None,
    ):
        # The start date of the validity period of the scheduled auto scaling policy. Valid values:
        # 
        # *   If both the **BeginDate** and **EndDate** parameters are set to **null**, the auto scaling policy can always be triggered. The default value for these parameters is null.
        # *   If the two parameters are set to specific dates, the scheduled auto scaling policy can be triggered during the period between the two dates. For example, if **BeginDate** is **2021-03-25** and **EndDate** is **2021-04-25**, the auto scaling policy is valid for one month.
        self.begin_date = begin_date
        # The end date of the validity period of the scheduled auto scaling policy. Valid values:
        # 
        # *   If both the **BeginDate** and **EndDate** parameters are set to **null**, the auto scaling policy can always be triggered. The default value for these parameters is null.
        # *   If the two parameters are set to specific dates, the scheduled auto scaling policy can be triggered during the period between the two dates. For example, if **BeginDate** is **2021-03-25** and **EndDate** is **2021-04-25**, the auto scaling policy is valid for one month.
        self.end_date = end_date
        # The days on which the scheduled auto scaling policy takes effect. Valid values:
        # 
        # *   **\\* \\* \\***: The scheduled auto scaling policy takes effect at a specified time every day.
        # 
        # *   **\\* \\* Fri,Mon**: The scheduled auto scaling policy takes effect at a specified time on one or multiple days of a week. The specified time is in the GMT+8 time zone. Valid values:
        # 
        #     *   **Sun**: Sunday
        #     *   **Mon**: Monday
        #     *   **Tue**: Tuesday
        #     *   **Wed**: Wednesday
        #     *   **Thu**: Thursday
        #     *   **Fri**: Friday
        #     *   **Sat**: Saturday
        # 
        # *   **1,2,3,28,31 \\* \\***: The scheduled auto scaling policy takes effect at a specified time on one or multiple days of a month. Valid values: 1 to 31. If the month does not have a 31st day, the auto scaling policy takes effect on the specified days other than the 31st day.
        self.period = period
        # The points in time when the auto scaling policy is triggered within one day.
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
                temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k1))

        return self

class DescribeApplicationScalingRuleResponseBodyDataTimerSchedules(DaraModel):
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

class DescribeApplicationScalingRuleResponseBodyDataMetric(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetrics] = None,
        metrics_status: main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus = None,
        min_replicas: int = None,
        scale_down_rules: main_models.DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules = None,
        scale_up_rules: main_models.DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules = None,
    ):
        # The maximum number of instances.
        self.max_replicas = max_replicas
        # The list of metrics that are used to trigger the auto scaling policy.
        self.metrics = metrics
        # The execution status of the metric-based auto scaling policy.
        self.metrics_status = metrics_status
        # The minimum number of instances.
        self.min_replicas = min_replicas
        # Rules that determine the application scale-in.
        self.scale_down_rules = scale_down_rules
        # Rules that determine the application scale-out.
        self.scale_up_rules = scale_up_rules

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.metrics_status:
            self.metrics_status.validate()
        if self.scale_down_rules:
            self.scale_down_rules.validate()
        if self.scale_up_rules:
            self.scale_up_rules.validate()

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

        if self.metrics_status is not None:
            result['MetricsStatus'] = self.metrics_status.to_map()

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        if self.scale_down_rules is not None:
            result['ScaleDownRules'] = self.scale_down_rules.to_map()

        if self.scale_up_rules is not None:
            result['ScaleUpRules'] = self.scale_up_rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('MetricsStatus') is not None:
            temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus()
            self.metrics_status = temp_model.from_map(m.get('MetricsStatus'))

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        if m.get('ScaleDownRules') is not None:
            temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules()
            self.scale_down_rules = temp_model.from_map(m.get('ScaleDownRules'))

        if m.get('ScaleUpRules') is not None:
            temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules()
            self.scale_up_rules = temp_model.from_map(m.get('ScaleUpRules'))

        return self

class DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        # Indicates whether the application scale-in is disabled. Valid values:
        # 
        # *   **true**: The application scale-in is disabled.
        # *   **false**: The application scale-in is enabled.
        # 
        # >  When this parameter is set to true, the application instances are never reduced. This prevents risks to your business in peak hours. By default, this parameter is set to false.
        self.disabled = disabled
        # The cooldown time of the scale-out. Valid values: 0 to 3600. Unit: seconds. Default value: 0.
        self.stabilization_window_seconds = stabilization_window_seconds
        # The step size for the scale-out. The maximum number of instances that can be added within a specific period of time.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        # Indicates whether the application scale-in is disabled. Valid values:
        # 
        # *   **true**: disabled.
        # *   **false**: enabled.
        # 
        # >  When this parameter is set to true, the application instances are never reduced. This prevents risks to your business in peak hours. By default, this parameter is set to false.
        self.disabled = disabled
        # The cooldown time of the scale-in. Valid values: 0 to 3600. Unit: seconds. Default value: 0.
        self.stabilization_window_seconds = stabilization_window_seconds
        # The step size for the scale-in. The maximum number of instances that can be reduced within a specific period of time.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus(DaraModel):
    def __init__(
        self,
        current_metrics: List[main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics] = None,
        current_replicas: int = None,
        desired_replicas: int = None,
        last_scale_time: str = None,
        next_scale_metrics: List[main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics] = None,
        next_scale_time_period: int = None,
    ):
        # The metrics that is used to trigger the current auto scaling policy.
        self.current_metrics = current_metrics
        # The current number of instances.
        self.current_replicas = current_replicas
        # The expected number of instances.
        self.desired_replicas = desired_replicas
        # The time when the auto scaling policy was last triggered.
        self.last_scale_time = last_scale_time
        # The metrics that are used to trigger the auto scaling policy next time.
        self.next_scale_metrics = next_scale_metrics
        # The duration for which the metric-based auto scaling policy takes effect next time.
        self.next_scale_time_period = next_scale_time_period

    def validate(self):
        if self.current_metrics:
            for v1 in self.current_metrics:
                 if v1:
                    v1.validate()
        if self.next_scale_metrics:
            for v1 in self.next_scale_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k1 in self.current_metrics:
                result['CurrentMetrics'].append(k1.to_map() if k1 else None)

        if self.current_replicas is not None:
            result['CurrentReplicas'] = self.current_replicas

        if self.desired_replicas is not None:
            result['DesiredReplicas'] = self.desired_replicas

        if self.last_scale_time is not None:
            result['LastScaleTime'] = self.last_scale_time

        result['NextScaleMetrics'] = []
        if self.next_scale_metrics is not None:
            for k1 in self.next_scale_metrics:
                result['NextScaleMetrics'].append(k1.to_map() if k1 else None)

        if self.next_scale_time_period is not None:
            result['NextScaleTimePeriod'] = self.next_scale_time_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k1 in m.get('CurrentMetrics'):
                temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k1))

        if m.get('CurrentReplicas') is not None:
            self.current_replicas = m.get('CurrentReplicas')

        if m.get('DesiredReplicas') is not None:
            self.desired_replicas = m.get('DesiredReplicas')

        if m.get('LastScaleTime') is not None:
            self.last_scale_time = m.get('LastScaleTime')

        self.next_scale_metrics = []
        if m.get('NextScaleMetrics') is not None:
            for k1 in m.get('NextScaleMetrics'):
                temp_model = main_models.DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics()
                self.next_scale_metrics.append(temp_model.from_map(k1))

        if m.get('NextScaleTimePeriod') is not None:
            self.next_scale_time_period = m.get('NextScaleTimePeriod')

        return self

class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics(DaraModel):
    def __init__(
        self,
        name: str = None,
        next_scale_in_average_utilization: int = None,
        next_scale_out_average_utilization: int = None,
    ):
        # The name of the metric.
        # 
        # *   **cpu**: the CPU utilization.
        # *   **memory**: the memory usage.
        # *   **tcpActiveConn**: the number of active TCP connections.
        # *   **slb_incall_qps**: the QPS of the Internet-facing SLB instance.
        # *   **slb_incall_rt**: the response time of the Internet-facing SLB instance.
        self.name = name
        # The metric value as a percentage that triggers the application scale-in next time.
        self.next_scale_in_average_utilization = next_scale_in_average_utilization
        # The metric value as a percentage that triggers the application scale-out next time.
        self.next_scale_out_average_utilization = next_scale_out_average_utilization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.next_scale_in_average_utilization is not None:
            result['NextScaleInAverageUtilization'] = self.next_scale_in_average_utilization

        if self.next_scale_out_average_utilization is not None:
            result['NextScaleOutAverageUtilization'] = self.next_scale_out_average_utilization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextScaleInAverageUtilization') is not None:
            self.next_scale_in_average_utilization = m.get('NextScaleInAverageUtilization')

        if m.get('NextScaleOutAverageUtilization') is not None:
            self.next_scale_out_average_utilization = m.get('NextScaleOutAverageUtilization')

        return self

class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics(DaraModel):
    def __init__(
        self,
        current_value: int = None,
        name: str = None,
        type: str = None,
    ):
        # The current value of the metric.
        self.current_value = current_value
        # The name of the metric.
        # 
        # *   **cpu**: the CPU utilization.
        # *   **memory**: the memory usage.
        # *   **tcpActiveConn**: the number of active TCP connections.
        # *   **slb_incall_qps**: the QPS of the Internet-facing SLB instance.
        # *   **slb_incall_rt**: the response time of the Internet-facing SLB instance.
        self.name = name
        # The type of the data. This parameter corresponds to the metric.
        # 
        # *   **Resource**: used when the metric is the **CPU utilization** or **memory usage**.
        # *   **Pods**: used when the metric is the **number of active TCP connections**.
        # *   **External**: used when the metric is about the **SLB** instance or from **Application Real-Time Monitoring Service (ARMS)**.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeApplicationScalingRuleResponseBodyDataMetricMetrics(DaraModel):
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
        # *   **tcpActiveConn**: the average number of active TCP connections for an instance in 30 seconds.
        # *   **SLB_QPS**: the average QPS of the Internet-facing SLB instance associated with an application instance in 15 seconds.
        # *   **SLB_RT**: the average response time of the Internet-facing SLB instance in 15 seconds.
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

