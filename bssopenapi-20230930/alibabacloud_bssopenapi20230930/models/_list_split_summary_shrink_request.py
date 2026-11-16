# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSplitSummaryShrinkRequest(DaraModel):
    def __init__(
        self,
        common_filters_shrink: str = None,
        cost_categories_filters_shrink: str = None,
        ec_id_account_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        period_shrink: str = None,
        tag_filters_shrink: str = None,
    ):
        # The common filter conditions. Supports filtering by product, commodity, region, billing item, fee type, resource, account, financial unit, resource group, and split item. Different fields are combined by AND. Only one object can be passed for the same field. For more information, see the supplementary description of request parameters.
        self.common_filters_shrink = common_filters_shrink
        # The cost category filter conditions. Different objects in the list and multiple values of the same cost category are matched by OR. The overall cost category filter is combined with the tag filter and CommonFilters by AND.
        self.cost_categories_filters_shrink = cost_categories_filters_shrink
        # The query scope for enterprises and accounts. If not passed, the bill scope of the current account is queried. Only one enterprise object can be specified per request. The actual accessible scope is limited by permissions.
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # The maximum number of records expected to be returned per page. It is used in conjunction with `NextToken`. Pass a positive integer. We recommend that you explicitly set this parameter and keep it unchanged during pagination. The actual number of returned records may be less than this value.
        self.max_results = max_results
        # The token for the next page of query results. Do not pass this parameter for the first query. For subsequent queries, pass the `NextToken` returned in the previous response as is. The query ends when the token is empty or no longer returned. Do not construct or parse the token yourself. Keep `Period`, account scope, all filter conditions, and `MaxResults` consistent during pagination.
        self.next_token = next_token
        # The query time range. It is required for business logic and includes Granularity, StartTime, and EndTime. Only one billing month can be queried per request. If passed, it overrides the legacy flat time parameters.
        self.period_shrink = period_shrink
        # The resource tag filter conditions. Different objects in the list and multiple values of the same tag key are matched by OR. The overall tag filter is combined with the cost category filter and CommonFilters by AND.
        self.tag_filters_shrink = tag_filters_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_filters_shrink is not None:
            result['CommonFilters'] = self.common_filters_shrink

        if self.cost_categories_filters_shrink is not None:
            result['CostCategoriesFilters'] = self.cost_categories_filters_shrink

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period_shrink is not None:
            result['Period'] = self.period_shrink

        if self.tag_filters_shrink is not None:
            result['TagFilters'] = self.tag_filters_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonFilters') is not None:
            self.common_filters_shrink = m.get('CommonFilters')

        if m.get('CostCategoriesFilters') is not None:
            self.cost_categories_filters_shrink = m.get('CostCategoriesFilters')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period_shrink = m.get('Period')

        if m.get('TagFilters') is not None:
            self.tag_filters_shrink = m.get('TagFilters')

        return self

