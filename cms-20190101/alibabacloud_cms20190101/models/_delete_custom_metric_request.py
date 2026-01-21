# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCustomMetricRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        md_5: str = None,
        metric_name: str = None,
        region_id: str = None,
        uuid: str = None,
    ):
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The MD5 value of the HTTP request body. The MD5 value is a 128-bit hash value used to verify the uniqueness of the reported monitoring data.
        # 
        # >  `Md5` is returned when you query the reported monitoring data of a metric.
        self.md_5 = md_5
        # The name of the metric.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        self.region_id = region_id
        # The ID of the request for reporting monitoring data.
        # 
        # >  `UUID` is returned when you query the reported monitoring data of a metric. We recommend that you specify the `Md5` parameter.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['UUID'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        return self

