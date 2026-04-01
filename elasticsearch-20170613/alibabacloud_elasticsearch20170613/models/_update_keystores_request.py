# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class UpdateKeystoresRequest(DaraModel):
    def __init__(
        self,
        remove: List[str] = None,
        update: Dict[str, str] = None,
        force: str = None,
    ):
        self.remove = remove
        self.update = update
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remove is not None:
            result['remove'] = self.remove

        if self.update is not None:
            result['update'] = self.update

        if self.force is not None:
            result['force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('remove') is not None:
            self.remove = m.get('remove')

        if m.get('update') is not None:
            self.update = m.get('update')

        if m.get('force') is not None:
            self.force = m.get('force')

        return self

