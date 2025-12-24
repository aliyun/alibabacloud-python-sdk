# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteGatewayLabelRequest(DaraModel):
    def __init__(
        self,
        label_keys: List[str] = None,
    ):
        # This parameter is required.
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')

        return self

