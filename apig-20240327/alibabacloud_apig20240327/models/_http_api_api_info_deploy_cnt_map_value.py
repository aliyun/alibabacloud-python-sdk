# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpApiApiInfoDeployCntMapValue(DaraModel):
    def __init__(
        self,
        deployed_cnt: int = None,
        cnt: int = None,
    ):
        self.deployed_cnt = deployed_cnt
        self.cnt = cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployed_cnt is not None:
            result['deployedCnt'] = self.deployed_cnt

        if self.cnt is not None:
            result['Cnt'] = self.cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deployedCnt') is not None:
            self.deployed_cnt = m.get('deployedCnt')

        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')

        return self

