# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListCustomPrivacyPoliciesForBrandResponseBody(DaraModel):
    def __init__(
        self,
        brand_custom_privacy_policies: List[main_models.ListCustomPrivacyPoliciesForBrandResponseBodyBrandCustomPrivacyPolicies] = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.brand_custom_privacy_policies = brand_custom_privacy_policies
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        # 本次调用返回的查询凭证（Token）值，用于上一次翻页查询。
        self.previous_token = previous_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.brand_custom_privacy_policies:
            for v1 in self.brand_custom_privacy_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BrandCustomPrivacyPolicies'] = []
        if self.brand_custom_privacy_policies is not None:
            for k1 in self.brand_custom_privacy_policies:
                result['BrandCustomPrivacyPolicies'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.brand_custom_privacy_policies = []
        if m.get('BrandCustomPrivacyPolicies') is not None:
            for k1 in m.get('BrandCustomPrivacyPolicies'):
                temp_model = main_models.ListCustomPrivacyPoliciesForBrandResponseBodyBrandCustomPrivacyPolicies()
                self.brand_custom_privacy_policies.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomPrivacyPoliciesForBrandResponseBodyBrandCustomPrivacyPolicies(DaraModel):
    def __init__(
        self,
        custom_privacy_policy_id: str = None,
    ):
        # 条款ID
        self.custom_privacy_policy_id = custom_privacy_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_privacy_policy_id is not None:
            result['CustomPrivacyPolicyId'] = self.custom_privacy_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPrivacyPolicyId') is not None:
            self.custom_privacy_policy_id = m.get('CustomPrivacyPolicyId')

        return self

