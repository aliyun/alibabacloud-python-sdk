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
        # The IDs of clients and the status of each client. The parameter value is a JSON string, for example, `{"client1": "EVICTING","client2":"EVICTED"}`.
        # 
        # Available client statuses include:
        # 
        # *   EVICTING: The client is being evicted.
        # *   EVICTED: The client is evicted.
        # *   ACCEPTING: The write access to the file system is being granted to the client.
        # *   ACCEPTABLE: The write access to the file system is granted to the client.
        self.clients = clients
        # The request ID.
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

