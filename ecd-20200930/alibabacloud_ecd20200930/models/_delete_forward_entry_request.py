# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteForwardEntryRequest(DaraModel):
    def __init__(
        self,
        forward_entry_id: str = None,
        forward_table_id: str = None,
        region_id: str = None,
    ):
        self.forward_entry_id = forward_entry_id
        # This parameter is required.
        self.forward_table_id = forward_table_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id

        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')

        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

