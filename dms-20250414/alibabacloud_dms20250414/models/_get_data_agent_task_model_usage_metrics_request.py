# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetDataAgentTaskModelUsageMetricsRequest(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        dmsunit: str = None,
        end_time: str = None,
        instance_ids: List[str] = None,
        pay_level: str = None,
        region_id: str = None,
    ):
        # The start time of the query time range. The value is a UNIX timestamp in seconds. The recommended interval length is no longer than one month.
        self.begin_time = begin_time
        # The current DMS unit.
        self.dmsunit = dmsunit
        # The end time of the query time range. The value is a UNIX timestamp in seconds. The recommended interval length is no longer than one month.
        self.end_time = end_time
        self.instance_ids = instance_ids
        self.pay_level = pay_level
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.pay_level is not None:
            result['PayLevel'] = self.pay_level

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PayLevel') is not None:
            self.pay_level = m.get('PayLevel')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

