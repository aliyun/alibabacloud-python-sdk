# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackScriptRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        rollback_version: str = None,
        script_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.rollback_version = rollback_version
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

        if self.rollback_version is not None:
            result['RollbackVersion'] = self.rollback_version

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RollbackVersion') is not None:
            self.rollback_version = m.get('RollbackVersion')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

