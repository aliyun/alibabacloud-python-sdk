# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GotoPresetRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        preset_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        # This parameter is required.
        self.preset_id = preset_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.preset_id is not None:
            result['PresetId'] = self.preset_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')

        return self

