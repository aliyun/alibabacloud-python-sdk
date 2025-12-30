# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDNSSLBWeightResponseBody(DaraModel):
    def __init__(
        self,
        record_id: str = None,
        request_id: str = None,
        weight: int = None,
    ):
        # The ID of the DNS record.
        self.record_id = record_id
        # The request ID.
        self.request_id = request_id
        # The updated weight.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

