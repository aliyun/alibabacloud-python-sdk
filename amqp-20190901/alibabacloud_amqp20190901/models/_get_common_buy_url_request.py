# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCommonBuyUrlRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.action_type = action_type
        self.console_session_id = console_session_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

