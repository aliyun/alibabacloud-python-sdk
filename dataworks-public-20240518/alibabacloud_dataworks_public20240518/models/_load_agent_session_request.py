# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class LoadAgentSessionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.LoadAgentSessionRequestParams = None,
    ):
        # The client-generated request ID, which is returned in the response.
        self.id = id
        # The JSON-RPC version. The value must be `2.0`.
        self.jsonrpc = jsonrpc
        # Business parameters.
        self.params = params

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.params is not None:
            result['Params'] = self.params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Params') is not None:
            temp_model = main_models.LoadAgentSessionRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        return self

class LoadAgentSessionRequestParams(DaraModel):
    def __init__(
        self,
        meta: main_models.LoadAgentSessionRequestParamsMeta = None,
        session_id: str = None,
    ):
        # DataWorks-specific extended parameters for ACP.
        self.meta = meta
        # The ID of the target session. If the session does not exist, an SSE error frame is returned.
        self.session_id = session_id

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            temp_model = main_models.LoadAgentSessionRequestParamsMeta()
            self.meta = temp_model.from_map(m.get('Meta'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class LoadAgentSessionRequestParamsMeta(DaraModel):
    def __init__(
        self,
        begin_log_offset: int = None,
        is_reload: bool = None,
    ):
        # In a resumable transfer scenario, this specifies the offset from which to resume fetching the SSE output.
        self.begin_log_offset = begin_log_offset
        # Specifies whether to use resumable transfer. If the SSE stream is interrupted due to issues like an unstable network connection, you can set this parameter to `true` to re-fetch the stream data from the point of failure.
        self.is_reload = is_reload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_log_offset is not None:
            result['BeginLogOffset'] = self.begin_log_offset

        if self.is_reload is not None:
            result['IsReload'] = self.is_reload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginLogOffset') is not None:
            self.begin_log_offset = m.get('BeginLogOffset')

        if m.get('IsReload') is not None:
            self.is_reload = m.get('IsReload')

        return self

