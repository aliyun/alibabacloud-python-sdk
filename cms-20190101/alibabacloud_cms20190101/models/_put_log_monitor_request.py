# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutLogMonitorRequest(DaraModel):
    def __init__(
        self,
        aggregates: List[main_models.PutLogMonitorRequestAggregates] = None,
        group_id: str = None,
        groupbys: List[main_models.PutLogMonitorRequestGroupbys] = None,
        log_id: str = None,
        metric_express: str = None,
        metric_name: str = None,
        region_id: str = None,
        sls_logstore: str = None,
        sls_project: str = None,
        sls_region_id: str = None,
        tumblingwindows: str = None,
        unit: str = None,
        value_filter: List[main_models.PutLogMonitorRequestValueFilter] = None,
        value_filter_relation: str = None,
    ):
        # The aggregation logic.
        # 
        # This parameter is required.
        self.aggregates = aggregates
        # The ID of the application group.
        self.group_id = group_id
        # The dimension based on which the data is grouped. This parameter is equivalent to the GROUP BY clause in SQL statements. If no dimension is specified, all data is aggregated based on the aggregate function.
        self.groupbys = groupbys
        # The ID of the log monitoring metric.
        self.log_id = log_id
        # The extended field. The extended field allows you to perform basic operations on the aggregation results.
        # 
        # For example, you have calculated TotalNumber and 5XXNumber by aggregating the data. TotalNumber indicates the total number of HTTP requests, and 5XXNumber indicates the number of HTTP requests whose status code is greater than 499. You can calculate the server error rate by adding the following formula to the extended field: 5XXNumber/TotalNumber\\*100.
        # 
        # JSON format: {"extend":{"errorPercent":"5XXNumber/TotalNumber\\*100"}}. Description:
        # 
        # *   extend: required.
        # *   errorPercent: the alias of the field generated in the calculation result. You can specify the alias as needed.
        # *   5XXNumber/TotalNumber\\*100: the calculation expression.
        self.metric_express = metric_express
        # The metric name. For more information about the metrics for cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        self.region_id = region_id
        # The name of the Simple Log Service Logstore.
        # 
        # This parameter is required.
        self.sls_logstore = sls_logstore
        # The name of the Simple Log Service project.
        # 
        # This parameter is required.
        self.sls_project = sls_project
        # The region in which the Simple Log Service project resides.
        # 
        # This parameter is required.
        self.sls_region_id = sls_region_id
        # The size of the tumbling window for calculation. Unit: seconds. CloudMonitor performs aggregation for each tumbling window.
        self.tumblingwindows = tumblingwindows
        # The unit.
        self.unit = unit
        # The condition that is used to filter logs. The ValueFilter and ValueFilterRelation parameters are used in pair. The filter condition is equivalent to the WHERE clause in SQL statements. If no filter condition is specified, all logs are processed. For example, logs contain the Level and Error fields. If you need to calculate the number of times that logs of the Error level appear every minute, you can set the filter condition to Level=Error and count the number of logs that meet this condition.
        self.value_filter = value_filter
        # The logical operator that is used between log filter conditions. Valid values:
        # 
        # *   and
        # *   or
        # 
        # >  The ValueFilterRelation and `ValueFilter.N.Key` parameters must be used in pair.
        # 
        # This parameter is required.
        self.value_filter_relation = value_filter_relation

    def validate(self):
        if self.aggregates:
            for v1 in self.aggregates:
                 if v1:
                    v1.validate()
        if self.groupbys:
            for v1 in self.groupbys:
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['Groupbys'] = []
        if self.groupbys is not None:
            for k1 in self.groupbys:
                result['Groupbys'].append(k1.to_map() if k1 else None)

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.metric_express is not None:
            result['MetricExpress'] = self.metric_express

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.tumblingwindows is not None:
            result['Tumblingwindows'] = self.tumblingwindows

        if self.unit is not None:
            result['Unit'] = self.unit

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
                temp_model = main_models.PutLogMonitorRequestAggregates()
                self.aggregates.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.groupbys = []
        if m.get('Groupbys') is not None:
            for k1 in m.get('Groupbys'):
                temp_model = main_models.PutLogMonitorRequestGroupbys()
                self.groupbys.append(temp_model.from_map(k1))

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('MetricExpress') is not None:
            self.metric_express = m.get('MetricExpress')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('Tumblingwindows') is not None:
            self.tumblingwindows = m.get('Tumblingwindows')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        self.value_filter = []
        if m.get('ValueFilter') is not None:
            for k1 in m.get('ValueFilter'):
                temp_model = main_models.PutLogMonitorRequestValueFilter()
                self.value_filter.append(temp_model.from_map(k1))

        if m.get('ValueFilterRelation') is not None:
            self.value_filter_relation = m.get('ValueFilterRelation')

        return self

class PutLogMonitorRequestValueFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The name of the log field that is used for matching in the filter condition. Valid values of N: 1 to 10.
        self.key = key
        # The method that is used to match the field value. Valid values of N: 1 to 10. Valid values:
        # 
        # *   `contain`: contains
        # *   `notContain`: does not contain
        # *   `>`: greater than
        # *   `<`: less than
        # *   `>=`: greater than or equal to
        # *   `<=`: less than or equal to
        self.operator = operator
        # The field value to be matched in the filter condition. Valid values of N: 1 to 10.
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

class PutLogMonitorRequestGroupbys(DaraModel):
    def __init__(
        self,
        alias: str = None,
        field_name: str = None,
    ):
        # The alias of the dimension based on which the data is grouped. Valid values of N: 1 to 10.
        self.alias = alias
        # The name of the field that is specified as the dimension. Valid values of N: 1 to 10.
        self.field_name = field_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        return self

class PutLogMonitorRequestAggregates(DaraModel):
    def __init__(
        self,
        alias: str = None,
        field_name: str = None,
        function: str = None,
    ):
        # The alias of the aggregate function. Valid values of N: 1 to 10.
        # 
        # This parameter is required.
        self.alias = alias
        # The name of the field to be aggregated. Valid values of N: 1 to 10.
        # 
        # This parameter is required.
        self.field_name = field_name
        # The function that is used to aggregate log data within a statistical period. Valid values of N: 1 to 10. Valid values:
        # 
        # *   count: counts the number.
        # *   sum: calculates the total value.
        # *   avg: calculates the average value.
        # *   max: calculates the maximum value.
        # *   min: calculates the minimum value.
        # *   countps: calculates the number of values of the specified field divided by the total number of seconds within a statistical period.
        # *   sumps: calculates the sum of the values of the specified field divided by the total number of seconds within a statistical period.
        # *   distinct: calculates the number of unique values of the specified field within a statistical period.
        # 
        # This parameter is required.
        self.function = function

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Function') is not None:
            self.function = m.get('Function')

        return self

