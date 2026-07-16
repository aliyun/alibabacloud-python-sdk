# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConsumerAPIKey(DaraModel):
    def __init__(
        self,
        active: bool = None,
        consumer_api_key_id: str = None,
        created_at: str = None,
        description: str = None,
        last_updated_at: str = None,
        masked_key: str = None,
        model_connection_id: str = None,
    ):
        # Specifies if the key is enabled (true) or disabled (false).
        self.active = active
        # The unique identifier of the consumer API key.
        self.consumer_api_key_id = consumer_api_key_id
        # The creation time of the consumer API key, in ISO 8601 format.
        self.created_at = created_at
        # A user-defined description for the consumer API key.
        self.description = description
        # The last update time of the consumer API key, in ISO 8601 format.
        self.last_updated_at = last_updated_at
        # The masked API key, showing only the first and last few characters.
        self.masked_key = masked_key
        # The identifier of the associated model connection.
        self.model_connection_id = model_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.consumer_api_key_id is not None:
            result['consumerApiKeyId'] = self.consumer_api_key_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.masked_key is not None:
            result['maskedKey'] = self.masked_key

        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('consumerApiKeyId') is not None:
            self.consumer_api_key_id = m.get('consumerApiKeyId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('maskedKey') is not None:
            self.masked_key = m.get('maskedKey')

        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

        return self

