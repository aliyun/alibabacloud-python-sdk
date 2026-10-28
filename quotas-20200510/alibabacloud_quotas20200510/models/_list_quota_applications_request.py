# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaApplicationsRequest(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.ListQuotaApplicationsRequestDimensions] = None,
        key_word: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        status: str = None,
    ):
        # The quota dimensions.
        # The dimensions are properties of a quota item. A combination of dimensions (Dimensions) and a quota ID (QuotaActionCode) uniquely identifies a quota item.
        # > Some cloud services require dimensions. You can call [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) to query the quota dimensions supported by a cloud service. The `Requisite` response parameter indicates whether a dimension is required.
        self.dimensions = dimensions
        # The keyword for searching quota increase applications.
        self.key_word = key_word
        # The maximum number of records to return in this query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. Leave this parameter empty to query from the beginning.
        self.next_token = next_token
        # The abbreviation of the cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota category. Valid values:
        # - CommonQuota: general quota.
        # - FlowControl: API rate limit.
        # - WhiteListLabel: privilege.
        self.quota_category = quota_category
        # The approval status of the quota increase application. Valid values:
        # 
        # - Disagree: Rejected.
        # 
        # - Agree: Approved.
        # 
        # - Process: Under review.
        # 
        # - Cancel: Closed.
        self.status = status

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.ListQuotaApplicationsRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListQuotaApplicationsRequestDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > `Dimensions.N.Key` and `Dimensions.N.Value` must be specified together. The valid values of N depend on the number of dimensions supported by the cloud service. You can call [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) to query the quota dimensions supported by a cloud service. The length of the returned array is the value of N.
        self.key = key
        # The value of the quota dimension.
        # 
        # > `Dimensions.N.Key` and `Dimensions.N.Value` must be specified together. The valid values of N depend on the number of dimensions supported by the cloud service. You can call [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) to query the quota dimensions supported by a cloud service. The length of the returned array is the value of N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

