# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class ReplyAgentSessionResponseBody(DaraModel):
    def __init__(
        self,
        json_rpc_response: Any = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The JSON-RPC response. For core embedded fields, see the supplementary description.
        self.json_rpc_response = json_rpc_response
        # The ID of the current request, used for troubleshooting.
        self.request_id = request_id
        # Indicates whether the current API call is successful. This parameter cannot replace the business acceptance result.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_rpc_response is not None:
            result['JsonRpcResponse'] = self.json_rpc_response

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonRpcResponse') is not None:
            self.json_rpc_response = m.get('JsonRpcResponse')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

