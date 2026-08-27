# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBillingTrendShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_shrink: str = None,
        granularity: str = None,
        group_by_shrink: str = None,
        locale: str = None,
        region_id: str = None,
        time_period_shrink: str = None,
        top_num: int = None,
        zero_filter: bool = None,
    ):
        self.filter_shrink = filter_shrink
        self.granularity = granularity
        self.group_by_shrink = group_by_shrink
        self.locale = locale
        self.region_id = region_id
        self.time_period_shrink = time_period_shrink
        self.top_num = top_num
        self.zero_filter = zero_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.group_by_shrink is not None:
            result['groupBy'] = self.group_by_shrink

        if self.locale is not None:
            result['locale'] = self.locale

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.time_period_shrink is not None:
            result['timePeriod'] = self.time_period_shrink

        if self.top_num is not None:
            result['topNum'] = self.top_num

        if self.zero_filter is not None:
            result['zeroFilter'] = self.zero_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('groupBy') is not None:
            self.group_by_shrink = m.get('groupBy')

        if m.get('locale') is not None:
            self.locale = m.get('locale')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('timePeriod') is not None:
            self.time_period_shrink = m.get('timePeriod')

        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')

        if m.get('zeroFilter') is not None:
            self.zero_filter = m.get('zeroFilter')

        return self

