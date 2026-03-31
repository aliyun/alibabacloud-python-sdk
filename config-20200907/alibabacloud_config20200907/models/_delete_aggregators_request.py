# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAggregatorsRequest(DaraModel):
    def __init__(
        self,
        aggregator_ids: str = None,
        client_token: str = None,
    ):
        # The ID of the account group. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.aggregator_ids = aggregator_ids
        # The client token that you want to use to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_ids is not None:
            result['AggregatorIds'] = self.aggregator_ids

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorIds') is not None:
            self.aggregator_ids = m.get('AggregatorIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

