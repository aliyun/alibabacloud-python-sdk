# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFCTriggerRequest(DaraModel):
    def __init__(
        self,
        trigger_arn: str = None,
    ):
        # The trigger that corresponds to the Function Compute service.
        # 
        # This parameter is required.
        self.trigger_arn = trigger_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trigger_arn is not None:
            result['TriggerARN'] = self.trigger_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TriggerARN') is not None:
            self.trigger_arn = m.get('TriggerARN')

        return self

