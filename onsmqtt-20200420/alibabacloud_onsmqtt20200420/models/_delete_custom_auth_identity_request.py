# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCustomAuthIdentityRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        identity_type: str = None,
        instance_id: str = None,
        username: str = None,
    ):
        # The client ID of the device. This parameter is required when the identity type is CLIENT.
        self.client_id = client_id
        # The identity type. Valid values:
        # - USER: Username only.
        # - CLIENT: Specific to the client.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the MSMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The username.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

