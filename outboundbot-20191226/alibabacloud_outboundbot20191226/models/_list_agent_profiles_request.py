# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentProfilesRequest(DaraModel):
    def __init__(
        self,
        app_ip: str = None,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.app_ip = app_ip
        # This parameter is required.
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ip is not None:
            result['AppIp'] = self.app_ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIp') is not None:
            self.app_ip = m.get('AppIp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        return self

