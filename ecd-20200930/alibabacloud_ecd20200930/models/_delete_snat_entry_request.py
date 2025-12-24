# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSnatEntryRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        snat_entry_id: str = None,
        snat_table_id: str = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.snat_entry_id = snat_entry_id
        # This parameter is required.
        self.snat_table_id = snat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        return self

