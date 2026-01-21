# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeLogMonitorListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        log_monitor_list: List[main_models.DescribeLogMonitorListResponseBodyLogMonitorList] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The log monitoring metrics.
        self.log_monitor_list = log_monitor_list
        # The returned message.
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
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.log_monitor_list:
            for v1 in self.log_monitor_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['LogMonitorList'] = []
        if self.log_monitor_list is not None:
            for k1 in self.log_monitor_list:
                result['LogMonitorList'].append(k1.to_map() if k1 else None)

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.log_monitor_list = []
        if m.get('LogMonitorList') is not None:
            for k1 in m.get('LogMonitorList'):
                temp_model = main_models.DescribeLogMonitorListResponseBodyLogMonitorList()
                self.log_monitor_list.append(temp_model.from_map(k1))

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

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeLogMonitorListResponseBodyLogMonitorList(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        group_id: int = None,
        log_id: int = None,
        metric_name: str = None,
        sls_logstore: str = None,
        sls_project: str = None,
        sls_region_id: str = None,
        value_filter: List[main_models.DescribeLogMonitorListResponseBodyLogMonitorListValueFilter] = None,
        value_filter_relation: str = None,
    ):
        # The time when the log monitoring metric was created.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_create = gmt_create
        # The ID of the application group.
        self.group_id = group_id
        # The ID of the log monitoring metric.
        self.log_id = log_id
        # The metric name. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The name of the Simple Log Service (SLS) Logstore.
        self.sls_logstore = sls_logstore
        # The name of the SLS project.
        self.sls_project = sls_project
        # The ID of the region where the SLS Logstore resides.
        self.sls_region_id = sls_region_id
        # The condition that is used to filter logs. The ValueFilter and ValueFilterRelation parameters are used in pair. The filter condition is equivalent to the WHERE clause in SQL statements. If no filter condition is specified, all logs are processed. For example, logs contain the Level and Error fields. If you need to calculate the number of times that logs of the Error level appear every minute, you can set the filter condition to Level=Error and count the number of logs that meet this condition.
        self.value_filter = value_filter
        # The logical operator that is used between log filter conditions. The ValueFilter and ValueFilterRelation parameters are used in pair. Valid values:
        # 
        # *   and
        # *   or
        self.value_filter_relation = value_filter_relation

    def validate(self):
        if self.value_filter:
            for v1 in self.value_filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        result['ValueFilter'] = []
        if self.value_filter is not None:
            for k1 in self.value_filter:
                result['ValueFilter'].append(k1.to_map() if k1 else None)

        if self.value_filter_relation is not None:
            result['ValueFilterRelation'] = self.value_filter_relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        self.value_filter = []
        if m.get('ValueFilter') is not None:
            for k1 in m.get('ValueFilter'):
                temp_model = main_models.DescribeLogMonitorListResponseBodyLogMonitorListValueFilter()
                self.value_filter.append(temp_model.from_map(k1))

        if m.get('ValueFilterRelation') is not None:
            self.value_filter_relation = m.get('ValueFilterRelation')

        return self

class DescribeLogMonitorListResponseBodyLogMonitorListValueFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The name of the log field used for matching in the filter condition.
        self.key = key
        # The method that is used to match the field value. Valid values:
        # 
        # *   contain: contains
        # *   notContain: does not contain
        # *   `>`: greater than
        # *   `<`: less than
        # *   `>=`: greater than or equal to
        # *   `<=`: less than or equal to
        self.operator = operator
        # The field value to be matched in the filter condition.
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

