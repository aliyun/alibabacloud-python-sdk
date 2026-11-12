# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderSCIMRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateIdentityProviderSCIMRequestBody = None,
    ):
        # Submit business parameters as described in this operation. The body parameters of public APIs are mapped to backend wrappers by the gateway. Do not mix them with direct backend body wrappers.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateIdentityProviderSCIMRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateIdentityProviderSCIMRequestBody(DaraModel):
    def __init__(
        self,
        sync_enabled: bool = None,
    ):
        # Do not set this parameter to true during CustomSSO initialization. You can only update this parameter later by calling UpdateIdentityProviderSCIM. Determine the result based on the operationStatus field.
        # 
        # This parameter is required.
        self.sync_enabled = sync_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        return self

