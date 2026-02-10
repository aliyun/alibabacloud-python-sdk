# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteClientUserDefineRuleRequest(DaraModel):
    def __init__(
        self,
        id_list: List[int] = None,
    ):
        # The IDs of the custom defense rules.
        # 
        # This parameter is required.
        self.id_list = id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id_list is not None:
            result['IdList'] = self.id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        return self

