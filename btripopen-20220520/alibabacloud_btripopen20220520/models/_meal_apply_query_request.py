# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MealApplyQueryRequest(DaraModel):
    def __init__(
        self,
        third_part_apply_id: str = None,
    ):
        # This parameter is required.
        self.third_part_apply_id = third_part_apply_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        return self

