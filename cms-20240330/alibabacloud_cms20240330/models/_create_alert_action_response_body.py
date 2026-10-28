# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlertActionResponseBody(DaraModel):
    def __init__(
        self,
        alert_action_id: str = None,
        request_id: str = None,
    ):
        self.alert_action_id = alert_action_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_id is not None:
            result['alertActionId'] = self.alert_action_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionId') is not None:
            self.alert_action_id = m.get('alertActionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

