# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeExporterRuleListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        datapoints: main_models.DescribeExporterRuleListResponseBodyDatapoints = None,
        message: str = None,
        page_number: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code.
        # 
        # > The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The details of the data export rules.
        self.datapoints = datapoints
        # The returned message.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.datapoints:
            self.datapoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

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

        if m.get('Datapoints') is not None:
            temp_model = main_models.DescribeExporterRuleListResponseBodyDatapoints()
            self.datapoints = temp_model.from_map(m.get('Datapoints'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeExporterRuleListResponseBodyDatapoints(DaraModel):
    def __init__(
        self,
        datapoint: List[main_models.DescribeExporterRuleListResponseBodyDatapointsDatapoint] = None,
    ):
        self.datapoint = datapoint

    def validate(self):
        if self.datapoint:
            for v1 in self.datapoint:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Datapoint'] = []
        if self.datapoint is not None:
            for k1 in self.datapoint:
                result['Datapoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datapoint = []
        if m.get('Datapoint') is not None:
            for k1 in m.get('Datapoint'):
                temp_model = main_models.DescribeExporterRuleListResponseBodyDatapointsDatapoint()
                self.datapoint.append(temp_model.from_map(k1))

        return self

class DescribeExporterRuleListResponseBodyDatapointsDatapoint(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        describe: str = None,
        dimension: str = None,
        dst_name: main_models.DescribeExporterRuleListResponseBodyDatapointsDatapointDstName = None,
        enabled: bool = None,
        metric_name: str = None,
        namespace: str = None,
        rule_name: str = None,
        target_windows: str = None,
    ):
        # The time when the rule was created. The value is a UNIX timestamp.
        self.create_time = create_time
        # The description of the rule.
        self.describe = describe
        # The associated dimensions.
        self.dimension = dimension
        self.dst_name = dst_name
        # Indicates whether the rule is enabled.
        self.enabled = enabled
        # The name of the metric.
        # 
        # > For more information, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Appendix 1: Metrics](https://help.aliyun.com/document_detail/28619.html).
        self.metric_name = metric_name
        # The namespace of the service.
        # 
        # > For more information, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Appendix 1: Metrics](https://help.aliyun.com/document_detail/28619.html).
        self.namespace = namespace
        # The name of the data export rule.
        self.rule_name = rule_name
        # The time window of the exported data.\\
        # Multiple windows are separated with commas (,).
        # 
        # > Data in a time window of less than 60 seconds cannot be exported.
        self.target_windows = target_windows

    def validate(self):
        if self.dst_name:
            self.dst_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.dst_name is not None:
            result['DstName'] = self.dst_name.to_map()

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.target_windows is not None:
            result['TargetWindows'] = self.target_windows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('DstName') is not None:
            temp_model = main_models.DescribeExporterRuleListResponseBodyDatapointsDatapointDstName()
            self.dst_name = temp_model.from_map(m.get('DstName'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TargetWindows') is not None:
            self.target_windows = m.get('TargetWindows')

        return self

class DescribeExporterRuleListResponseBodyDatapointsDatapointDstName(DaraModel):
    def __init__(
        self,
        dst_name: List[str] = None,
    ):
        self.dst_name = dst_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_name is not None:
            result['DstName'] = self.dst_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')

        return self

