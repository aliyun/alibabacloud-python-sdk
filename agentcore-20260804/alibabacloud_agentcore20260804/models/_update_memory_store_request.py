# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateMemoryStoreRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateMemoryStoreRequestBody = None,
        client_token: str = None,
    ):
        # The update MemoryStore request.
        # 
        # This parameter is required.
        self.body = body
        # The client request token.
        self.client_token = client_token

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

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateMemoryStoreRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateMemoryStoreRequestBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        extract_instructions: str = None,
    ):
        # The MemoryStore description. Maximum length: 1,024 characters.
        self.description = description
        # The custom memory extraction instructions. Maximum length: 4,096 characters.
        self.extract_instructions = extract_instructions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.extract_instructions is not None:
            result['extractInstructions'] = self.extract_instructions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extractInstructions') is not None:
            self.extract_instructions = m.get('extractInstructions')

        return self

