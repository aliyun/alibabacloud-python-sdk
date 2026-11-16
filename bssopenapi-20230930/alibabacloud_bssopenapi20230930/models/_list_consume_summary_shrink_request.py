# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConsumeSummaryShrinkRequest(DaraModel):
    def __init__(
        self,
        common_filters_shrink: str = None,
        dimension_type: str = None,
        ec_id_account_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        period_shrink: str = None,
    ):
        # The common filter conditions. Valid conditions for different fields take effect simultaneously. For supported fields and operations, see "Common filtering" in the supplementary description of request parameters.
        self.common_filters_shrink = common_filters_shrink
        # The aggregation dimension.
        # 
        # `BILLING_ITEM`: aggregates by billing item. This is the default value.
        # 
        # `RESOURCE`: aggregates by resource.
        # 
        # `PRODUCT`: aggregates by product.
        # 
        # `ACCOUNT`: aggregates by account.
        self.dimension_type = dimension_type
        # The query scope for enterprises and accounts. If this parameter is not specified, the default billing scope of the current calling account is used. Only one enterprise object can be specified per request, and the actual scope is limited by permissions.
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # The maximum number of records expected to be returned for a single query. Specify a positive integer. Keep this value unchanged during pagination. The actual number of returned records may be less than this value.
        self.max_results = max_results
        # The query token for the next page. Do not specify this parameter for the first request. For subsequent requests, pass the value returned in the previous response.
        self.next_token = next_token
        # The query time range, which specifies the time granularity, start time, and end time.
        self.period_shrink = period_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_filters_shrink is not None:
            result['CommonFilters'] = self.common_filters_shrink

        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period_shrink is not None:
            result['Period'] = self.period_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonFilters') is not None:
            self.common_filters_shrink = m.get('CommonFilters')

        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period_shrink = m.get('Period')

        return self

