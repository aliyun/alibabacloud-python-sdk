# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentAuthorizationPrincipal(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # This parameter is required.
        self.principal_id = principal_id
        # This parameter is required.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        return self

