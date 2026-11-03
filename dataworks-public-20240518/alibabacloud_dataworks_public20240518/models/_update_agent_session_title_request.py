# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentSessionTitleRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.UpdateAgentSessionTitleRequestParams = None,
    ):
        # The JSON-RPC correlation ID for the current request. It is specified by the caller and used to correlate the request and response.
        self.id = id
        # The JSON-RPC protocol version. Set the value to 2.0.
        self.jsonrpc = jsonrpc
        # The request parameters for modifying the session title, including the target session ID and the new title.
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
            temp_model = main_models.UpdateAgentSessionTitleRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        return self

class UpdateAgentSessionTitleRequestParams(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        title: str = None,
    ):
        # The ID of the agent session that belongs to the current account.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The new title. The length must be 1 to 512 characters after leading and trailing whitespaces are removed.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

