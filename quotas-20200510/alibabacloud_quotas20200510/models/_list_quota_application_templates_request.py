# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaApplicationTemplatesRequest(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.ListQuotaApplicationTemplatesRequestDimensions] = None,
        id: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        # The quota dimensions.
        self.dimensions = dimensions
        # The ID of the quota item.
        self.id = id
        # The maximum number of records that can be returned for the query. Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query.
        # 
        # > If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > To query the abbreviation of an Alibaba Cloud service name, call the [ListProducts](https://help.aliyun.com/document_detail/440555.html) operation and check the value of `ProductCode` in the response.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # 
        # - CommonQuota: general quota.
        # 
        # - WhiteListLabel: whitelist quota.
        # 
        # - FlowControl: API rate limit.
        self.quota_category = quota_category

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

        if self.id is not None:
            result['Id'] = self.id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.ListQuotaApplicationTemplatesRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        return self

class ListQuotaApplicationTemplatesRequestDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # >
        # 
        # - The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # 
        # - You must specify both Key and Value for each quota dimension.
        self.key = key
        # The value of the dimension.
        # 
        # >
        # 
        # - The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # 
        # - You must specify both Key and Value for each quota dimension.
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

