# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetSyntheticMonitorsRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.GetSyntheticMonitorsRequestFilter = None,
        region_id: str = None,
    ):
        # The query conditions.
        # 
        # This parameter is required.
        self.filter = filter
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = main_models.GetSyntheticMonitorsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetSyntheticMonitorsRequestFilter(DaraModel):
    def __init__(
        self,
        monitor_category: int = None,
        network: int = None,
        task_type: int = None,
    ):
        # The type of the monitoring point. Valid values: 1: PC. 2: mobile device.
        # 
        # This parameter is required.
        self.monitor_category = monitor_category
        # The network type. Valid values: 1: private network. 2: Internet.
        # 
        # This parameter is required.
        self.network = network
        # The type of the monitoring task. Valid values:
        # 
        # 1: ICMP. 2: TCP. 3: DNS. 4: HTTP. 5: website speed. 6: file download.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_category is not None:
            result['MonitorCategory'] = self.monitor_category

        if self.network is not None:
            result['Network'] = self.network

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorCategory') is not None:
            self.monitor_category = m.get('MonitorCategory')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

