# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class CreateWarmPoolInput(DaraModel):
    def __init__(
        self,
        capacity_policy: main_models.WarmPoolCapacityPolicyInput = None,
        template_id: str = None,
    ):
        # The warm pool capacity policy, which includes the base target capacity and optional scheduled rules.
        # 
        # This parameter is required.
        self.capacity_policy = capacity_policy
        # The template ID, which specifies the template associated with the warm pool.
        # 
        # This parameter is required.
        self.template_id = template_id

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

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capacityPolicy') is not None:
            temp_model = main_models.WarmPoolCapacityPolicyInput()
            self.capacity_policy = temp_model.from_map(m.get('capacityPolicy'))

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

