# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataChannelCredentialRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        instance_id: str = None,
    ):
        # The client device ID used to apply for data channel credentials. It cannot be empty. It must be consistent with the DeviceId used by the same client for subsequent BridgeWebCall or MakePilotCall operations. The business identifier is provided by the integrator according to the agreement, and is not the ClientId returned by the service or the ChannelId of the voice channel.
        self.device_id = device_id
        # The instance identity of the associated product. You must use an instance that the user who invokes the operation has access to and that actually exists. It must be consistent with the instance to which the scenario, channel, and session belong. The maximum length is subject to the current POP parameter definition.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

