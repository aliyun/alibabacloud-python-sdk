# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListSplitSummaryRequest(DaraModel):
    def __init__(
        self,
        common_filters: List[main_models.ListSplitSummaryRequestCommonFilters] = None,
        cost_categories_filters: List[main_models.ListSplitSummaryRequestCostCategoriesFilters] = None,
        ec_id_account_ids: List[main_models.ListSplitSummaryRequestEcIdAccountIds] = None,
        max_results: int = None,
        next_token: str = None,
        period: main_models.ListSplitSummaryRequestPeriod = None,
        tag_filters: List[main_models.ListSplitSummaryRequestTagFilters] = None,
    ):
        # The common filter conditions. Supports filtering by product, commodity, region, billing item, fee type, resource, account, financial unit, resource group, and split item. Different fields are combined by AND. Only one object can be passed for the same field. For more information, see the supplementary description of request parameters.
        self.common_filters = common_filters
        # The cost category filter conditions. Different objects in the list and multiple values of the same cost category are matched by OR. The overall cost category filter is combined with the tag filter and CommonFilters by AND.
        self.cost_categories_filters = cost_categories_filters
        # The query scope for enterprises and accounts. If not passed, the bill scope of the current account is queried. Only one enterprise object can be specified per request. The actual accessible scope is limited by permissions.
        self.ec_id_account_ids = ec_id_account_ids
        # The maximum number of records expected to be returned per page. It is used in conjunction with `NextToken`. Pass a positive integer. We recommend that you explicitly set this parameter and keep it unchanged during pagination. The actual number of returned records may be less than this value.
        self.max_results = max_results
        # The token for the next page of query results. Do not pass this parameter for the first query. For subsequent queries, pass the `NextToken` returned in the previous response as is. The query ends when the token is empty or no longer returned. Do not construct or parse the token yourself. Keep `Period`, account scope, all filter conditions, and `MaxResults` consistent during pagination.
        self.next_token = next_token
        # The query time range. It is required for business logic and includes Granularity, StartTime, and EndTime. Only one billing month can be queried per request. If passed, it overrides the legacy flat time parameters.
        self.period = period
        # The resource tag filter conditions. Different objects in the list and multiple values of the same tag key are matched by OR. The overall tag filter is combined with the cost category filter and CommonFilters by AND.
        self.tag_filters = tag_filters

    def validate(self):
        if self.common_filters:
            for v1 in self.common_filters:
                 if v1:
                    v1.validate()
        if self.cost_categories_filters:
            for v1 in self.cost_categories_filters:
                 if v1:
                    v1.validate()
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()
        if self.period:
            self.period.validate()
        if self.tag_filters:
            for v1 in self.tag_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommonFilters'] = []
        if self.common_filters is not None:
            for k1 in self.common_filters:
                result['CommonFilters'].append(k1.to_map() if k1 else None)

        result['CostCategoriesFilters'] = []
        if self.cost_categories_filters is not None:
            for k1 in self.cost_categories_filters:
                result['CostCategoriesFilters'].append(k1.to_map() if k1 else None)

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period.to_map()

        result['TagFilters'] = []
        if self.tag_filters is not None:
            for k1 in self.tag_filters:
                result['TagFilters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_filters = []
        if m.get('CommonFilters') is not None:
            for k1 in m.get('CommonFilters'):
                temp_model = main_models.ListSplitSummaryRequestCommonFilters()
                self.common_filters.append(temp_model.from_map(k1))

        self.cost_categories_filters = []
        if m.get('CostCategoriesFilters') is not None:
            for k1 in m.get('CostCategoriesFilters'):
                temp_model = main_models.ListSplitSummaryRequestCostCategoriesFilters()
                self.cost_categories_filters.append(temp_model.from_map(k1))

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.ListSplitSummaryRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            temp_model = main_models.ListSplitSummaryRequestPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        self.tag_filters = []
        if m.get('TagFilters') is not None:
            for k1 in m.get('TagFilters'):
                temp_model = main_models.ListSplitSummaryRequestTagFilters()
                self.tag_filters.append(temp_model.from_map(k1))

        return self

class ListSplitSummaryRequestTagFilters(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # The tag key. It cannot be empty or a string of only whitespace characters.
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The list of tag values. Matches any given value under the specified tag key. If this parameter is not passed or an empty array is passed, it only requires the existence of the tag key.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_values is not None:
            result['TagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')

        return self

class ListSplitSummaryRequestPeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        granularity: str = None,
        start_time: str = None,
    ):
        # The end time. It is inclusive. It is required for `DAILY` and the format is `yyyy-MM-dd`. It cannot be earlier than `StartTime` and must be in the same month as `StartTime`. It is optional for `MONTHLY`, but if passed, it must be the same as `StartTime`.
        self.end_time = end_time
        # The time granularity. This parameter is required for business logic and is case-insensitive. Valid values:
        # - DAILY: aggregates by day
        # - MONTHLY: aggregates by month
        self.granularity = granularity
        # The start time. It is required for business logic and is inclusive. The format is yyyy-MM for MONTHLY and yyyy-MM-dd for DAILY.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListSplitSummaryRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # The list of account IDs to access. If it is empty, all accounts under the current enterprise entity are selected. The actual scope is limited by permissions.
        self.account_ids = account_ids
        # The enterprise entity ID.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

class ListSplitSummaryRequestCostCategoriesFilters(DaraModel):
    def __init__(
        self,
        cost_categories_key: str = None,
        cost_categories_values: List[str] = None,
    ):
        # The cost category name. It cannot be empty or a string of only whitespace characters.
        # 
        # This parameter is required.
        self.cost_categories_key = cost_categories_key
        # The list of cost category values. Matches any given value under the specified cost category. If this parameter is not passed or an empty array is passed, it only requires the existence of the cost category.
        self.cost_categories_values = cost_categories_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_categories_key is not None:
            result['CostCategoriesKey'] = self.cost_categories_key

        if self.cost_categories_values is not None:
            result['CostCategoriesValues'] = self.cost_categories_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCategoriesKey') is not None:
            self.cost_categories_key = m.get('CostCategoriesKey')

        if m.get('CostCategoriesValues') is not None:
            self.cost_categories_values = m.get('CostCategoriesValues')

        return self

class ListSplitSummaryRequestCommonFilters(DaraModel):
    def __init__(
        self,
        filter_field: str = None,
        operation: str = None,
        values: List[str] = None,
    ):
        # The name of the filter field. It is required when setting conditions. For supported fields and matching rules, see the supplementary description of request parameters.
        self.filter_field = filter_field
        # The matching method. This parameter is case-insensitive and defaults to IN if it is not specified or is empty. Valid values:
        # - IN: includes
        # - NOT: excludes
        # - PREFIX: literal prefix match
        # For the supported scope of each field, refer to the supplementary description of the request parameters.
        self.operation = operation
        # The filter values. It is always an array of strings. Arrays are also used for single values, Boolean values, and account IDs.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_field is not None:
            result['FilterField'] = self.filter_field

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterField') is not None:
            self.filter_field = m.get('FilterField')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

