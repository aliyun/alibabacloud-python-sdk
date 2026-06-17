# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeLogMonitorAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        log_monitor: main_models.DescribeLogMonitorAttributeResponseBodyLogMonitor = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # > A status code of 200 indicates a successful request.
        self.code = code
        # The details of the Log Monitoring task.
        self.log_monitor = log_monitor
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # 
        # - true: The operation was successful.
        # 
        # - false: The operation failed.
        self.success = success

    def validate(self):
        if self.log_monitor:
            self.log_monitor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.log_monitor is not None:
            result['LogMonitor'] = self.log_monitor.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('LogMonitor') is not None:
            temp_model = main_models.DescribeLogMonitorAttributeResponseBodyLogMonitor()
            self.log_monitor = temp_model.from_map(m.get('LogMonitor'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeLogMonitorAttributeResponseBodyLogMonitor(DaraModel):
    def __init__(
        self,
        aggregates: List[main_models.DescribeLogMonitorAttributeResponseBodyLogMonitorAggregates] = None,
        gmt_create: int = None,
        group_id: int = None,
        groupbys: List[str] = None,
        log_id: int = None,
        metric_express: str = None,
        metric_name: str = None,
        sls_logstore: str = None,
        sls_project: str = None,
        sls_region_id: str = None,
        tumblingwindows: List[str] = None,
        value_filter: List[main_models.DescribeLogMonitorAttributeResponseBodyLogMonitorValueFilter] = None,
        value_filter_relation: str = None,
    ):
        # The definitions of aggregations.
        self.aggregates = aggregates
        # The time when the task was created.
        # 
        # This value is a UNIX timestamp that represents the number of milliseconds that have elapsed since January 1, 1970.
        self.gmt_create = gmt_create
        # The ID of the application group.
        self.group_id = group_id
        # The dimension based on which log data is aggregated. This parameter is equivalent to the \\`GROUP BY\\` clause in an SQL statement. You can specify a dimension to group monitoring data. If you do not specify this parameter, all monitoring data is aggregated based on the aggregation method.
        self.groupbys = groupbys
        # The ID of the Log Monitoring task.
        self.log_id = log_id
        # The metric expression.
        self.metric_express = metric_express
        # The name of the metric.
        self.metric_name = metric_name
        # The name of the Simple Log Service Logstore.
        self.sls_logstore = sls_logstore
        # The name of the Simple Log Service project.
        self.sls_project = sls_project
        # The ID of the region where Simple Log Service resides.
        self.sls_region_id = sls_region_id
        # The pre-aggregation window. Unit: seconds. Cloud Monitor aggregates data in the specified pre-aggregation window.
        self.tumblingwindows = tumblingwindows
        # The filter conditions. This parameter is used with \\`ValueFilterRelation\\`. This parameter is equivalent to the \\`WHERE\\` clause in an SQL statement.
        # 
        # If you do not specify this parameter, all data is processed. For example, if a log contains a \\`Level\\` field and you want to count the number of logs where the value of \\`Level\\` is \\`Error\\`, you can set the aggregation function to \\`count\\` and specify a filter condition where \\`Level\\` equals \\`Error\\`.
        self.value_filter = value_filter
        # The logical operator for the filter conditions. This parameter is used with \\`ValueFilter\\`. Valid values:
        # 
        # - and: The logical AND operator.
        # 
        # - or: The logical OR operator.
        self.value_filter_relation = value_filter_relation

    def validate(self):
        if self.aggregates:
            for v1 in self.aggregates:
                 if v1:
                    v1.validate()
        if self.value_filter:
            for v1 in self.value_filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Aggregates'] = []
        if self.aggregates is not None:
            for k1 in self.aggregates:
                result['Aggregates'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.groupbys is not None:
            result['Groupbys'] = self.groupbys

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.metric_express is not None:
            result['MetricExpress'] = self.metric_express

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.tumblingwindows is not None:
            result['Tumblingwindows'] = self.tumblingwindows

        result['ValueFilter'] = []
        if self.value_filter is not None:
            for k1 in self.value_filter:
                result['ValueFilter'].append(k1.to_map() if k1 else None)

        if self.value_filter_relation is not None:
            result['ValueFilterRelation'] = self.value_filter_relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregates = []
        if m.get('Aggregates') is not None:
            for k1 in m.get('Aggregates'):
                temp_model = main_models.DescribeLogMonitorAttributeResponseBodyLogMonitorAggregates()
                self.aggregates.append(temp_model.from_map(k1))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Groupbys') is not None:
            self.groupbys = m.get('Groupbys')

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('MetricExpress') is not None:
            self.metric_express = m.get('MetricExpress')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('Tumblingwindows') is not None:
            self.tumblingwindows = m.get('Tumblingwindows')

        self.value_filter = []
        if m.get('ValueFilter') is not None:
            for k1 in m.get('ValueFilter'):
                temp_model = main_models.DescribeLogMonitorAttributeResponseBodyLogMonitorValueFilter()
                self.value_filter.append(temp_model.from_map(k1))

        if m.get('ValueFilterRelation') is not None:
            self.value_filter_relation = m.get('ValueFilterRelation')

        return self

class DescribeLogMonitorAttributeResponseBodyLogMonitorValueFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The key.
        self.key = key
        # The operator that is used to match the field value. Valid values:
        # 
        # - `contain`: contains.
        # 
        # - `notContain`: does not contain.
        # 
        # - `>`: greater than.
        # 
        # - `<`: less than.
        # 
        # - `>=`: greater than or equal to.
        # 
        # - `<=`: less than or equal to.
        self.operator = operator
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLogMonitorAttributeResponseBodyLogMonitorAggregates(DaraModel):
    def __init__(
        self,
        alias: str = None,
        field_name: str = None,
        function: str = None,
        max: str = None,
        min: str = None,
    ):
        # The alias of the field.
        self.alias = alias
        # The original name of the field in the log.
        self.field_name = field_name
        # The function that is used to aggregate log data in a statistical period. Valid values:
        # 
        # - count: Counts the number of logs.
        # 
        # - sum: Calculates the sum of values in a field.
        # 
        # - avg: Calculates the average of values in a field.
        # 
        # - max: Selects the maximum value in a field.
        # 
        # - min: Selects the minimum value in a field.
        # 
        # - countps: Calculates the average number of logs that are generated per second in a statistical period.
        # 
        # - sumps: Calculates the average sum of values in a field per second in a statistical period.
        # 
        # - distinct: Counts the number of unique values in a field in a statistical period.
        self.function = function
        # The maximum value.
        self.max = max
        # The minimum value.
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.function is not None:
            result['Function'] = self.function

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

