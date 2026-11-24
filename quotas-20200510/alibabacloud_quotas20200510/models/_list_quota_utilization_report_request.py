# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListQuotaUtilizationReportRequest(DaraModel):
    def __init__(
        self,
        adjustable: bool = None,
        key_words: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_category: str = None,
        quota_region_id: str = None,
        utilization_statuses: List[str] = None,
    ):
        # Specifies whether to filter quotas by adjustability. Valid values:
        # - true: Queries only adjustable quotas.
        # - false: Queries only non-adjustable quotas.
        # If this parameter is not specified, quotas are not filtered by adjustability.
        self.adjustable = adjustable
        # The search keyword. Performs a fuzzy match based on the quota name or quota ID.
        self.key_words = key_words
        # The maximum number of entries to return for this query.
        self.max_results = max_results
        # The pagination token. Do not specify this parameter for the first query. For subsequent queries, pass the NextToken value returned in the previous response as is, and keep the quota type and filter conditions unchanged. Do not parse or construct the token.
        self.next_token = next_token
        # The abbreviation of the cloud service.
        # 
        # > For information about how to obtain the abbreviation of a cloud service, see ProductCode in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        self.product_code = product_code
        # CommonQuota, FlowControl
        self.quota_category = quota_category
        # The region ID of the quota, such as cn-hangzhou. If this parameter is not specified or is left empty, quotas are not filtered by region.
        self.quota_region_id = quota_region_id
        # The utilization statuses. You can specify multiple values. If this parameter is not specified or an empty list is passed, quotas are not filtered by utilization status.
        self.utilization_statuses = utilization_statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable

        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        if self.quota_region_id is not None:
            result['QuotaRegionId'] = self.quota_region_id

        if self.utilization_statuses is not None:
            result['UtilizationStatuses'] = self.utilization_statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')

        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        if m.get('QuotaRegionId') is not None:
            self.quota_region_id = m.get('QuotaRegionId')

        if m.get('UtilizationStatuses') is not None:
            self.utilization_statuses = m.get('UtilizationStatuses')

        return self

