# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchDBInstanceNetTypeResponseBody(DaraModel):
    def __init__(
        self,
        new_connection_string: str = None,
        old_connection_string: str = None,
        request_id: str = None,
    ):
        # The endpoint that is used to connect to the instance after the switch of endpoints.
        self.new_connection_string = new_connection_string
        # The endpoint that is used to connect to the instance before the switch of endpoints.
        self.old_connection_string = old_connection_string
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_connection_string is not None:
            result['NewConnectionString'] = self.new_connection_string

        if self.old_connection_string is not None:
            result['OldConnectionString'] = self.old_connection_string

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewConnectionString') is not None:
            self.new_connection_string = m.get('NewConnectionString')

        if m.get('OldConnectionString') is not None:
            self.old_connection_string = m.get('OldConnectionString')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

