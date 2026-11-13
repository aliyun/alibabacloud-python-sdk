# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ModifyAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm_actions: List[str] = None,
        alarm_task_id: str = None,
        comparison_operator: str = None,
        description: str = None,
        dimensions: List[main_models.ModifyAlarmRequestDimensions] = None,
        effective: str = None,
        evaluation_count: int = None,
        expressions: List[main_models.ModifyAlarmRequestExpressions] = None,
        expressions_logic_operator: str = None,
        group_id: int = None,
        metric_name: str = None,
        metric_type: str = None,
        name: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # The list of unique identifiers of the scaling rules associated with the event-triggered task.
        self.alarm_actions = alarm_actions
        # The ID of the event-triggered task.
        # 
        # This parameter is required.
        self.alarm_task_id = alarm_task_id
        # The comparison operator between the statistical value and the threshold of the metric. The comparison operator indicates the relationship in which the statistical value and the threshold can satisfy the condition. Valid values:
        # 
        # - The statistical value is greater than or equal to the threshold. Value: `>=`.
        # - The statistical value is less than or equal to the threshold. Value: `<=`.
        # - The statistical value is greater than the threshold. Value: `>`.
        # - The statistical value is less than the threshold. Value: `<`.
        self.comparison_operator = comparison_operator
        # The description of the event-triggered task.
        self.description = description
        # The dimension information associated with the metric.
        self.dimensions = dimensions
        # Specifies the effective period of the event-triggered task.
        # 
        # This parameter follows cron expressions. The default format is `X X X X X ?`, where:
        # - X: a placeholder for a field, which sequentially represents seconds, minutes, hours, day, and month. X can be a specific value or a special character with logical meaning. For more information about the valid values of X, see [Cron expression](https://help.aliyun.com/document_detail/25907.html).
        # 
        # - ?: specifies no value.
        # 
        # > The value of this parameter is **in the UTC+8 time zone by default**. You can add time zone information `TZ=+yy` before the cron expression to specify a time zone, where y represents the numeric value of the time zone. For example, `TZ=+00 * * 1-2 * * ?` indicates that the event-triggered task takes effect between 01:00 and 02:59 every day in the UTC+0 time zone.
        # 
        # Examples and descriptions:
        # 
        # -  `* * * * * ?  `: takes effect at all times.
        # 
        # -  `* * 17-18 * * ? `: takes effect between 17:00 and 18:59 every day in the UTC+8 time zone.
        # 
        # - `TZ=+00 * * 1-2 * * ?`: takes effect between 01:00 and 02:59 every day in the UTC+0 time zone.
        self.effective = effective
        # The number of times that the threshold expression must be met before the scaling rule is triggered. For example, the average CPU utilization must be greater than or equal to 80% in three consecutive statistical results.
        self.evaluation_count = evaluation_count
        # The monitoring metrics of the multi-metric event-triggered task.
        self.expressions = expressions
        # The relationship between multiple monitoring metrics conditions. Valid values:
        # 
        # - `&&`: An alert is triggered only when all monitoring metrics meet the alert conditions. An alert is triggered only when all expressions in the multi-metric event-triggered task evaluate to `true`.
        # - `||`: An alert is triggered when any monitoring metric meets the alert condition.
        # 
        # Default value: `&&`.
        self.expressions_logic_operator = expressions_logic_operator
        # The ID of the CloudMonitor application group to which the custom metric belongs. This parameter is required only when MetricType is set to custom.
        self.group_id = group_id
        # The name of the metric. Valid values vary based on the monitoring type of the event-triggered task: 
        # 
        # - If the event-triggered task is of the custom monitoring type (MetricType=custom), valid values are your custom metrics.
        # 
        # - If the event-triggered task is of the system monitoring type (MetricType=system), valid values: 
        # 
        #     - CpuUtilization: (ECS) CPU utilization (%).
        # 
        #     - IntranetTx: (ECS) outbound traffic over the internal network (KByte/min).
        # 
        #     - IntranetRx: (ECS) inbound traffic over the internal network (KByte/min).
        # 
        #     - VpcInternetTx: (ECS) outbound traffic over the Internet (KByte/min).
        # 
        #     - VpcInternetRx: (ECS) inbound traffic over the Internet (KByte/min).
        # 
        #     - SystemDiskReadBps: (ECS) system cloud disk read BPS (Byte/s).
        # 
        #     - SystemDiskWriteBps: (ECS) system cloud disk write BPS (Byte/s).
        # 
        #     - SystemDiskReadOps: (ECS) system cloud disk read IOPS (count/s).
        # 
        #     - SystemDiskWriteOps: (ECS) system cloud disk write IOPS (count/s).
        # 
        #     - CpuUtilizationAgent: (Agent) CPU utilization (%).
        # 
        #     - GpuMemoryFreeUtilizationAgent: (Agent) GPU memory idle rate (%).
        # 
        #     - GpuMemoryUtilizationAgent: (Agent) GPU memory utilization (%).
        # 
        #     - MemoryUtilization: (Agent) memory utilization (%).
        # 
        #     - LoadAverage: (Agent) average system load.
        # 
        #     - TcpConnection: (Agent) total number of TCP connections.
        # 
        #     - TcpConnection: (Agent) number of established TCP connections.
        # 
        #     - PackagesNetOut: (Agent) number of packets sent by the NIC.
        # 
        #     - PackagesNetIn: (Agent) number of packets received by the NIC.
        # 
        #     - EciPodCpuUtilization: CPU utilization (%).
        # 
        #     - EciPodMemoryUtilization: memory utilization (%).
        # 
        # For more information, see [Event-triggered tasks for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The type of the metric. Valid values:
        # - system: uses CloudMonitor system metrics.
        # - custom: uses custom metrics reported to CloudMonitor.
        self.metric_type = metric_type
        # The name of the event-triggered task.
        self.name = name
        self.owner_id = owner_id
        # The statistical period for the metric data, in seconds. Valid values:
        # 
        # - 15.
        # - 60.
        # - 120.
        # - 300.
        # - 900.
        # 
        # > A statistical period of 15 seconds is applicable only to metrics collected by the CloudMonitor agent (metrics that start with Agent) when monitoring ECS-type scaling groups. For all other metrics, the statistical period can be set to 60, 120, 300, or 900 seconds.
        self.period = period
        # The region ID of the event-triggered task.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The method used to aggregate the metric data. Valid values:
        # 
        # - Average: average value.
        # - Minimum: minimum value.
        # - Maximum: maximum value.
        self.statistics = statistics
        # The threshold of the monitoring metrics in a multi-metric event-triggered task. The scaling rule is executed when the threshold expression is met the specified number of times.
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

        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id

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

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmActions') is not None:
            self.alarm_actions = m.get('AlarmActions')

        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')

        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.ModifyAlarmRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        self.expressions = []
        if m.get('Expressions') is not None:
            for k1 in m.get('Expressions'):
                temp_model = main_models.ModifyAlarmRequestExpressions()
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

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class ModifyAlarmRequestExpressions(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # The comparison operator between the statistical value and the threshold of the metric. The comparison operator indicates the relationship in which the statistical value and the threshold can satisfy the condition. Valid values:
        # 
        # - The statistical value is greater than or equal to the threshold. Value: `>=`.
        # - The statistical value is less than or equal to the threshold. Value: `<=`.
        # - The statistical value is greater than the threshold. Value: `>`.
        # - The statistical value is less than the threshold. Value: `<`.
        # 
        # Default value: >=.
        self.comparison_operator = comparison_operator
        # The name of the monitoring metric in the multi-metric event-triggered node. Valid values vary based on the monitoring type of the event-triggered task: 
        # 
        # - If the event-triggered task is of the custom monitoring type (MetricType=custom), valid values are your custom monitoring metrics.
        # 
        # - If the event-triggered task is of the system monitoring type (MetricType=system), valid values: 
        # 
        #     - CpuUtilization: (ECS) CPU utilization (%).
        # 
        #     - IntranetTx: (ECS) outbound traffic over the internal network (KByte/min).
        # 
        #     - IntranetRx: (ECS) inbound traffic over the internal network (KByte/min).
        # 
        #     - VpcInternetTx: (ECS) outbound traffic over the Internet (KByte/min).
        # 
        #     - VpcInternetRx: (ECS) inbound traffic over the Internet (KByte/min).
        # 
        #     - SystemDiskReadBps: (ECS) system cloud disk read BPS (Byte/s).
        # 
        #     - SystemDiskWriteBps: (ECS) system cloud disk write BPS (Byte/s).
        # 
        #     - SystemDiskReadOps: (ECS) system cloud disk read IOPS (count/s).
        # 
        #     - SystemDiskWriteOps: (ECS) system cloud disk write IOPS (count/s).
        # 
        #     - CpuUtilizationAgent: (Agent) CPU utilization (%).
        # 
        #     - GpuUtilizationAgent: (Agent) GPU utilization (%).
        # 
        #     - GpuMemoryFreeUtilizationAgent: (Agent) GPU memory idle rate (%).
        # 
        #     - GpuMemoryUtilizationAgent: (Agent) GPU memory utilization (%).
        # 
        #     - MemoryUtilization: (Agent) memory utilization (%).
        # 
        #     - LoadAverage: (Agent) average system load.
        # 
        #     - TcpConnection: (Agent) total number of TCP connections.
        # 
        #     - TcpConnection: (Agent) number of established TCP connections.
        # 
        #     - PackagesNetOut: (Agent) number of packets sent by the network interface controller (NIC).
        # 
        #     - PackagesNetIn: (Agent) number of packets received by the network interface controller (NIC).
        # 
        #     - EciPodCpuUtilization: CPU utilization (%).
        # 
        #     - EciPodMemoryUtilization: memory utilization (%).
        # 
        # For more information, see [Event-triggered tasks for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The statistical period for the metric data in the multi-metric event-triggered task, in seconds. Valid values:
        # 
        # - 15.
        # - 60.
        # - 120.
        # - 300.
        # - 900.
        # 
        # > A statistical period of 15 seconds is applicable only to metrics collected by the CloudMonitor agent (metrics that start with Agent) when monitoring ECS-type scaling groups. For all other metrics, the statistical period can be set to 60, 120, 300, or 900 seconds.
        # 
        # Default value: 300.
        self.period = period
        # The method used to aggregate the metric data in the multi-metric event-triggered task. Valid values:
        # 
        # - Average: average value.
        # - Minimum: minimum value.
        # - Maximum: maximum value.
        self.statistics = statistics
        # The threshold of the monitoring metrics in a multi-metric event-triggered task. The scaling rule is executed when the threshold expression is met the specified number of times.
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

class ModifyAlarmRequestDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the dimension information associated with the metric. Valid values vary based on the monitoring type of the event-triggered node:
        # 
        # - If the event-triggered task is of the custom monitoring type (MetricType=custom), valid values are not restricted. You can specify custom values.
        # 
        # 
        # - If the event-triggered task is of the system monitoring type (MetricType=system), valid values:
        # 
        #     - user_id: your account ID.
        #     - scaling_group: the scaling group to be monitored.
        #     - device: the type of the network interface controller (NIC) device.
        #     - state: the state of the TCP connection.
        #     - rulePool: the server group specified for the ALB QPS monitoring metrics.
        self.dimension_key = dimension_key
        # The value of the dimension information associated with the metric. Valid values are determined by Dimension.N.DimensionKey:
        # 
        # - If Dimension.N.DimensionKey is set to a custom value, which means the event-triggered task is of the custom monitoring type (MetricType=custom), valid values are not restricted. You can specify custom values.
        # 
        # - If Dimension.N.DimensionKey is set to a system-specified value, which means the event-triggered task is of the system monitoring type (MetricType=system), valid values:
        # 
        #     - user_id: automatically populated by the system.
        # 
        #     - scaling_group: automatically populated by the system.
        # 
        #     - device:
        # 
        #         - eth0: for classic network instances, eth0 represents the internal NIC. For VPC-connected instances, only the eth0 NIC exists.
        #         - eth1: for classic network instances, eth1 represents the public NIC.
        # 
        #     - state:
        # 
        #         - TCP_TOTAL: the total number of TCP connections.
        #         - ESTABLISHED: the number of established TCP connections.
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

