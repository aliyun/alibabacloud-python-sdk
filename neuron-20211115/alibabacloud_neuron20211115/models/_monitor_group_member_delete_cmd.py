# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MonitorGroupMemberDeleteCmd(DaraModel):
    def __init__(
        self,
        contact_ids: List[int] = None,
        group_id: int = None,
    ):
        self.contact_ids = contact_ids
        # This parameter is required.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['contactIds'] = self.contact_ids

        if self.group_id is not None:
            result['groupId'] = self.group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactIds') is not None:
            self.contact_ids = m.get('contactIds')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        return self

