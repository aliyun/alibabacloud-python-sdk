# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationScalingRuleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        enable_idle: bool = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        scaling_rule_metric: str = None,
        scaling_rule_name: str = None,
        scaling_rule_timer: str = None,
        scaling_rule_type: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to enable or disable the idle mode.
        self.enable_idle = enable_idle
        # The minimum percentage of instances that must remain available during a rolling deployment. Valid values:
        # 
        # - **-1**: An initial value that indicates that a percentage is not used.
        # 
        # - **0 to 100**: A percentage that is rounded up. For example, if you have 5 instances and set this parameter to **50**, the minimum number of surviving instances is 3.
        # 
        # > If you specify both **MinReadyInstances** and **MinReadyInstanceRatio**, and **MinReadyInstanceRatio** is not **-1**, **MinReadyInstanceRatio** takes precedence. For example, if **MinReadyInstances** is set to **5** and **MinReadyInstanceRatio** is set to **50**, the system uses **50%** to calculate the minimum number of surviving instances.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of instances that must remain available during a rolling deployment. Valid values:
        # 
        # - If you set this parameter to **0**, your application experiences service interruptions during a rolling deployment.
        # 
        # - If you set this parameter to **-1**, the system uses a recommended value, which is 25% of the current number of instances. For example, if you have 5 instances, the minimum number of surviving instances is 2 (5 × 25% = 1.25, rounded up).
        # 
        # > To ensure business continuity, we recommend that you set the minimum number of surviving instances for each rolling deployment to 1 or higher.
        self.min_ready_instances = min_ready_instances
        # The configuration for the metric-based scaling policy. This parameter is required for metric-based scaling policies.
        # 
        # The parameter includes the following fields:
        # 
        # - **maxReplicas**: The maximum number of application instances.
        # 
        # - **minReplicas**: The minimum number of application instances.
        # 
        # - **metricType**: The metric that triggers the policy. Valid values:
        # 
        #   - **CPU**: The CPU usage.
        # 
        #   - **MEMORY**: The memory usage.
        # 
        #   - **QPS**: The average QPS of a single instance of a Java application over a 1-minute period.
        # 
        #   - **RT**: The average RT of all service interfaces of a Java application over a 1-minute period.
        # 
        #   - **tcpActiveConn**: The average number of active TCP connections per instance over a 30-second period.
        # 
        #   - **SLB_QPS**: The average QPS of an internet-facing SLB, measured per instance over a 15-second period.
        # 
        #   - **SLB_RT**: The average RT of an internet-facing SLB over a 15-second period.
        # 
        #   - **INTRANET_SLB_QPS**: The average QPS of an internal-facing SLB, measured per instance over a 15-second period.
        # 
        #   - **INTRANET_SLB_RT**: The average RT of an internal-facing SLB over a 15-second period.
        # 
        # - **metricTargetAverageUtilization**: The target value for the specified **metricType**.
        # 
        #   - Target CPU usage, in percent.
        # 
        #   - Target memory usage, in percent.
        # 
        #   - Target QPS.
        # 
        #   - Target RT, in milliseconds.
        # 
        #   - Average number of active TCP connections, in connections/second.
        # 
        #   - Target internet-facing SLB QPS.
        # 
        #   - Target internet-facing SLB RT, in milliseconds.
        # 
        #   - Target internal-facing SLB QPS.
        # 
        #   - Target internal-facing SLB RT, in milliseconds.
        # 
        # - **slbId**: The SLB ID.
        # 
        # - **slbProject**: The Simple Log Service project.
        # 
        # - **slbLogstore**: The Simple Log Service Logstore.
        # 
        # - **vport**: The listening port of the SLB. Both HTTP and HTTPS are supported.
        # 
        # - **scaleUpRules**: The scale-out rules.
        # 
        # - **scaleDownRules**: The scale-in rules.
        # 
        # - **step**: The step size for a scale-out or scale-in action. It defines the maximum number of instances that can be added or removed at a time.
        # 
        # - **disabled**: Specifies whether to disable scale-in. Disabling scale-in prevents the application from scaling in, which can mitigate risks during peak traffic.
        # 
        #   - **true**: Disables scale-in.
        # 
        #   - **false**: Enables scale-in. This is the default value.
        # 
        # - **stabilizationWindowSeconds**: The cooldown time, in seconds, for a scaling action. The value must be an integer from 0 to 3,600. The default is 0.
        # 
        # > If you specify multiple metrics, a scale-out is triggered when any metric meets its target. The number of instances will not exceed maxReplicas. A scale-in is triggered only when all metrics are below their targets. The number of instances will not drop below minReplicas.
        self.scaling_rule_metric = scaling_rule_metric
        # The name of the auto scaling policy. The name must start with a lowercase letter, contain only lowercase letters, digits, and hyphens (-), and be no more than 32 characters long.
        # 
        # > You cannot change the name of an auto scaling policy after it is created.
        # 
        # This parameter is required.
        self.scaling_rule_name = scaling_rule_name
        # The configuration of the scheduled scaling policy. This parameter is required for scheduled scaling policies.
        # 
        # The parameter includes the following fields:
        # 
        # - **beginDate** and **endDate**: The start and end dates for the policy\\"s effective period.
        # 
        #   - If both parameters are set to **null**, the policy is always active. This is the default.
        # 
        #   - If you set **beginDate** to **2021-03-25** and **endDate** to **2021-04-25**, the policy is effective for one month.
        # 
        # - **period**: The execution schedule for the policy. Valid values:
        # 
        #   - **\\* \\* \\***: Executes the policy at a specified time every day.
        # 
        #   - **\\* \\* Fri,Mon**: Executes the policy at a specified time on specified days of the week. You can select multiple days. The time is in the UTC+8 time zone. Valid values:
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
        #   - **1,2,3,28,31 \\* \\***: Executes the policy at a specified time on specified days of a month. The value ranges from 1 to 31. If a specified day does not exist in a given month (for example, the 31st), the policy skips it.
        # 
        # - **schedules**: The trigger times and the corresponding target number of instances. You can specify up to 20 time points. This field includes the following parameters:
        # 
        #   - **atTime**: The trigger time. The format is **HH:mm**, for example, **08:00**.
        # 
        #   - **targetReplicas**: The target number of application instances. The value ranges from 1 to 50.
        # 
        #     > To ensure business continuity, we recommend that you set the minimum number of surviving instances for each rolling deployment to **1** or higher. If you set this parameter to **0**, your application is interrupted during an upgrade.
        self.scaling_rule_timer = scaling_rule_timer
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

        if m.get('ScalingRuleMetric') is not None:
            self.scaling_rule_metric = m.get('ScalingRuleMetric')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')

        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')

        return self

