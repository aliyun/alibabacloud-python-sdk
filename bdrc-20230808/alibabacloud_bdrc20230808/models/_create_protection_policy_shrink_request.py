# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProtectionPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        bound_resource_category_ids_shrink: str = None,
        client_token: str = None,
        protection_policy_name: str = None,
        protection_policy_region_id: str = None,
        sub_protection_policies_shrink: str = None,
    ):
        # The IDs of associated resource categories.
        self.bound_resource_category_ids_shrink = bound_resource_category_ids_shrink
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
        self.sub_protection_policies_shrink = sub_protection_policies_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_resource_category_ids_shrink is not None:
            result['BoundResourceCategoryIds'] = self.bound_resource_category_ids_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.protection_policy_name is not None:
            result['ProtectionPolicyName'] = self.protection_policy_name

        if self.protection_policy_region_id is not None:
            result['ProtectionPolicyRegionId'] = self.protection_policy_region_id

        if self.sub_protection_policies_shrink is not None:
            result['SubProtectionPolicies'] = self.sub_protection_policies_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundResourceCategoryIds') is not None:
            self.bound_resource_category_ids_shrink = m.get('BoundResourceCategoryIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProtectionPolicyName') is not None:
            self.protection_policy_name = m.get('ProtectionPolicyName')

        if m.get('ProtectionPolicyRegionId') is not None:
            self.protection_policy_region_id = m.get('ProtectionPolicyRegionId')

        if m.get('SubProtectionPolicies') is not None:
            self.sub_protection_policies_shrink = m.get('SubProtectionPolicies')

        return self

