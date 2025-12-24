# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetInstanceSummaryResponseBody(DaraModel):
    def __init__(
        self,
        locking_count: int = None,
        regional_summary: List[main_models.GetInstanceSummaryResponseBodyRegionalSummary] = None,
        request_id: str = None,
        running_count: int = None,
        total: int = None,
    ):
        self.locking_count = locking_count
        self.regional_summary = regional_summary
        self.request_id = request_id
        self.running_count = running_count
        self.total = total

    def validate(self):
        if self.regional_summary:
            for v1 in self.regional_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.locking_count is not None:
            result['LockingCount'] = self.locking_count

        result['RegionalSummary'] = []
        if self.regional_summary is not None:
            for k1 in self.regional_summary:
                result['RegionalSummary'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_count is not None:
            result['RunningCount'] = self.running_count

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockingCount') is not None:
            self.locking_count = m.get('LockingCount')

        self.regional_summary = []
        if m.get('RegionalSummary') is not None:
            for k1 in m.get('RegionalSummary'):
                temp_model = main_models.GetInstanceSummaryResponseBodyRegionalSummary()
                self.regional_summary.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetInstanceSummaryResponseBodyRegionalSummary(DaraModel):
    def __init__(
        self,
        locking_count: int = None,
        region_id: str = None,
        running_count: int = None,
        total: int = None,
    ):
        self.locking_count = locking_count
        self.region_id = region_id
        self.running_count = running_count
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.locking_count is not None:
            result['LockingCount'] = self.locking_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.running_count is not None:
            result['RunningCount'] = self.running_count

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockingCount') is not None:
            self.locking_count = m.get('LockingCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

