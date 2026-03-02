# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPbcInvokeReviewsRequest(DaraModel):
    def __init__(
        self,
        applicant: str = None,
        company_id: int = None,
        market_id: int = None,
        order_direction: int = None,
        orderby: int = None,
        reviewer: str = None,
    ):
        self.applicant = applicant
        self.company_id = company_id
        self.market_id = market_id
        self.order_direction = order_direction
        self.orderby = orderby
        self.reviewer = reviewer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant is not None:
            result['applicant'] = self.applicant

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.orderby is not None:
            result['orderby'] = self.orderby

        if self.reviewer is not None:
            result['reviewer'] = self.reviewer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            self.applicant = m.get('applicant')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('orderby') is not None:
            self.orderby = m.get('orderby')

        if m.get('reviewer') is not None:
            self.reviewer = m.get('reviewer')

        return self

