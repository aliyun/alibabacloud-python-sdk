# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOrganizationalUnitParentIdsResponseBody(DaraModel):
    def __init__(
        self,
        parent_ids: List[str] = None,
    ):
        # The IDs of the parent organizational units. The IDs of the organizational unit are ordered based on their levels from high to low. Only the IDs of the organizational units within the authorization scope are displayed.
        self.parent_ids = parent_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parent_ids is not None:
            result['parentIds'] = self.parent_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentIds') is not None:
            self.parent_ids = m.get('parentIds')

        return self

