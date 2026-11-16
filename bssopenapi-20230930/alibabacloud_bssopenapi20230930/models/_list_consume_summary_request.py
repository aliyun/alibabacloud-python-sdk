# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListConsumeSummaryRequest(DaraModel):
    def __init__(
        self,
        common_filters: List[main_models.ListConsumeSummaryRequestCommonFilters] = None,
        dimension_type: str = None,
        ec_id_account_ids: List[main_models.ListConsumeSummaryRequestEcIdAccountIds] = None,
        max_results: int = None,
        next_token: str = None,
        period: main_models.ListConsumeSummaryRequestPeriod = None,
    ):
        # The common filter conditions. Valid conditions for different fields take effect simultaneously. For supported fields and operations, see "Common filtering" in the supplementary description of request parameters.
        self.common_filters = common_filters
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
        self.ec_id_account_ids = ec_id_account_ids
        # The maximum number of records expected to be returned for a single query. Specify a positive integer. Keep this value unchanged during pagination. The actual number of returned records may be less than this value.
        self.max_results = max_results
        # The query token for the next page. Do not specify this parameter for the first request. For subsequent requests, pass the value returned in the previous response.
        self.next_token = next_token
        # The query time range, which specifies the time granularity, start time, and end time.
        self.period = period

    def validate(self):
        if self.common_filters:
            for v1 in self.common_filters:
                 if v1:
                    v1.validate()
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()
        if self.period:
            self.period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommonFilters'] = []
        if self.common_filters is not None:
            for k1 in self.common_filters:
                result['CommonFilters'].append(k1.to_map() if k1 else None)

        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_filters = []
        if m.get('CommonFilters') is not None:
            for k1 in m.get('CommonFilters'):
                temp_model = main_models.ListConsumeSummaryRequestCommonFilters()
                self.common_filters.append(temp_model.from_map(k1))

        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.ListConsumeSummaryRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            temp_model = main_models.ListConsumeSummaryRequestPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        return self

class ListConsumeSummaryRequestPeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        granularity: str = None,
        start_time: str = None,
    ):
        # For monthly queries, only one month is supported at a time. The value must be the same as the start month, and the format is `yyyy-MM`.
        # 
        # For daily queries, this parameter is required. The format is `yyyy-MM-dd`. The end date cannot be earlier than the start date, and the start and end dates must be in the same month.
        self.end_time = end_time
        # `MONTHLY`: aggregates by month. `DAILY`: aggregates by day.
        self.granularity = granularity
        # For monthly queries, the format is `yyyy-MM`.
        # 
        # For daily queries, the format is `yyyy-MM-dd`.
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

class ListConsumeSummaryRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # The list of account IDs to query. This parameter is required when an enterprise object is passed. If the entire EcIdAccountIds parameter is omitted, the data of the current calling account is queried by default.
        self.account_ids = account_ids
        # The ID of the enterprise entity.
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

class ListConsumeSummaryRequestCommonFilters(DaraModel):
    def __init__(
        self,
        filter_field: str = None,
        operation: str = None,
        values: List[str] = None,
    ):
        # The name of the filter field. For supported fields and operations, see "Common filtering" in the supplementary description of request parameters.
        self.filter_field = filter_field
        # The operator. Default value: `IN`. `IN` indicates inclusion or exact match, `NOT` indicates exclusion, and `PREFIX` indicates prefix match. For the specific support scope, see "Common filtering" in the supplementary description of request parameters.
        self.operation = operation
        # The filter values always use a string array, including single values, Boolean values, and account IDs.
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

