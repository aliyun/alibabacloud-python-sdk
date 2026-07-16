# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FullSampleItem(DaraModel):
    def __init__(
        self,
        id: str = None,
        modify_time: str = None,
        operator: str = None,
    ):
        self.id = id
        self.modify_time = modify_time
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.operator is not None:
            result['Operator'] = self.operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        return self

