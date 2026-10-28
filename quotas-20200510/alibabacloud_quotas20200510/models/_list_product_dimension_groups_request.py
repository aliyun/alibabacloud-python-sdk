# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductDimensionGroupsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
    ):
        # The maximum number of records to return for the query.
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For information about how to obtain the abbreviation of an Alibaba Cloud service name, see the \\`ProductCode\\` parameter in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code

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

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

