# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConnectedClusterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connected_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID of the remote instance that is connected over the network.
        # 
        # This parameter is required.
        self.connected_instance_id = connected_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.connected_instance_id is not None:
            result['connectedInstanceId'] = self.connected_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('connectedInstanceId') is not None:
            self.connected_instance_id = m.get('connectedInstanceId')

        return self

