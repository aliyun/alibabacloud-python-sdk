# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class BillingCostBreakdownRespDTO(DaraModel):
    def __init__(
        self,
        granularity: str = None,
        page: int = None,
        page_size: int = None,
        rows: List[main_models.BillingCostBreakdownRowDTO] = None,
        total: int = None,
    ):
        self.granularity = granularity
        self.page = page
        self.page_size = page_size
        self.rows = rows
        self.total = total

    def validate(self):
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['rows'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.rows = []
        if m.get('rows') is not None:
            for k1 in m.get('rows'):
                temp_model = main_models.BillingCostBreakdownRowDTO()
                self.rows.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

