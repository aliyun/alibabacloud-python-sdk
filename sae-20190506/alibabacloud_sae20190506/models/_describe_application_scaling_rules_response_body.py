# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationScalingRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationScalingRulesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: The request was invalid.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The returned data.
        self.data = data
        # The error code. This parameter is returned only when the request fails.
        # 
        # -
        # 
        # - For more information, see the **Error codes** section of this topic.
        self.error_code = error_code
        # The response message. Valid values:
        # 
        # - Returns **success** if the request is successful.
        # 
        # - Returns an error message if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # 
        # - **false**: The call failed.
        self.success = success
        # The trace ID used to query the details of a request.
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
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyData()
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

class DescribeApplicationScalingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        application_scaling_rules: List[main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # A list of auto scaling policies for the application.
        self.application_scaling_rules = application_scaling_rules
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of auto scaling policies for the application.
        self.total_size = total_size

    def validate(self):
        if self.application_scaling_rules:
            for v1 in self.application_scaling_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationScalingRules'] = []
        if self.application_scaling_rules is not None:
            for k1 in self.application_scaling_rules:
                result['ApplicationScalingRules'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_scaling_rules = []
        if m.get('ApplicationScalingRules') is not None:
            for k1 in m.get('ApplicationScalingRules'):
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules()
                self.application_scaling_rules.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        last_disable_time: int = None,
        metric: main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        timer: main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer = None,
        update_time: int = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The timestamp of the policy\\"s creation, in milliseconds.
        self.create_time = create_time
        # The timestamp of when the policy was last disabled.
        self.last_disable_time = last_disable_time
        # The metric-based scaling policy.
        self.metric = metric
        # The minimum number of available instances, specified as a percentage. Valid values:
        # 
        # - **-1**: Indicates that this parameter is not used.
        # 
        # - **0 to 100**: a percentage that is rounded up to the nearest integer. For example, if you set this parameter to 50% and you have five instances, the minimum number of available instances is 3.
        # 
        # > If you specify both **MinReadyInstances** and **MinReadyInstanceRatio**, the value of **MinReadyInstanceRatio** takes precedence, unless it is set to **-1**.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Valid values:
        # 
        # - If you set this parameter to **0**, the application may be interrupted during an upgrade.
        # 
        # - If you set this parameter to **-1**, a recommended value is used, which is 25% of the current number of instances, rounded up to the nearest integer. For example, if an application has five instances, the minimum number of available instances is 2 (5 \\* 25% = 1.25, rounded up).
        # 
        # > To ensure business continuity during a rolling deployment, we recommend that you set this parameter to a value greater than or equal to 1.
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
        # - **timing**: A scheduled scaling policy.
        # 
        # - **metric**: A metric-based scaling policy.
        # 
        # - **mix**: A hybrid scaling policy.
        self.scale_rule_type = scale_rule_type
        # The scheduled scaling policy.
        self.timer = timer
        # The timestamp of the last policy update, in milliseconds.
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
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric()
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
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer()
            self.timer = temp_model.from_map(m.get('Timer'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        period: str = None,
        schedules: List[main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules] = None,
        time_zone: str = None,
    ):
        # The start date of the short-term scheduled scaling policy. The following rules apply:
        # 
        # - If **BeginDate** and **EndDate** are not specified, the policy is long-term by default.
        # 
        # - If you specify a `BeginDate` and an `EndDate`, the policy is short-term and applies only within that date range.
        self.begin_date = begin_date
        # The end date of the short-term scheduled scaling policy. The following rules apply:
        # 
        # - If **BeginDate** and **EndDate** are not specified, the policy is long-term by default.
        # 
        # - If you specify a `BeginDate` and an `EndDate`, the policy is short-term and applies only within that date range.
        self.end_date = end_date
        # The days on which the scheduled scaling policy runs. Valid values:
        # 
        # - **\\* \\* \\***: The policy is executed at a specified time every day.
        # 
        # - **\\* \\* Fri,Mon**: Executes the policy on specified days of the week. The time zone is GMT+8. Valid days are listed below:
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
        # - **1,2,3,28,31 \\* \\***: Executes the policy on specified days of the month (1-31). If a specified day does not exist in a given month (e.g., the 31st), the policy does not run on that day.
        self.period = period
        # The daily trigger schedule for the policy.
        self.schedules = schedules
        # The time zone.
        self.time_zone = time_zone

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

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

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
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules()
                self.schedules.append(temp_model.from_map(k1))

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules(DaraModel):
    def __init__(
        self,
        at_time: str = None,
        max_replicas: int = None,
        min_replicas: int = None,
        target_replicas: int = None,
    ):
        # The trigger time in `HH:mm` format.
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

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        metric_source: str = None,
        metrics: List[main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics] = None,
        metrics_status: main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus = None,
        min_replicas: int = None,
        prometheus_metrics: List[main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricPrometheusMetrics] = None,
        prometheus_token: str = None,
        prometheus_url: str = None,
        scale_down_rules: main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules = None,
        scale_up_rules: main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules = None,
    ):
        # The maximum number of instances.
        self.max_replicas = max_replicas
        # The source of the metrics.
        self.metric_source = metric_source
        # The metric-based conditions that trigger scaling.
        self.metrics = metrics
        # The status of the metric-based scaling policy.
        self.metrics_status = metrics_status
        # The minimum number of instances.
        self.min_replicas = min_replicas
        # The Prometheus metrics.
        self.prometheus_metrics = prometheus_metrics
        # The Prometheus token.
        self.prometheus_token = prometheus_token
        # The endpoint of the Prometheus service.
        self.prometheus_url = prometheus_url
        # Configuration for scale-in events.
        self.scale_down_rules = scale_down_rules
        # Configuration for scale-out events.
        self.scale_up_rules = scale_up_rules

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.metrics_status:
            self.metrics_status.validate()
        if self.prometheus_metrics:
            for v1 in self.prometheus_metrics:
                 if v1:
                    v1.validate()
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

        if self.metric_source is not None:
            result['MetricSource'] = self.metric_source

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.metrics_status is not None:
            result['MetricsStatus'] = self.metrics_status.to_map()

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        result['PrometheusMetrics'] = []
        if self.prometheus_metrics is not None:
            for k1 in self.prometheus_metrics:
                result['PrometheusMetrics'].append(k1.to_map() if k1 else None)

        if self.prometheus_token is not None:
            result['PrometheusToken'] = self.prometheus_token

        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url

        if self.scale_down_rules is not None:
            result['ScaleDownRules'] = self.scale_down_rules.to_map()

        if self.scale_up_rules is not None:
            result['ScaleUpRules'] = self.scale_up_rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('MetricSource') is not None:
            self.metric_source = m.get('MetricSource')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('MetricsStatus') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus()
            self.metrics_status = temp_model.from_map(m.get('MetricsStatus'))

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        self.prometheus_metrics = []
        if m.get('PrometheusMetrics') is not None:
            for k1 in m.get('PrometheusMetrics'):
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricPrometheusMetrics()
                self.prometheus_metrics.append(temp_model.from_map(k1))

        if m.get('PrometheusToken') is not None:
            self.prometheus_token = m.get('PrometheusToken')

        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')

        if m.get('ScaleDownRules') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules()
            self.scale_down_rules = temp_model.from_map(m.get('ScaleDownRules'))

        if m.get('ScaleUpRules') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules()
            self.scale_up_rules = temp_model.from_map(m.get('ScaleUpRules'))

        return self

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        # Specifies whether to disable scale-out. Valid values:
        # 
        # - **true**: Disables scale-out.
        # 
        # - **false**: Enables scale-out.
        # 
        # > If this parameter is set to `true`, application instances are never scaled out. This can be useful to freeze the application capacity during specific events. By default, this parameter is set to `false`.
        self.disabled = disabled
        # The cooldown time for scale-out events, in seconds. During this period, no further scaling events are triggered. The value must be an integer from 0 to 3,600. The default value is 0.
        self.stabilization_window_seconds = stabilization_window_seconds
        # The number of instances to add in a single scale-out event.
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

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        stabilization_window_seconds: int = None,
        step: int = None,
    ):
        # Specifies whether to disable scale-in. Valid values:
        # 
        # - **true**: Disables scale-in.
        # 
        # - **false**: Enables scale-in.
        # 
        # > Setting this to `true` prevents the application from scaling in, which can be useful to avoid service disruptions from unexpected capacity reduction during peak hours. Default: `false`.
        self.disabled = disabled
        # The cooldown time for scale-in events, in seconds. During this period, no further scaling events are triggered. The value must be an integer from 0 to 3,600. The default value is 0.
        self.stabilization_window_seconds = stabilization_window_seconds
        # The number of instances to remove in a single scale-in event.
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

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricPrometheusMetrics(DaraModel):
    def __init__(
        self,
        prometheus_query: str = None,
        target_metric_value: str = None,
    ):
        # The Prometheus query.
        self.prometheus_query = prometheus_query
        # The target value for the Prometheus query that triggers a scaling event.
        self.target_metric_value = target_metric_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_query is not None:
            result['PrometheusQuery'] = self.prometheus_query

        if self.target_metric_value is not None:
            result['TargetMetricValue'] = self.target_metric_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrometheusQuery') is not None:
            self.prometheus_query = m.get('PrometheusQuery')

        if m.get('TargetMetricValue') is not None:
            self.target_metric_value = m.get('TargetMetricValue')

        return self

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus(DaraModel):
    def __init__(
        self,
        current_metrics: List[main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics] = None,
        current_replicas: int = None,
        desired_replicas: int = None,
        last_scale_time: str = None,
        max_replicas: int = None,
        min_replicas: int = None,
        next_scale_metrics: List[main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics] = None,
        next_scale_time_period: int = None,
    ):
        # A list of the current metrics for scaling.
        self.current_metrics = current_metrics
        # The current number of instances.
        self.current_replicas = current_replicas
        # The target number of instances.
        self.desired_replicas = desired_replicas
        # The time of the last scaling activity.
        self.last_scale_time = last_scale_time
        # The maximum number of instances.
        self.max_replicas = max_replicas
        # The minimum number of instances.
        self.min_replicas = min_replicas
        # A list of metrics for the next scaling activity.
        self.next_scale_metrics = next_scale_metrics
        # The next period for metric-based scaling.
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

        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

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
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k1))

        if m.get('CurrentReplicas') is not None:
            self.current_replicas = m.get('CurrentReplicas')

        if m.get('DesiredReplicas') is not None:
            self.desired_replicas = m.get('DesiredReplicas')

        if m.get('LastScaleTime') is not None:
            self.last_scale_time = m.get('LastScaleTime')

        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        self.next_scale_metrics = []
        if m.get('NextScaleMetrics') is not None:
            for k1 in m.get('NextScaleMetrics'):
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics()
                self.next_scale_metrics.append(temp_model.from_map(k1))

        if m.get('NextScaleTimePeriod') is not None:
            self.next_scale_time_period = m.get('NextScaleTimePeriod')

        return self

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics(DaraModel):
    def __init__(
        self,
        name: str = None,
        next_scale_in_average_utilization: int = None,
        next_scale_out_average_utilization: int = None,
    ):
        # The name of the trigger condition.
        # 
        # - **cpu**: CPU usage.
        # 
        # - **memory**: memory usage.
        # 
        # - **arms_incall_qps_v2**: QPS of a Java application.
        # 
        # - **arms_incall_rt**: Response time of a Java application.
        # 
        # - **tcpActiveConn**: The number of active TCP connections.
        # 
        # - **slb_incall_qps**: QPS of a public-facing SLB instance.
        # 
        # - **slb_incall_rt**: Response time of a public-facing SLB instance.
        # 
        # - **intranet_slb_incall_qps**: QPS of a private SLB instance.
        # 
        # - **intranet_slb_incall_rt**: Response time of a private SLB instance.
        self.name = name
        # The metric value that triggers the next scale-in event. The value is a percentage.
        self.next_scale_in_average_utilization = next_scale_in_average_utilization
        # The metric value that triggers the next scale-out event. The value is a percentage.
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

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics(DaraModel):
    def __init__(
        self,
        current_value: int = None,
        name: str = None,
        type: str = None,
    ):
        # The current value.
        self.current_value = current_value
        # The name of the trigger condition.
        # 
        # - **cpu**: CPU usage.
        # 
        # - **memory**: memory usage.
        # 
        # - **arms_incall_qps_v2**: QPS of a Java application.
        # 
        # - **arms_incall_rt**: Response time of a Java application.
        # 
        # - **tcpActiveConn**: The number of active TCP connections.
        # 
        # - **slb_incall_qps**: QPS of a public-facing SLB instance.
        # 
        # - **slb_incall_rt**: Response time of a public-facing SLB instance.
        # 
        # - **intranet_slb_incall_qps**: QPS of a private SLB instance.
        # 
        # - **intranet_slb_incall_rt**: Response time of a private SLB instance.
        self.name = name
        # The data type. This parameter is associated with the specified metric.
        # 
        # - **Resource**: The metric value for **cpu** or **memory**.
        # 
        # - **Pods**: The metric value for **tcpActiveConn**.
        # 
        # - **External**: The metric value for **arms** or **slb**.
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

class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics(DaraModel):
    def __init__(
        self,
        metric_target_average_utilization: int = None,
        metric_type: str = None,
        slb_id: str = None,
        slb_logstore: str = None,
        slb_project: str = None,
        vport: str = None,
    ):
        # The target value for the metric. The unit varies based on the value of `MetricType`.
        # 
        # - Target CPU usage, in percent.
        # 
        # - Target memory usage, in percent.
        # 
        # - Target QPS, in queries per second.
        # 
        # - Target response time, in milliseconds.
        # 
        # - Target number of active TCP connections.
        # 
        # - Target QPS of a public-facing SLB instance, in queries per second.
        # 
        # - Target response time of a public-facing SLB instance, in milliseconds.
        # 
        # - Target QPS of a private SLB instance, in queries per second.
        # 
        # - Target response time of a private SLB instance, in milliseconds.
        self.metric_target_average_utilization = metric_target_average_utilization
        # The metric used to trigger the auto scaling policy. Valid values:
        # 
        # - **CPU**: CPU usage.
        # 
        # - **MEMORY**: memory usage.
        # 
        # - **QPS**: Average queries per second (QPS) per instance over a 1-minute period. This metric applies to Java applications only.
        # 
        # - **RT**: Average response time of all service interfaces in a Java application over a 1-minute period.
        # 
        # - **tcpActiveConn**: Average number of active TCP connections per instance over a 30-second period.
        # 
        # - **SLB_QPS**: Average QPS per instance for a public-facing SLB instance over a 15-second period.
        # 
        # - **SLB_RT**: Average response time of a public-facing SLB instance over a 15-second period.
        # 
        # - **INTRANET_SLB_QPS**: Average QPS per instance for a private SLB instance over a 15-second period.
        # 
        # - **INTRANET_SLB_RT**: Average response time of a private SLB instance over a 15-second period.
        self.metric_type = metric_type
        # The ID of the SLB instance.
        self.slb_id = slb_id
        # The Logstore in Log Service that stores SLB access logs.
        self.slb_logstore = slb_logstore
        # The project in Log Service that stores SLB access logs.
        self.slb_project = slb_project
        # The monitored port of the SLB instance.
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

