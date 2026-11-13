# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class CreateAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm_actions: List[str] = None,
        comparison_operator: str = None,
        description: str = None,
        dimensions: List[main_models.CreateAlarmRequestDimensions] = None,
        effective: str = None,
        evaluation_count: int = None,
        expressions: List[main_models.CreateAlarmRequestExpressions] = None,
        expressions_logic_operator: str = None,
        group_id: int = None,
        metric_name: str = None,
        metric_type: str = None,
        name: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # The list of unique identifiers of the scaling rules associated with the event-triggered task.
        self.alarm_actions = alarm_actions
        # The comparison operator used to compare the aggregated metric value with the threshold. This operator specifies the condition under which the threshold is met. Valid values:
        # 
        # - >=: The aggregated metric value is greater than or equal to the threshold.
        # - <=: The aggregated metric value is less than or equal to the threshold.
        # - >: The aggregated metric value is greater than the threshold.
        # - <: The aggregated metric value is less than the threshold.
        # 
        # Default value: >=.
        self.comparison_operator = comparison_operator
        # The description of the event-triggered task.
        self.description = description
        # The dimension information associated with the metric.
        self.dimensions = dimensions
        # Specifies the effective period of the event-triggered task. By default, the task takes effect at all times.
        # 
        # This parameter follows the cron expression format. The default format is `X X X X X ?`, which is described as follows:
        # - X: a placeholder for a field, representing seconds, minutes, hours, day of month, and month in sequence. X can be a specific value or a special character with logical meaning. For more information about the valid values of X, see [Cron expressions](https://help.aliyun.com/document_detail/25907.html).
        # 
        # - ?: indicates that no value is specified.
        # 
        # > The specified value of this parameter **defaults to the UTC+8 time zone**. You can add the time zone information `TZ=+yy` before the cron expression to specify a time zone, where y represents the time zone offset. For example, `TZ=+00 * * 1-2 * * ?` indicates that the event-triggered task takes effect between 01:00 and 02:59 every day in the UTC+0 time zone.
        # 
        # Examples and their meanings:
        # 
        # - `* * * * * ?`: takes effect at all times.
        # 
        # - `* * 17-18 * * ?`: takes effect between 17:00 and 18:59 every day in the UTC+8 time zone.
        # 
        # - `TZ=+00 * * 1-2 * * ?`: takes effect between 01:00 and 02:59 every day in the UTC+0 time zone.
        self.effective = effective
        # The number of times that the threshold expression must be met to trigger a scaling rule. For example, if this parameter is set to 3, the scaling rule is triggered when the average CPU utilization is greater than or equal to 80% for three consecutive times.
        # 
        # Default value: 3.
        self.evaluation_count = evaluation_count
        # The information about the multi-metric alert rule.
        self.expressions = expressions
        # The logical operator between multiple metric alert conditions. Valid values:
        # 
        # - `&&`: An alert is triggered only when all monitoring metrics meet the alert conditions. That is, an alert is triggered only when all expressions in the multi-metric alert rule evaluate to `true`.
        # - `||`: An alert is triggered if any one of the metrics meets the alert condition.
        # 
        # Default value: `&&`.
        self.expressions_logic_operator = expressions_logic_operator
        # The ID of the CloudMonitor application group to which the custom metric belongs. This parameter is required only when the metric type is custom.
        self.group_id = group_id
        # The name of the metric. The valid values vary based on the monitoring type of the event-triggered task:
        # 
        # - If the event-triggered task is of the custom monitoring type (MetricType=custom), the valid values are your custom metrics.
        # 
        # - If the event-triggered task is of the system monitoring type (MetricType=system), valid values: 
        #     - CpuUtilization: the CPU utilization of an ECS instance (%).
        # 
        #     - ConcurrentConnections: the number of concurrent connections to an ECS instance.
        # 
        #     - IntranetTx: the outbound internal network traffic of an ECS instance (Kb/min).
        # 
        #     - IntranetRx: the inbound internal network traffic of an ECS instance (Kb/min).
        # 
        #     - VpcInternetTx: the outbound Internet traffic of an ECS instance (Kb/min).
        # 
        #     - VpcInternetRx: the inbound Internet traffic of an ECS instance (Kb/min).
        # 
        #     - SystemDiskReadBps: the read BPS of the system cloud disk (Byte/s).
        # 
        #     - SystemDiskWriteBps: the write BPS of the system cloud disk (Byte/s).
        # 
        #     - SystemDiskReadOps: the read IOPS of the system cloud disk (operations/s).
        # 
        #     - SystemDiskWriteOps: the write IOPS of the system cloud disk (operations/s).
        # 
        #     - CpuUtilizationAgent: the CPU utilization monitored by the agent (%).
        # 
        #     - GpuUtilizationAgent: the GPU utilization monitored by the agent (%).
        # 
        #     - GpuMemoryFreeUtilizationAgent: the percentage of idle GPU memory monitored by the agent (%).
        # 
        #     - GpuMemoryUtilizationAgent: the GPU memory utilization monitored by the agent (%).
        # 
        #     - MemoryUtilization: the memory utilization monitored by the agent (%).
        # 
        #     - LoadAverage: the average system load monitored by the agent.
        # 
        #     - TcpConnection: the total number of TCP connections monitored by the agent.
        #     
        #     - TcpConnection: the number of established TCP connections monitored by the agent.
        # 
        #     - PackagesNetOut: the number of packets sent by the internal NIC per second monitored by the agent (packets/s).
        # 
        #     - PackagesNetIn: the number of packets received by the internal NIC per second monitored by the agent (packets/s).
        #    
        #     - PackagesNetOut: the number of packets sent by the public NIC per second monitored by the agent (packets/s).
        # 
        #     - PackagesNetIn: the number of packets received by the public NIC per second monitored by the agent (packets/s).
        # 
        #     - EciPodCpuUtilization: the CPU utilization (%).
        # 
        #     - EciPodMemoryUtilization: the memory utilization (%).
        # 
        #     - LoadBalancerRealServerAverageQps: the average QPS per backend server in an ALB server group (queries/s).
        # 
        # For more information, see [System monitoring event-triggered tasks](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The type of the metric. Valid values:
        # - system: uses system metrics of CloudMonitor.
        # - custom: uses custom metrics reported to CloudMonitor.
        self.metric_type = metric_type
        # The name of the event-triggered task.
        self.name = name
        self.owner_id = owner_id
        # The epoch for aggregating monitoring metric data. Unit: seconds. Valid values:
        # 
        # - 15
        # - 60
        # - 120
        # - 300
        # - 900
        # 
        # > Only scaling groups of the ECS instance type support a 15-second statistical period.
        # 
        # Default value: 300.
        self.period = period
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group associated with the event-triggered task.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The method for aggregating metric data. Valid values:
        # 
        # - Average: the average value.
        # - Minimum: the minimum value.
        # - Maximum: the maximum value.
        # 
        # Default value: Average.
        self.statistics = statistics
        # The threshold of the monitoring metrics. When the monitoring threshold expression is met for a specified number of times, it triggers the execution of a scaling rule.
        self.threshold = threshold

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()
        if self.expressions:
            for v1 in self.expressions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_actions is not None:
            result['AlarmActions'] = self.alarm_actions

        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.description is not None:
            result['Description'] = self.description

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.effective is not None:
            result['Effective'] = self.effective

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        result['Expressions'] = []
        if self.expressions is not None:
            for k1 in self.expressions:
                result['Expressions'].append(k1.to_map() if k1 else None)

        if self.expressions_logic_operator is not None:
            result['ExpressionsLogicOperator'] = self.expressions_logic_operator

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmActions') is not None:
            self.alarm_actions = m.get('AlarmActions')

        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.CreateAlarmRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        self.expressions = []
        if m.get('Expressions') is not None:
            for k1 in m.get('Expressions'):
                temp_model = main_models.CreateAlarmRequestExpressions()
                self.expressions.append(temp_model.from_map(k1))

        if m.get('ExpressionsLogicOperator') is not None:
            self.expressions_logic_operator = m.get('ExpressionsLogicOperator')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class CreateAlarmRequestExpressions(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # The comparison operator used to compare the aggregated metric value with the threshold for the multi-metric alert rule. This operator specifies the condition under which the threshold is met. Valid values:
        # 
        # - >=: The aggregated metric value is greater than or equal to the threshold.
        # - <=: The aggregated metric value is less than or equal to the threshold.
        # - >: The aggregated metric value is greater than the threshold.
        # - <: The aggregated metric value is less than the threshold.
        # 
        # Default value: >=.
        self.comparison_operator = comparison_operator
        # The name of the monitoring metrics for the multi-metric alert rule. Valid values vary based on the monitoring type of the event-triggered task:
        # 
        # - If the event-triggered task is of the custom monitoring type (MetricType=custom), the valid values are your custom metrics.
        # 
        # - If the event-triggered task is of the system monitoring type (MetricType=system), valid values: 
        #     
        #     - CpuUtilization: the CPU utilization of an ECS instance (%).
        # 
        #     - ConcurrentConnections: the number of concurrent connections to an ECS instance.
        # 
        #     - IntranetTx: the outbound internal network traffic of an ECS instance (Kb/min).
        # 
        #     - IntranetRx: the inbound internal network traffic of an ECS instance (Kb/min).
        # 
        #     - VpcInternetTx: the outbound Internet traffic of an ECS instance (Kb/min).
        # 
        #     - VpcInternetRx: the inbound Internet traffic of an ECS instance (Kb/min).
        # 
        #     - SystemDiskReadBps: the read BPS of the system cloud disk (Byte/s).
        # 
        #     - SystemDiskWriteBps: the write BPS of the system cloud disk (Byte/s).
        # 
        #     - SystemDiskReadOps: the read IOPS of the system cloud disk (operations/s).
        # 
        #     - SystemDiskWriteOps: the write IOPS of the system cloud disk (operations/s).
        # 
        #     - CpuUtilizationAgent: the CPU utilization monitored by the agent (%).
        # 
        #     - GpuUtilizationAgent: the GPU utilization monitored by the agent (%).
        # 
        #     - GpuMemoryFreeUtilizationAgent: the percentage of idle GPU memory monitored by the agent (%).
        # 
        #     - GpuMemoryUtilizationAgent: the GPU memory utilization monitored by the agent (%).
        # 
        #     - MemoryUtilization: the memory utilization monitored by the agent (%).
        # 
        #     - LoadAverage: the average system load monitored by the agent.
        # 
        #     - TcpConnection: the total number of TCP connections monitored by the agent.
        #     
        #     - TcpConnection: the number of established TCP connections monitored by the agent.
        # 
        #     - PackagesNetOut: the number of packets sent by the internal network interface controller (NIC) per second monitored by the agent (packets/s).
        # 
        #     - PackagesNetIn: the number of packets received by the internal network interface controller (NIC) per second monitored by the agent (packets/s).
        # 
        #     - PackagesNetOut: the number of packets sent by the public network interface controller (NIC) per second monitored by the agent (packets/s).
        # 
        #     - PackagesNetIn: the number of packets received by the public network interface controller (NIC) per second monitored by the agent (packets/s).
        #    
        #     - EciPodCpuUtilization: the CPU utilization (%).
        # 
        #     - EciPodMemoryUtilization: the memory utilization (%).
        # 
        #     - LoadBalancerRealServerAverageQps: the average QPS per backend server in an ALB server group (queries/s).
        # 
        # For more information, see [System monitoring event-triggered tasks](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The epoch for aggregating monitoring metric data in the multi-metric alert rule. Unit: seconds. Valid values:
        # 
        # - 15
        # - 60
        # - 120
        # - 300
        # - 900
        # 
        # > Only scaling groups of the ECS instance type support a 15-second statistical period.
        # 
        # Default value: 300.
        self.period = period
        # The method for aggregating metric data in the multi-metric alert rule. Valid values:
        # 
        # - Average: the average value.
        # - Minimum: the minimum value.
        # - Maximum: the maximum value.
        # 
        # Default value: Average.
        self.statistics = statistics
        # The threshold of the monitoring metrics in the multi-metric alert rule. When the monitoring threshold expression is met for a specified number of times, it triggers the execution of a scaling rule.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.period is not None:
            result['Period'] = self.period

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class CreateAlarmRequestDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the dimension information associated with the metric. Valid values vary based on the monitoring type of the event-triggered task:
        # - If the event-triggered task is of the custom monitoring type (MetricType=custom), the valid values are not limited and can be specified by you.
        # 
        # - If the event-triggered task is of the system monitoring type (MetricType=system), valid values:
        # 
        #     - user_id: the ID of your account.
        #     - scaling_group: the monitored scaling group.
        #     - device: the type of the network interface controller (NIC) device.
        #     - state: the state of the TCP connection.
        #     - rulePool: the ALB server group specified for the QPS monitoring metrics.
        self.dimension_key = dimension_key
        # The value of the dimension information associated with the metric. Valid values vary based on Dimensions.DimensionKey:
        # - If Dimensions.DimensionKey is custom, which means the event-triggered task is of the custom monitoring type (MetricType=custom), the valid values are not limited and can be specified by you.
        # 
        # - If Dimensions.DimensionKey is within the system-specified range, which means the event-triggered task is of the system monitoring type (MetricType=system), valid values:
        # 
        #     - user_id: automatically populated by the system.
        # 
        #     - scaling_group: automatically populated by the system.
        # 
        #     - device:
        # 
        #         - eth0: For classic network instances, eth0 represents the internal NIC. For VPC-connected instances, only the eth0 NIC exists.
        # 
        #         - eth1: For classic network instances, eth1 represents the public NIC.
        # 
        #     - state:
        # 
        #         - TCP_TOTAL: the total number of TCP connections.
        # 
        #         - ESTABLISHED: the number of established TCP connections.
        # 
        #     - rulePool: the ID of the ALB server group. Example: sgp-xxxxx.
        self.dimension_value = dimension_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key

        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')

        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')

        return self

