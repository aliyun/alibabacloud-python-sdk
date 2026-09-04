# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteResourceRecordRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
    ):
        # The IDs of the records to delete. Separate multiple IDs with commas (,). You can specify up to 200 IDs at a time.
        # 
        # This parameter is required.
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['ids'] = self.ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')

        return self

