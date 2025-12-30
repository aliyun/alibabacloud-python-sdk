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
        self.client_token = client_token
        self.record_id = record_id
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

