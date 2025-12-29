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
        self.enable_idle = enable_idle
        # The percentage of the minimum number of available instances. Valid values:
        # 
        # *   **-1** (default value): The minimum number of available instances is not determined based on this parameter.
        # *   **0 to 100**: The minimum number of available instances is calculated by using the following formula: Number of existing instances × Value of MinReadyInstanceRatio × 100%. The calculation result is rounded up to the nearest integer. For example, if the number of existing instances is 5 and MinReadyInstanceRatio is set to 50, the minimum number of available instances is 3.
        # 
        # >  When **MinReadyInstance** and **MinReadyInstanceRatio** are passed at the same time and the **MinReadyInstanceRatio** value is not \\*\\*-1\\*\\*, the **MinReadyInstanceRatio** parameter takes precedence. **Note**When both **MinReadyInstance** and **MinReadyInstanceRatio** are specified and **MinReadyInstanceRatio** is set to a number from 0 to 100, the value of **MinReadyInstanceRatio** takes precedence.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Special values:
        # 
        # *   If you set the value to **0**, business is interrupted when the application is updated.
        # *   If you set this property to -1, the system calculates a recommended value as the minimum number of available instances by using the following formula: Recommended value = Number of existing instances × 25%. The calculation result is rounded up to the nearest integer. For example, if the number of existing instances is 5, the recommended value is calculated by using the following formula: 5 × 25% = 1.25. In this case, the minimum number of available instances is 2.
        # 
        # >  To ensure business continuity, make sure that at least one instance is available during application deployment and rollback.
        self.min_ready_instances = min_ready_instances
        # Specifies whether to enable the auto scaling policy. Valid values:
        # 
        # *   **true**: The auto scaling policy is enabled.
        # *   **false**: The auto scaling policy is disabled.
        self.scaling_rule_enable = scaling_rule_enable
        # The configurations of the metric-based auto scaling policy. This parameter is required if you set the ScalingRuleType parameter to metric.
        # 
        # The following list describes the involved parameters:
        # 
        # *   **maxReplicas**: the maximum number of instances in the application.
        # 
        # *   **minReplicas**: the minimum number of instances in the application.
        # 
        # *   **metricType**: the metric that is used to trigger the auto scaling policy.
        # 
        #     *   **CPU**: the CPU utilization.
        #     *   **MEMORY**: the memory usage.
        #     *   **QPS**: the average QPS within 1 minute per Java application instance.
        #     *   **RT**: the average response time of all API operations within 1 minute in the Java application.
        #     *   **tcpActiveConn**: the average number of active TCP connections within 30 seconds per instance.
        #     *   **SLB_QPS**: the average QPS of the Internet-facing SLB instance within 15 seconds per instance.
        #     *   **SLB_RT**: the average response time of the Internet-facing SLB instance within 15 seconds.
        #     *   **INTRANET_SLB_QPS**: the average QPS of the internal-facing SLB instance within 15 seconds per instance.
        #     *   **INTRANET_SLB_RT**: the average response time of the internal-facing SLB instance within 15 seconds.
        # 
        # *   **metricTargetAverageUtilization**: the limit on the metric that is specified by **metricType**. You can specify following limits:
        # 
        #     *   The limit on the CPU utilization. Unit: percentage.
        #     *   The limit on the memory usage. Unit: percentage.
        #     *   The limit on the QPS.
        #     *   The limit on the response time. Unit: milliseconds.
        #     *   The limit on the average number of active TCP connections per second.
        #     *   The limit on the QPS of the Internet-facing SLB instance.
        #     *   The limit on the response time of the Internet-facing SLB instance. Unit: milliseconds.
        #     *   The limit on the QPS of the internal-facing SLB instance.
        #     *   The limit on the response time of the internal-facing SLB instance. Unit: milliseconds.
        # 
        # *   **slbId**: the ID of the SLB instance.
        # 
        # *   **slbProject**: the Simple Log Service (SLS) project.
        # 
        # *   **slbLogstore**: the SLS Logstore.
        # 
        # *   **vport**: the listener port of the SLB instance. HTTP and HTTPS are supported.
        # 
        # *   **scaleUpRules**: the scale-out rules.
        # 
        # *   **scaleDownRules**: the scale-in rule.
        # 
        # *   **step**: the scale-out or scale-in step size. This parameter specifies the maximum number of instances that can be added or removed per unit time.
        # 
        # *   **disabled**: specifies whether to disable the application scale-in. If you set this parameter to true, the application instances are never reduced. This prevents business risks during peak hours.
        # 
        #     *   **true**: disables the application scale-in.
        #     *   **false**: enables the application scale-in. Default value: false.
        # 
        # *   **stabilizationWindowSeconds**: the cooldown period during which the system is stable and does not perform scale-out or scale-in operations. Valid values: 0 to 3600. Unit: seconds. Default value: 0.
        # 
        # >  NoteYou can specify one or more metrics as the trigger conditions of the auto scaling policy. If one of the values of the specified metrics is greater than or equal to the specified limit, the application is scaled out. The number of instances after the scale-out operation is less than or equal to the value of the specified maximum application instances. If the values of all specified metrics are less than the limits, the application is scaled in. The number of instances after the scale-in operation is greater than or equal to the value of the specified minimum application instances.
        self.scaling_rule_metric = scaling_rule_metric
        # The name of the auto scaling policy. The name must be unique in an application, and can be up to 32 characters in length. It must start with a lowercase letter and can contain only lowercase letters, digits, and hyphens (-).
        # 
        # >  You cannot change the names of created auto scaling policies.
        # 
        # This parameter is required.
        self.scaling_rule_name = scaling_rule_name
        # The configuration of the scheduled elasticity policy. This parameter is required if you select Scheduled Scaling Policy or Use SDK to Set.
        # 
        # The following table describes the parameters.
        # 
        # *   **beginDate** and **endDate**: **beginDate** is the start date and **endDate** is the end date, which is used to configure the timing Auto Scaling policy. Valid values:
        # 
        #     *   If both values are **null**, long-term execution is performed. This is the default value.
        #     *   If the value is a specific date, for example, the **beginDate** is **2021-03-25** and the **endDate** is **2021-04-25**, the validity period is one month.
        # 
        # *   **period**: The period during which the timed Auto Scaling policy is executed. Valid values:
        # 
        #     *   **\\* \\* \\***: The scheduled policy is executed at a specified time every day.
        # 
        #     *   **\\* \\* Fri,Mon**: The scheduled policy is executed at the specified time on the specified number of days per week. You can select multiple time zones. The time zone is GMT +8. Valid values:
        # 
        #         *   **Sun**: Sunday
        #         *   **Mon**: Monday
        #         *   **Tue**: Tuesday
        #         *   **Wed**: Wednesday
        #         *   **Thu**: Thursday
        #         *   **Fri**: Friday
        #         *   **Sat**: Saturday
        # 
        #     *   **1,2,3,28,31 \\* \\***: The scheduled auto scaling policy is executed at a specified point in time on one or more dates of each month. Valid values: 1 to 31. If a month does not have the 31st day, the auto scaling policy is executed on the specified days other than the 31st day.
        # 
        # *   **schedules**: the points in time at which the scheduled auto scaling policy is triggered and the number of application instances that are retained during the time periods. You can specify up to 20 points in time. The following list describes the involved parameters:
        # 
        #     *   **atTime**: the point in time at which the policy is triggered. **targetReplicas**: the number of application instances that you want to retain during the corresponding time period or the minimum number of available instances required for each deployment.****
        # 
        #     *   **Valid values: 1 to 50.** Valid values: 1 to 50.
        # 
        #         **
        # 
        #         **Note**Make sure that at least one instance is available during the application deployment and rollback to prevent your business from being interrupted. If you set the value to **0**, business interruptions occur when the application is updated. If you set the value to **0**, business interruptions occur when the application is updated.
        self.scaling_rule_timer = scaling_rule_timer
        # The type of the auto scaling policy. Take note of the following rules:
        # 
        # *   **timing**: a scheduled auto scaling policy.
        # *   **metric**: a metric-based auto scaling policy.
        # *   **mix**: a hybrid auto scaling policy.
        # 
        # > 
        # 
        # *   If you set this parameter to timing, the ScalingRuleTimer parameter must be specified.
        # 
        # *   If you set this parameter to metric, the ScalingRuleMetric parameter must be specified.
        # 
        # *   If you set this parameter to mix, the ScalingRuleMetric parameter must be specified. You can specify the ScalingRuleTimer parameter based on your business requirements.
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

