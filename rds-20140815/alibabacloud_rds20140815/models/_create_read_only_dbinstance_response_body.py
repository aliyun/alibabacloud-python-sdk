# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReadOnlyDBInstanceResponseBody(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        order_id: str = None,
        port: str = None,
        request_id: str = None,
    ):
        # The internal endpoint that is used to connect to the read-only instance.
        self.connection_string = connection_string
        # The ID of the read-only instance.
        self.dbinstance_id = dbinstance_id
        # The ID of the order.
        self.order_id = order_id
        # The internal port number that is used to connect to the read-only instance.
        self.port = port
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.port is not None:
            result['Port'] = self.port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

