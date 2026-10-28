# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductQuotaDimensionsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_category: str = None,
    ):
        # The maximum number of entries to return for this query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The pagination token that specifies the starting position of the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviated name of the cloud service.
        # 
        # > For more information about how to obtain the abbreviated name of a cloud service, see `ProductCode` in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The quota category. Valid values:
        # 
        # - FlowControl: API rate limits.
        # 
        # - CommonQuota: general quotas. This is the default value.
        # 
        # > Privileges (WhiteListLabel) do not have quota dimensions.
        self.quota_category = quota_category

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

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        return self

