# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitIndexJobRequest(DaraModel):
    def __init__(
        self,
        index_id: str = None,
    ):
        # The knowledge base ID, which is the `Data.Id` returned by the **CreateIndex** operation.
        # 
        # This parameter is required.
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_id is not None:
            result['IndexId'] = self.index_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        return self

