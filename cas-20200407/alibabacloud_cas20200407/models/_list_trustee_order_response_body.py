# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTrusteeOrderResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        trustee_order_list: str = None,
    ):
        # The maximum number of records to return in this request.
        self.max_results = max_results
        # The token for the next query. If NextToken is empty, no more results are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of orders.
        self.total_count = total_count
        # The list of orders.
        self.trustee_order_list = trustee_order_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.trustee_order_list is not None:
            result['TrusteeOrderList'] = self.trustee_order_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TrusteeOrderList') is not None:
            self.trustee_order_list = m.get('TrusteeOrderList')

        return self

