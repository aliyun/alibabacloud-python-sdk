# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSnatEntryRequest(DaraModel):
    def __init__(
        self,
        snat_entry_id: str = None,
    ):
        # The ID of the SNAT entry that you want to delete.
        # 
        # This parameter is required.
        self.snat_entry_id = snat_entry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        return self

