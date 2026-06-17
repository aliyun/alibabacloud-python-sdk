# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchExportShrinkRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        length: int = None,
        measurements_shrink: str = None,
        metric: str = None,
        namespace: str = None,
    ):
        # When you call this operation in a loop to export data, you must specify the value of `Cursor`. You can obtain the value of `Cursor` by using the following methods:
        # 
        # - When you call this operation for the first time, you must first call the Cursor operation to obtain the value of `Cursor`. For more information, see [Cursor](https://help.aliyun.com/document_detail/2330730.html).
        # 
        # - When you call this operation again, you can obtain the value of `Cursor` from the response of the last call.
        # 
        # This parameter is required.
        self.cursor = cursor
        # The maximum number of data entries to return each time.
        # 
        # Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.length = length
        # The measurements that are used to customize the returned data. By default, all measurements are returned.
        # 
        # For example, the metric `cpu_idle` of the cloud service `acs_ecs_dashboard` has three measurement columns: `Average`, `Maximum`, and `Minimum`. If you only need to return the `Average` and `Maximum` columns, set this parameter to the array `["Average", "Maximum"]`.
        # 
        # For information about how to obtain the measurements of a metric of a cloud service, see the `statistics` column of [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.measurements_shrink = measurements_shrink
        # The name of the metric of the cloud service.
        # 
        # For information about how to obtain the name of a metric of a cloud service, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > This parameter must be the same as the request parameter `Metric` in the Cursor operation.
        # 
        # This parameter is required.
        self.metric = metric
        # The data namespace of the cloud service.
        # 
        # For information about how to obtain the data namespace of a cloud service, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        # 
        # > This parameter must be the same as the request parameter `Namespace` in the Cursor operation.
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

        if self.measurements_shrink is not None:
            result['Measurements'] = self.measurements_shrink

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
            self.measurements_shrink = m.get('Measurements')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

