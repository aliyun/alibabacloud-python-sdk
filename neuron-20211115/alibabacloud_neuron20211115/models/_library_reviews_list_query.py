# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LibraryReviewsListQuery(DaraModel):
    def __init__(
        self,
        applicant: str = None,
        market_id: int = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        reviewer: str = None,
    ):
        self.applicant = applicant
        self.market_id = market_id
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
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

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.reviewer is not None:
            result['reviewer'] = self.reviewer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            self.applicant = m.get('applicant')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('reviewer') is not None:
            self.reviewer = m.get('reviewer')

        return self

