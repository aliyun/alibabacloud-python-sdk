# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGatewayIntranetLinkedVpcPeerResponseBody(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The ID of the private gateway.
        self.gateway_id = gateway_id
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

