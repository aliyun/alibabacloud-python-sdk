# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListProductQuotasRequest(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.ListProductQuotasRequestDimensions] = None,
        group_code: str = None,
        key_word: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        sort_field: str = None,
        sort_order: str = None,
    ):
        # The quota dimensions.
        self.dimensions = dimensions
        # The code of the dimension group.
        self.group_code = group_code
        # The search keyword for the quota.
        # > This parameter applies only to Elastic Computing Service server instance type quotas (ecs-spec). The search scope includes `QuotaName` and `QuotaActionCode`.
        self.key_word = key_word
        # The maximum number of entries to return in a single request.
        # 
        # Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token used to retrieve the next page of results.
        # 
        # - Leave this parameter empty for the first request or when no more results are available.
        # - If more results are available, set this parameter to the NextToken value returned when you invoke the previous API call.
        self.next_token = next_token
        # The abbreviation of the cloud service.
        # 
        # > For more information about how to obtain the abbreviation of a cloud service, see `ProductCode` in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The quota category.
        # 
        # Default value: CommonQuota.
        self.quota_category = quota_category
        # The sorting method supported by the quota.
        # 
        # > This parameter applies only to Elastic Computing Service server instance type quotas (ecs-spec). If no Settings are specified, it is left empty.
        self.sort_field = sort_field
        # The sorting method supported by the quota.
        # 
        # > This parameter applies only to Elastic Computing Service server instance type quotas (ecs-spec). If no Settings are specified, it is left empty.
        self.sort_order = sort_order

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

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

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

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.ListProductQuotasRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

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

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class ListProductQuotasRequestDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > The value range of N depends on the number of dimensions supported by the corresponding cloud service.
        self.key = key
        # The value of the quota dimension.
        # 
        # > The value range of N depends on the number of dimensions supported by the corresponding cloud service.
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

