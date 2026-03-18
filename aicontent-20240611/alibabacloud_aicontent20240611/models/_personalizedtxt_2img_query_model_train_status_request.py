# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Personalizedtxt2imgQueryModelTrainStatusRequest(DaraModel):
    def __init__(
        self,
        model_id: str = None,
    ):
        # This parameter is required.
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['modelId'] = self.model_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        return self

