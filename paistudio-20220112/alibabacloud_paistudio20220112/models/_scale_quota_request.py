# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ScaleQuotaRequest(DaraModel):
    def __init__(
        self,
        min: main_models.ResourceSpec = None,
        resource_group_ids: List[str] = None,
    ):
        self.min = min
        self.resource_group_ids = resource_group_ids

    def validate(self):
        if self.min:
            self.min.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.min is not None:
            result['Min'] = self.min.to_map()

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Min') is not None:
            temp_model = main_models.ResourceSpec()
            self.min = temp_model.from_map(m.get('Min'))

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        return self

