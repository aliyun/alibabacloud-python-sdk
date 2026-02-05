# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBeebotIntentUserSayShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        user_say_definition_shrink: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.script_id = script_id
        # This parameter is required.
        self.user_say_definition_shrink = user_say_definition_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.user_say_definition_shrink is not None:
            result['UserSayDefinition'] = self.user_say_definition_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('UserSayDefinition') is not None:
            self.user_say_definition_shrink = m.get('UserSayDefinition')

        return self

