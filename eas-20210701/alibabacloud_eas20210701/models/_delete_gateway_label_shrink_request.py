# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGatewayLabelShrinkRequest(DaraModel):
    def __init__(
        self,
        label_keys_shrink: str = None,
    ):
        # This parameter is required.
        self.label_keys_shrink = label_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_keys_shrink is not None:
            result['LabelKeys'] = self.label_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys_shrink = m.get('LabelKeys')

        return self

