# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class InvokeEsAgentRequest(DaraModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The request body in JSON-RPC 2.0 format.
        # 
        # Common request parameters (all at the top level of the request body, not inside params):
        # - jsonrpc: String. Required. The JSON-RPC version. Fixed value: 2.0. Example: 2.0.
        # - method: String. Required. The method to call. For valid values, see the method list below. Example: session/prompt.
        # - id: String. Optional. The request ID specified by the caller. This value is passed through in the response. Example: 1774339902987004.
        # - params: Object. Optional. The parameters for the specified method. For examples, refer to the supplementary description.
        # - sessionCode: String. Optional. The session ID for exact match queries in session/list. Example: 49b82154-ac20-4f27-a6ec-eb5f4cfc5304.
        # - pageNum: Integer. Optional. The page number for session/list. Default value is handled by the server. Example: 1.
        # - pageSize: Integer. Optional. The number of entries per page for session/list. Default value is handled by the server. Example: 10.
        # 
        # Valid values of method:
        # - session/new: Creates a session. Returns JSON.
        # - session/list: Queries the session list or a specified session. Returns JSON.
        # - session/prompt: Sends a message. Returns SSE.
        # - session/load: Resumes from a breakpoint. Used only when _meta.isReload=true. Returns SSE.
        # - session/cancel: Cancels in-progress tasks in a session. Returns JSON.
        # - session/delete: Deletes a session. Returns JSON.
        # - session/hitlRespond: Submits a HITL user response. Returns JSON.
        # 
        # Response modes: session/prompt and session/load return an SSE event stream with Content-Type text/event-stream. Each event is in the format data: {JSON}. Other methods return a standard JSON response with Content-Type application/json.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        return self

