# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBillingOverviewShrinkRequest(DaraModel):
    def __init__(
        self,
        bill_month: str = None,
        filter_shrink: str = None,
        group_by_shrink: str = None,
        locale: str = None,
        region_id: str = None,
        top_num: int = None,
        zero_filter: bool = None,
    ):
        # The billing month. This parameter is required.
        self.bill_month = bill_month
        # The filter condition.
        self.filter_shrink = filter_shrink
        # The list of grouping conditions. Currently, you must specify exactly one grouping dimension.
        self.group_by_shrink = group_by_shrink
        # The response language. Default value: en-US.
        self.locale = locale
        # The region.
        self.region_id = region_id
        # The number of groups to return. Valid values: 1 to 20. Default value: 20.
        self.top_num = top_num
        # Specifies whether to filter out groups with a zero amount. Default value: true.
        self.zero_filter = zero_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_month is not None:
            result['billMonth'] = self.bill_month

        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink

        if self.group_by_shrink is not None:
            result['groupBy'] = self.group_by_shrink

        if self.locale is not None:
            result['locale'] = self.locale

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.top_num is not None:
            result['topNum'] = self.top_num

        if self.zero_filter is not None:
            result['zeroFilter'] = self.zero_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billMonth') is not None:
            self.bill_month = m.get('billMonth')

        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')

        if m.get('groupBy') is not None:
            self.group_by_shrink = m.get('groupBy')

        if m.get('locale') is not None:
            self.locale = m.get('locale')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topNum') is not None:
            self.top_num = m.get('topNum')

        if m.get('zeroFilter') is not None:
            self.zero_filter = m.get('zeroFilter')

        return self

