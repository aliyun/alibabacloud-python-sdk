# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class ChatRefDocPageNum(DaraModel):
    def __init__(
        self,
        num: int = None,
        pos: List[List[main_models.ChatRefDocPostion]] = None,
    ):
        self.num = num
        self.pos = pos

    def validate(self):
        if self.pos:
            for v1 in self.pos:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.num is not None:
            result['num'] = self.num

        result['pos'] = []
        if self.pos is not None:
            for k1 in self.pos:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['pos'].append(l1)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('num') is not None:
            self.num = m.get('num')

        self.pos = []
        if m.get('pos') is not None:
            for k1 in m.get('pos'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.ChatRefDocPostion()
                    l1.append(temp_model.from_map(k2))
                self.pos.append(l1)

        return self

