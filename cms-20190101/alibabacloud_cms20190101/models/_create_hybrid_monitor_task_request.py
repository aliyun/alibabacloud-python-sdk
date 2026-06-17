# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class CreateHybridMonitorTaskRequest(DaraModel):
    def __init__(
        self,
        attach_labels: List[main_models.CreateHybridMonitorTaskRequestAttachLabels] = None,
        cloud_access_id: List[str] = None,
        collect_interval: str = None,
        collect_target_type: str = None,
        description: str = None,
        group_id: str = None,
        namespace: str = None,
        region_id: str = None,
        slsprocess_config: main_models.CreateHybridMonitorTaskRequestSLSProcessConfig = None,
        target_user_id: str = None,
        target_user_id_list: str = None,
        task_name: str = None,
        task_type: str = None,
        yarmconfig: str = None,
    ):
        # The tags of the metric.
        # 
        # > This parameter is required only when TaskType is set to `aliyun_sls`.
        self.attach_labels = attach_labels
        # The IDs of the accounts of other cloud providers that are connected to CloudMonitor.
        self.cloud_access_id = cloud_access_id
        # The collection period of the metric. Valid values:
        # 
        # - 15
        # - 60 (default)
        # 
        # Unit: seconds.
        # 
        # > This parameter is required only when TaskType is set to `aliyun_sls`.
        self.collect_interval = collect_interval
        # The type of the collection target for monitoring data.
        # - If TaskType is set to `aliyun_fc`, set this parameter to `aliyun_fc`.
        # - If TaskType is set to `aliyun_sls`, set this parameter to the name of the Logstore group for SLS logs.
        # 
        # This parameter is required.
        self.collect_target_type = collect_target_type
        # The description of the monitoring task.
        self.description = description
        # The ID of the application group.
        # 
        # For information about how to obtain the application group ID, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        # 
        # > This parameter is required only when TaskType is set to `aliyun_sls`.
        self.group_id = group_id
        # The name of the metric repository.
        # 
        # For information about how to obtain the name of a metric repository, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        self.region_id = region_id
        # The configurations of SLS logs.
        # 
        # > This parameter is required only when TaskType is set to `aliyun_sls`.
        self.slsprocess_config = slsprocess_config
        # The ID of the member account.
        # 
        # When you call this operation by using a management account, you can connect any Alibaba Cloud service of any member account in the resource directory to Hybrid Cloud Monitoring. This allows you to use the resource directory to monitor the Alibaba Cloud services of member accounts across the enterprise in a unified manner.
        # 
        # > This parameter is required only when TaskType is set to `aliyun_fc`.
        self.target_user_id = target_user_id
        # The IDs of the member accounts. Separate multiple IDs with commas (,).
        # 
        # > This parameter is required only when you call this operation by using a management account.
        self.target_user_id_list = target_user_id_list
        # The name of the monitoring task.
        # 
        # - If TaskType is set to `aliyun_fc`, specify the name of the data import task for the Alibaba Cloud service.
        # - If TaskType is set to `aliyun_sls`, specify the metric name for SLS logs.
        self.task_name = task_name
        # The type of the monitoring task. Valid values:
        # 
        # - aliyun_fc: data import task for an Alibaba Cloud service.
        # - aliyun_sls: metric for SLS logs.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The configuration file of the Alibaba Cloud service that is connected to Hybrid Cloud Monitoring.
        # 
        # - namespace: the namespace of the Alibaba Cloud service. For information about how to query the namespace of an Alibaba Cloud service, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html).
        # - metric_list: the metrics of the Alibaba Cloud service. For information about how to query the metrics of an Alibaba Cloud service, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html).
        # 
        # The following example shows a sample configuration file:
        # 
        # ```
        # products:
        # - namespace: acs_ecs_dashboard
        #   metric_info:
        #   - metric_list:
        #     - cpu_total
        #     - cpu_idle
        #     - diskusage_utilization
        #     - CPUUtilization
        #     - DiskReadBPS
        #     - InternetOut
        #     - IntranetOut
        #     - cpu_system
        # - namespace: acs_rds_dashboard
        #   metric_info:
        #   - metric_list:
        #     - MySQL_QPS
        #     - MySQL_TPS
        # ```
        # > This parameter is required only when TaskType is set to `aliyun_fc`.
        self.yarmconfig = yarmconfig

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

        if self.cloud_access_id is not None:
            result['CloudAccessId'] = self.cloud_access_id

        if self.collect_interval is not None:
            result['CollectInterval'] = self.collect_interval

        if self.collect_target_type is not None:
            result['CollectTargetType'] = self.collect_target_type

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slsprocess_config is not None:
            result['SLSProcessConfig'] = self.slsprocess_config.to_map()

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        if self.target_user_id_list is not None:
            result['TargetUserIdList'] = self.target_user_id_list

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.yarmconfig is not None:
            result['YARMConfig'] = self.yarmconfig

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attach_labels = []
        if m.get('AttachLabels') is not None:
            for k1 in m.get('AttachLabels'):
                temp_model = main_models.CreateHybridMonitorTaskRequestAttachLabels()
                self.attach_labels.append(temp_model.from_map(k1))

        if m.get('CloudAccessId') is not None:
            self.cloud_access_id = m.get('CloudAccessId')

        if m.get('CollectInterval') is not None:
            self.collect_interval = m.get('CollectInterval')

        if m.get('CollectTargetType') is not None:
            self.collect_target_type = m.get('CollectTargetType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SLSProcessConfig') is not None:
            temp_model = main_models.CreateHybridMonitorTaskRequestSLSProcessConfig()
            self.slsprocess_config = temp_model.from_map(m.get('SLSProcessConfig'))

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        if m.get('TargetUserIdList') is not None:
            self.target_user_id_list = m.get('TargetUserIdList')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('YARMConfig') is not None:
            self.yarmconfig = m.get('YARMConfig')

        return self

class CreateHybridMonitorTaskRequestSLSProcessConfig(DaraModel):
    def __init__(
        self,
        express: List[main_models.CreateHybridMonitorTaskRequestSLSProcessConfigExpress] = None,
        filter: main_models.CreateHybridMonitorTaskRequestSLSProcessConfigFilter = None,
        group_by: List[main_models.CreateHybridMonitorTaskRequestSLSProcessConfigGroupBy] = None,
        statistics: List[main_models.CreateHybridMonitorTaskRequestSLSProcessConfigStatistics] = None,
    ):
        # The result of arithmetic operations on the extended fields of SLS log statistics results.
        self.express = express
        # The filter conditions for parameters in SLS logs.
        self.filter = filter
        # Aggregates data by spatial dimension, which is equivalent to the GROUP BY clause in SQL.
        self.group_by = group_by
        # The method used to aggregate SLS log data.
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
                temp_model = main_models.CreateHybridMonitorTaskRequestSLSProcessConfigExpress()
                self.express.append(temp_model.from_map(k1))

        if m.get('Filter') is not None:
            temp_model = main_models.CreateHybridMonitorTaskRequestSLSProcessConfigFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        self.group_by = []
        if m.get('GroupBy') is not None:
            for k1 in m.get('GroupBy'):
                temp_model = main_models.CreateHybridMonitorTaskRequestSLSProcessConfigGroupBy()
                self.group_by.append(temp_model.from_map(k1))

        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.CreateHybridMonitorTaskRequestSLSProcessConfigStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class CreateHybridMonitorTaskRequestSLSProcessConfigStatistics(DaraModel):
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
        # Aggregates log data within the statistical period by using the specified statistical method. Valid values:
        # - count: counts the number of occurrences.
        # - sum: calculates the sum.
        # - avg: calculates the average.
        # - max: returns the maximum value.
        # - min: returns the minimum value.
        # - value: samples within the statistical period.
        # - countps: calculates the average count per second for the specified field within the statistical period.
        # - sumps: calculates the average sum per second for the specified field within the statistical period.
        # - distinct: counts the number of occurrences of the specified field after deduplication within the statistical period.
        # - distribution: counts the number of occurrences of field values within a specified range.
        # - percentile: calculates the distribution value of field values, such as P50.
        self.function = function
        # The statistical value of SLS logs.
        # 
        # - If Function is set to `distribution`, this parameter specifies the lower limit of the statistical range. For example, to count the number of 2XX HTTP status codes, set this parameter to 200.
        # 
        # - If Function is set to `percentile`, this parameter specifies the percentile of the statistical distribution. For example, 0.5 indicates P50.
        self.parameter_1 = parameter_1
        # The statistical value of SLS logs.
        # 
        # > This parameter is required only when Function is set to `distribution`. This parameter specifies the upper limit of the statistical range. For example, to count the number of 2XX HTTP status codes, set this parameter to 299.
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

class CreateHybridMonitorTaskRequestSLSProcessConfigGroupBy(DaraModel):
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

class CreateHybridMonitorTaskRequestSLSProcessConfigFilter(DaraModel):
    def __init__(
        self,
        filters: List[main_models.CreateHybridMonitorTaskRequestSLSProcessConfigFilterFilters] = None,
        relation: str = None,
    ):
        # The list of filter conditions for parameters in SLS logs.
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
                temp_model = main_models.CreateHybridMonitorTaskRequestSLSProcessConfigFilterFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        return self

class CreateHybridMonitorTaskRequestSLSProcessConfigFilterFilters(DaraModel):
    def __init__(
        self,
        operator: str = None,
        slskey_name: str = None,
        value: str = None,
    ):
        # The method used to filter parameter values in SLS logs. Valid values:
        # - `contain`: contains.
        # - `notContain`: does not contain.
        # - `>`: greater than.
        # - `<`: less than.
        # - `=`: equal to.
        # - `!=`: not equal to.
        # - `>=`: greater than or equal to.
        # - `<=`: less than or equal to.
        self.operator = operator
        # The name of the parameter to filter in SLS logs.
        self.slskey_name = slskey_name
        # The filter value of the parameter in SLS logs.
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

class CreateHybridMonitorTaskRequestSLSProcessConfigExpress(DaraModel):
    def __init__(
        self,
        alias: str = None,
        express: str = None,
    ):
        # The alias of the arithmetic operation result on the extended fields of SLS log statistics results.
        self.alias = alias
        # The result of arithmetic operations on the extended fields of SLS log statistics results.
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

class CreateHybridMonitorTaskRequestAttachLabels(DaraModel):
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

