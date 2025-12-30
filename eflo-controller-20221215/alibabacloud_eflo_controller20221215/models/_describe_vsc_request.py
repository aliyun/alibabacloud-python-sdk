# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVscRequest(DaraModel):
    def __init__(
        self,
        vsc_id: str = None,
    ):
        # The VSC ID.
        # 
        # This parameter is required.
        self.vsc_id = vsc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        return self

