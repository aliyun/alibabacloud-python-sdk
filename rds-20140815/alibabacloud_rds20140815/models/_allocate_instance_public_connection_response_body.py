# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateInstancePublicConnectionResponseBody(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        db_instance_name: str = None,
        request_id: str = None,
    ):
        # The endpoint that is used to connect to the database instance.
        self.connection_string = connection_string
        # The ID of the instance.
        self.db_instance_name = db_instance_name
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

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

