# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionRecordWeightRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        record_id: str = None,
        weight: int = None,
    ):
        # The client token that ensures the idempotence of the request. Generate a unique token for each request. The token can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The unique ID of the DNS record.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The weight. The value can be an integer from 0 to 100.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

