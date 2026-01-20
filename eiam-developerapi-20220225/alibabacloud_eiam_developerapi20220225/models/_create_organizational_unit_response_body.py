# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrganizationalUnitResponseBody(DaraModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
    ):
        # The ID of the organizational unit.
        self.organizational_unit_id = organizational_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')

        return self

