# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeAlarmsResponseBody(DaraModel):
    def __init__(
        self,
        alarm_list: List[main_models.DescribeAlarmsResponseBodyAlarmList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of event-triggered tasks.
        self.alarm_list = alarm_list
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of event-triggered tasks.
        self.total_count = total_count

    def validate(self):
        if self.alarm_list:
            for v1 in self.alarm_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmList'] = []
        if self.alarm_list is not None:
            for k1 in self.alarm_list:
                result['AlarmList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_list = []
        if m.get('AlarmList') is not None:
            for k1 in m.get('AlarmList'):
                temp_model = main_models.DescribeAlarmsResponseBodyAlarmList()
                self.alarm_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAlarmsResponseBodyAlarmList(DaraModel):
    def __init__(
        self,
        alarm_actions: List[str] = None,
        alarm_task_id: str = None,
        comparison_operator: str = None,
        description: str = None,
        dimensions: List[main_models.DescribeAlarmsResponseBodyAlarmListDimensions] = None,
        effective: str = None,
        enable: bool = None,
        evaluation_count: int = None,
        expressions: List[main_models.DescribeAlarmsResponseBodyAlarmListExpressions] = None,
        expressions_logic_operator: str = None,
        hybrid_metrics: List[main_models.DescribeAlarmsResponseBodyAlarmListHybridMetrics] = None,
        hybrid_monitor_namespace: str = None,
        metric_name: str = None,
        metric_type: str = None,
        name: str = None,
        period: int = None,
        prom_ql: str = None,
        scaling_group_id: str = None,
        state: str = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # The list of unique identifiers of the scaling rules associated with the event-triggered task.
        self.alarm_actions = alarm_actions
        # The ID of the event-triggered task.
        self.alarm_task_id = alarm_task_id
        # The comparison operator used to compare the metric value with the threshold. Valid values:
        # 
        # - >=: The metric value is greater than or equal to the threshold.
        # - <=: The metric value is less than or equal to the threshold.
        # - >: The metric value is greater than the threshold.
        # - <: The metric value is less than the threshold.
        self.comparison_operator = comparison_operator
        # The description of the event-triggered task.
        self.description = description
        # The dimension information associated with the metric.
        self.dimensions = dimensions
        # The effective period of the event-triggered node.
        self.effective = effective
        # Indicates whether the event-triggered task is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.enable = enable
        # The number of times that the threshold condition must be met before the scaling rule is triggered. For example, if this parameter is set to 3, the scaling rule is triggered only when the average CPU utilization is greater than or equal to 80% for three consecutive times.
        self.evaluation_count = evaluation_count
        # The information about the multi-metric alert rule.
        self.expressions = expressions
        # The logical operator that specifies the relationship among multiple monitoring alert conditions. Valid values:
        # - `&&`: An alert is triggered only when all monitoring metrics meet the alert conditions. That is, an alert is triggered only when all expressions in the multi-metric alert rule evaluate to `true`.
        # - `||`: An alert is triggered when any of the monitoring metrics meets the alert condition.
        self.expressions_logic_operator = expressions_logic_operator
        # The monitoring metrics settings of Hybrid Cloud Monitoring. For more information about how to configure the settings, see [Use formulas to customize target tracking scaling rules](https://help.aliyun.com/document_detail/2852162.html).
        self.hybrid_metrics = hybrid_metrics
        # The ID of the Hybrid Cloud Monitoring metrics repository.
        # 
        # For more information about how to manage metrics repositories, see [Manage metrics repositories](https://help.aliyun.com/document_detail/217606.html).
        self.hybrid_monitor_namespace = hybrid_monitor_namespace
        # The name of the metric. Valid values: 
        # 
        # - CpuUtilization: the CPU utilization of an ECS instance. Unit: %.
        # - ConcurrentConnections: the number of concurrent connections to an ECS instance.
        # - IntranetTx: the outbound internal traffic of an ECS instance. Unit: Kbit/min.
        # - IntranetRx: the inbound internal traffic of an ECS instance. Unit: Kbit/min.
        # - VpcInternetTx: the outbound Internet traffic of an ECS instance. Unit: Kbit/min.
        # - VpcInternetRx: the inbound Internet traffic of an ECS instance. Unit: Kbit/min.
        # - SystemDiskReadBps: the number of bytes read from the system cloud disk per second. Unit: Byte/s.
        # - SystemDiskWriteBps: the number of bytes written to the system cloud disk per second. Unit: Byte/s.
        # - SystemDiskReadOps: the number of read operations on the system cloud disk per second. Unit: IOPS.
        # - SystemDiskWriteOps: the number of write operations on the system cloud disk per second. Unit: IOPS.
        # - CpuUtilizationAgent: the CPU utilization collected by the CloudMonitor agent. Unit: %.
        # - GpuUtilizationAgent: the GPU utilization collected by the CloudMonitor agent. Unit: %.
        # - GpuMemoryFreeUtilizationAgent: the percentage of idle GPU memory collected by the CloudMonitor agent. Unit: %.
        # - GpuMemoryUtilizationAgent: the GPU memory utilization collected by the CloudMonitor agent. Unit: %.
        # - MemoryUtilization: the memory utilization collected by the CloudMonitor agent. Unit: %.
        # - LoadAverage: the average system load collected by the CloudMonitor agent.
        # - TcpConnection: the total number of TCP connections collected by the CloudMonitor agent.
        # - TcpConnection: the number of established TCP connections collected by the CloudMonitor agent.
        # - PackagesNetOut: the number of packets sent by the internal NIC per second collected by the CloudMonitor agent. Unit: packets/s.
        # - PackagesNetIn: the number of packets received by the internal NIC per second collected by the CloudMonitor agent. Unit: packets/s.
        # - PackagesNetOut: the number of packets sent by the public NIC per second collected by the CloudMonitor agent. Unit: packets/s.
        # - PackagesNetIn: the number of packets received by the public NIC per second collected by the CloudMonitor agent. Unit: packets/s.
        # - EciPodCpuUtilization: the CPU utilization. Unit: %.
        # - EciPodMemoryUtilization: the memory utilization. Unit: %.
        # - LoadBalancerRealServerAverageQps: the average QPS per backend server in an ALB server group. Unit: queries/s.
        # 
        # For more information, see [Event-triggered tasks for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The type of the metric. Valid values:
        # 
        # - system: system metrics of CloudMonitor.
        # - custom: custom metrics reported to CloudMonitor.
        # - hybrid: metrics of Hybrid Cloud Monitoring.
        self.metric_type = metric_type
        # The name of the event-triggered task.
        self.name = name
        # The period at which metric data is collected. Unit: seconds. Valid values:
        # 
        # - 15
        # - 60
        # - 120
        # - 300
        # - 900
        # 
        # > A statistical period of 15 seconds is supported only for scaling groups that contain ECS instances.
        self.period = period
        # The PromQL query statement for Hybrid Cloud Monitoring.
        self.prom_ql = prom_ql
        # The ID of the scaling group with which the event-triggered task is associated.
        self.scaling_group_id = scaling_group_id
        # The state of the event-triggered task. Valid values:
        # 
        # - ALARM: Alerting. The alert condition is met.
        # - OK: Normal. The alert condition is not met.
        # - INSUFFICIENT_DATA: Insufficient data. The data is insufficient to determine whether the alert condition is met.
        self.state = state
        # The statistical method used for metric data. Valid values:
        # 
        # - Average: the average value.
        # - Minimum: the minimum value.
        # - Maximum: the maximum value.
        self.statistics = statistics
        # The threshold of the monitoring metrics. The scaling rule is triggered when the threshold expression is met for the specified number of times.
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
        if self.hybrid_metrics:
            for v1 in self.hybrid_metrics:
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

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        result['Expressions'] = []
        if self.expressions is not None:
            for k1 in self.expressions:
                result['Expressions'].append(k1.to_map() if k1 else None)

        if self.expressions_logic_operator is not None:
            result['ExpressionsLogicOperator'] = self.expressions_logic_operator

        result['HybridMetrics'] = []
        if self.hybrid_metrics is not None:
            for k1 in self.hybrid_metrics:
                result['HybridMetrics'].append(k1.to_map() if k1 else None)

        if self.hybrid_monitor_namespace is not None:
            result['HybridMonitorNamespace'] = self.hybrid_monitor_namespace

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.name is not None:
            result['Name'] = self.name

        if self.period is not None:
            result['Period'] = self.period

        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.state is not None:
            result['State'] = self.state

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
                temp_model = main_models.DescribeAlarmsResponseBodyAlarmListDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        self.expressions = []
        if m.get('Expressions') is not None:
            for k1 in m.get('Expressions'):
                temp_model = main_models.DescribeAlarmsResponseBodyAlarmListExpressions()
                self.expressions.append(temp_model.from_map(k1))

        if m.get('ExpressionsLogicOperator') is not None:
            self.expressions_logic_operator = m.get('ExpressionsLogicOperator')

        self.hybrid_metrics = []
        if m.get('HybridMetrics') is not None:
            for k1 in m.get('HybridMetrics'):
                temp_model = main_models.DescribeAlarmsResponseBodyAlarmListHybridMetrics()
                self.hybrid_metrics.append(temp_model.from_map(k1))

        if m.get('HybridMonitorNamespace') is not None:
            self.hybrid_monitor_namespace = m.get('HybridMonitorNamespace')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class DescribeAlarmsResponseBodyAlarmListHybridMetrics(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.DescribeAlarmsResponseBodyAlarmListHybridMetricsDimensions] = None,
        expression: str = None,
        id: str = None,
        metric_name: str = None,
        statistic: str = None,
    ):
        # The dimensions of the metric. This is used to specify the resources monitored by the metric.
        self.dimensions = dimensions
        # The metric calculation expression for multiple Hybrid Cloud Monitoring metrics. The calculation result of the expression is used to trigger scaling activities. The calculation expression must comply with the Reverse Polish Notation (RPN) specification, and only the `+`, `-`, `*`, and `/` operators are supported.
        self.expression = expression
        # The reference ID of the metric in the metric calculation expression.
        self.id = id
        # The name of the monitoring metrics in the Hybrid Cloud Monitoring metrics repository.
        self.metric_name = metric_name
        # The statistical method of the metric. Valid values:
        # - Average: the average value of all data points in the specified period.
        # - Minimum: the minimum value of all data points in the specified period.
        # - Maximum: the maximum value of all data points in the specified period.
        self.statistic = statistic

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.id is not None:
            result['Id'] = self.id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.statistic is not None:
            result['Statistic'] = self.statistic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.DescribeAlarmsResponseBodyAlarmListHybridMetricsDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Statistic') is not None:
            self.statistic = m.get('Statistic')

        return self

class DescribeAlarmsResponseBodyAlarmListHybridMetricsDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the metric dimension.
        self.dimension_key = dimension_key
        # The value of the metric dimension.
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

class DescribeAlarmsResponseBodyAlarmListExpressions(DaraModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # The comparison operator used to compare the metric value with the threshold in the multi-metric alert rule. Valid values:
        # 
        # - >=: The metric value is greater than or equal to the threshold.
        # - <=: The metric value is less than or equal to the threshold.
        # - >: The metric value is greater than the threshold.
        # - <: The metric value is less than the threshold.
        self.comparison_operator = comparison_operator
        # The name of the monitoring metrics in the multi-metric alert rule. Valid values: 
        # 
        # - CpuUtilization: the CPU utilization of an ECS instance. Unit: %.
        # - ConcurrentConnections: the number of concurrent connections to an ECS instance.
        # - IntranetTx: the outbound internal network traffic of an ECS instance. Unit: Kbit/min.
        # - IntranetRx: the inbound internal network traffic of an ECS instance. Unit: Kbit/min.
        # - VpcInternetTx: the outbound Internet traffic of an ECS instance. Unit: Kbit/min.
        # - VpcInternetRx: the inbound Internet traffic of an ECS instance. Unit: Kbit/min.
        # - SystemDiskReadBps: the number of bytes read from the system cloud disk per second. Unit: Byte/s.
        # - SystemDiskWriteBps: the number of bytes written to the system cloud disk per second. Unit: Byte/s.
        # - SystemDiskReadOps: the number of read operations on the system cloud disk per second. Unit: IOPS.
        # - SystemDiskWriteOps: the number of write operations on the system cloud disk per second. Unit: IOPS.
        # - CpuUtilizationAgent: the CPU utilization collected by the CloudMonitor agent. Unit: %.
        # - GpuUtilizationAgent: the GPU utilization collected by the CloudMonitor agent. Unit: %.
        # - GpuMemoryFreeUtilizationAgent: the percentage of idle GPU memory collected by the CloudMonitor agent. Unit: %.
        # - GpuMemoryUtilizationAgent: the GPU memory utilization collected by the CloudMonitor agent. Unit: %.
        # - MemoryUtilization: the memory utilization collected by the CloudMonitor agent. Unit: %.
        # - LoadAverage: the average system load collected by the CloudMonitor agent.
        # - TcpConnection: the total number of TCP connections collected by the CloudMonitor agent.
        # - TcpConnection: the number of established TCP connections collected by the CloudMonitor agent.
        # - PackagesNetOut: the number of packets sent by the internal network interface controller (NIC) per second collected by the CloudMonitor agent. Unit: packets/s.
        # - PackagesNetIn: the number of packets received by the internal network interface controller (NIC) per second collected by the CloudMonitor agent. Unit: packets/s.
        # - PackagesNetOut: the number of packets sent by the public network interface controller (NIC) per second collected by the CloudMonitor agent. Unit: packets/s.
        # - PackagesNetIn: the number of packets received by the public network interface controller (NIC) per second collected by the CloudMonitor agent. Unit: packets/s.
        # - EciPodCpuUtilization: the CPU utilization. Unit: %.
        # - EciPodMemoryUtilization: the memory utilization. Unit: %.
        # - LoadBalancerRealServerAverageQps: the average QPS per backend server in an ALB server group. Unit: queries/s.
        # 
        # For more information, see [Event-triggered nodes for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The period at which metric data is collected in the multi-metric alert rule. Unit: seconds. Valid values:
        # 
        # - 15
        # - 60
        # - 120
        # - 300
        # - 900
        # 
        # > A statistical period of 15 seconds is supported only when you monitor a scaling group that contains ECS instances and use metrics collected by the CloudMonitor agent (metrics whose names start with Agent).
        self.period = period
        # The statistical method used for metric data in the multi-metric alert rule. Valid values:
        # - Average: the average value.
        # - Minimum: the minimum value.
        # - Maximum: the maximum value.
        self.statistics = statistics
        # The threshold of the monitoring metrics in the multi-metric alert rule. The scaling rule is triggered when the threshold expression is met for the specified number of times.
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

class DescribeAlarmsResponseBodyAlarmListDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the dimension associated with the metric. Valid values:
        # 
        # - user_id: the ID of your account.
        # - scaling_group: the monitored scaling group.
        # - device: the type of the NIC device.
        # - state: the state of the TCP connection.
        self.dimension_key = dimension_key
        # The value of the dimension associated with the metric. The valid values vary based on the dimension key.
        # 
        # - `user_id`: automatically populated by the system.
        # 
        # - `scaling_group`: automatically populated by the system.
        # 
        # - Valid values for `device`:
        #     - eth0: For classic network instances, eth0 represents the internal NIC. For VPC-connected instances, only the eth0 NIC exists.
        #     - eth1: For classic network instances, eth1 represents the public NIC.
        # 
        # - Valid values for `state`:
        #     - TCP_TOTAL: the total number of TCP connections.
        #     - ESTABLISHED: the number of established TCP connections.
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

