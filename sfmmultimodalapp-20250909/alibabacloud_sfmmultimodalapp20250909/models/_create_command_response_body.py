# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCommandResponseBody(DaraModel):
    def __init__(
        self,
        domain_code: str = None,
        request_id: str = None,
        tool_id: str = None,
    ):
        self.domain_code = domain_code
        self.request_id = request_id
        self.tool_id = tool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tool_id is not None:
            result['ToolId'] = self.tool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')

        return self

