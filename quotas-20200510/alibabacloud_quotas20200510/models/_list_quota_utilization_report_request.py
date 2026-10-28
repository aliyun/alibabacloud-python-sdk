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
        self.adjustable = adjustable
        self.key_words = key_words
        self.max_results = max_results
        self.next_token = next_token
        self.product_code = product_code
        self.quota_category = quota_category
        self.quota_region_id = quota_region_id
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

