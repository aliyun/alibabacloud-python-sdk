# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLLMGatewayMetricsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        granularity: str = None,
        instance_name: str = None,
        metric_type: str = None,
        model: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.granularity = granularity
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.metric_type = metric_type
        self.model = model
        self.region_id = region_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.model is not None:
            result['Model'] = self.model

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

