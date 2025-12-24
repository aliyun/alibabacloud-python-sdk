# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteServiceLabelRequest(DaraModel):
    def __init__(
        self,
        keys: List[str] = None,
        label_keys: List[str] = None,
    ):
        # The service tags that you want to delete.
        self.keys = keys
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keys is not None:
            result['Keys'] = self.keys

        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')

        return self

