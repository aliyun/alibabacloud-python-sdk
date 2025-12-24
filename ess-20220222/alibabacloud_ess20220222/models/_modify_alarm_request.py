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
        # The list of unique identifiers of the scaling rules that are associated with the event-triggered task.
        self.alarm_actions = alarm_actions
        # The ID of the event-triggered task.
        # 
        # This parameter is required.
        self.alarm_task_id = alarm_task_id
        # The operator that is used to compare the metric value and the threshold. Valid values:
        # 
        # *   If the metric value is greater than or equal to the threshold, set the value to `>=`.
        # *   If the metric value is less than or equal to the threshold, set the value to `<=`.
        # *   If the metric value is greater than the threshold, set the value to `>`.
        # *   If the metric value is less than the threshold, set the value to `<`.
        self.comparison_operator = comparison_operator
        # The description of the event-triggered task.
        self.description = description
        # Details of the dimensions.
        self.dimensions = dimensions
        # The effective period of the event-triggered task.
        # 
        # This parameter follows the cron expression format. The default format is `X X X X X ?`, in which:
        # 
        # *   X: a placeholder for a field, which represents seconds, minutes, hours, days, and months in sequence. X can be a definite value or a special character that has logical meaning. For information about the valid values of X, see [Cron expression](https://help.aliyun.com/document_detail/25907.html).
        # *   ?: No value is specified.
        # 
        # > By default, the value of this parameter is specified in **UTC+8**. You can specify the time zone in the `TZ=+yy` format before a cron expression. y indicates the time zone. For example, `TZ=+00 * * 1-2 * * ?` specifies that the event-triggered task is in effect between 01:00 and 02:59 (UTC+0) every day.
        # 
        # Examples:
        # 
        # *   ` * * * * * ?  `: The event-triggered task is in effect all the time.
        # *   ` * * 17-18 * * ?  `: The event-triggered task is in effect between 17:00 and 18:59 (UTC+8) every day.
        # *   `TZ=+00 * * 1-2 * * ?`: The event-triggered task is in effect between 01:00 and 02:59 (UTC+0) every day.
        self.effective = effective
        # The number of times that the threshold must be reached before a scaling rule can be executed. For example, if you set this parameter to 3, the average CPU utilization must reach or exceed 80% three times in a row before a scaling rule is triggered.
        self.evaluation_count = evaluation_count
        # The expressions that are specified in the multi-metric alert rule.
        self.expressions = expressions
        # The relationship between the trigger conditions in the multi-metric alert rule. Valid values:
        # 
        # *   `&&`: An alert is triggered only if all metrics in the multi-metric alert rule meet the trigger conditions. In this case, an alert is triggered only if the results of all trigger conditions that are specified in the multi-metric alert rule are `true`.
        # *   `||`: An alert is triggered if one of the metrics in the multi-metric alert rule meets the trigger condition.
        # 
        # Default value: `&&`.
        self.expressions_logic_operator = expressions_logic_operator
        # The ID of the application group to which the custom metric belongs. If you set the MetricType parameter to custom, you must specify this parameter.
        self.group_id = group_id
        # The name of the metric. The valid values vary based on the metric type.
        # 
        # *   If you set the MetricType parameter to custom, the valid values are your custom metrics.
        # 
        # *   If you set the MetricType parameter to system, the MetricName parameter has the following valid values:
        # 
        #     *   CpuUtilization: the CPU utilization of an ECS instance. Unit: %.
        #     *   IntranetTx: the outbound traffic over the internal network from an ECS instance. Unit: KB/min.
        #     *   IntranetRx: the inbound traffic over the Internet to an ECS instance that resides in a virtual private cloud (VPC). Unit: KB/min.
        #     *   VpcInternetTx: the outbound traffic over the Internet from an ECS instance that resides in a VPC. Unit: KB/min.
        #     *   VpcInternetRx: the inbound traffic over the Internet to an ECS instance that resides in a VPC. Unit: KB/min.
        #     *   SystemDiskReadBps: the number of bytes read from the system disk used by an ECS instance per second.
        #     *   SystemDiskWriteBps: the number of bytes written to the system disk used by an ECS instance per second.
        #     *   SystemDiskReadOps: the number of read operations on the system disk used by an ECS instance per second.
        #     *   SystemDiskWriteOps: the number of write operations on the system disk used by an ECS instance per second.
        #     *   CpuUtilizationAgent: the CPU utilization of an agent. Unit: %.
        #     *   GpuMemoryFreeUtilizationAgent: the percentage of idle GPU memory of an agent.
        #     *   GpuMemoryUtilizationAgent: the GPU memory usage of an agent. Unit: %.
        #     *   MemoryUtilization: the memory usage of an agent. Unit: %.
        #     *   LoadAverage: the average system load of an agent.
        #     *   TcpConnection: the total number of TCP connections of an agent.
        #     *   TcpConnection: the number of established TCP connections of an agent.
        #     *   PackagesNetOut: the number of packets that are sent by the internal network interface controller (NIC) used by an agent.
        #     *   PackagesNetIn: the number of packets that are received by the internal NIC used by an agent.
        #     *   EciPodCpuUtilization: the CPU utilization of an elastic container instance. Unit: %.
        #     *   EciPodMemoryUtilization: the memory usage of an elastic container instance. Unit: %.
        # 
        # For more information, see [Event-triggered task for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The metric type. Valid values:
        # 
        # *   system: a system metric of CloudMonitor
        # *   custom: a custom metric that is reported to CloudMonitor.
        self.metric_type = metric_type
        # The name of the event-triggered task.
        self.name = name
        self.owner_id = owner_id
        # The period of time during which statistics about the metric is collected. Unit: seconds. Valid values:
        # 
        # *   15
        # *   60
        # *   120
        # *   300
        # *   900
        # 
        # > If your scaling group is of the ECS type and uses CloudMonitor metrics, you can set the Period parameter to 15. In other cases, you can set the Period parameter to 60, 120, 300, or 900. In most cases, the name of a CloudMonitor metric contains Agent.
        self.period = period
        # The region ID of the event-triggered task.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The method that is used to aggregate statistics for the metric. Valid values:
        # 
        # *   Average
        # *   Minimum
        # *   Maximum
        self.statistics = statistics
        # The thresholds of the metric values in the multi-metric alert rule. If the thresholds are reached the specified number of times within the specified period, a scaling rule is executed.
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
        # The operator that is used to compare the metric value and the threshold. Valid values:
        # 
        # *   If the metric value is greater than or equal to the threshold, set the value to `>=`.
        # *   If the metric value is less than or equal to the threshold, set the value to `<=`.
        # *   If the metric value is greater than the threshold, set the value to `>`.
        # *   If the metric value is less than the threshold, set the value to `<`.
        # 
        # Default value: >=.
        self.comparison_operator = comparison_operator
        # The name of the metric that is specified in the multi-metric alert rule. The valid values vary based on the metric type.
        # 
        # *   If you set the MetricType parameter to custom, the valid values are your custom metrics.
        # 
        # *   If you set the MetricType parameter to system, the MetricName parameter has the following valid values:
        # 
        #     *   CpuUtilization: the CPU utilization of an ECS instance. Unit: %.
        #     *   IntranetTx: the outbound traffic over the internal network from an ECS instance. Unit: KB/min.
        #     *   IntranetRx: the inbound traffic over the Internet to an ECS instance that resides in a VPC. Unit: KB/min.
        #     *   VpcInternetTx: the outbound traffic over the Internet from an ECS instance that resides in a VPC. Unit: KB/min.
        #     *   VpcInternetRx: the inbound traffic over the Internet to an ECS instance that resides in a VPC. Unit: KB/min.
        #     *   SystemDiskReadBps: the number of bytes read from the system disk used by an ECS instance per second.
        #     *   SystemDiskWriteBps: the number of bytes written to the system disk used by an ECS instance per second.
        #     *   SystemDiskReadOps: the number of read operations on the system disk used by an ECS instance per second.
        #     *   SystemDiskWriteOps: the number of write operations on the system disk used by an ECS instance per second.
        #     *   CpuUtilizationAgent: the CPU utilization of an agent. Unit: %.
        #     *   GpuUtilizationAgent: the GPU utilization of an agent. Unit: %.
        #     *   GpuMemoryFreeUtilizationAgent: the percentage of idle GPU memory of an agent.
        #     *   GpuMemoryUtilizationAgent: the GPU memory usage of an agent. Unit: %.
        #     *   MemoryUtilization: the memory usage of an agent. Unit: %.
        #     *   LoadAverage: the average system load of an agent.
        #     *   TcpConnection: the total number of TCP connections of an agent.
        #     *   TcpConnection: the number of established TCP connections of an agent.
        #     *   PackagesNetOut: the number of packets that are sent by the internal NIC used by an agent.
        #     *   PackagesNetIn: the number of packets that are received by the internal NIC used by an agent.
        #     *   EciPodCpuUtilization: the CPU utilization of an elastic container instance. Unit: %.
        #     *   EciPodMemoryUtilization: the memory usage of an elastic container instance. Unit: %.
        # 
        # For more information, see [Event-triggered task for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The period of time during which statistics about the metrics in the multi-metric alert rule is collected. Unit: seconds. Valid values:
        # 
        # *   15
        # *   60
        # *   120
        # *   300
        # *   900
        # 
        # > If your scaling group is of the ECS type and the event-triggered task associated with your scaling group monitors CloudMonitor metrics, you can set the Period parameter to 15. In other cases, you can set the Period parameter to 60, 120, 300, or 900. In most cases, the name of a CloudMonitor metric contains Agent.
        # 
        # Default value: 300.
        self.period = period
        # The method that is used to aggregate statistics about the metrics that are specified in the multi-metric alert rule. Valid values:
        # 
        # *   Average
        # *   Minimum
        # *   Maximum
        self.statistics = statistics
        # The thresholds of the metric values in the multi-metric alert rule. If the thresholds are reached the specified number of times within the specified period, a scaling rule is executed.
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
        # The key of the dimension. The valid values vary based on the metric type.
        # 
        # *   If you set the MetricType parameter to custom, you can specify this parameter based on your business requirements.
        # 
        # *   If you set the MetricType parameter to system, this parameter has the following valid values:
        # 
        #     *   user_id: the ID of your Alibaba Cloud account
        #     *   scaling_group: the scaling group that you want to monitor
        #     *   device: the type of the NIC
        #     *   state: the status of the TCP connection
        self.dimension_key = dimension_key
        # The value of the dimension. The valid values vary based on the value of the DimensionKey parameter.
        # 
        # *   If you set the MetricType parameter to custom, you can specify this parameter based on your business requirements.
        # 
        # *   If you set the MetricType parameter to system, this parameter has the following valid values:
        # 
        #     *   If you set the DimensionKey parameter to user_id, the system specifies the value
        # 
        #     *   scaling_group: The system specifies the value of the DimensionValue parameter.
        # 
        #     *   If you set the DimensionKey parameter to device, you can set the DimensionValue parameter to eth0 or eth1.
        # 
        #         *   For instances that reside in the classic network type, eth0 specifies the internal NIC. Only one eth0 NIC exists on each instance that resides in a VPC.
        #         *   For instances that reside in the classic network, eth1 specifies the public NIC.
        # 
        #     *   If you set the DimensionKey parameter to state, you can set the DimensionValue parameter to TCP_TOTAL or ESTABLISHED.
        # 
        #         *   TCP_TOTAL specifies the total number of TCP connections.
        #         *   ESTABLISHED specifies the number of established TCP connections.
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

