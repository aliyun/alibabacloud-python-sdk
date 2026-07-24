# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PricingRequest(DaraModel):
    def __init__(
        self,
        solution_id: str = None,
    ):
        # solution_id.
        # 
        # This parameter is required.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.solution_id is not None:
            result['solution_id'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

