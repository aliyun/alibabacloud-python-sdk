# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAnswerSampleRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        self.ids = ids
        self.lib_id = lib_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

