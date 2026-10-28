# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstructionRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        config: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        # The unique code for the instruction.
        self.code = code
        # The configuration for the instruction, specified as a JSON string.
        # 
        # > - `providerId`: The ID of the live agent service provider. Call the `ListCallCenterProviders` operation to obtain this ID.
        # >
        # > - `transferMethod`: The method used for the transfer. Valid values: `BYE`, `BRIDGE`, and `REFER`.
        # >
        # > - `transferType`: The transfer destination type. Valid values: `External` (external number), `Agent` (agent), and `SkillGroup` (skill group).
        # >
        # > - `transferTarget`: The destination of the transfer, such as a phone number, an agent ID, or a skill group ID. The value of this parameter depends on the `transferType`.
        # >
        # > - `transferor`: The caller ID to display for the transfer. If this parameter is not specified, the caller\\"s original phone number is used.
        # >
        # > - `timeoutSeconds`: The timeout in seconds for transferring a call to an agent. Default: 30.
        self.config = config
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instruction.
        self.name = name
        # The type of the instruction.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

