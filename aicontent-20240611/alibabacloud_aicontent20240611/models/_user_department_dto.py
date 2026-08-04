# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UserDepartmentDTO(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        client_name: str = None,
        role_code: str = None,
        role_name: str = None,
    ):
        self.client_id = client_id
        self.client_name = client_name
        self.role_code = role_code
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_name is not None:
            result['clientName'] = self.client_name

        if self.role_code is not None:
            result['roleCode'] = self.role_code

        if self.role_name is not None:
            result['roleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')

        if m.get('roleCode') is not None:
            self.role_code = m.get('roleCode')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        return self

