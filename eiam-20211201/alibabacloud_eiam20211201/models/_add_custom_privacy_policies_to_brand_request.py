# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddCustomPrivacyPoliciesToBrandRequest(DaraModel):
    def __init__(
        self,
        brand_id: str = None,
        custom_privacy_policy_ids: List[str] = None,
        instance_id: str = None,
    ):
        # 品牌化Id
        # 
        # This parameter is required.
        self.brand_id = brand_id
        # 条款ID列表
        # 
        # This parameter is required.
        self.custom_privacy_policy_ids = custom_privacy_policy_ids
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_id is not None:
            result['BrandId'] = self.brand_id

        if self.custom_privacy_policy_ids is not None:
            result['CustomPrivacyPolicyIds'] = self.custom_privacy_policy_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')

        if m.get('CustomPrivacyPolicyIds') is not None:
            self.custom_privacy_policy_ids = m.get('CustomPrivacyPolicyIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

