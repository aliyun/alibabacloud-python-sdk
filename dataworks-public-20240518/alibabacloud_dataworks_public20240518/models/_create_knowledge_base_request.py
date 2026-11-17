# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        # The idempotency token for the creation request. This parameter is optional. It accepts up to 64 characters and must contain at least one non-whitespace character. Use the same value when the same caller retries the same creation request in the same region. Reusing a token with different request content returns a conflict. If you omit the token, repeated requests may create multiple knowledge bases.
        self.client_token = client_token
        # The description of the knowledge base. This parameter is optional. The maximum length is 1024 characters.
        self.description = description
        # The name of the knowledge base. This parameter cannot be empty. The maximum length is 128 characters.
        # 
        # This parameter is required.
        self.name = name
        # The type of the knowledge base. PERSONAL: personal knowledge base. ENTERPRISE: enterprise knowledge base. If this parameter is omitted, the default value is PERSONAL. Creating an enterprise knowledge base requires the corresponding enterprise knowledge base capabilities.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

