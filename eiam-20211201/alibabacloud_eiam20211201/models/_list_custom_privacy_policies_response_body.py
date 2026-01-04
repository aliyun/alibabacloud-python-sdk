# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListCustomPrivacyPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        custom_privacy_policies: List[main_models.ListCustomPrivacyPoliciesResponseBodyCustomPrivacyPolicies] = None,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.custom_privacy_policies = custom_privacy_policies
        # 分页查询时每页行数。
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        # 本次调用返回的查询凭证（Token）值，用于上一次翻页查询。
        self.previous_token = previous_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.custom_privacy_policies:
            for v1 in self.custom_privacy_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomPrivacyPolicies'] = []
        if self.custom_privacy_policies is not None:
            for k1 in self.custom_privacy_policies:
                result['CustomPrivacyPolicies'].append(k1.to_map() if k1 else None)

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
        self.custom_privacy_policies = []
        if m.get('CustomPrivacyPolicies') is not None:
            for k1 in m.get('CustomPrivacyPolicies'):
                temp_model = main_models.ListCustomPrivacyPoliciesResponseBodyCustomPrivacyPolicies()
                self.custom_privacy_policies.append(temp_model.from_map(k1))

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

class ListCustomPrivacyPoliciesResponseBodyCustomPrivacyPolicies(DaraModel):
    def __init__(
        self,
        custom_privacy_policy_id: str = None,
        custom_privacy_policy_name: str = None,
        default_language_code: str = None,
        instance_id: str = None,
        status: str = None,
        user_consent_type: str = None,
    ):
        # 自定义条款Id
        self.custom_privacy_policy_id = custom_privacy_policy_id
        # 自定义条款名称
        self.custom_privacy_policy_name = custom_privacy_policy_name
        # 若显示语言未配置时，门户侧展示默认语言展示条款。
        self.default_language_code = default_language_code
        # 实例id
        self.instance_id = instance_id
        # 自定义条款状态
        self.status = status
        # 自定义条款同意类型，是默认同意，还是用户勾选同意
        self.user_consent_type = user_consent_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_privacy_policy_id is not None:
            result['CustomPrivacyPolicyId'] = self.custom_privacy_policy_id

        if self.custom_privacy_policy_name is not None:
            result['CustomPrivacyPolicyName'] = self.custom_privacy_policy_name

        if self.default_language_code is not None:
            result['DefaultLanguageCode'] = self.default_language_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_consent_type is not None:
            result['UserConsentType'] = self.user_consent_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPrivacyPolicyId') is not None:
            self.custom_privacy_policy_id = m.get('CustomPrivacyPolicyId')

        if m.get('CustomPrivacyPolicyName') is not None:
            self.custom_privacy_policy_name = m.get('CustomPrivacyPolicyName')

        if m.get('DefaultLanguageCode') is not None:
            self.default_language_code = m.get('DefaultLanguageCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserConsentType') is not None:
            self.user_consent_type = m.get('UserConsentType')

        return self

