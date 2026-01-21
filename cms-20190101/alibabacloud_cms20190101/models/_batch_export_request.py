# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchExportRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        length: int = None,
        measurements: List[str] = None,
        metric: str = None,
        namespace: str = None,
    ):
        # When you call this operation to export data, you must specify the `Cursor` parameter. You can obtain the value of the `Cursor` parameter by using one of the following methods:
        # 
        # *   When you call this operation for the first time, you must call the Cursor operation to obtain the `Cursor` value. For more information, see [Cursor](https://help.aliyun.com/document_detail/2330730.html).
        # *   When you call this operation again, you can obtain the `Cursor` value from the returned data of the last call.
        # 
        # This parameter is required.
        self.cursor = cursor
        # The maximum number of data entries that can be returned in each response.
        # 
        # Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.length = length
        # The statistical methods used to customize the returned data. By default, the measurements based on all statistical methods are returned.
        # 
        # For example, the `cpu_idle` metric of ECS (`acs_ecs_dashboard`) has three statistical methods: `Average`, `Maximum`, and `Minimum`. If you want to return only the measurements based on the `Average` and `Maximum` statistical methods, set this parameter to `["Average", "Maximum"]`.
        # 
        # The statistical methods of metrics are displayed in the `Statistics` column on the Metrics page of each cloud service. For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.measurements = measurements
        # The metric that is used to monitor the cloud service.
        # 
        # For more information about the metrics of cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # >  The value of this parameter must be the same as the value of the request parameter `Metric` in the Cursor operation.
        # 
        # This parameter is required.
        self.metric = metric
        # The namespace of the cloud service.
        # 
        # For more information about the namespaces of cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # >  The value of this parameter must be the same as the value of the request parameter `Namespace` in the Cursor operation.
        # 
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['Cursor'] = self.cursor

        if self.length is not None:
            result['Length'] = self.length

        if self.measurements is not None:
            result['Measurements'] = self.measurements

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Measurements') is not None:
            self.measurements = m.get('Measurements')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

