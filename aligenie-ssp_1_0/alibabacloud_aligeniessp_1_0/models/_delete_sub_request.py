# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSubRequest(DaraModel):
    def __init__(
        self,
        sub_id: int = None,
    ):
        # Subscription album record ID
        # 
        # This parameter is required.
        self.sub_id = sub_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        return self

