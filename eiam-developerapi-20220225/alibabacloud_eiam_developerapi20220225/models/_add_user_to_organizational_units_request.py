# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddUserToOrganizationalUnitsRequest(DaraModel):
    def __init__(
        self,
        organizational_unit_ids: List[str] = None,
    ):
        # This parameter is required.
        self.organizational_unit_ids = organizational_unit_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organizational_unit_ids is not None:
            result['organizationalUnitIds'] = self.organizational_unit_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('organizationalUnitIds')

        return self

