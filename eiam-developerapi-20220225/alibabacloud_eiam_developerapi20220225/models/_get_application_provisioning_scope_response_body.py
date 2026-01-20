# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetApplicationProvisioningScopeResponseBody(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        organizational_unit_ids: List[str] = None,
    ):
        self.group_ids = group_ids
        # The IDs of organizational units.
        self.organizational_unit_ids = organizational_unit_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['groupIds'] = self.group_ids

        if self.organizational_unit_ids is not None:
            result['organizationalUnitIds'] = self.organizational_unit_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupIds') is not None:
            self.group_ids = m.get('groupIds')

        if m.get('organizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('organizationalUnitIds')

        return self

