# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class VerifyConnectorRequest(DaraModel):
    def __init__(
        self,
        body: main_models.VerifyConnectorRequestBody = None,
    ):
        # The validation request body.
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
            temp_model = main_models.VerifyConnectorRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class VerifyConnectorRequestBody(DaraModel):
    def __init__(
        self,
        metadata: str = None,
    ):
        # A JSON string. qodercli uses apiKey. This parameter is used only for validation and is not persisted.
        # 
        # This parameter is required.
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['metadata'] = self.metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        return self

