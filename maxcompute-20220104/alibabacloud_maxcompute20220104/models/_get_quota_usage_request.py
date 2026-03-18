# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetQuotaUsageRequest(DaraModel):
    def __init__(
        self,
        agg_method: str = None,
        from_: int = None,
        plot_types: List[str] = None,
        product_id: str = None,
        region: str = None,
        sub_quota_nickname: str = None,
        tenant_id: str = None,
        to: int = None,
        y_axis_types: List[str] = None,
    ):
        self.agg_method = agg_method
        # This parameter is required.
        self.from_ = from_
        self.plot_types = plot_types
        self.product_id = product_id
        self.region = region
        self.sub_quota_nickname = sub_quota_nickname
        self.tenant_id = tenant_id
        # This parameter is required.
        self.to = to
        self.y_axis_types = y_axis_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_method is not None:
            result['aggMethod'] = self.agg_method

        if self.from_ is not None:
            result['from'] = self.from_

        if self.plot_types is not None:
            result['plotTypes'] = self.plot_types

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.region is not None:
            result['region'] = self.region

        if self.sub_quota_nickname is not None:
            result['subQuotaNickname'] = self.sub_quota_nickname

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.to is not None:
            result['to'] = self.to

        if self.y_axis_types is not None:
            result['yAxisTypes'] = self.y_axis_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggMethod') is not None:
            self.agg_method = m.get('aggMethod')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('plotTypes') is not None:
            self.plot_types = m.get('plotTypes')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('subQuotaNickname') is not None:
            self.sub_quota_nickname = m.get('subQuotaNickname')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('yAxisTypes') is not None:
            self.y_axis_types = m.get('yAxisTypes')

        return self

