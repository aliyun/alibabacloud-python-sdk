# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelConnectionConsumerAPIKey(DaraModel):
    def __init__(
        self,
        api_key_id: str = None,
        value: str = None,
    ):
        # The unique identifier for the consumer API key.
        self.api_key_id = api_key_id
        # The value of the consumer API key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

