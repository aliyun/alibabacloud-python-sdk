# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class UpdateWarmPoolInput(DaraModel):
    def __init__(
        self,
        capacity_policy: main_models.WarmPoolCapacityPolicyInput = None,
    ):
        # The warm pool capacity policy, which includes the base target capacity and optional scheduled rules.
        # 
        # This parameter is required.
        self.capacity_policy = capacity_policy

    def validate(self):
        if self.capacity_policy:
            self.capacity_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_policy is not None:
            result['capacityPolicy'] = self.capacity_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacityPolicy') is not None:
            temp_model = main_models.WarmPoolCapacityPolicyInput()
            self.capacity_policy = temp_model.from_map(m.get('capacityPolicy'))

        return self

