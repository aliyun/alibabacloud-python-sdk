# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMonitorGroupMemberRequest(DaraModel):
    def __init__(
        self,
        contact_ids: str = None,
    ):
        # This parameter is required.
        self.contact_ids = contact_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['contactIds'] = self.contact_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactIds') is not None:
            self.contact_ids = m.get('contactIds')

        return self

