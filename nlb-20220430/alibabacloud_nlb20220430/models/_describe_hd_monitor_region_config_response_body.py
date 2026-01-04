# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHdMonitorRegionConfigResponseBody(DaraModel):
    def __init__(
        self,
        log_project: str = None,
        metric_store: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The name of the Log Service project.
        self.log_project = log_project
        # The name of the Metricstore in Simple Log Service.
        self.metric_store = metric_store
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to obtain the region ID.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_project is not None:
            result['LogProject'] = self.log_project

        if self.metric_store is not None:
            result['MetricStore'] = self.metric_store

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        if m.get('MetricStore') is not None:
            self.metric_store = m.get('MetricStore')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

