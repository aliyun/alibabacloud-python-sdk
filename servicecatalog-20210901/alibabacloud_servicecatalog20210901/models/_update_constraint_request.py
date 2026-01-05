# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConstraintRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        constraint_id: str = None,
        description: str = None,
    ):
        # The configurations of the constraint.
        # 
        # Format: { "LocalRoleName": "\\<role_name>" }.
        # 
        # This parameter is required.
        self.config = config
        # The ID of the constraint.
        # 
        # This parameter is required.
        self.constraint_id = constraint_id
        # The description of the constraint.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

