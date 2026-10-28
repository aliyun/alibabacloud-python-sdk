# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstructionRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        config: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        # The instruction code.
        # >Notice: Globally unique.</notice>
        self.code = code
        # The instruction configuration.
        # 
        # > - providerId: the ID of the human agent service provider. You can obtain the ID by calling ListCallCenterProviders.
        # > - transferMethod: the transfer method. Valid values: BYE, BRIDGE, and REFER.
        # > - transferType: the transfer target type. Valid values: External (external number), Agent (agent), and SkillGroup (skill group).
        # > - transferTarget: the transfer target.
        # > - transferor: the caller number. If this parameter is left empty, the mobile phone number of the calling customer is used by default.
        # > - timeoutSeconds: the timeout period for transferring to a human agent, in seconds. Default value: 30.
        self.config = config
        # The instance ID.
        self.instance_id = instance_id
        # The instruction name.
        self.name = name
        # The instruction type.
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

