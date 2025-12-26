# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        app_policy_id: str = None,
        product_type: str = None,
        video_policy_shrink: str = None,
    ):
        # The policy ID.
        # 
        # This parameter is required.
        self.app_policy_id = app_policy_id
        # The product type.
        # 
        # Enumerated values:
        # 
        # *   CloudApp: RDS Cloud App
        # 
        # This parameter is required.
        self.product_type = product_type
        # Displays the policy.
        self.video_policy_shrink = video_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.video_policy_shrink is not None:
            result['VideoPolicy'] = self.video_policy_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('VideoPolicy') is not None:
            self.video_policy_shrink = m.get('VideoPolicy')

        return self

