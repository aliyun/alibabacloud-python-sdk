# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridMonitorTaskListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: str = None,
        task_list: List[main_models.DescribeHybridMonitorTaskListResponseBodyTaskList] = None,
        total: int = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        # 
        # *   If the request was successful, the value `successful` is returned.
        # *   If the request failed, an error message is returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The metric import tasks.
        self.task_list = task_list
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TaskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['TaskList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeHybridMonitorTaskListResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        attach_labels: List[main_models.DescribeHybridMonitorTaskListResponseBodyTaskListAttachLabels] = None,
        collect_interval: int = None,
        collect_target_endpoint: str = None,
        collect_target_path: str = None,
        collect_target_type: str = None,
        collect_timout: int = None,
        create_time: str = None,
        description: str = None,
        extra_info: str = None,
        group_id: str = None,
        instances: List[str] = None,
        log_file_path: str = None,
        log_process: str = None,
        log_sample: str = None,
        log_split: str = None,
        match_express: List[main_models.DescribeHybridMonitorTaskListResponseBodyTaskListMatchExpress] = None,
        match_express_relation: str = None,
        namespace: str = None,
        network_type: str = None,
        slsprocess: str = None,
        slsprocess_config: main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfig = None,
        target_user_id: str = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
        upload_region: str = None,
        yarmconfig: str = None,
    ):
        # The tags of the metric import task.
        self.attach_labels = attach_labels
        # The interval at which the CloudMonitor agent collects host monitoring data. Valid values:
        # 
        # *   15
        # *   30
        # *   60
        # 
        # Unit: seconds.
        self.collect_interval = collect_interval
        # The URL of the destination from which the CloudMonitor agent collects host monitoring data.
        self.collect_target_endpoint = collect_target_endpoint
        # The relative path from which the CloudMonitor agent collects monitoring data.
        self.collect_target_path = collect_target_path
        # The type of the monitoring data. Valid values: Spring, Tomcat, Nginx, Tengine, JVM, Redis, and MySQL.
        self.collect_target_type = collect_target_type
        # The timeout period during which the CloudMonitor agent collects host monitoring data. Valid values:
        # 
        # *   0
        # *   15
        # *   30
        # *   60
        # 
        # Unit: seconds.
        self.collect_timout = collect_timout
        # The timestamp when the metric import task was created.
        # 
        # Unit: milliseconds.
        self.create_time = create_time
        # The description of the metric import task.
        self.description = description
        # The additional information of the instance.
        self.extra_info = extra_info
        # The ID of the application group.
        self.group_id = group_id
        # The instances where monitoring data is collected in batches.
        self.instances = instances
        self.log_file_path = log_file_path
        # The method that is used to aggregate on-premises log data.
        self.log_process = log_process
        # The sample on-premises log.
        self.log_sample = log_sample
        # The result that is returned after on-premises log data is split based on the specified matching mode.
        # 
        # > The matching modes of on-premises log data include full regex mode, delimiter mode, and JSON mode.
        self.log_split = log_split
        # The conditions that are used to match the instances in the application group.
        self.match_express = match_express
        # The relationship between the conditions that are used to filter metric import tasks. Valid values:
        # 
        # *   or
        # *   and
        self.match_express_relation = match_express_relation
        # The namespace to which the host belongs.
        self.namespace = namespace
        # The network type of the host. Valid values:
        # 
        # *   `vpc`
        # *   `Internet`
        self.network_type = network_type
        # The configurations of the logs that are imported from Log Service.
        self.slsprocess = slsprocess
        # The configurations of the logs that are imported from Log Service.
        # 
        # > This parameter is returned only if the `TaskType` parameter is set to `aliyun_sls`.
        self.slsprocess_config = slsprocess_config
        # The ID of the member account.
        # 
        # > This parameter is displayed only when you call this operation by using a management account.
        self.target_user_id = target_user_id
        # The ID of the metric import task.
        self.task_id = task_id
        # The name of the metric import task.
        self.task_name = task_name
        # The type of the metric import task. Valid values:
        # 
        # *   aliyun_fc: metric import tasks for Alibaba Cloud services
        # *   aliyun_sls: metrics for logs imported from Log Service
        self.task_type = task_type
        # The region where the host resides.
        self.upload_region = upload_region
        # The configuration file of the Alibaba Cloud service that you want to monitor by using Hybrid Cloud Monitoring.
        # 
        # *   namespace: the namespace of the Alibaba Cloud service.
        # *   metric_list: the metrics of the Alibaba Cloud service.
        self.yarmconfig = yarmconfig

    def validate(self):
        if self.attach_labels:
            for v1 in self.attach_labels:
                 if v1:
                    v1.validate()
        if self.match_express:
            for v1 in self.match_express:
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

        if self.collect_target_endpoint is not None:
            result['CollectTargetEndpoint'] = self.collect_target_endpoint

        if self.collect_target_path is not None:
            result['CollectTargetPath'] = self.collect_target_path

        if self.collect_target_type is not None:
            result['CollectTargetType'] = self.collect_target_type

        if self.collect_timout is not None:
            result['CollectTimout'] = self.collect_timout

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instances is not None:
            result['Instances'] = self.instances

        if self.log_file_path is not None:
            result['LogFilePath'] = self.log_file_path

        if self.log_process is not None:
            result['LogProcess'] = self.log_process

        if self.log_sample is not None:
            result['LogSample'] = self.log_sample

        if self.log_split is not None:
            result['LogSplit'] = self.log_split

        result['MatchExpress'] = []
        if self.match_express is not None:
            for k1 in self.match_express:
                result['MatchExpress'].append(k1.to_map() if k1 else None)

        if self.match_express_relation is not None:
            result['MatchExpressRelation'] = self.match_express_relation

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.slsprocess is not None:
            result['SLSProcess'] = self.slsprocess

        if self.slsprocess_config is not None:
            result['SLSProcessConfig'] = self.slsprocess_config.to_map()

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.upload_region is not None:
            result['UploadRegion'] = self.upload_region

        if self.yarmconfig is not None:
            result['YARMConfig'] = self.yarmconfig

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attach_labels = []
        if m.get('AttachLabels') is not None:
            for k1 in m.get('AttachLabels'):
                temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListAttachLabels()
                self.attach_labels.append(temp_model.from_map(k1))

        if m.get('CollectInterval') is not None:
            self.collect_interval = m.get('CollectInterval')

        if m.get('CollectTargetEndpoint') is not None:
            self.collect_target_endpoint = m.get('CollectTargetEndpoint')

        if m.get('CollectTargetPath') is not None:
            self.collect_target_path = m.get('CollectTargetPath')

        if m.get('CollectTargetType') is not None:
            self.collect_target_type = m.get('CollectTargetType')

        if m.get('CollectTimout') is not None:
            self.collect_timout = m.get('CollectTimout')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Instances') is not None:
            self.instances = m.get('Instances')

        if m.get('LogFilePath') is not None:
            self.log_file_path = m.get('LogFilePath')

        if m.get('LogProcess') is not None:
            self.log_process = m.get('LogProcess')

        if m.get('LogSample') is not None:
            self.log_sample = m.get('LogSample')

        if m.get('LogSplit') is not None:
            self.log_split = m.get('LogSplit')

        self.match_express = []
        if m.get('MatchExpress') is not None:
            for k1 in m.get('MatchExpress'):
                temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListMatchExpress()
                self.match_express.append(temp_model.from_map(k1))

        if m.get('MatchExpressRelation') is not None:
            self.match_express_relation = m.get('MatchExpressRelation')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('SLSProcess') is not None:
            self.slsprocess = m.get('SLSProcess')

        if m.get('SLSProcessConfig') is not None:
            temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfig()
            self.slsprocess_config = temp_model.from_map(m.get('SLSProcessConfig'))

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UploadRegion') is not None:
            self.upload_region = m.get('UploadRegion')

        if m.get('YARMConfig') is not None:
            self.yarmconfig = m.get('YARMConfig')

        return self

class DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfig(DaraModel):
    def __init__(
        self,
        express: List[main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigExpress] = None,
        filter: main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigFilter = None,
        group_by: List[main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigGroupBy] = None,
        statistics: List[main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigStatistics] = None,
    ):
        # The extended fields that indicate the results of basic operations that are performed on aggregation results.
        self.express = express
        # The conditions that are used to filter logs imported from Log Service.
        self.filter = filter
        # The dimensions based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL.
        self.group_by = group_by
        # The methods that are used to aggregate logs imported from Log Service.
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
                temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigExpress()
                self.express.append(temp_model.from_map(k1))

        if m.get('Filter') is not None:
            temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        self.group_by = []
        if m.get('GroupBy') is not None:
            for k1 in m.get('GroupBy'):
                temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigGroupBy()
                self.group_by.append(temp_model.from_map(k1))

        self.statistics = []
        if m.get('Statistics') is not None:
            for k1 in m.get('Statistics'):
                temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigStatistics(DaraModel):
    def __init__(
        self,
        alias: str = None,
        function: str = None,
        parameter_1: str = None,
        parameter_2: str = None,
        slskey_name: str = None,
    ):
        # The alias of the aggregation result.
        self.alias = alias
        # The function that is used to aggregate log data within a statistical period. Valid values:
        # 
        # *   count: counts the number.
        # *   sum: calculates the total value.
        # *   avg: calculates the average value.
        # *   max: calculates the maximum value.
        # *   min: calculates the minimum value.
        # *   value: collects samples within the statistical period.
        # *   countps: calculates the average number of the specified field per second by using the following formula: Counted number of the specified field/Total number of seconds within the statistical period.
        # *   sumps: calculates the average number of the specified field per second by using the following formula: Total value of the specified field/Total number of seconds within the statistical period.
        # *   distinct: counts the number of logs where the specified field appears within the statistical period.
        # *   distribution: counts the number of logs that meet a specified condition within the statistical period.
        # *   percentile: sorts the values of the specified field in ascending order, and then returns the value that is at the specified percentile within the statistical period. Example: P50.
        self.function = function
        # The value of the function that is used to aggregate logs imported from Log Service.
        # 
        # *   If the `Function` parameter is set to `distribution`, this parameter indicates the lower limit of the statistical interval. For example, 200 indicates that the number of HTTP requests whose status code is 2XX is calculated.
        # *   If the `Function` parameter is set to `percentile`, this parameter specifies the percentile at which the expected value is. For example, 0.5 specifies P50.
        self.parameter_1 = parameter_1
        # The value of the function that is used to aggregate logs imported from Log Service.
        # 
        # > This parameter is returned only if the `Function` parameter is set to `distribution`. This parameter indicates the upper limit of the statistical interval. For example, 299 indicates that the number of HTTP requests whose status code is 2XX is calculated.
        self.parameter_2 = parameter_2
        # The name of the key that is used to aggregate logs imported from Log Service.
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

class DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigGroupBy(DaraModel):
    def __init__(
        self,
        alias: str = None,
        slskey_name: str = None,
    ):
        # The alias of the aggregation result.
        self.alias = alias
        # The name of the key that is used to aggregate logs imported from Log Service.
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

class DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigFilter(DaraModel):
    def __init__(
        self,
        filters: List[main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigFilterFilters] = None,
        relation: str = None,
    ):
        # The conditions that are used to filter logs imported from Log Service.
        self.filters = filters
        # The relationship between multiple filter conditions. Valid values:
        # 
        # *   and (default): Logs are processed only if all filter conditions are met.
        # *   or: Logs are processed if one of the filter conditions is met.
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
                temp_model = main_models.DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigFilterFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        return self

class DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigFilterFilters(DaraModel):
    def __init__(
        self,
        operator: str = None,
        slskey_name: str = None,
        value: str = None,
    ):
        # The method that is used to filter logs imported from Log Service. Valid values:
        # 
        # *   `contain`: contains
        # *   `notContain`: does not contain
        # *   `>`: greater than
        # *   `<`: less than
        # *   `=`: equal to
        # *   `! =`: not equal to
        # *   `>=`: greater than or equal to
        # *   `<=`: less than or equal to
        self.operator = operator
        # The name of the key that is used to filter logs imported from Log Service.
        self.slskey_name = slskey_name
        # The value of the key that is used to filter logs imported from Log Service.
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

class DescribeHybridMonitorTaskListResponseBodyTaskListSLSProcessConfigExpress(DaraModel):
    def __init__(
        self,
        alias: str = None,
        express: str = None,
    ):
        # The alias of the extended field that indicates the result of basic operations that are performed on aggregation results.
        self.alias = alias
        # The extended field that indicates the result of basic operations that are performed on aggregation results.
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

class DescribeHybridMonitorTaskListResponseBodyTaskListMatchExpress(DaraModel):
    def __init__(
        self,
        function: str = None,
        name: str = None,
        value: str = None,
    ):
        # The method that is used to match the instance name. Valid values:
        # 
        # *   startWith: starts with a prefix
        # *   endWith: ends with a suffix
        # *   all: matches all
        # *   equals: equals
        # *   contains: contains
        # *   notContains: does not contain
        self.function = function
        # The instance name.
        self.name = name
        # The keyword that corresponds to the instance name.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeHybridMonitorTaskListResponseBodyTaskListAttachLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The tag key.
        self.name = name
        # The tag value.
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

