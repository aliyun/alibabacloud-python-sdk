# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribePolarClawMCPServersResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        servers: Dict[str, Any] = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The status code.
        self.code = code
        # The message returned for the request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The configurations of the MCP servers.
        self.servers = servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.servers is not None:
            result['Servers'] = self.servers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Servers') is not None:
            self.servers = m.get('Servers')

        return self

