# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateModelConnectionRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateModelConnectionRequestBody = None,
        client_token: str = None,
    ):
        # The request body.
        self.body = body
        # The client token used for idempotence. Not currently supported.
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
            temp_model = main_models.UpdateModelConnectionRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateModelConnectionRequestBody(DaraModel):
    def __init__(
        self,
        api_keys: List[str] = None,
        description: str = None,
        endpoint: str = None,
        name: str = None,
        protocol: str = None,
        provider_type: str = None,
    ):
        # The list of API keys used to access the upstream model service. The list must contain at least one non-empty value.
        self.api_keys = api_keys
        # The description of the model connection. The description can be up to 255 characters in length.
        self.description = description
        # The absolute HTTP or HTTPS address of the upstream model service. The address can be up to 1024 characters in length.
        self.endpoint = endpoint
        # The model connection name. The name must be 1 to 128 non-whitespace characters in length.
        self.name = name
        # The model invocation protocol. Currently, only OpenAI/v1 is supported. If not specified in Settings when the model connection is created, this default value is used.
        self.protocol = protocol
        # The model provider type.
        self.provider_type = provider_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys

        if self.description is not None:
            result['description'] = self.description

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.provider_type is not None:
            result['providerType'] = self.provider_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('providerType') is not None:
            self.provider_type = m.get('providerType')

        return self

