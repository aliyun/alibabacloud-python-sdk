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
        # The event-triggered tasks.
        self.alarm_list = alarm_list
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
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
        # The unique identifiers of the scaling rules that are associated with the event-triggered task.
        self.alarm_actions = alarm_actions
        # The ID of the event-triggered task.
        self.alarm_task_id = alarm_task_id
        # The operator that is used to compare the metric value and the metric threshold.
        # 
        # *   Valid value if the metric value is greater than or equal to the threshold: >=.
        # *   Valid value if the metric value is less than or equal to the threshold: <=.
        # *   Valid value if the metric value is greater than the threshold: >.
        # *   Valid value if the metric value is less than the threshold: <.
        self.comparison_operator = comparison_operator
        # The description of the event-triggered task.
        self.description = description
        # The metric dimensions.
        self.dimensions = dimensions
        # The effective period of the event-triggered task.
        self.effective = effective
        # Indicates whether the event-triggered task feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable = enable
        # The number of consecutive times that the threshold must be reached before a scaling rule is executed. For example, if you set this parameter to 3, the average CPU utilization must reach or exceed 80% three times in a row before a scaling rule is executed.
        self.evaluation_count = evaluation_count
        # The alert conditions of the multi-metric alert rule.
        self.expressions = expressions
        # The relationship between the trigger conditions that are specified in the multi-metric alert rule. Valid values:
        # 
        # *   `&&`: An alert is triggered only if all metrics in the multi-metric alert rule meet their trigger conditions. In this case, an alert is triggered only if the results of all trigger conditions that are specified in the multi-metric alert rule are `true`.
        # *   `||`: An alert is triggered only if one of the metrics in the multi-metric alert rule meets its trigger condition.
        self.expressions_logic_operator = expressions_logic_operator
        # The Hybrid Cloud Monitoring metrics.
        self.hybrid_metrics = hybrid_metrics
        # The ID of the Hybrid Cloud Monitoring namespace.
        # 
        # For information about how to manage Hybrid Cloud Monitoring namespaces, see [Manage namespaces](https://help.aliyun.com/document_detail/217606.html).
        self.hybrid_monitor_namespace = hybrid_monitor_namespace
        # The metric name. Valid values:
        # 
        # *   CpuUtilization: the CPU utilization of an Elastic Compute Service (ECS) instance. Unit: %.
        # *   ConcurrentConnections: the number of current connections to an ECS instance.
        # *   IntranetTx: the outbound traffic over an internal network. Unit: KB/min.
        # *   IntranetRx: the inbound traffic over an internal network. Unit: KB/min.
        # *   VpcInternetTx: the outbound traffic over a virtual private cloud (VPC). Unit: KB/min.
        # *   VpcInternetRx: the inbound traffic over a VPC. Unit: KB/min.
        # *   SystemDiskReadBps: the number of bytes read from the system disk per second.
        # *   SystemDiskWriteBps: the number of bytes written to the system disk per second.
        # *   SystemDiskReadOps: the read IOPS of the system disk. Unit: counts/s.
        # *   SystemDiskWriteOps: the write IOPS of the system disk. Unit: counts/s.
        # *   CpuUtilizationAgent: the CPU utilization. Unit: %.
        # *   GpuUtilizationAgent: the GPU utilization. Unit: %.
        # *   GpuMemoryFreeUtilizationAgent: the idle GPU memory usage. Unit: %.
        # *   GpuMemoryUtilizationAgent: the GPU memory usage. Unit: %.
        # *   MemoryUtilization: the memory usage. Unit: %.
        # *   LoadAverage: the average system load.
        # *   TcpConnection: the total number of TCP connections.
        # *   TcpConnection: the number of established TCP connections.
        # *   PackagesNetOut: the number of packets sent by the internal NIC. Unit: counts/s.
        # *   PackagesNetIn: the number of packets received by the internal NIC. Unit: counts/s.
        # *   PackagesNetOut: the number of packets sent by the public NIC. Unit: counts/s.
        # *   PackagesNetIn: the number of packets received by the public NIC. Unit: counts/s.
        # *   EciPodCpuUtilization: the CPU utilization. Unit: %.
        # *   EciPodMemoryUtilization: the memory usage. Unit: %.
        # *   LoadBalancerRealServerAverageQps: the queries per second (QPS) of an instance.
        # 
        # For more information, see [Event-triggered tasks of the system monitoring type](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The type of the metric. Valid values:
        # 
        # *   system: system metrics of CloudMonitor
        # *   custom: custom metrics that are reported to CloudMonitor.
        # *   hybrid: metrics of Hybrid Cloud Monitoring.
        self.metric_type = metric_type
        # The name of the event-triggered task.
        self.name = name
        # The statistical period of the metric data. Unit: seconds. Valid values:
        # 
        # *   15
        # *   60
        # *   120
        # *   300
        # *   900
        # 
        # >  You can set the value of this parameter to 15 Seconds only for scaling groups of the ECS type.
        self.period = period
        # The PromQL statement of Hybrid Cloud Monitoring.
        self.prom_ql = prom_ql
        # The ID of the scaling group to which the event-triggered task is associated.
        self.scaling_group_id = scaling_group_id
        # The status of the event-triggered task. Valid values:
        # 
        # *   ALARM: The alert condition is met and an alert is triggered.
        # *   OK: The alert condition is not met.
        # *   INSUFFICIENT_DATA: Auto Scaling cannot determine whether the alert condition is met due to insufficient data.
        self.state = state
        # The method that is used to aggregate the metric data. Valid values:
        # 
        # *   Average: the average value
        # *   Minimum: the minimum value
        # *   Maximum: the maximum value
        self.statistics = statistics
        # The threshold of the metric. If the threshold is reached the specified number of times within the statistical period, a scaling rule is executed.
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
        # The metric dimensions. This parameter is used to specify the monitored resources.
        self.dimensions = dimensions
        # The metric expression that consists of multiple Hybrid Cloud Monitoring metrics. It calculates a result used to trigger scaling events.
        # 
        # The expression is written in Reverse Polish Notation (RPN) format and supports only the following operators: `+, -, *, /`.
        self.expression = expression
        # The reference ID of the metric in the metric expression.
        self.id = id
        # The name of the Hybrid Cloud Monitoring metric.
        self.metric_name = metric_name
        # The statistical method of the metric value. Valid values:
        # 
        # *   Average: The average value of all metric values within a specified interval is calculated.
        # *   Minimum: The minimum value of all metric values within a specified interval is calculated.
        # *   Maximum: The maximum value of all metric values within a specified interval is calculated.
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
        # The key of the metric dimension.
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
        # The operator that is used to compare the metric value and the threshold.
        # 
        # *   Valid value if the metric value is greater than or equal to the threshold: >=.
        # *   Valid value if the metric value is less than or equal to the threshold: <=.
        # *   Valid value if the metric value is greater than the threshold: >.
        # *   Valid value if the metric value is less than the threshold: <.
        self.comparison_operator = comparison_operator
        # The name of the metric that is specified in the multi-metric alert rule. Valid values:
        # 
        # *   CpuUtilization: the CPU utilization of an ECS instance. Unit: %.
        # *   ConcurrentConnections: the number of current connections to an ECS instance.
        # *   IntranetTx: the outbound traffic over an internal network. Unit: KB/min.
        # *   IntranetRx: the inbound traffic over an internal network. Unit: KB/min.
        # *   VpcInternetTx: the outbound traffic over a VPC. Unit: KB/min.
        # *   VpcInternetRx: the inbound traffic over a VPC. Unit: KB/min.
        # *   SystemDiskReadBps: the number of bytes read from the system disk per second.
        # *   SystemDiskWriteBps: the number of bytes written to the system disk per second.
        # *   SystemDiskReadOps: the read IOPS of the system disk. Unit: counts/s.
        # *   SystemDiskWriteOps: the write IOPS of the system disk. Unit: counts/s.
        # *   CpuUtilizationAgent: the CPU utilization. Unit: %.
        # *   GpuUtilizationAgent: the GPU utilization. Unit: %.
        # *   GpuMemoryFreeUtilizationAgent: the idle GPU memory usage. Unit: %.
        # *   GpuMemoryUtilizationAgent: the GPU memory usage. Unit: %.
        # *   MemoryUtilization: the memory usage. Unit: %.
        # *   LoadAverage: the average system load.
        # *   TcpConnection: the total number of TCP connections.
        # *   TcpConnection: the number of established TCP connections.
        # *   PackagesNetOut: the number of packets sent by the internal NIC. Unit: counts/s.
        # *   PackagesNetIn: the number of packets received by the internal NIC. Unit: counts/s.
        # *   PackagesNetOut: the number of packets sent by the public NIC. Unit: counts/s.
        # *   PackagesNetIn: the number of packets received by the public NIC. Unit: counts/s.
        # *   EciPodCpuUtilization: the CPU utilization. Unit: %.
        # *   EciPodMemoryUtilization: the memory usage. Unit: %.
        # *   LoadBalancerRealServerAverageQps: the QPS of an instance.
        # 
        # For more information, see [Event-triggered tasks of the system monitoring type](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The statistical period of the metric data in the multi-metric alert rule. Unit: seconds. Valid values:
        # 
        # *   15
        # *   60
        # *   120
        # *   300
        # *   900
        # 
        # >  If your scaling group is of the ECS type and the event-triggered task that is associated with your scaling group monitors CloudMonitor metrics, you can set Period to 15. In most cases, the name of a CloudMonitor metric contains Agent.
        self.period = period
        # The method that is used to aggregate statistics about the metrics in the multi-metric alert rule. Valid values:
        # 
        # *   Average: the average value
        # *   Minimum: the minimum value
        # *   Maximum: the maximum value
        self.statistics = statistics
        # The threshold of the metric value. If the threshold is reached the specified number of times within the specified period, a scaling rule is executed.
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
        # The dimension key of the metric. Valid values:
        # 
        # *   user_id: the ID of your Alibaba Cloud account.
        # *   scaling_group: the scaling group that is monitored by the event-triggered task.
        # *   device: the NIC type.
        # *   state: the status of the TCP connection.
        self.dimension_key = dimension_key
        # The dimension value of the metric. The value of DimensionValue varies based on the value of DimensionKey.
        # 
        # *   If you set DimensionKey to `user_id`, the system specifies the value of DimensionValue.
        # 
        # *   If you set DimensionKey to `scaling_group`, the system specifies the value of DimensionValue.
        # 
        # *   If you set DimensionKey to `device`, you can set DimensionValue to eth0 or eth1.
        # 
        #     *   For instances of the classic network type, eth0 indicates the internal NIC. Only one eth0 NIC exists on each instance that resides in VPCs.
        #     *   For instances of the classic network type, eth1 indicates the public NIC.
        # 
        # *   If you set DimensionKey to `state`, you can set DimensionValue to TCP_TOTAL or ESTABLISHED.
        # 
        #     *   TCP_TOTAL indicates the total number of TCP connections.
        #     *   ESTABLISHED indicates the number of TCP connections that are established.
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

