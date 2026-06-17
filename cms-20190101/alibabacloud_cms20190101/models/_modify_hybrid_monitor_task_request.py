# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class ModifyHybridMonitorTaskRequest(DaraModel):
    def __init__(
        self,
        attach_labels: List[main_models.ModifyHybridMonitorTaskRequestAttachLabels] = None,
        collect_interval: str = None,
        description: str = None,
        region_id: str = None,
        slsprocess_config: main_models.ModifyHybridMonitorTaskRequestSLSProcessConfig = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The tags of the metric.
        self.attach_labels = attach_labels
        # The collection interval of the metric. Valid values:
        # 
        # - 15
        # 
        # - 60
        # 
        # Unit: seconds.
        self.collect_interval = collect_interval
        # The description of the monitoring task.
        self.description = description
        self.region_id = region_id
        # The SLS log configuration.
        self.slsprocess_config = slsprocess_config
        # The monitoring task ID.
        # 
        # For information about how to obtain the monitoring task ID, see [DescribeHybridMonitorTaskList](https://help.aliyun.com/document_detail/428624.html).
        # 
        # This parameter is required.
        self.task_id = task_id
        # The monitoring task name.
        # 
        # For information about how to obtain the monitoring task ID, see [DescribeHybridMonitorTaskList](https://help.aliyun.com/document_detail/428624.html).
        self.task_name = task_name

    def validate(self):
        if self.attach_labels:
            for v1 in self.attach_labels:
                 if v1:
                    v1.validate()
        if self.slsprocess_config:
            self.slsprocess_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachLabels'] = []
        if self.attach_labels is not None:
            for k1 in self.attach_labels:
                result['AttachLabels'].append(k1.to_map() if k1 else None)

        if self.collect_interval is not None:
            result['CollectInterval'] = self.collect_interval

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slsprocess_config is not None:
            result['SLSProcessConfig'] = self.slsprocess_config.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attach_labels = []
        if m.get('AttachLabels') is not None:
            for k1 in m.get('AttachLabels'):
                temp_model = main_models.ModifyHybridMonitorTaskRequestAttachLabels()
                self.attach_labels.append(temp_model.from_map(k1))

        if m.get('CollectInterval') is not None:
            self.collect_interval = m.get('CollectInterval')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SLSProcessConfig') is not None:
            temp_model = main_models.ModifyHybridMonitorTaskRequestSLSProcessConfig()
            self.slsprocess_config = temp_model.from_map(m.get('SLSProcessConfig'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

class ModifyHybridMonitorTaskRequestSLSProcessConfig(DaraModel):
    def __init__(
        self,
        express: List[main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigExpress] = None,
        filter: main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigFilter = None,
        group_by: List[main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigGroupBy] = None,
        statistics: List[main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigStatistics] = None,
    ):
        # The arithmetic operation result of the extended field in the SLS log statistics result.
        self.express = express
        # The filter conditions for parameters in the SLS log.
        self.filter = filter
        # Aggregates data by spatial dimension, which is equivalent to GROUP BY in SQL.
        self.group_by = group_by
        # None.
        self.statistics = statistics

    def validate(self):
        if self.express:
            for v1 in self.express:
                 if v1:
                    v1.validate()
        if self.filter:
            self.filter.validate()
        if self.group_by:
            for v1 in self.group_by:
                 if v1:
                    v1.validate()
        if self.statistics:
            for v1 in self.statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Express'] = []
        if self.express is not None:
            for k1 in self.express:
                result['Express'].append(k1.to_map() if k1 else None)

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        result['GroupBy'] = []
        if self.group_by is not None:
            for k1 in self.group_by:
                result['GroupBy'].append(k1.to_map() if k1 else None)

        result['Statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['Statistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.express = []
        if m.get('Express') is not None:
            for k1 in m.get('Express'):
                temp_model = main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigExpress()
                self.express.append(temp_model.from_map(k1))

        if m.get('Filter') is not None:
            temp_model = main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        self.group_by = []
        if m.get('GroupBy') is not None:
            for k1 in m.get('GroupBy'):
                temp_model = main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigGroupBy()
                self.group_by.append(temp_model.from_map(k1))

        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class ModifyHybridMonitorTaskRequestSLSProcessConfigStatistics(DaraModel):
    def __init__(
        self,
        alias: str = None,
        function: str = None,
        parameter_1: str = None,
        parameter_2: str = None,
        slskey_name: str = None,
    ):
        # The alias of the SLS log statistics result.
        self.alias = alias
        # The statistical method used to aggregate log data within a statistical period. Valid values:
        # - count: counts the number of occurrences.
        # - sum: calculates the sum.
        # - avg: calculates the average.
        # - max: returns the maximum value.
        # - min: returns the minimum value.
        # - value: samples within the period.
        # - countps: calculates the per-second average of the count for the specified field within the statistical period.
        # - sumps: calculates the per-second average of the sum for the specified field within the statistical period.
        # - distinct: calculates the number of occurrences of the specified field after deduplication within the statistical period.
        # - distribution: calculates the number of occurrences of field values within a specified range.
        # - percentile: calculates the distribution value of field values, such as P50.
        self.function = function
        # The statistical value of the SLS log.
        # 
        # - If `Function` is set to `distribution`, this parameter specifies the lower limit of the statistical range. For example, to count the number of 2XX HTTP status codes, set this parameter to 200.
        # 
        # - If `Function` is set to `percentile`, this parameter specifies the percentile of the statistical distribution. For example, 0.5 indicates P50.
        self.parameter_1 = parameter_1
        # The statistical value of the SLS log.
        # 
        # > This parameter is required only when `Function` is set to `distribution`. It specifies the upper limit of the statistical range. For example, to count the number of 2XX HTTP status codes, set this parameter to 299.
        self.parameter_2 = parameter_2
        # The name of the parameter for SLS log statistics.
        self.slskey_name = slskey_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.function is not None:
            result['Function'] = self.function

        if self.parameter_1 is not None:
            result['Parameter1'] = self.parameter_1

        if self.parameter_2 is not None:
            result['Parameter2'] = self.parameter_2

        if self.slskey_name is not None:
            result['SLSKeyName'] = self.slskey_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('Parameter1') is not None:
            self.parameter_1 = m.get('Parameter1')

        if m.get('Parameter2') is not None:
            self.parameter_2 = m.get('Parameter2')

        if m.get('SLSKeyName') is not None:
            self.slskey_name = m.get('SLSKeyName')

        return self

class ModifyHybridMonitorTaskRequestSLSProcessConfigGroupBy(DaraModel):
    def __init__(
        self,
        alias: str = None,
        slskey_name: str = None,
    ):
        # The alias of the SLS log statistics result.
        self.alias = alias
        # The name of the parameter for SLS log statistics.
        self.slskey_name = slskey_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.slskey_name is not None:
            result['SLSKeyName'] = self.slskey_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('SLSKeyName') is not None:
            self.slskey_name = m.get('SLSKeyName')

        return self

class ModifyHybridMonitorTaskRequestSLSProcessConfigFilter(DaraModel):
    def __init__(
        self,
        filters: List[main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigFilterFilters] = None,
        relation: str = None,
    ):
        # None.
        self.filters = filters
        # The relationship between multiple filter conditions. Valid values:
        # 
        # - and (default): Logs are processed only when all filter conditions are met.
        # - or: Logs are processed when any filter condition is met.
        self.relation = relation

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.relation is not None:
            result['Relation'] = self.relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ModifyHybridMonitorTaskRequestSLSProcessConfigFilterFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        return self

class ModifyHybridMonitorTaskRequestSLSProcessConfigFilterFilters(DaraModel):
    def __init__(
        self,
        operator: str = None,
        slskey_name: str = None,
        value: str = None,
    ):
        # The method used to filter parameter values in the SLS log. Valid values:
        # - `contain`: contains.
        # - `notContain`: does not contain.
        # - `>`: greater than.
        # - `<`: less than.
        # - `=`: equal to.
        # - `!=`: not equal to.
        # - `>=`: greater than or equal to.
        # - `<=`: less than or equal to.
        self.operator = operator
        # The name of the parameter to filter in the SLS log.
        self.slskey_name = slskey_name
        # The filter value of the parameter in the SLS log.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['Operator'] = self.operator

        if self.slskey_name is not None:
            result['SLSKeyName'] = self.slskey_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('SLSKeyName') is not None:
            self.slskey_name = m.get('SLSKeyName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ModifyHybridMonitorTaskRequestSLSProcessConfigExpress(DaraModel):
    def __init__(
        self,
        alias: str = None,
        express: str = None,
    ):
        # The alias of the arithmetic operation result of the extended field in the SLS log statistics result.
        self.alias = alias
        # The arithmetic operation result of the extended field in the SLS log statistics result.
        self.express = express

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.express is not None:
            result['Express'] = self.express

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Express') is not None:
            self.express = m.get('Express')

        return self

class ModifyHybridMonitorTaskRequestAttachLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The tag key of the metric.
        self.name = name
        # The tag value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

