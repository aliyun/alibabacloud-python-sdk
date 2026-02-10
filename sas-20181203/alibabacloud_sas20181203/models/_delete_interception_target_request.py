# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInterceptionTargetRequest(DaraModel):
    def __init__(
        self,
        target_ids: str = None,
    ):
        # The IDs of the network objects that you want to remove. You can call the [ListInterceptionTargetPage](~~ListInterceptionTargetPage~~) operation to query the IDs of the network objects.
        # 
        # This parameter is required.
        self.target_ids = target_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')

        return self

