# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronAppUpdateCmd(DaraModel):
    def __init__(
        self,
        desc: str = None,
        id: int = None,
        status: str = None,
    ):
        self.desc = desc
        # This parameter is required.
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.id is not None:
            result['id'] = self.id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

