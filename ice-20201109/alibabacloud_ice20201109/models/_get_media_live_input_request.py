# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaLiveInputRequest(DaraModel):
    def __init__(
        self,
        input_id: str = None,
    ):
        # The ID of the input.
        # 
        # This parameter is required.
        self.input_id = input_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_id is not None:
            result['InputId'] = self.input_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputId') is not None:
            self.input_id = m.get('InputId')

        return self

