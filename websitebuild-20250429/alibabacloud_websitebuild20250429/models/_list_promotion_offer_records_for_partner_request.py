# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPromotionOfferRecordsForPartnerRequest(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        belong_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The activity code.
        self.activity_code = activity_code
        # The belong ID.
        self.belong_id = belong_id
        # The number of entries per query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The token for the next query. This parameter is empty if no more results exist.
        self.next_token = next_token
        # The field used for sorting.
        self.order_column = order_column
        # The sort type. Valid values: ASC and DESC.
        self.order_type = order_type
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code

        if self.belong_id is not None:
            result['BelongId'] = self.belong_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('BelongId') is not None:
            self.belong_id = m.get('BelongId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

