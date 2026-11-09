# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCustomAuthPermissionRequest(DaraModel):
    def __init__(
        self,
        effect: str = None,
        identity: str = None,
        identity_type: str = None,
        instance_id: str = None,
        permit_action: str = None,
        topic: str = None,
    ):
        # The authorization effect.
        # 
        # This parameter is required.
        self.effect = effect
        # The username or client ID.
        # 
        # This parameter is required.
        self.identity = identity
        # The identity type. Valid values:
        # - USER: username only.
        # - CLIENT: specific client.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the MSMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The authorized action.
        # 
        # This parameter is required.
        self.permit_action = permit_action
        # The authorized topic. Multi-level MQTT topics and wildcards are supported.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect is not None:
            result['Effect'] = self.effect

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.permit_action is not None:
            result['PermitAction'] = self.permit_action

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PermitAction') is not None:
            self.permit_action = m.get('PermitAction')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

