# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConnectorModelsRequest(DaraModel):
    def __init__(
        self,
        connector_key_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The Connector Key ID. This parameter is not supported in the current version.
        self.connector_key_id = connector_key_id
        # The page size. This parameter is not supported in the current version.
        self.max_results = max_results
        # The next page token. This parameter is not supported in the current version.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_key_id is not None:
            result['connectorKeyId'] = self.connector_key_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectorKeyId') is not None:
            self.connector_key_id = m.get('connectorKeyId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

