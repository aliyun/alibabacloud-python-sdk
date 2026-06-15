# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBlackListClientsResponseBody(DaraModel):
    def __init__(
        self,
        clients: str = None,
        request_id: str = None,
    ):
        # The IDs of clients and the status of each client. This parameter contains a JSON object, for example, {"client1": "EVICTING","client2":"EVICTED"}.
        # 
        # Available client statuses include:
        # 
        # *   EVICTING indicates that a client is being removed
        # *   EVICTED indicates that a client is removed
        # *   ACCEPTING indicates that the write access to the file system is being granted to a client
        # *   ACCEPTABLE indicates that the write access to the file system is granted to a client
        self.clients = clients
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clients is not None:
            result['Clients'] = self.clients

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clients') is not None:
            self.clients = m.get('Clients')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

