# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteYikeAssetMediaInfosRequest(DaraModel):
    def __init__(
        self,
        logic_delete: bool = None,
        media_ids: str = None,
    ):
        self.logic_delete = logic_delete
        self.media_ids = media_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logic_delete is not None:
            result['LogicDelete'] = self.logic_delete

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicDelete') is not None:
            self.logic_delete = m.get('LogicDelete')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        return self

