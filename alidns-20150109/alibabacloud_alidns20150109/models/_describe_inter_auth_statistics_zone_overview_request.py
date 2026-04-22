# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInterAuthStatisticsZoneOverviewRequest(DaraModel):
    def __init__(
        self,
        overview_period: str = None,
        server_region: str = None,
        zone_name: str = None,
    ):
        self.overview_period = overview_period
        self.server_region = server_region
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overview_period is not None:
            result['OverviewPeriod'] = self.overview_period

        if self.server_region is not None:
            result['ServerRegion'] = self.server_region

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverviewPeriod') is not None:
            self.overview_period = m.get('OverviewPeriod')

        if m.get('ServerRegion') is not None:
            self.server_region = m.get('ServerRegion')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

