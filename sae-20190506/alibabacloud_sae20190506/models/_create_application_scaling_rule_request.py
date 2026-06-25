# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationScalingRuleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        enable_idle: bool = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        scaling_rule_enable: bool = None,
        scaling_rule_metric: str = None,
        scaling_rule_name: str = None,
        scaling_rule_timer: str = None,
        scaling_rule_type: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to enable idle mode for the application.
        self.enable_idle = enable_idle
        # The minimum number of ready instances, specified as a percentage of the total number of instances. Valid values:
        # 
        # - **-1**: Indicates that a percentage is not used. In this case, the value of `MinReadyInstances` is used.
        # 
        # - **0\\~100**: A percentage. The result is rounded up. For example, if you set this parameter to 50 (%) and the application has 5 instances, the minimum number of ready instances is 3.
        # 
        # > If you specify both `MinReadyInstances` and a `MinReadyInstanceRatio` other than `-1`, `MinReadyInstanceRatio` takes precedence. For example, if `MinReadyInstances` is set to `5` and `MinReadyInstanceRatio` is set to `50`, the system uses `50` (%) to calculate the minimum number of ready instances.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of ready instances. Valid values:
        # 
        # - If you set this parameter to `0`, the application is interrupted during an update.
        # 
        # - If you set this parameter to `-1`, the system sets the value to 25% of the current number of instances, rounded up. For example, if the application has 5 instances, the minimum number of ready instances is 2 (5 × 25% = 1.25, rounded up to 2).
        # 
        # > To ensure service continuity during a rolling deployment, we recommend setting the minimum number of ready instances to 1 or more.
        self.min_ready_instances = min_ready_instances
        # Specifies whether to enable the auto scaling policy. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.scaling_rule_enable = scaling_rule_enable
        # Configurations for the metric-based auto scaling policy. This parameter is required if `ScalingRuleType` is set to `metric` or `mix`.
        # 
        # The parameter is a JSON string that contains the following fields:
        # 
        # - **maxReplicas**: The maximum number of application instances.
        # 
        # - **minReplicas**: The minimum number of application instances.
        # 
        # - **metricType**: The metric that triggers the auto scaling policy. Valid values:
        # 
        #   - **CPU**: CPU utilization.
        # 
        #   - **MEMORY**: Memory utilization.
        # 
        #   - **QPS**: The average queries per second (QPS) per instance for a Java application over a 1-minute period.
        # 
        #   - **RT**: The average response time (RT) of all service interfaces for a Java application over a 1-minute period.
        # 
        #   - **tcpActiveConn**: The average number of active TCP connections per instance over a 30-second period.
        # 
        #   - **SLB_QPS**: The average QPS per instance for a public-facing SLB instance over a 15-second period.
        # 
        #   - **SLB_RT**: The average RT of a public-facing SLB instance over a 15-second period.
        # 
        #   - **INTRANET_SLB_QPS**: The average QPS per instance for an internal-facing SLB instance over a 15-second period.
        # 
        #   - **INTRANET_SLB_RT**: The average RT of an internal-facing SLB instance over a 15-second period.
        # 
        # - **metricTargetAverageUtilization**: The target value for the metric specified by `metricType`. The unit of this value depends on `metricType`.
        # 
        #   - Target CPU utilization, in percentage.
        # 
        #   - Target memory utilization, in percentage.
        # 
        #   - Target QPS, in requests per second.
        # 
        #   - Target response time, in milliseconds.
        # 
        #   - Average number of active TCP connections.
        # 
        #   - Target public-facing SLB QPS, in requests per second.
        # 
        #   - Target public-facing SLB response time, in milliseconds.
        # 
        #   - Target internal-facing SLB QPS, in requests per second.
        # 
        #   - Target internal-facing SLB response time, in milliseconds.
        # 
        # - **slbId**: The SLB instance ID.
        # 
        # - **slbProject**: The Log Service project.
        # 
        # - **slbLogstore**: The Log Service Logstore.
        # 
        # - **vport**: The SLB listener port. The HTTP and HTTPS protocols are supported.
        # 
        # - **scaleUpRules**: The rules to scale out the application.
        # 
        # - **scaleDownRules**: The rules to scale in the application.
        # 
        # - **step**: The step size for scaling out or scaling in. This is the maximum number of instances that can be added or removed in a single scaling activity.
        # 
        # - **disabled**: Specifies whether to prevent the application from scaling in. If set to `true`, the number of application instances is never reduced. This can prevent business risks caused by scaling in during peak hours.
        # 
        #   - **true**: Scale-in is disabled.
        # 
        #   - **false**: Scale-in is enabled. This is the default value.
        # 
        # - **stabilizationWindowSeconds**: The cooldown period for scaling out or scaling in, in seconds. Valid values: 0 to 3600. The default value is 0.
        # 
        # > You can configure one or more metrics. If you configure multiple metrics, the application scales out when any of the metrics meets or exceeds its target value, up to the specified maximum number of instances. The application scales in only when all metrics are below their target values, down to the specified minimum number of instances.
        self.scaling_rule_metric = scaling_rule_metric
        # The name of the auto scaling policy. The name must be unique within an application, start with a lowercase letter, and contain only lowercase letters, digits, and hyphens (-). The name can be up to 32 characters long.
        # 
        # > The policy name cannot be changed after creation.
        # 
        # This parameter is required.
        self.scaling_rule_name = scaling_rule_name
        # Configurations for the scheduled auto scaling policy. This parameter is required if `ScalingRuleType` is set to `timing` or if you use an SDK.
        # 
        # The parameter is a JSON string that contains the following fields:
        # 
        # - **beginDate** and **endDate**: The start and end dates of the policy\\"s effective period.
        # 
        #   - If both fields are set to `null` (default), the policy is effective indefinitely.
        # 
        #   - If you specify a date range, for example, `beginDate` is `2021-03-25` and `endDate` is `2021-04-25`, the policy is effective for one month.
        # 
        # - **period**: The recurrence rule for the scheduled auto scaling policy.
        # 
        #   - **\\* \\* \\***: The policy is executed at a specified time every day.
        # 
        #   - **\\* \\* Fri,Mon**: The policy is executed at a specified time on specific days of the week. You can select multiple days. The time is in the GMT+8 time zone. Valid values:
        # 
        #     - **Sun**: Sunday
        # 
        #     - **Mon**: Monday
        # 
        #     - **Tue**: Tuesday
        # 
        #     - **Wed**: Wednesday
        # 
        #     - **Thu**: Thursday
        # 
        #     - **Fri**: Friday
        # 
        #     - **Sat**: Saturday
        # 
        #   - **1,2,3,28,31 \\* \\***: The policy is executed at a specified time on specific days of a month. You can select multiple days. The value can be from 1 to 31. If a month does not have the specified day, for example, the 31st, the policy is not executed on that day for that month.
        # 
        # - **schedules**: The trigger times and the corresponding target number of instances. You can specify a maximum of 20 schedules. The parameter includes the following fields:
        # 
        #   - **atTime**: The trigger time in `HH:mm` format. For example, `08:00`.
        # 
        #   - **targetReplicas**: The target number of application instances. Valid values: 1 to 50.
        # 
        #     > During a rolling deployment, we recommend that you set the minimum number of ready instances to 1 or more to prevent service interruptions. If you set the minimum number of ready instances to `0`, your application will be interrupted during an update.
        self.scaling_rule_timer = scaling_rule_timer
        # The type of the auto scaling policy. Valid values:
        # 
        # - **timing**: scheduled auto scaling.
        # 
        # - **metric**: metric-based auto scaling.
        # 
        # - **mix**: mixed auto scaling.
        # 
        # > * If you set this parameter to `timing`, the `ScalingRuleTimer` parameter is required.
        # >
        # > * If you set this parameter to `metric`, the `ScalingRuleMetric` parameter is required.
        # >
        # > * If you set this parameter to `mix`, the `ScalingRuleMetric` parameter is required. You can also configure the `ScalingRuleTimer` parameter as needed.
        # 
        # This parameter is required.
        self.scaling_rule_type = scaling_rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.enable_idle is not None:
            result['EnableIdle'] = self.enable_idle

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

        if self.scaling_rule_enable is not None:
            result['ScalingRuleEnable'] = self.scaling_rule_enable

        if self.scaling_rule_metric is not None:
            result['ScalingRuleMetric'] = self.scaling_rule_metric

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer

        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EnableIdle') is not None:
            self.enable_idle = m.get('EnableIdle')

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        if m.get('ScalingRuleEnable') is not None:
            self.scaling_rule_enable = m.get('ScalingRuleEnable')

        if m.get('ScalingRuleMetric') is not None:
            self.scaling_rule_metric = m.get('ScalingRuleMetric')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')

        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')

        return self

