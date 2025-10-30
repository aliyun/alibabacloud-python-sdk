# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckHadoopNetConnectionResponseBody(DaraModel):
    def __init__(
        self,
        connection_message: str = None,
        connection_status: str = None,
        request_id: str = None,
    ):
        # Return message: Returns error information if the connection fails, otherwise returns an empty string ("").
        self.connection_message = connection_message
        # Connection status:
        # 
        # - Network connected: Success
        # 
        # - Network not connected: Failed
        self.connection_status = connection_status
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_message is not None:
            result['ConnectionMessage'] = self.connection_message

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionMessage') is not None:
            self.connection_message = m.get('ConnectionMessage')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

