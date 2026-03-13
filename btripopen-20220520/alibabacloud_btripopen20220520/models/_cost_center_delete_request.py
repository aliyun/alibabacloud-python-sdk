# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CostCenterDeleteRequest(DaraModel):
    def __init__(
        self,
        thirdpart_id: str = None,
    ):
        # This parameter is required.
        self.thirdpart_id = thirdpart_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        return self

