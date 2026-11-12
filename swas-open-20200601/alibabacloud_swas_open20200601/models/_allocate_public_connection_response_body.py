# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocatePublicConnectionResponseBody(DaraModel):
    def __init__(
        self,
        public_connection: str = None,
        request_id: str = None,
    ):
        # The public endpoint.
        self.public_connection = public_connection
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.public_connection is not None:
            result['PublicConnection'] = self.public_connection

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicConnection') is not None:
            self.public_connection = m.get('PublicConnection')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

