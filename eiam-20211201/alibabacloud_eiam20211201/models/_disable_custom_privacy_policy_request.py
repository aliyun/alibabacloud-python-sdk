# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableCustomPrivacyPolicyRequest(DaraModel):
    def __init__(
        self,
        custom_privacy_policy_id: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.custom_privacy_policy_id = custom_privacy_policy_id
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
        if self.custom_privacy_policy_id is not None:
            result['CustomPrivacyPolicyId'] = self.custom_privacy_policy_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomPrivacyPolicyId') is not None:
            self.custom_privacy_policy_id = m.get('CustomPrivacyPolicyId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

