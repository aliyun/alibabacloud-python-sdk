# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DepartmentRoleCmd(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        role_code: str = None,
    ):
        self.client_id = client_id
        self.role_code = role_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.role_code is not None:
            result['roleCode'] = self.role_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('roleCode') is not None:
            self.role_code = m.get('roleCode')

        return self

