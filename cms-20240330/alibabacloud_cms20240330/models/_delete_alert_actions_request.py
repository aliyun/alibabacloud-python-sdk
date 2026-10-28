# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAlertActionsRequest(DaraModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
    ):
        # The unique identifiers of the alert action integrations to delete.
        # 
        # This parameter is required.
        self.alert_action_ids = alert_action_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_ids is not None:
            result['alertActionIds'] = self.alert_action_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids = m.get('alertActionIds')

        return self

