# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_id: int = None,
    ):
        # The ID of the alert contact group.
        # 
        # This parameter is required.
        self.contact_group_id = contact_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')

        return self

