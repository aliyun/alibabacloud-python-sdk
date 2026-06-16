# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConsumerAPIKeyInput(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        description: str = None,
        model_connection_id: str = None,
    ):
        # A custom API key. If omitted, the service generates one automatically.
        self.api_key = api_key
        # A description for the consumer API key.
        self.description = description
        # The identifier for the model connection.
        # 
        # This parameter is required.
        self.model_connection_id = model_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.description is not None:
            result['description'] = self.description

        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

        return self

