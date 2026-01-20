# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PatchOrganizationalUnitRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        organizational_unit_name: str = None,
    ):
        # The description of the organizational unit.
        self.description = description
        # The name of the organizational unit.
        self.organizational_unit_name = organizational_unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')

        return self

