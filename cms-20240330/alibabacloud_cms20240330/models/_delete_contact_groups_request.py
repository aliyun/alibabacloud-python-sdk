# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteContactGroupsRequest(DaraModel):
    def __init__(
        self,
        contact_group_ids: List[str] = None,
    ):
        # The IDs of the contact groups.
        # 
        # This parameter is required.
        self.contact_group_ids = contact_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_ids is not None:
            result['contactGroupIds'] = self.contact_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactGroupIds') is not None:
            self.contact_group_ids = m.get('contactGroupIds')

        return self

