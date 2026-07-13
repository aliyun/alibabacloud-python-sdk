# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class CreateProtectionPolicyRequest(DaraModel):
    def __init__(
        self,
        bound_resource_category_ids: List[str] = None,
        client_token: str = None,
        protection_policy_name: str = None,
        protection_policy_region_id: str = None,
        sub_protection_policies: List[main_models.CreateProtectionPolicyRequestSubProtectionPolicies] = None,
    ):
        # The IDs of associated resource categories.
        self.bound_resource_category_ids = bound_resource_category_ids
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The name of the protection policy.
        # 
        # This parameter is required.
        self.protection_policy_name = protection_policy_name
        # The region ID of the protection policy.
        # 
        # This parameter is required.
        self.protection_policy_region_id = protection_policy_region_id
        # The sub-protection policies.
        # 
        # This parameter is required.
        self.sub_protection_policies = sub_protection_policies

    def validate(self):
        if self.sub_protection_policies:
            for v1 in self.sub_protection_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_resource_category_ids is not None:
            result['BoundResourceCategoryIds'] = self.bound_resource_category_ids

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.protection_policy_name is not None:
            result['ProtectionPolicyName'] = self.protection_policy_name

        if self.protection_policy_region_id is not None:
            result['ProtectionPolicyRegionId'] = self.protection_policy_region_id

        result['SubProtectionPolicies'] = []
        if self.sub_protection_policies is not None:
            for k1 in self.sub_protection_policies:
                result['SubProtectionPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundResourceCategoryIds') is not None:
            self.bound_resource_category_ids = m.get('BoundResourceCategoryIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProtectionPolicyName') is not None:
            self.protection_policy_name = m.get('ProtectionPolicyName')

        if m.get('ProtectionPolicyRegionId') is not None:
            self.protection_policy_region_id = m.get('ProtectionPolicyRegionId')

        self.sub_protection_policies = []
        if m.get('SubProtectionPolicies') is not None:
            for k1 in m.get('SubProtectionPolicies'):
                temp_model = main_models.CreateProtectionPolicyRequestSubProtectionPolicies()
                self.sub_protection_policies.append(temp_model.from_map(k1))

        return self

class CreateProtectionPolicyRequestSubProtectionPolicies(DaraModel):
    def __init__(
        self,
        config: str = None,
        sub_protection_policy_type: str = None,
    ):
        # The configuration of the sub-protection policy.
        self.config = config
        # The type of the sub-protection policy.
        # 
        # This parameter is required.
        self.sub_protection_policy_type = sub_protection_policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.sub_protection_policy_type is not None:
            result['SubProtectionPolicyType'] = self.sub_protection_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('SubProtectionPolicyType') is not None:
            self.sub_protection_policy_type = m.get('SubProtectionPolicyType')

        return self

