# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloneVoiceRequest(DaraModel):
    def __init__(
        self,
        business_unit_id: str = None,
        clone_voice_id: str = None,
        name: str = None,
    ):
        self.business_unit_id = business_unit_id
        self.clone_voice_id = clone_voice_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.clone_voice_id is not None:
            result['CloneVoiceId'] = self.clone_voice_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('CloneVoiceId') is not None:
            self.clone_voice_id = m.get('CloneVoiceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

