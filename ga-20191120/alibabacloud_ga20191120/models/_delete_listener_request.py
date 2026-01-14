# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteListenerRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        listener_id: str = None,
    ):
        # The ID of the GA instance for which you want to delete a listener.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the listener that you want to delete.
        # 
        # This parameter is required.
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        return self

