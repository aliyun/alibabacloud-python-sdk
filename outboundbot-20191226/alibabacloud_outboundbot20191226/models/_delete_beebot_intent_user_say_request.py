# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBeebotIntentUserSayRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        intent_id: str = None,
        script_id: str = None,
        user_say_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.intent_id = intent_id
        # This parameter is required.
        self.script_id = script_id
        # This parameter is required.
        self.user_say_id = user_say_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.user_say_id is not None:
            result['UserSayId'] = self.user_say_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('UserSayId') is not None:
            self.user_say_id = m.get('UserSayId')

        return self

