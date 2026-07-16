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
        # The HTTP status code or a POP error code. Valid values:
        # 
        # - **2xx**: The operation is successful.
        # 
        # - **3xx**: A redirection is required.
        # 
        # - **4xx**: A request error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The returned data.
        self.data = data
        # The error code. Valid values:
        # 
        # - If the request is successful, the **ErrorCode** field is not returned.
        # 
        # - If the request fails, the **ErrorCode** field is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The additional information. Valid values:
        # 
        # - If the request is successful, **success** is returned.
        # 
        # - If the request fails, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the application instance was successfully restarted.
        # 
        # - **true**: The restart succeeded.
        # 
        # - **false**: The restart failed.
        self.success = success
        # The trace ID. Use this ID to query the details of a request.
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
        # The application ID.
        self.app_id = app_id
        # The time when the auto scaling policy was created. Unit: milliseconds.
        self.create_time = create_time
        # The time when the auto scaling policy was last disabled.
        self.last_disable_time = last_disable_time
        # The metric-based scaling policy.
        self.metric = metric
        # The percentage of the minimum number of ready instances. Valid values:
        # 
        # - **-1**: an initial value, which indicates that a percentage is not used.
        # 
        # - **0 to 100**: a percentage that is rounded up. For example, if you set this parameter to 50% and the current number of instances is 5, the minimum number of ready instances is 3.
        # 
        # > If you specify both MinReadyInstances and MinReadyInstanceRatio, and the value of **MinReadyInstanceRatio** is not **-1**, the value of **MinReadyInstanceRatio** prevails. For example, if **MinReadyInstances** is set to **5** and **MinReadyInstanceRatio** is set to **50**, the value **50** is used to calculate the minimum number of ready instances.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of ready instances. Valid values:
        # 
        # - If you set this parameter to **0**, the application is interrupted during an upgrade.
        # 
        # - If you set this parameter to -1, the system uses a recommended value for the minimum number of ready instances. The value is 25% of the current number of instances. For example, if the current number of instances is 5, the minimum number of ready instances is 2 after 5 × 25% = 1.25 is rounded up.
        # 
        # > Set the minimum number of ready instances to a value greater than or equal to 1 for each rolling deployment to ensure business continuity.
        self.min_ready_instances = min_ready_instances
        # Indicates whether the auto scaling policy is enabled. Valid values:
        # 
        # - **true**: The policy is enabled.
        # 
        # - **false**: The policy is disabled.
        self.scale_rule_enabled = scale_rule_enabled
        # The name of the auto scaling policy.
        self.scale_rule_name = scale_rule_name
        # The type of the auto scaling policy. Valid values:
        # 
        # - **timing**: scheduled scaling.
        # 
        # - **metric**: metric-based scaling.
        # 
        # - **mix**: hybrid scaling.
        self.scale_rule_type = scale_rule_type
        # The scheduled scaling policy.
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
        # The start date of a short-term scheduled scaling policy. The following list describes the valid values:
        # 
        # - If you leave both **BeginDate** and **EndDate** empty, the policy is a long-term policy. This is the default value.
        # 
        # - If you specify a date, for example, you set **BeginDate** to **2021-03-25** and **EndDate** to **2021-04-25**, the policy is effective for one month.
        self.begin_date = begin_date
        # The end date of a short-term scheduled scaling policy. The following list describes the valid values:
        # 
        # - If you leave both **BeginDate** and **EndDate** empty, the policy is a long-term policy. This is the default value.
        # 
        # - If you specify a date, for example, you set **BeginDate** to **2021-03-25** and **EndDate** to **2021-04-25**, the policy is effective for one month.
        self.end_date = end_date
        # The period in which the scheduled scaling policy is executed. Valid values:
        # 
        # - **\\* \\* \\***: The policy is executed at a specified time every day.
        # 
        # - **\\* \\* Fri,Mon**: The policy is executed at a specified time on one or more days of a week. You can select multiple days. The time is in GMT+8. Valid values:
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
        # - **1,2,3,28,31 \\* \\***: The policy is executed at a specified time on one or more days of a month. You can select multiple days. The value can be an integer from 1 to 31. If a month does not have a 31st day, the policy is not executed on that day.
        self.period = period
        # The points in time when the auto scaling policy is triggered within a day.
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
        # The point in time. Format: **HH:mm**.
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
        # The list of metric-based scaling policies.
        self.metrics = metrics
        # The status of the metric-based scaling policy.
        self.metrics_status = metrics_status
        # The minimum number of instances.
        self.min_replicas = min_replicas
        # The scale-in rules.
        self.scale_down_rules = scale_down_rules
        # The scale-out rules.
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
        # Indicates whether scale-in is disabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        # 
        # > If you enable this feature, the application is never scaled in. This prevents business risks that are caused by scale-ins during peak hours. By default, this feature is disabled.
        self.disabled = disabled
        # The cooldown period for scale-outs. The value can be an integer from 0 to 3600. Unit: seconds. Default value: 0.
        self.stabilization_window_seconds = stabilization_window_seconds
        # The scaling step size for scale-outs. The maximum number of instances that can be added at a time.
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
        # Indicates whether scale-in is disabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        # 
        # > If you enable this feature, the application is never scaled in. This prevents business risks that are caused by scale-ins during peak hours. By default, this feature is disabled.
        self.disabled = disabled
        # The cooldown period for scale-ins. The value can be an integer from 0 to 3600. Unit: seconds. Default value: 0.
        self.stabilization_window_seconds = stabilization_window_seconds
        # The scaling step size for scale-ins. The maximum number of instances that can be removed at a time.
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
        # The data of the current metric-based scaling.
        self.current_metrics = current_metrics
        # The current number of instances.
        self.current_replicas = current_replicas
        # The target number of instances.
        self.desired_replicas = desired_replicas
        # The time of the last scaling activity.
        self.last_scale_time = last_scale_time
        # The list of metrics for the next scaling activity.
        self.next_scale_metrics = next_scale_metrics
        # The period of the next metric-based scaling.
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
        # - **cpu**: CPU utilization.
        # 
        # - **memory**: memory usage.
        # 
        # - **arms_incall_qps**: the average QPS of a single instance of a Java application in one minute.
        # 
        # - **arms_incall_rt**: the average RT of all service interfaces of a Java application in one minute.
        # 
        # - **tcpActiveConn**: the number of active TCP connections.
        # 
        # - **slb_incall_qps**: the QPS of a public-facing SLB instance.
        # 
        # - **slb_incall_rt**: the RT of a public-facing SLB instance.
        # 
        # - **intranet_slb_incall_qps**: the QPS of a private SLB instance.
        # 
        # - **intranet_slb_incall_rt**: the RT of a private SLB instance.
        self.name = name
        # The metric threshold for the next scale-in. The value is a percentage.
        self.next_scale_in_average_utilization = next_scale_in_average_utilization
        # The metric threshold for the next scale-out. The value is a percentage.
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
        # The current value.
        self.current_value = current_value
        # The name of the metric.
        # 
        # - **cpu**: CPU utilization.
        # 
        # - **memory**: memory usage.
        # 
        # - **arms_incall_qps**: the average QPS of a single instance of a Java application in one minute.
        # 
        # - **arms_incall_rt**: the average RT of all service interfaces of a Java application in one minute.
        # 
        # - **tcpActiveConn**: the number of active TCP connections.
        # 
        # - **slb_incall_qps**: the QPS of a public-facing SLB instance.
        # 
        # - **slb_incall_rt**: the RT of a public-facing SLB instance.
        # 
        # - **intranet_slb_incall_qps**: the QPS of a private SLB instance.
        # 
        # - **intranet_slb_incall_rt**: the RT of a private SLB instance.
        self.name = name
        # The type of the metric. This parameter is associated with the monitoring metric.
        # 
        # - **Resource**: the metric value of **cpu** or **memory**.
        # 
        # - **Pods**: the metric value of **tcpActiveConn**.
        # 
        # - **External**: the metric value of **arms** or **slb**.
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
        # The target value of the metric.
        # 
        # - The target CPU utilization. Unit: percent.
        # 
        # - The target memory usage. Unit: percent.
        # 
        # - The number of queries per second (QPS).
        # 
        # - The response time. Unit: milliseconds.
        # 
        # - The average number of active TCP connections per second.
        # 
        # - The QPS of a public-facing SLB instance.
        # 
        # - The response time of a public-facing SLB instance. Unit: milliseconds.
        # 
        # - The QPS of a private SLB instance.
        # 
        # - The response time of a private SLB instance. Unit: milliseconds.
        self.metric_target_average_utilization = metric_target_average_utilization
        # The metric that is used to trigger the auto scaling policy. Valid values:
        # 
        # - **CPU**: CPU utilization.
        # 
        # - **MEMORY**: memory usage.
        # 
        # - **QPS**: the average QPS of a single instance of a Java application in one minute.
        # 
        # - **RT**: the average response time (RT) of all service interfaces of a Java application in one minute.
        # 
        # - **tcpActiveConn**: the average number of active TCP connections of a single instance in 30 seconds.
        # 
        # - **SLB_QPS**: the average QPS of a single instance for a public-facing SLB instance in 15 seconds.
        # 
        # - **SLB_RT**: the average RT of a public-facing SLB instance in 15 seconds.
        # 
        # - **INTRANET_SLB_QPS**: the average QPS of a single instance for a private SLB instance in 15 seconds.
        # 
        # - **INTRANET_SLB_RT**: the average RT of a private SLB instance in 15 seconds.
        self.metric_type = metric_type
        # The ID of the SLB instance.
        self.slb_id = slb_id
        # The SLB access log Logstore.
        self.slb_logstore = slb_logstore
        # The SLB access log Project.
        self.slb_project = slb_project
        # The port of the SLB instance.
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

