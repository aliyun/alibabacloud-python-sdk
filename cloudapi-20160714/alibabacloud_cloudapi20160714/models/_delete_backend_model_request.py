# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBackendModelRequest(DaraModel):
    def __init__(
        self,
        backend_id: str = None,
        backend_model_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        # The ID of the backend service.
        self.backend_id = backend_id
        # The ID of the backend model.
        # 
        # This parameter is required.
        self.backend_model_id = backend_model_id
        self.security_token = security_token
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **PRE**
        # *   **TEST**
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_id is not None:
            result['BackendId'] = self.backend_id

        if self.backend_model_id is not None:
            result['BackendModelId'] = self.backend_model_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendId') is not None:
            self.backend_id = m.get('BackendId')

        if m.get('BackendModelId') is not None:
            self.backend_model_id = m.get('BackendModelId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

