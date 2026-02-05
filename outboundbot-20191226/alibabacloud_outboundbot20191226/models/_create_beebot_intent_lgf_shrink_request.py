# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBeebotIntentLgfShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lgf_definition_shrink: str = None,
        script_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.lgf_definition_shrink = lgf_definition_shrink
        # This parameter is required.
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lgf_definition_shrink is not None:
            result['LgfDefinition'] = self.lgf_definition_shrink

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LgfDefinition') is not None:
            self.lgf_definition_shrink = m.get('LgfDefinition')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

