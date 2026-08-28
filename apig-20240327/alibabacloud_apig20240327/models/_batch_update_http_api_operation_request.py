# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class BatchUpdateHttpApiOperationRequest(DaraModel):
    def __init__(
        self,
        auth_config: main_models.BatchUpdateHttpApiOperationRequestAuthConfig = None,
        enable_auth: bool = None,
        operation_ids: List[str] = None,
    ):
        self.auth_config = auth_config
        self.enable_auth = enable_auth
        self.operation_ids = operation_ids

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth

        if self.operation_ids is not None:
            result['operationIds'] = self.operation_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = main_models.BatchUpdateHttpApiOperationRequestAuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')

        if m.get('operationIds') is not None:
            self.operation_ids = m.get('operationIds')

        return self

class BatchUpdateHttpApiOperationRequestAuthConfig(DaraModel):
    def __init__(
        self,
        auth_mode: str = None,
        auth_type: str = None,
    ):
        self.auth_mode = auth_mode
        self.auth_type = auth_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_mode is not None:
            result['authMode'] = self.auth_mode

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMode') is not None:
            self.auth_mode = m.get('authMode')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        return self

