# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAlertActionsShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_action_ids_shrink: str = None,
    ):
        # The unique identifiers of the alert action integrations to delete.
        # 
        # This parameter is required.
        self.alert_action_ids_shrink = alert_action_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_ids_shrink is not None:
            result['alertActionIds'] = self.alert_action_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids_shrink = m.get('alertActionIds')

        return self

