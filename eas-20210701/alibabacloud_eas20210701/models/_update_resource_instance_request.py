# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceInstanceRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
    ):
        # The operation that updates the scheduling state of the instance in a dedicated resource group. Valid values:
        # 
        # *   Uncordon: allows scheduling the service to this instance.
        # *   Cordon: prohibits scheduling the service to this instance.
        # *   Drain: evicts the service that has been scheduled to this instance.
        # 
        # This parameter is required.
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        return self

