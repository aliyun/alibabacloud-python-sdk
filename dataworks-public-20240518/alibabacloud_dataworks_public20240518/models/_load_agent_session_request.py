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
        self.id = id
        self.jsonrpc = jsonrpc
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
        self.meta = meta
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
        self.begin_log_offset = begin_log_offset
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

