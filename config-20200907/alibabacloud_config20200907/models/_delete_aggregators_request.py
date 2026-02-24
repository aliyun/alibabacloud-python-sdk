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
        # This parameter is required.
        self.aggregator_ids = aggregator_ids
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

