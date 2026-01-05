# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConstraintRequest(DaraModel):
    def __init__(
        self,
        constraint_id: str = None,
    ):
        # The ID of the constraint.
        # 
        # This parameter is required.
        self.constraint_id = constraint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')

        return self

