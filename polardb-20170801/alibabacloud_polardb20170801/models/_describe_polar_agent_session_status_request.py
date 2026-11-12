# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarAgentSessionStatusRequest(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        source: str = None,
    ):
        # The session ID, which is used to identify a visitor\\"s session and maintain context information. Usage notes: You can obtain this ID by calling the GetPolarAgent API and retrieving the SessionId field from the response. Note that GetPolarAgent requires Signature Version 3.0 and the SSE protocol. The ID must be in the standard UUID format, such as 1e28530a-0da2-c475-5f16-5b1b8b9a73c9.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The product source. Valid values: polardb-console.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

